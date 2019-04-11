from random import randint
random_user = randint(0, 9)
user_left = 3
while user_left > 0:

     user = int(input("Veuillez entrer un nombre compris entre 0 et 9: "))
     if user == random_user:
           print ("Bravo!tu as choisi le bon numéro")
     elif user != random_user:
           print ("Opss! mauvais numéro reéssayer")
           break
     user_left -= 1
else:
    print ("Désolé, vous avez échoué 3 fois!")  
 
