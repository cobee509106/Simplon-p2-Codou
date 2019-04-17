from random import randint
x = randint(0,9)
user_answer= int(input("Veuillez entrer un nombre compris entre 0 et 9 "))
if user_answer == x :
    print("Bravo, you Win!!")
else:
    print("Ouuupss!, sorry!")
