import google.generativeai as genai

genai.configure(api_key="AIzaSyCWwDKIkDUx5namNldIyUhPn4xVfPeKFGk")

model = genai.GenerativeModel(model_name = "gemini-1.5-flash")

response = model.generate_content("Suggest 3 innovative SaaS ideas using Python and AI")

print("Gemini Response:", response.text)