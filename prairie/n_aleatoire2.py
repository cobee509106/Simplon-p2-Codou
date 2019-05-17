from random import randint
random_user = randint(0 , 9)
user_answer = 3
while user_answer > 0:

     user = int(input("Veuillez entrer un nombre compris entre 0 et 9: "))
     if user == random_user:
           print ("Bravo!tu as choisi le bon numéro")
           break
     if user > random_user:
           print ("vous êtes sorti de l'intervalle 0 et 9")
     elif user != random_user:
            print ("Opss! mauvais numéro reéssayer")  
     user_answer -= 1
else:
    print ("Désolé, vous avez échoué 3 fois!")  
 
