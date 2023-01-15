# Exercice 1

def display_message():
  print("We are learning the fullstack python django bootcamp")

display_message()

# Exercice 2

def favorite_book(title):
  print(f"One of my favorite books is {title}")
favorite_book("40 RULES OF LOVE (D’ELIF ŞAFAK)")

# Exercice 3

def describe_city(ville, pays):
  print(f"{ville} is in {pays}")
describe_city("Ouagadougou", "BURKINA FASO")

# Exercice 4


import random
from random import randint
def randomNumber(a):
  randomNumb = random.randint(1, 100)
  if a == randomNumb:
    print(f" Success!!! \n number {a} and the random number {randomNumb}")
  else:
    print("")
    print(f" failure... The user number is {a} and the random number is {randomNumb}")
randomNumber(99)

# Exercice 5




def make_shirt(size=100, text="J'aime Python"):
  print(f"The size of the shirt is {size} and the text is {text}")
make_shirt()

# Exercice 6

magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
def show_magicians():
    for i in range(len(magician_names)):
        print(magician_names[i])

def make_great():
    for i in magician_names:
        i = i + " the Great"
        print(i)
make_great()

#Exercice 7
import random
from random import randint


def get_random_temp(saison):
    if saison == "hiver":
        tmpvalue = random.randint(0, 16)
    elif saison == "automne":
        tmpvalue = random.randint(16, 23)

    elif saison == "printemps":
        tmpvalue = random.randint(24, 32)

    elif saison == "ete":
        tmpvalue = random.randint(32, 40)
    else:
        tmpvalue = random.randint(-10, 0)
    return tmpvalue


def main():

    saison = input("Veiller saisir votre saison actuelle : ")
    if saison == saison:

        randtmp = get_random_temp(saison)
        print(f"la temperature actuelle est de {randtmp} dégré celsus nous en {saison}")
        if randtmp < 0:
            print("Brrr, c'est glacial ! Portez des couches supplémentaires aujourd'hui")
        elif randtmp >0 and randtmp < 16:
            print("Assez froid ! N'oubliez pas votre manteau")
        elif randtmp >=16 and randtmp <= 23:
            print("Un peut frais cas même mais beau temps")
        elif randtmp >=24 and randtmp < 32:
            print("Tres beau temps")
        elif randtmp >=32 and randtmp < 40:
            print("Quel challeur ! il fau la clim!!!")
        else:
            print("Mauvais temps trop de chaleur")
    else:
        print("aucune saison")
main()