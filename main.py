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

print("You're at a cross road. Will you go left, or right? ")

left_or_right = input()

if left_or_right.lower() == "left":
  print('You come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.')
else:
  print("You fell into a hole and perished. \nGAME OVER")
  quit()

swim_or_wait = input()

if swim_or_wait.lower() == "wait":
  print('You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, and one blue. Which color do you choose?.')
else:
  print("You were attacked by a killer trout and perished. \nGAME OVER")
  quit()

color_door = input()

if color_door.lower() == "yellow":
  print('You open the yellow door and are confronted with a treasure so vast, you cannot see the end of it. You are rich beyond your wildest dreams! \nYOU WIN!')
elif color_door.lower() == "red":
  print("The door knob is warm to the touch. It gets hotter as you twist the knob- you rip open the door, and behind it is a raging fire! You try to escape, but are not fast enough. The smoke fills your lungs, and you collapse. \nGAME OVER")
  quit()
elif color_door.lower() == "blue":
  print("You open the blue door, and a rabid beast like you've never seen jumps through, knocking you over. It is too large, and you cannot defend yourself. \n GAME OVER")
  quit()
else:
  print("Not an option. The house explodes. \n GAME OVER")
