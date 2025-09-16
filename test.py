import google.generativeai as genai
import os

# Load your Gemini API key from environment variable
genai.configure(AIzaSyCrgqlgzJGrUDC1lS4sB0Kf63IThFU7GDY=os.getenv("GEMINI_API_KEY"))

# Example: create a model and get response
model = genai.GenerativeModel("gemini-1.5-flash")

response = model.generate_content("Hello, Gemini!")
print(response.text)
