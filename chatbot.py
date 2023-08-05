import warnings
import gradio as gr
import datetime
from dotenv import load_dotenv
from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
load_dotenv()

warnings.filterwarnings('ignore')

current_date = datetime.datetime.now().date()
if current_date < datetime.date(2023, 9, 2):
    llm_name = "gpt-3.5-turbo-0301"
else:
    llm_name = "gpt-3.5-turbo"
# print(llm_name)

persist_directory = './docs/chroma/'
embedding = OpenAIEmbeddings()
vectordb = Chroma(persist_directory=persist_directory,
                  embedding_function=embedding)
llm = ChatOpenAI(model_name=llm_name, temperature=0)

template = """Use the following pieces of context to answer the question at the end. 
If you don't know the answer, just say that you don't know, don't try to make up an answer. 
Use three sentences maximum. Keep the answer as concise as possible.
    {context}
    Previous conversation:
    {chat_history}
    New human question: {question}
    Response:"""
QA_CHAIN_PROMPT = PromptTemplate.from_template(template)
print(f"{vectordb._collection.count()} results for vectordb")

memory = ConversationBufferMemory(
    memory_key="chat_history",
    output_key='answer',
    return_messages=True
)
retriever = vectordb.as_retriever()


def chatWithNCAIR(prompt, history):
    chain = ConversationalRetrievalChain.from_llm(
        llm,
        retriever=retriever,
        memory=memory,
        return_source_documents=True,
        get_chat_history=lambda h: h,
        combine_docs_chain_kwargs={"prompt": QA_CHAIN_PROMPT}
    )
    result = chain({"question": prompt})
    return result["answer"]


title = "NCAIR Chat Bot"

app = gr.ChatInterface(
    fn=chatWithNCAIR,
    title=title,
    retry_btn=None
).queue()

app.launch()
