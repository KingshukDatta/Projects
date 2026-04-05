# Creating a tic tac toe game in python using GUI
'''
## --Workflow ---##
Start → Show Window → Player clicks a box
       → Write X or O → Check for winner
       → Switch player → Repeat
                       ↓
                  Winner found → Show popup → Close game
'''
# importing necessary library
import tkinter as tk
# we want to use message box to  convey the result
from tkinter import messagebox
'''from tkinter import font'''

# creating a function which will check if the player is won or not
def check_winner():
  for combo in [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]:
    if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] != "":
      buttons[combo[1]].config(bg = "green")
      buttons[combo[2]].config(bg = "green")
      messagebox.showinfo("Tic-Tac_Toe", f"Player {buttons[combo[0]]['text']} wins!")
      root.quit()

# creating a function to toggle between players
def button_click(index):
  if buttons[index]["text"] == "" and not winner:
    buttons[index]['text'] = current_player
    check_winner()
    toggle_player()

# to change current player
def toggle_player():
  global current_player
  current_player = "X" if current_player == "O" else "O"
  label.config(text=f"player {current_player}'s turn")

# creating the main window
root = tk.Tk()
root.title("Tic-Tac_Toe")

# creating buttons for the tic tac toe grid
buttons = [tk.Button(root, text = "", font =("normal", 25), width = 6, height=2, command= lambda i=i: button_click(i)) for i in range(9)]

# arranging the buttons in a grid using enumerate function
for i, button in enumerate(buttons):
  button.grid(row = i //3, column = i %3)
  
current_player = "X"
winner = False
label = tk.Label(root, text=f"Player {current_player}'s turn", font=("normal", 16))
label.grid(row=3, column=0, columnspan=3)

root.mainloop()
