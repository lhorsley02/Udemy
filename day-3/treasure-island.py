print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

path_input = input("\nLets start our journey.\nYou find yourself on a forest path that splits in two before you. \nWhich path will you chose? Left or Right? \n")

path = path_input.lower()
# If left, mauled by a tiger, you lose
# If right, you follow a path to the edge of a lake
if path == "left":
  print(">>>\nYou follow the path to your left through the trees and it begins to get dark. \nThere seems to be no end in sight. As you continue, a large tiger ambushes you. \n\nGame Over.\n")
elif path == "right":
  print(">>>\n\nYou choose to follow the path to your right. \nAfter a delightful walk through the forest, you come \nto the edge of a lake.\n")
  
  print("As you look around, you see an island with a \ncastle in the center of the lake. You decide you would \nlike to investigate the castle but need a way across.\n")
  
  lake_input  = input("You see a boat slowly drifting towards the shore. \nThe boat will take an extra 10 mins to reach the shore. \nThere is also the option to swim across the lake instead of waiting for the boat. \n\nWhich do you choose? Wait or Swim? \n")

  lake = lake_input.lower()

# If swim, captured by the kraken and drowned, you lose
# If wait, you cross safely and arrive at the island. 
  if lake == "swim":
    print(">>>\n\nYou jump into the lake and begin to swim towards the castle. \nYou are actually swimming quite quickly and should get there \nin no time. However, about halfway across, you feel something grab your leg. \nThe Kraken drags you under and you drown. \n\nGame Over.\n")
    
  elif lake == "wait":
    print(">>>\n\nYou wait patiently for the boat to drift to shore. \nWhen it arrives, you climb in and find the oar. You quickly and safely \ncross the lake, arriving at the island with no trouble. You make \nyour way to the main door, and seeing as the castle seems to be \nabandoned, you open the door and walk in.\n")
    
    print("You find yourself faced with three different doors. \nIn the center, there is a bright white and gold door, with an ornate handle. \nOn your left, there is a solid dark steel door, one that looks like it goes to a dungeon. \nThe last one, on your right, is an old wooden door in the corner, \novergrown with vines and other greenery.\n")
    
    doors_input = input("Which door do you choose? Left, Center, or Right?\n")

    doors = doors_input.lower()

# If Golden door, you open it to find the door was set for a trap, you are shot by arrows. You lose
# If Dungeon door, you open it only to see a trapped dragon spit fire at you. you lose.
# If Wooden door overgrown with vines, you found the treasure chest under a shine of light, you win

    if doors == "left":
      print(">>>\n\nYou approach the dungeon door, and behind it there is a spiral \nset of stairs downwards. You follow the stairs and find yourself \nin a large dark room. You find a torch and light it, which lights up the dungeon. \nBut it also alerts a giant sleeping dragon, which when alarmed, \nspits fire at you and roasts you like rotisserie chicken. \n\nGame Over.\n")
      
    elif doors == "center":
      print(">>>\n\nYou approach the golden door, hoping for riches beyond \nyour wildest dreams to be behind the door. Instead, when you open \nthe door, you are met with a lovely arrow to the face. \n\nGame Over.\n")
      
    elif doors == "right":
      print(">>>\n\nYou approach the overgrown door in the corner, and slowly turn the handle. \nWhen the door is open, you find yourself in an indoor greenhouse, \nfull of greenery and streams, and, at the very center, illuminated \nby a ray of light, is the treasure you have been searching for. \n\nYou Win!\n")
      print("\nThanks for playing!\n")

