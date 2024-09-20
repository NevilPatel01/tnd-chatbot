""" 
FAQ Bot for The New Developers Club Discord Server.

This is a FAQ Bot for The New Developers Club which respond club member's FAQ questions,
and answer them by matching questions from the files, process the user input and return 
the most appropriate response. This bot make easier to address common questions in the server.

Nevil Patel, 12th September 2024
Sam Scott, Mohawk College, May 2023
"""

""" My Topic is The New Developers Club Discord Server, my all questions and answers 
are created and/or refined by myself with taking permissions from other club executives.
So, I don't have any specific reference for my questions and answers, the nearest reference
of my all questions and answers are general conversation in our discord server. I refined 
the question to make it detailed and nuanced as it asked in the requirements.
"""

import string

def file_input(filename):
    """Loads each line of the file into a list and returns it."""
    lines = []
    with open(filename) as file: # opens the file and assigns it to a variable
        for line in file:
            lines.append(line.strip()) # the strip method removes extra whitespace
    return lines


def load_FAQ_data():
    """This method returns a list of questions and answers. The
    lists are parallel, meaning that intent n pairs with response n."""

    try:
        questions = file_input('ques.txt')
        answers = file_input('answers.txt')
        return questions, answers
    except Exception: 
        return -1

def preprocess(text):
    """Processing strings to handle spaces, case, and punctuation for better understanding of questions."""
    filter_text = text.lower().translate(str.maketrans("", "", string.punctuation)).replace(" ", "")
    return filter_text.split()

def understand(utterance):
    """Processes the user input to determine the best matching intent index.
    The user's input is compared to each question to find the best match.
    It return the index of the match question from the question.txt file or if it doen't match it returns -1.
    """
    global intents # global 'intents' list

    # Preprocess the user's input
    processed_input = preprocess(utterance)
    # Iterate over the list of questions and find the best match
    for i in range(len(intents)):
        processed_question = preprocess(intents[i]) # Preprocess the question
        if processed_question == processed_input: # Check if user's question matches any questions from questions.txt
            return i # return the index of question

    # If no match is found, return -1
    return -1

def generate(intent):
    """This function returns an appropriate response given a user's
    intent."""

    global responses # declare that we will use a global variable

    if intent == -1:
        return "Sorry, It seems like your message doesn't match anything I know. But don't worry, I'm here to help! Feel free to rephrase or ask about something related to The New Developers Club, and I'll do my best to assist you."


    return responses[intent] # return the appropriate response for the best matched intent

## Load the questions and responses
intents, responses = load_FAQ_data()

## Main Function

def main():
    """Implements a chat session in the shell."""
    print("👋 Hello! Welcome to The New Developers Club! 💻✨")
    print("We're all about helping developers grow and succeed. 🚀")
    print("If you need anything, feel free to ask! 🤔💬")
    print("When you're ready to head out, just say 'goodbye'. 👋")
    print()
    utterance = ""
    while True:
        utterance = input(">>> ") # prompt user for input
        if utterance == "goodbye":  # Exit
            print("Goodbye! Nice talking to you!")
            break
        else:
            intent = understand(utterance)  # process user input
            response = generate(intent)  # generate response
            print(response)
        print()


## Run the chat code
# the if statement checks whether or not this module is being run
# as a standalone module. If it is beign imported, the if condition
# will be false and it will not run the chat method.
if __name__ == "__main__":
    main()