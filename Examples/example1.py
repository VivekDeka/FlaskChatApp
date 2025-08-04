from transformers import pipeline

summarizer = pipeline("summarization", model = "sshleifer/distilbart-cnn-12-6")

text = """
Python has become one of the most popular programming languages in the world due to its simplicity, readability, and wide range of libraries and frameworks. 
It is used in diverse fields such as web development, data science, machine learning, artificial intelligence, scripting, automation, and more.
The active community and constant updates have made Python a favorite among both beginners and experienced developers.
"""
        
summary = summarizer(text, max_length = 40, min_length = 10, do_sample = False)

print(f"Summary:, {summary[0]['summary_text']}")
