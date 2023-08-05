import os
import openai
import sys
from dotenv import load_dotenv, find_dotenv
from langchain.document_loaders import PyPDFDirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
import uuid

sys.path.append('../..')
_ = load_dotenv(find_dotenv()) # read local .env file
openai.api_key  = os.environ['OPENAI_API_KEY']

loader = PyPDFDirectoryLoader('./datasets')
documents = loader.load()
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1500,
    chunk_overlap=150,
)

docs = text_splitter.split_documents(documents)
print(f"{len(docs)} is length of docs")

# Create a list of unique ids for each document based on the content
ids = [str(uuid.uuid5(uuid.NAMESPACE_DNS, doc.page_content)) for doc in docs]
unique_ids = list(set(ids))

# Ensure that only docs that correspond to unique ids are kept and that only one of the duplicate ids is kept
seen_ids = set()
unique_docs = [
    doc for doc, id in zip(docs, ids) 
    if id not in seen_ids and (seen_ids.add(id) or True)
    ]

embedding = OpenAIEmbeddings()
persist_directory = 'docs/chroma/'
vectordb = Chroma.from_documents(
    documents=docs,
    embedding=embedding,
    ids=unique_ids,
    persist_directory=persist_directory
)
vectordb.persist()

print(f"{vectordb._collection.count()} in vector collection")