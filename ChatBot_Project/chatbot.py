from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

load_dotenv()

model = ChatMistralAI(model="mistral-small-2506", temperature=0.9)

history = [
  SystemMessage(content="You are a funny AI agent")
]

print("Welcome to the AI chatbot... Type Ctrl+C to exit")
while True:
  
  prompt = input("Your message: ")
  history.append(HumanMessage(content=prompt))
  
  if prompt == "0":
    break
  
  response = model.invoke(history)
  history.append(AIMessage(content=response.content))
  print("Bot: ",response.content)
print(history)