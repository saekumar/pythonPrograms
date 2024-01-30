# Define a function to greet the user
def greet():
    print("Hi! I'm a laptop service chat bot. How can I help you today?")

def chat():
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Bot: Goodbye!")
            break
        else:
            print("Bot: I'm sorry, I don't know how to help with that. Can you provide more information?")


greet()


chat()
