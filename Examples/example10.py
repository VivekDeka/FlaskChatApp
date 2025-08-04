import google.generativeai as genai
from PIL import Image

genai.configure(api_key="")

image = Image.open("ai_photo.jpg")

model = genai.GenerativeModel(model_name="gemini-pro-vision")

response = model.generate_content(
    [image, "Describe this image in one detailed sentence"]
)

print("Caption:", response.text)
