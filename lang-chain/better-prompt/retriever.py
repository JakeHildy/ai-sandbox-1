from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.chains.retrieval import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI()
# loader = WebBaseLoader("https://docs.smith.langchain.com/user_guide")
loader = WebBaseLoader("https://api.python.langchain.com/en/latest/prompts/langchain_core.prompts.base.BasePromptTemplate.html#langchain_core.prompts.base.BasePromptTemplate")
embeddings = OpenAIEmbeddings()
text_splitter = RecursiveCharacterTextSplitter()

# 1. Load docs using the loader
docs = loader.load()

# 2. Split the documents into smaller documents
documents = text_splitter.split_documents(docs)

# 3. Create a vector store from the documents
vector = FAISS.from_documents(documents, embeddings)

# 4. Create a retriever from the vector store
retriever = vector.as_retriever()

prompt = ChatPromptTemplate.from_template("""Answer the following question based only on the provided context:

<context>
{context}
</context>

Question: {input}""")


# 5. Create a document chain
document_chain = create_stuff_documents_chain(llm, prompt)

# 6. Create a retrieval chain
retrieval_chain = create_retrieval_chain(retriever, document_chain)

response = retrieval_chain.invoke({"input": "Write a 1 paragraph summary on BasePromptTemplate"})
print(response["answer"])

