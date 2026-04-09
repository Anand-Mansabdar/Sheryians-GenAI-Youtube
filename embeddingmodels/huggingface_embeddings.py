from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = HuggingFaceEmbeddings(
  model_name = "sentence-transformers/all-MiniLM-L6-v2"
)

lists = [
  "My name is Anand Mansabdar",
  "I am learning GenAI from Sheryians AI School",
  "This is my first video of GenAI",
  "I am enjoying every bit of it"
]

results = embedding.embed_documents(lists)
print(results)