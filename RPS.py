import random
import pandas as pd 
#This is an Rock - Paper and Scissors game
print("This iS an Rock-Paper-Scissor game ")
print()
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print()
print("Rules for the game are :- \n "
      + "Rock Vs Scissors - Rock Wins\n"
      + "Rock Vs Paper - Paper Wins\n"
      + "Paper Vs Scissor - Scissor Wins\n "
      + "If choices of both  You and Computer are same then this will be consider as draw")
print()
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print()

user_win = 0
computer_win = 0
draws = 0
while True:
      user_input = int(input(" 1 - For Rock \n 2 - for Paper \n 3 - For Scissors \n 4 For Exit the game \n Please enter the choice :-" ) )
      if user_input== 1:
          user_choice = "Rock"
      elif user_input==2:
          user_choice = "Paper"
      elif user_input== 3:
          user_choice = "Scissors"
      elif user_input == 4 :
          exit("Game Exit Successful")
      else :
            print("Please enter a valid choice ")
      
      
      print("The Entered choice is ",user_choice)
      print()
      print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
      print("The computer is making its choice")
      computer_input = random.randint(1,3)
      if computer_input== 1:
          com_choice = "Rock"
      elif computer_input==2:
          com_choice = "Paper"
      else :
          com_choice = "Scissors"
      
      
      print("computer choice is ",com_choice)
      
      print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
     
      
      
      if user_choice == "Rock" and com_choice == "Paper" :
            print("computer wins ")
            computer_win = computer_win + 1
      elif user_choice == "Rock" and com_choice=="Scissors":
            print("You Win")
            user_win = user_win +1
      elif user_choice=="Paper"and com_choice=="Rock":
            print("You win")
            user_win = user_win +1
      elif user_choice=="Paper"and com_choice=="Scissors":
            print("Computer wins")
            computer_win = computer_win + 1
      elif user_choice=="Scissors"and com_choice=="Rock":
            print("Computer win")
            computer_win = computer_win + 1
      elif user_choice=="Scissors"and com_choice=="Paper":
            print('You win')
            user_win = user_win +1
      else :
            print("Both The choices are same ")
            print("Its a Draw")
            draws = draws + 1
            
            
      print("###############################################################################################")
      print("If you want to continue the game (Y/N)")
      answer = input().lower()
      if answer == "n":                     #  if answer in ("n", "N", "no", "No"):
            print("THANK YOU FOR PLAYING")
            # Print the result of the game
            print("You won", user_win, "times")
            print("Computer won", computer_win, "times")
            print("There were", draws, "draws")
            # Create a data frame from a dictionary
            print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
            dict = {'User' : [user_win],
                  'Computer' : [computer_win],
                  'Draws' : [draws]}
            df = pd.DataFrame(dict)
            print(df)
            break
