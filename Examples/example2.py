memory = {}

def chat(input_text):
    memory['last'] = input_text
    
    return f"You said: {input_text}. I remember it!"

print(chat("Hello there!"))

print("Memory:", memory)