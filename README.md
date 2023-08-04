# Ncair ChatBot

### Description

This Chatbot uses ChatOpenAI model from Langchain to chat with your data and the interface uses Gradio.
It can load PDF documents from a directory named _datasets_.
Also it Currently uses chroma for vectorization and OpenAIEmbeddings for Embeddings.

### Resources

- [Langchain - Chat with your data](https://www.deeplearning.ai/short-courses/langchain-chat-with-your-data/)
- [Gradio Chat Interface](https://www.gradio.app/guides/creating-a-custom-chatbot-with-blocks)

### API

You'll need a free API key from [OPENAI](https://platform.openai.com/account/api-keys).

### Tips

- After downloading this repo, you need to install the packages used using the following code
  `pip install -r requirements.txt`
- You need to create a _.env_ file and create a variable in this format below, replace _sk-XXXXXXXX_ with the api key you get from openai
  `OPENAI_API_KEY=sk-XXXXXXXX`
- the code is also divided into two main apps, one for embedding and vectorization which is named _first.py_ and the other one is the chatbot which is _chatbot.py_
- You also need to create a folder named _datasets_ where you put all your pdf files.
- Finally you run the _first.py_, then the _chatbot.py_ which creates a localhost url to your chatbot running locally.

### Pending

- [] To change Embeddings Platform
- [] To change LLM
