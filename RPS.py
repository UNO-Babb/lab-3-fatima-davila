#RPS.py
#Name:Fatima Davila
#Date:2/9/2025
#Assignment:lab 3
import random

def main():
  wins = 0
  ties = 0
  losses = 0
  #Create a loop that continues as long as the user wants to play.
  #User can play as many games as they wish.
  
  #Randomly choose the computer between 'R', 'P', or 'S'
  print("\n")
  print("1) Rock")
  print("2) paper")
  print("3) scissors")
  selection = int(input("Enter Throws: "))
  if (selection == 1):
    player_throw = "rock"
  elif (selection == 2):  
    player_throw = "paper"
  else:
    player_throw = "scissors"
  print("\n")
  print("player throws", player_throw)
  throws = ["Rock, Paper, Scissors"]
  ai_throw = random.choice(throws)
  print("AI throws", ai_throw)
  if (player_throw == ai_throw):
    print("Tie game!")
  elif (player_throw == "rock"):
    if (ai_throw == " paper"):
      print("AI Won!")
      if (ai_throw == "scissors"):
        print("Player Won!")
  elif (player_throw == "Paper"):
    if(ai_throw == "scissors"):
      print("AI Won!")
    elif(ai_throw == "rock"):
      print("Player Won!")
  elif(player_throw == "Rock"):
    if(ai_throw == "paper"):
      print("Player Won!")
    elif(ai_throw == "scissors"):
      print("Ai Won!")
  
  play_again =input("play again? y/n: "). lower()
  if not play_again == "y":
    running = False

    print("thanks for playing!")


 


    
  #Prompt the user for their RPS selection
  #Determine winner and state what happened to the user
  #Ask the user if they would like to play again.

  #In the end, print the stats
  print("Wins \t Ties \t Losses")
  print("---- \t ---- \t ------")
  print(wins, "\t", ties , "\t", losses)

if __name__ == '__main__':
  main()
