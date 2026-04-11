import streamlit as st
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

model = ChatMistralAI(model="mistral-small-2506")

prompt = ChatPromptTemplate.from_messages(
  [
    (
      "system","""
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
""",
),
(
  "human","""
Extract information from this paragraph: {paragraph}
""",
),
  ]
)

st.title("Movie Review Analyzer")

paragraph = st.text_area("Enter a detailed movie review")

if st.button("Analyze"):
  if paragraph:
    analysis = prompt.invoke({"paragraph": paragraph})
    response = model.invoke(analysis)
    
    # Parse and format the response
    lines = response.content.strip().split("\n")
    
    for line in lines:
      if line.strip():  # Skip empty lines
        if ":" in line:
          # Split on first colon to separate heading from content
          heading, content = line.split(":", 1)
          st.markdown(f"**{heading.strip()}:** {content.strip()}")
        else:
          st.write(line)
  else:
    st.warning("Please enter a movie review.")