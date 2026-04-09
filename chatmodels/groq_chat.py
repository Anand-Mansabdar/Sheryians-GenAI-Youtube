# TO use models provided by groq
from dotenv import load_dotenv
load_dotenv()


# Using chat_models
from langchain.chat_models import init_chat_model
groq_model = init_chat_model("groq:openai/gpt-oss-120b") # Necessary to write "groq:" to make the model understand
response = groq_model.invoke("Give me 5 main points about the IPL in cricket")
print(response.content)

print()

# Using Model Class
from langchain_groq import ChatGroq
groq_model = ChatGroq(model="openai/gpt-oss-120b") # No need of writing ":groq" as we are importing CHatGroq directly
response = groq_model.invoke("Just give 5 sideheading about advantages of Electric 2 wheelers")
print(response.content)