from random import randint

def banner(): #defines title
  print("""
-------------------------------------------------------------
                  \nNumber Guessing Game\n
-------------------------------------------------------------\n""")

  print("To exit the program, please select the number 0 in the guessing prompt\n") #tells user how to exit program
  
def tryAgain(): #definition to try again
  input("\nSelect enter to try again ")
  
def clearScreen(): #definition to clear the screen
  print("\033[H\033[J", end="")

numberGuessing = True
number = randint(1, 10)
attempts = 0

while numberGuessing: #while loop to keep program running

  clearScreen() #screen clearing definition
  banner() #title banner definition
  attempts += 1 
  guess = int(input("Guess a number between 1 and 10: ")) #prompts user to guess a number between 1 and 10
  
  if guess == number: #states that if user guesses 7, they got it right
    print(f"\nYou're correct!! You found it in {attempts} attempts!")
    numberGuessing = False #ends the while loop
  
  elif guess == (number - 1) or guess == (number + 1): #states that if user guesses 6 or 8, they are close
    print("\nYou're close but not correct")
    tryAgain() #calls try again definition
  
  elif guess < 1 and guess != 0 or guess > 10: #states that if user guesses a number less than one or greater than 10 but isn't zero, they are out of range
    print("\nThis assessment is out of the range")
    tryAgain() #calls try again definition

  elif guess == 0:
    numberGuessing = False
  
  else:
    print("\nThis is not the correct number")
    tryAgain() 

print("\nHope you had a fun time guessing the number. Have a nice day!!")