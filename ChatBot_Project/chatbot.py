from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI

load_dotenv()

model = ChatMistralAI(model="mistral-small-2506", temperature=0.9)

history = []

print("Welcome to the AI chatbot... Type Ctrl+C to exit")
while True:
  
  prompt = input("Your message: ")
  history.append(prompt)
  
  if prompt == 0:
    break
  
  response = model.invoke(history)
  history.append(response.content)
  print("Bot: ",response.content)
  
  