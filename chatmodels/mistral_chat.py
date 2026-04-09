from dotenv import load_dotenv
load_dotenv()


from langchain.chat_models import init_chat_model
from langchain_mistralai import ChatMistralAI

mistral_model = init_chat_model("mistral-medium-latest")
response = mistral_model.invoke("Exlpain 5 advantages of learning GenAI")
print(response.content)

mistral_model = ChatMistralAI(model_name="mistral-medium-latest")
response = mistral_model.invoke("Give me 5 careers to start with zero investment")
print(response.content)