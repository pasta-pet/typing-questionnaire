import os
import sys
from time import sleep

save_path = 'PUT FILEPATH HERE'



words = " HELLO.\n IM HERE TO TEACH YOU CODING.\n BUT FIRST IVE GOT TO ASK YOU A COUPLE QUESTIONS.\n"
for char in words:
    sleep(0.05)
    sys.stdout.write(char)
    sys.stdout.flush()
    
wordser = " \n \n \n \n \n \n So here are your first couple questions.\n And your first question is \n \n ***********************\n \n \n What is your name? \n \n \n"
for char in wordser:
    sleep(0.05)
    sys.stdout.write(char)
    sys.stdout.flush()

name = input()

wordserer = ("So your name is\n" + name + "?\ny or n?\n")
for char in wordserer:
    sleep(0.05)
    sys.stdout.write(char)
    sys.stdout.flush()

confirm = input()

if confirm == "y":
        wordsererer = ("okay cool\n" + confirm + " is what you said " + name + ".")
        for char in wordsererer:
                 sleep(0.05)
                 sys.stdout.write(char)
                 sys.stdout.flush()


wordserererer = ("another question for you\nwhat is your plan for life?\n")

for char in wordserererer:                        
        sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()

belief = input()

file_name = "answers for "+ name + ".txt"
completeName = os.path.join(save_path, file_name)

file1 = open(completeName, "w")
file1.write(name + "\n\n" + belief)
file1.close()








