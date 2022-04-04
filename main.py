#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from random import randint
from art import logo 


EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(guess,answer,turns):
  if guess<answer:
    print("too low ")
    
    return turns-1
  elif guess>answer:
    print("too high")
    return turns-1
  else:
    print(f"you got the answer {answer}")


def set_difficulty():
  global turns 
  level = input("choose difficulty easy or hard: ")
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS 



def game():
  print(logo)
  print("welcome to the guessing game")
  print("i'm thinking of a number between 1 and 100")
  answer = randint(1,100)
  print(f"the correct answer is {answer}")
  
  
  turns = set_difficulty()
  # print(f"you have {turns} attempt to make the guess:")
  
  guess = 0
  while guess!= answer:
      print(f"you have {turns} attempt to make the guess:")
      guess = int(input("make a guess:"))
    
      turns = check_answer(guess, answer,turns)
      if turns ==0:
        print("you've run out of guess , you lose ")
        return 

game()