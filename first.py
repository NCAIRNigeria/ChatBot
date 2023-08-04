import os
import openai
import sys
sys.path.append('../..')

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file

openai.api_key  = os.environ['OPENAI_API_KEY']

from langchain.document_loaders import PyPDFDirectoryLoader

loader = PyPDFDirectoryLoader('./datasets')
documents = loader.load()

from langchain.text_splitter import RecursiveCharacterTextSplitter
text_splitter = RecursiveCharacterTextSplitter(
    # separator="\n",
    chunk_size=1500,
    chunk_overlap=150,
    # length_function=len
)

docs = text_splitter.split_documents(documents)

print(f"{len(docs)} is length of docs")

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
embedding = OpenAIEmbeddings()
persist_directory = 'docs/chroma/'
vectordb = Chroma.from_documents(
    documents=docs,
    embedding=embedding,
    persist_directory=persist_directory
)
vectordb.persist()

print(f"{vectordb._collection.count()} in vector collection")