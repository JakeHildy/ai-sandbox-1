from langchain.document_loaders import TextLoader
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores.chroma import Chroma
from dotenv import load_dotenv

load_dotenv()

# Embedding
embeddings = OpenAIEmbeddings()
# emb = embeddings.embed_query("hi there")


# Load and split the text
text_splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=200,
    chunk_overlap=0
)
loader = TextLoader("facts.txt")
docs = loader.load_and_split(
    text_splitter=text_splitter
)

db = Chroma.from_documents(
    docs,
    embedding=embeddings,
    persist_directory="emb"
)

results = db.similarity_search("What is an interesting fact about bees", k=2)

for result in results:
    print("\n")
    print(result.page_content)

