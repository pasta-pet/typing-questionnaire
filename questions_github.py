import os
import sys
from time import sleep
import json
import random

questions = ['Who is your hero?',
'If you could live anywhere, where would it be?',
'What is your biggest fear?',
'What is your favorite family vacation?',
'What would you change about yourself if you could?',
'What really makes you angry?',
'What motivates you to work hard?',
'What is your favorite thing about your career?',
'What is your biggest complaint about your job?',
'What is your proudest accomplishment?',
'What is your childs proudest accomplishment?',
'What is your favorite book to read?',
'What makes you laugh the most?',
'What was the last movie you went to? What did you think?',
'What did you want to be when you were small?',
'What does your child want to be when he/she grows up?',
'If you could choose to do anything for a day, what would it be?',
'What is your favorite game or sport to watch and play?',
'Would you rather ride a bike, ride a horse, or drive a car?',
'What would you sing at Karaoke night?',
'What two radio stations do you listen to in the car the most?',
'Which would you rather do: wash dishes, mow the lawn, clean the bathroom, or vacuum the house?',
'If you could hire someone to help you, would it be with cleaning, cooking, or yard work?',
'If you could only eat one meal for the rest of your life, what would it be?',
'Who is your favorite author?']
#path here to save responses.
save_path = ''

random_que  = random.choice(questions)
random_que2 = random.choice(questions)
random_que3 = random.choice(questions)
random_que4 = random.choice(questions)

print("PLEASE ANSWER IN FULL SENTENCES")
sleep(10)

words = " HELLO.\n IM HERE TO TEACH YOU CODING.\n BUT FIRST IVE GOT TO ASK YOU A COUPLE QUESTIONS.\n"
for char in words:
    sleep(0.01)
    sys.stdout.write(char)
    sys.stdout.flush()
    
wordser = " \n \n \n \n \n \n So here are your first couple questions.\n And your first question is \n \n ***********************\n \n \n What is your name? \n \n \n"
for char in wordser:
    sleep(0.01)
    sys.stdout.write(char)
    sys.stdout.flush()

global name
name = input()

wordserer = ("So your name is\n" + name + "?\ny or n?\n")
for char in wordserer:
    sleep(0.01)
    sys.stdout.write(char)
    sys.stdout.flush()

confirm = input()

if confirm == "y":
        wordsererer = ("okay cool\n" + confirm + " is what you said " + name + ".")
        for char in wordsererer:
                 sleep(0.01)
                 sys.stdout.write(char)
                 sys.stdout.flush()


wordserererer = ("another question for you\nwhat is your plan for life?\n")

for char in wordserererer:                        
        sleep(0.01)
        sys.stdout.write(char)
        sys.stdout.flush()

belief = input()

wordsy = ("and how old are you?\n")

for char in wordsy:
    sleep(0.01)
    sys.stdout.write(char)
    sys.stdout.flush()

age = input()

wordsys = (random_que + "\n")
for char in wordsys:
    sleep(0.01)
    sys.stdout.write(char)
    sys.stdout.flush()

ans1 = input()

wordsysy = (random_que2 + "\n")
for char in wordsysy:
    sleep(0.01)
    sys.stdout.write(char)
    sys.stdout.flush()
    

ans2 = input()

wordsysys = (random_que3 + "\n")
for char in wordsysys:
    sleep(0.01)
    sys.stdout.write(char)
    sys.stdout.flush()

ans3 = input()

wordsysysy = (random_que4 + "\n")
for char in wordsysysy:
    sleep(0.01)
    sys.stdout.write(char)
    sys.stdout.flush()

ans4 = input()
file_name = "answers for "+ name + ".txt"
completeName = os.path.join(save_path, file_name)

file1 = open(completeName, "w")
file1.write("name = " + name + "\n\n" + "age = " + age + "\n\n" + "plan for life = " + belief + "\n\n" + "answer 1 = " + ans1 + "\n\n" + "answer 2 = " + ans2 + "\n\n" + "answer 3 = " + ans3 + "\n\n" + "answer 4 = " + ans4 )
file1.close()







