def chatbot():
    print("Chatbot: Hello! Type 'bye' to exit.")

    while True:
        user = input("You: ").lower()

        if user == "hello":
            print("Chatbot: Hi!")

        elif user == "how are you":
            print("Chatbot: I'm fine, thanks!")

        elif user == "what is your name":
            print("Chatbot: My name is SimpleBot.")

        elif user == "who created you":
            print("Chatbot: I was created using Python.")

        elif user == "help":
            print("Chatbot: You can say 'hello', 'how are you', 'what is your name', or 'bye'.")

        elif user == "bye":
            print("Chatbot: Goodbye!")
            break

        else:
            print("Chatbot: Sorry, I don't understand that.")

# Run the chatbot
chatbot()