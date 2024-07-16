import openai

API_KEY = open("openaikey.txt", "r").read()
openai.api_key = API_KEY

conversation = []

def getGPTResponceForInput(input: str):
    message = {"role":"user", "content": input}
    conversation.append(message)

    responce = openai.chat.completions.create(
        model = "gpt-3.5-turbo", 
        messages = conversation
    )
    conversation.append(responce.choices[0].message)

    return responce.choices[0].message.content


def chat():
    while True:
        userInput = input("You: ")
        if userInput == "exit":
            return
        responce = getGPTResponceForInput(userInput)
        print(responce)

chat()