from random import shuffle
from replit import clear
from game_data import data   #50 accounts
import art

game_over = False
current_score = 0
shuffle(data)
print(art.logo)

for i in range(len(data)-1):
  if game_over == False:
    name1 = data[i]["name"]
    follower1 = int(data[i]["follower_count"])
    info1 = data[i]["description"]
    origin1 = data[i]["country"]
    
    name2 = data[i+1]["name"]
    follower2 = int(data[i+1]["follower_count"])
    info2 = data[i+1]["description"]
    origin2 = data[i+1]["country"]

    #Follower counts should be removed in final product
    print(f"\nCompare A: {name1}({follower1}), a {info1} from {origin1}.")
    print("\nvs.\n")
    print(f"Against B: {name2}({follower2}), a {info2} from {origin2}.")
    
    answer = input("\nWho has more followers on Instagram? Type 'A' or 'B': ").lower()
    clear()
    print(art.logo)
    if follower1 >= follower2 and answer == "a" :
      current_score += 1
      print(f"You're right! Current score: {current_score}")
    elif follower2 >= follower1 and answer == "b" :
      current_score += 1
      print(f"You're right! Current score: {current_score}")
    else:
      game_over = True
      print(f"That's wrong. Final score: {current_score}")

if current_score == 49:
  print("Got'em all! You've beaten the game. ")
