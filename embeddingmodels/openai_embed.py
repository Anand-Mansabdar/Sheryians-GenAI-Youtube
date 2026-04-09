from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings

load_dotenv()

embeddings = OpenAIEmbeddings(
  model="text-embedding-3-large",
  dimensions=64
)

# Emedding a single statement
vector = embeddings.embed_query("I am learning GenAI")
print(vector)


# Embedding multiple documents / statements
lists = [
  "My name is Anand Mansabdar",
  "I am learning GenAI from Sheryians AI School",
  "This is my first video of GenAI",
  "I am enjoying every bit of it"
]
vectors = embeddings.embed_documents(lists)
print(vectors)