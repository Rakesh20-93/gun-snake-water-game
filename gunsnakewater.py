''' s = snake , g = gun, w = water'''

import random

randnumber=random.randint(1,3)
if randnumber == 1:
    comp = "s"
elif randnumber == 2:
    comp = 'g'
elif randnumber == 3:
    comp = 'w'
    

you = input("chose your item : ")
      
def game(comp,you):
    if comp==you:
        print("This game is Tie !!!")
    if comp=='w':
        if you == 'g':
            print("Compter win This game !!!")
        elif you == 's':
            print("You win this game !!!!")
    if comp=='s':
        if you == 'w':
            print("Compter win This game !!!")
        elif you == 'g':
            print("You win this game !!!!")
    if comp=='g':
        if you == 's':
            print("Compter win This game !!!")
        elif you == 'w':
            print("You win this game !!!!")

print(game(comp,you)) 
print(f"Computer choose {comp}")
