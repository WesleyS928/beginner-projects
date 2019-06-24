'''rock, paper, scissors'''
import random
choices = ['rock', 'paper', 'scissors']
question = input("Rock, paper, or sccisors?")
print("You chose:" + question)
print("Your opponents choice:" + random.choice(choices))
if(question == random.choice(choices)):
        print("It's a tie!")
if(question == 'rock' and random.choice(choices) == 'scissors'):
    print("You win! :)")
if(question == 'paper' and random.choice(choices) == 'scissors'):
    print("You lost :(")
if(question == 'scissors' and random.choice(choices) == 'rock'):
    print("You win! :)")
if(question == 'paper' and random.choice(choices) == 'rock'):
    print("You win! :)")
if(question == 'rock' and random.choice(choices) == 'paper'):
    print("You lose! :)")
if(question == 'scissors' and random.choice(choices) == 'paper'):
    print("You win! :)")
