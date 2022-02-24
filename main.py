# Requirements
#
# Create a header explaining what this program is and what it does and how to use it.
# Have a UI so the user can interface with the chatbot..
# Output to the user the results.
#
# Using training data and training intents or use NLTK -  internal to the code.
# You will need 20 of each.  In NLTK, you should have multiple inputs and multiple outputs for each of these.
# Insure that each work properly.
# Use the data to train your model
# Use the results to give feedback to the user
#
# Place your finished code in github.
# Take a screen shot of your files / code in github
# Submit the zipped project file of your project.
# Submit a video of all functionality.
from nltk.chat.util import Chat, reflections

reflections = {
  "i am"       : "you are",
  "i was"      : "you were",
  "i"          : "you",
  "i'm"        : "you are",
  "i'd"        : "you would",
  "i've"       : "you have",
  "i'll"       : "you will",
  "my"         : "your",
  "you are"    : "I am",
  "you were"   : "I was",
  "you've"     : "I have",
  "you'll"     : "I will",
  "your"       : "my",
  "yours"      : "mine",
  "you"        : "me",
  "me"         : "you"
}

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today ?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"what is your name ?",
        ["I am a chatbot name 'I know'",]
    ],
    [
        r"how are you ?",
        ["I'm doing good, How about You ?",]
    ],
    [
        r"(.*) married ?",
        ["Dwayne Johnson is married to Lauren Hashian since 2019.",]
    ],
    [
        r"How old is Dwayne Johnson?",
        ["Dwayne Johnson was born on May 2, 1972 and is 49 years old.",]
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that","How can I help you?:)",]
    ],
    [
        r"(.*) age?",
        ["I'm a computer program, my age is irreverent.",]
    ],
    [
        r"Did Dwayne Johnson(.*) school?",
        ["Dwayne Johnson went to University of Miami and obtained a Bachelor of General Studies.",]
    ],
    [
        r"(.*) created ?",
        ["My Creator is Ke'Ondrae Mell",]
    ],
    [
        r"(.*) (location|city) ?",
        ['Tempe, AZ',]
    ],
    [
        r"how is the weather (.*)?",
        ["It was pretty cold today. "]
    ],
    [
        r"Does Dwayne Johnson have kids ?",
        ["Dwayne Johnson has 3 kids",]
    ],
    [
        r"(.*)size of (.*)",
        ["Dwayne Johnson is 6 foot 5 inches and is 260lb. "]
    ],
    [
        r"how (.*) health(.*)",
        ["I believe Dwayne Johnson is very health.",]
    ],
    [
        r"(.*) (sports|game) ?",
        ["I'm a very big fan of Dwayne Johnson",]
    ],
    [
        r"who (.*) Dwayne Johnson?",
        ["Dwayne Douglas Johnson is an American actor, businessman, and former professional wrestler."]
    ],
    [
        r"who (.*) (moviestar|actor)?",
        ["I am I know"]
    ],
    [
        r"Who is the greatest actor?",
        ["Dwayne Johnson of course!"]
    ],
    [
        r"quit",
        ["Bye take care. See you soon :) ","It was nice talking with you about stuff. See you soon :)"]
    ],
]

def chat():
    print("Hello, I am a chatbot name 'I know' that is a knowledge base about Dwayne Johnson")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == '__main__':
    chat()