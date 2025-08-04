import spacy

nlp = spacy.load("en_core_web_sm")

doc = nlp("Python simplifies AI development with powerful libaries and tools")

keywords = [token.text for token in doc if token.is_alpha and not token.is_stop]

print("Keywords:", keywords)

