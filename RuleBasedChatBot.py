print("ChatBot: Hello! Welcome to my chatbot.")
print("ChatBot: You can ask me simple questions.")
print("ChatBot: Type 'bye' to exit.\n")

while True:
    user_input = input("You: ").lower()

    if "hello" in user_input or "hi" in user_input or "hey" in user_input:
        print("ChatBot: Hello! How can I help you?")

    elif "your name" in user_input or "who are you" in user_input:
        print("ChatBot: I am a simple rule-based chatbot.")

    elif "how are you" in user_input:
        print("ChatBot: I am fine! Thank you for asking.")

    elif "python" in user_input:
        print("ChatBot: Python is a popular programming language.")

    elif "time" in user_input:
        print("ChatBot: Sorry, I cannot provide the current time.")

    elif "help" in user_input:
        print("ChatBot: Sure! Ask me about Python, my name, or greetings.")

    elif "bye" in user_input or "exit" in user_input:
        print("ChatBot: Goodbye! Have a nice day.")
        break

    else:
        print("ChatBot: Sorry, I don't understand that. Please try again.")
