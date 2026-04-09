from dotenv import load_dotenv 
# to use API KEYS from dotenv
load_dotenv()


# Using Chat Models - OpenAI
from langchain.chat_models import init_chat_model
# model = init_chat_model("gpt-4.1")
# print(model)
# # To check what all things(features) your model provides
# response = model.invoke("What is cricket?")
# print(response.content)


# Using a Model CLass
# from langchain_openai import ChatOpenAI
# model2 = ChatOpenAI(model="gpt-4.1")
# response2 = model2.invoke("Explain cricket rules in simple terms?")
# print(response2.content)


# Using Gemini Models (chat models)
gemini_model = init_chat_model("google_genai:gemini-2.5-flash-lite")

gemini_response = gemini_model.invoke("Exlain me about the ongoing situation of Iran-Israel War")
print(gemini_response.content)

# Using Model Class
from langchain_google_genai import ChatGoogleGenerativeAI
gemini_model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")
gemini_response = gemini_model.invoke("Give me 5 main points to differentiate between an ML enginner and GenAI Engineer")
print(gemini_response.content)