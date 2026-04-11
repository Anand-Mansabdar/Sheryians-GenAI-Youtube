from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

model = ChatMistralAI(model="mistral-small-2506")
prompt = ChatPromptTemplate.from_messages(
[  ("system", """
   You are an expert movie analyst.

Your task is to carefully read the given movie description and extract the most useful information.

Return the output in the following format:

Movie Name: <movie name>
Director: <director name>
Lead Cast: <main actors>
Genre: <genre>
Release Year: <year>
Duration: <duration if mentioned>
Main Character: <main character>
Theme: <main plot or central idea>
Key Highlights: <important technical, emotional, visual, or storytelling elements>
Overall Tone: <tone of the paragraph>
Generated Summary: <2-3 line easy-to-understand summary>

Rules:
- Only use details clearly present in the paragraph
- If something is missing, write "Not mentioned"
- Keep the generated summary concise and meaningful
- Maintain a professional movie-review style

Movie Summary:
"""), 
("human", """
  Extract information from this paragraph: {paragraph} 
""")]
)

paragraph = input("Enter a detailed movie review: ")

analysis = prompt.invoke(
  {"paragraph": paragraph}
)

response = model.invoke(analysis)

print(response.content )