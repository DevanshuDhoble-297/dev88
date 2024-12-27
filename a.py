import google.generativeai as genai

genai.configure(api_key="AIzaSyDSw5Gz4gwI2PW36JzuYBgZRrJTBZAwemk")

model = genai.GenerativeModel(
    model_name="gemini-1.5-pro"
)

chat = model.start_chat(history=[])
response = chat.send_message("Test message")
print(response.text)
