'''
# --- Workflow----#
1- Input from user-(Rock, Paper, Scissor)
2- Computer Choice-(Rock, Paper, Scissor)-will choose randomly
3- Result print


#--- Logic ---#
## Cases ##
A- Rock
Rock - Rock = Tie
Rock - Paper = Computer Wins
Rock - Scissor = User Wins

B- Paper
Paper - Rock = User Wins
Paper - Paper = Tie
Paper - Scissor = Computer Wins

C- Scissor
Scissor - Rock = Computer Wins
Scissor - Paper = User Wins 
Scissor - Scissor = Tie
'''
# Importing necessary libraries
import random

# creating a list of items to choose from
itemList = ["Rock", "Paper", "Scissor"]

# creating a function to check the result of the game
def rock_paper_scissor(userChoice, computerChoice):
  if userChoice == computerChoice:
    return "It's a Tie!"
  elif userChoice == "Rock":
    if computerChoice == "Paper":
      return "Computer Wins!"
    else:
      return "User Wins!"
  elif userChoice == "Paper":
    if computerChoice == "Scissor":
      return "Computer Wins!"
    else:
      return "User Wins!"
  elif userChoice == "Scissor":
    if computerChoice == "Rock":
      return "Computer Wins!"
    else:
      return "User Wins!"

# for continuous play, we will use a while loop   
while True:
  # simple message to show the user how to exit the game
  print("Welcome to the game. To exit please type 'exit' or to start the game please press enter.")
  
  # taking input from user to start the game or exit
  startGame = input("Start the game? type 'start' or type 'exit' to quit): ")
  
  if startGame.lower() == 'exit'or startGame.lower() == 'quit' or startGame.lower() == 'e' or startGame.lower() == 'q':
    print("Thanks for playing! Goodbye!")
    break
  elif startGame.lower() == 'start' or startGame.lower() == 's':
    # taking input from user
    userChoice = input('Enter your choice \n1- Rock \n2- Paper \n3- Scissor\n: ')

    # checking if the user input is valid or not
    if userChoice not in itemList:
      print("Invalid input! Please enter Rock, Paper, or Scissor.")
      userChoice = input('Enter your choice \n1- Rock \n2- Paper \n3- Scissor\n: ')

    # generating computer choice randomly using random function
    computerChoice = random.choice(itemList)

    # showing the choices that both user and computer has made.
    print(f"User has Choosen: {userChoice} and Computer has Choosen: {computerChoice} ")
    print("\n")
    # Calling the function and displaying the result
    result = rock_paper_scissor(userChoice, computerChoice)
    print(result)
    print("\n")
  else:
    print("Invalid input! Please type 'start' to start or type 'exit' to quit.")
    print("\n")
  