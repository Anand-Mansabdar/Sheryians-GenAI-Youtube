from dotenv import load_dotenv 
# to use API KEYS from dotenv
load_dotenv()


# Using Chat Models
from langchain.chat_models import init_chat_model
model = init_chat_model("gpt-4.1")
print(model)
# To check what all things(features) your model provides
response = model.invoke("What is cricket?")
print(response.content)