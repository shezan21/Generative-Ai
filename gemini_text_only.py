import google.generativeai as genai

genai.configure(api_key= "AIzaSyDhi-Fwvm81Ct46glFmie37NAOBDtYS1_I")

model = genai.GenerativeModel("gemini-pro")

response = model.generate_content("What is the meaning of life?")
print(response.text)