from textblob import TextBlob

text =  TextBlob("I absolutely love learning Python with AI")

print("Sentiment polarity", text.sentiment)