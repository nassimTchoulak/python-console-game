from classes.Game import Game

total_alumette = 0

while total_alumette < 10 or total_alumette > 60:
    try:
        total_alumette = int(input("Entrez un nombre max d'allumette au depart entre 10 et 60."))
    except:
        print("saisie incorrecte")
        print(total_alumette)

max_draw = 0

while max_draw <= 1:
    try:
        max_draw = int(input("Entrez un nombre max retirable > 1 "))
    except:
        print("saisie incorrecte")

pc_first = 0


try:
        pc_first = int(input("si pc first 1 sinon moi first  "))
except:
        print("saisie incorrecte")

print("la partie commence avec all = " + total_alumette.__str__() + " et max = " + max_draw.__str__())
game = Game(total_alumette, max_draw, pc_first)
game.pc_play_first()

my_draw = 0
z = 0

while game.winner == "":
    my_draw = 0
    while my_draw == 0:
        try:
            my_draw = int(input("\n \nveuillez introduire votre nombre "))
            game.jeu_joueur(my_draw)
        except:
            print("saisie incorrecte")
            my_draw = 0

    game.afficher_restant()
    z = game.jeu_ordinateur()
    print(" \n \nle pc joue aussi ! il prend " + z.__str__())
    game.afficher_restant()

print("le vainquer est " + game.winner)
