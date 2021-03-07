rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

choice = ["rock", "paper", "scissors"]
cpu_choice = random.randint(0, len(choice))
cpu_choice = choice[cpu_choice - 1]

player_choice = int(input("Rock(1), Paper(2) or Scissors(3)? "))
if(player_choice < 1 or player_choice > 3):
  print("You picked an invalid number. You lose!")
else:
  player_choice = choice[player_choice - 1]

  if(player_choice == "rock"):
    print(rock)
  elif(player_choice == "paper"):
    print(paper)
  else:
    print(scissors)

  if(cpu_choice == "rock"):
    print("CPU chooses:\n" + rock)
  elif(cpu_choice == "paper"):
    print("CPU chooses:\n" + paper)
  else:
    print("CPU chooses:\n" + scissors)

  if(player_choice == cpu_choice):
    print("It's a draw!")
  elif(player_choice == "rock" and cpu_choice != "paper"):
    print("You win!")
  elif(player_choice == "paper" and cpu_choice != "scissors"):
    print("You win!")
  elif(player_choice == "scissors" and cpu_choice != "rock"):
    print("You win!")
  else:
    print("You lose!")
