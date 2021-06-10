import random
from os import system
from art import logo, vs
from game_data import data

score = 0
while True:
  system("cls")
  print(logo)
  if score > 0:
    print(f"You're right! Current score: {score}")
  first_celebrity = data[random.randint(0, len(data) - 1)]
  second_celebrity = data[random.randint(0, len(data) - 1)]
  while first_celebrity["follower_count"] == second_celebrity["follower_count"]:
    second_celebrity = data[random.randint(0, len(data) - 1)]
  print(f'Compare A: {first_celebrity["name"]}, {first_celebrity["description"]}, from {first_celebrity["country"]}.')
  print(vs)
  print(f'Compare B: {second_celebrity["name"]}, {second_celebrity["description"]}, from {second_celebrity["country"]}.')
  player_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
  while player_choice != "a" and player_choice != "b":
    print("Please provide a valid input.")
    player_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
  if player_choice == "a":
    if first_celebrity["follower_count"] > second_celebrity["follower_count"]:
      score +=1
    else: 
      system("cls")
      print(logo)
      print(f"Sorry, that is wrong. Final score: {score}")
      break
  else:
    if first_celebrity["follower_count"] < second_celebrity["follower_count"]:
      score +=1
    else: 
      system("cls")
      print(logo)
      print(f"Sorry, that is wrong. Final score: {score}")
      break