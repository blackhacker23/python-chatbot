from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a chatbot instance
chatbot = ChatBot('MyChatBot')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot using the English corpus
trainer.train('chatterbot.corpus.english')

# Train the chatbot using additional custom data
trainer.train('path_to_your_custom_corpus')

# Define a function to get a response from the chatbot
def get_response(user_input):
    response = chatbot.get_response(user_input)
    return str(response)

# Main conversation loop
while True:
    user_input = input("You: ")

    # Break the loop if the user says 'exit'
    if user_input.lower() == 'exit':
        break

    response = get_response(user_input)
    print("ChatBot:", response)
