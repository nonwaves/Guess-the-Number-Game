#Number Guessing Game
import random
from replit import clear
from ART import logo
def play_game():
  clear()
  print(logo)
  print("Welcome to the number guessing game!")
  # GENERATE RANDOM NUMBER BETWEEN 1-100
  num = random.randint(1,100)
  print("I'm thinking of a number between 1-100.")
  #choose a difficulty level, sets number of attempts
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard'\n")
  tries = 0
  if difficulty == 'easy':
    tries = 10
  elif difficulty == 'hard':
    tries = 5
#Game logic below!
  while tries > 0:
      print(f"You have {tries} guesses")
      guess = int(input("Make a guess: "))
      if guess > num:
        print("Too high.")
        tries -=1
      elif guess < num:
        print("Too low")
        tries -=1
      elif guess == num:
        print("You won!")
        play_again = input("Would you like to play again? type 'y' or 'n': ")
        if play_again == 'y':
          play_game()
        elif play_again == 'n':
          break
  print(f"Not your win today, pal. Number was {num}")
  play_again = input("Would you like to play again? type 'y' or 'n': ")
  if play_again == 'y':
    play_game()
  elif play_again == 'n':
    quit()
play_game()
        