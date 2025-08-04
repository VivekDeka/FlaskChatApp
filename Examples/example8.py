import markovify

sample_text = """
Python is an amazing programming language. It’s used for web development, data science, and artificial intelligence.
Many developers enjoy its readability and simplicity. With powerful libraries like pandas and TensorFlow, Python is great for rapid development.
"""

text_model = markovify.Text(sample_text)

print("Generated sentence: ", text_model.make_sentence())