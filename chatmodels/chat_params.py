from dotenv import load_dotenv
load_dotenv()


from langchain_mistralai import ChatMistralAI

mistral_model = ChatMistralAI(model_name="mistral-medium-latest", temperature=0, max_tokens=20)
response = mistral_model.invoke("Give me a poem on engineer")
print(response.content)

print("---------------------------------------------")

mistral_model = ChatMistralAI(model_name="mistral-medium-latest", temperature=0.6)
response = mistral_model.invoke("Give me a poem on engineer")
print(response.content)