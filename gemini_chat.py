import google.generativeai as genai

genai.configure(api_key = "AIzaSyDhi-Fwvm81Ct46glFmie37NAOBDtYS1_I")

model = genai.GenerativeModel("gemini-pro")

chat = model.start_chat()

while True:
    message = input("You: ")
    response = chat.send_message(message)
    print("Gemini: " + response.text)