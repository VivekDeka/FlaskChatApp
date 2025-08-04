import google.generativeai as genai

genai.configure(api_key="AIzaSyCWwDKIkDUx5namNldIyUhPn4xVfPeKFGk")

model = genai.GenerativeModel(model_name = "gemini-1.5-flash")


code_snippet = '''
    def multiply(x, y):
        return x*y
'''

prompt = f"Review this python function and suggest improvement: \n {code_snippet}"
response = model.generate_content(prompt)

print("Review: ", response.text)
