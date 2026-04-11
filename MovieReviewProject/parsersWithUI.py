import streamlit as st
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel
from typing import List, Optional
from langchain_core.output_parsers import PydanticOutputParser

load_dotenv()

model = ChatMistralAI(model="mistral-small-2506")

# Creating Schema
class Movie(BaseModel):
    title: str
    release_year: Optional[int]
    genre: List[str]
    director: Optional[str]
    cast: List[str]
    rating: Optional[float]
    summary: str


parser = PydanticOutputParser(pydantic_object=Movie)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
Extract movie information from the paragraph.
{format_instructions}
""",
        ),
        (
            "human",
            """
{paragraph}
""",
        ),
    ]
)

st.title("CineMind")

paragraph = st.text_area("Enter a detailed movie review")

if st.button("Analyze"):
    if paragraph:
        analysis = prompt.invoke(
            {
                "paragraph": paragraph,
                "format_instructions": parser.get_format_instructions(),
            }
        )

        response = model.invoke(analysis)
        st.write(response.content)
    else:
        st.warning("Please enter a movie review.")