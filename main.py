import random
import sys

NOMBRE_MIN = 1
NOMBRE_MAX = 0
NB_QUESTIONS = 10

print("Bienvenue dans The Game of Maths.")
nom = input("Comment vous appelez-vous ? ")
if nom == "Larissa":
    print(f"Bonjour {nom}. Vous portez un très joli prénom ")
    print()
else:
    print(f"Bonjour, {nom}.")
    print()

print("Mon jeu consiste en la résolution de calculs mathématiques simples.")
print()
print("Je vous propose 3 difficultés différentes:")
print()
print("Facile : additions")
print("Moyen : soustractions")
print("Difficile : multiplications")
print()
difficulty = input("Choisissez la difficulté : ")
print()



if difficulty == "Facile":
    print("Vous avez choisi la facilité, honte à vous")
    NOMBRE_MAX = 10
elif difficulty == "Moyen":
    print("Vous avez choisi la difficulté moyenne, on acceptera pour cette fois")
    NOMBRE_MAX = 100
else:
    print("Vous avez choisi le mode difficile, bravo à vous !")
    NOMBRE_MAX = 20

print()
decision =input(f"Etes-vous prêt {nom} à commencer le jeu? Il n'est pas trop tard pour renoncer. ")
if decision == "Oui":
    print("Bonne chance!")
    print()
else :
    print("Vous n'en aviez pas les capacités de toute manière")
    print()
    
    sys.exit()
    
    


def poser_question():
    a = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    b = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    o = random.randint(0, 1)
    
    operateur_str = ""
    if difficulty == "Facile" :
        operateur_str ="+"
    elif difficulty == "Moyen":
        operateur_str = "-"
    else:
        operateur_str = "*"

    reponse_str = input(f"Calculez : {a} {operateur_str} {b} = ")
    reponse_int = int(reponse_str)

    calcul = ""
    if operateur_str == "+":
        calcul = a+b
    elif operateur_str =="-":
        calcul = a-b
    else:
        calcul = a*b                                                                                                                              

    if reponse_int == calcul:
        #print("réponse correcte")
        return True
    #else:
       # print("réponse incorrecte")
    return False
    

# a, b

nb_points = 0

for i in range(0, NB_QUESTIONS):
    print(f"Question numéro {i+1} sur {NB_QUESTIONS} ")
    if poser_question():
        print("Réponse correcte")
        nb_points += 1
        
    else:
        print("Réponse incorrecte")
    print()
   
print(f"Votre note est {nb_points}/{NB_QUESTIONS}")

moyenne = int(NB_QUESTIONS/2)

if nb_points == NB_QUESTIONS:
        print("Excellent")
elif nb_points == 0:
        print("Révisez vos maths !")

elif nb_points > moyenne:
    print("Pas mal")
else:
    print("Peut mieux faire")
#Calculez 1 + 5 = 