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
- the code is also divided into two main apps, one for embedding and vectorization which is named _first.py_ and the other one is the chatbot which is _chatbot.py_ which creates a localhost url to run your chatbot locally.
- You also need to create a folder named _datasets_ where you put all your pdf files.

### RUN NOTE

- if you want to chat with ncair data, you need the _docs/chroma_ folder and you only need to run the _chatbot.py_ file.
- if you want to test the chatbot with your own data, you dont need the _docs/chroma_ folder and you can delete it. The first.py file run will create the _docs/chroma_ for you which will contain your Vector Store for the data you put in _datasets_ folder, then you run the _chatbot.py_ file.


### System Requirements

#### Python Version

To use this software, you must have Python 3.10 or later installed. Earlier versions of Python will not compile.

## C++ Compiler

If you encounter an error while building a wheel during the `pip install` process, you may need to install a C++ compiler on your computer.

### For Windows 10/11

To install a C++ compiler on Windows 10/11, follow these steps:

1. Install Visual Studio 2022.
2. Make sure the following components are selected:
   - Universal Windows Platform development
   - C++ CMake tools for Windows
3. Run the installer and select the "gcc" component.

### Pending

- [ ] To change Embeddings Platform
- [ ] To change LLM

