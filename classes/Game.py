from .NoDrawException import NoDrawException


class Game:

    def __init__(self, total_alum: int, max_draw: int, pc_first: bool):
        self.nb_restantes = total_alum
        self.max_draw = max_draw
        self.pc_first = pc_first
        self.winner = ""

    def get_winner(self) -> str:
        return self.winner

    def jeu_ordinateur(self) -> int:
        s = self.max_draw + 1
        t = (self.nb_restantes - s) % (self.max_draw + 1)
        while t != 0:
            s -= 1
            t = (self.nb_restantes - s) % (self.max_draw + 1)
        prise = s - 1

        if prise == 0:
            prise = 1

        self.nb_restantes -= prise

        if self.nb_restantes == 0:
            self.winner = "humain"

        return prise

    def jeu_joueur(self, nb: int):
        if (nb > self.max_draw) | (nb <= 0):
            raise NoDrawException
        else:
            self.nb_restantes -= nb

        if self.nb_restantes == 0:
            self.winner = "ordinateur"

    def afficher_vainquer(self):
        print("\n le gagnant est " + self.winner)

    def pc_play_first(self):
        if self.pc_first:
            z = self.jeu_ordinateur()
            print(" le pc joue en premier ! il prend "+z.__str__())
            self.afficher_restant()

    def afficher_restant(self):
        back = self.nb_restantes

        per_ligne = 20

        while back > per_ligne:
            for t in range(0, per_ligne):
                print(" O ", end="")
            print("\n")
            for t in range(0, per_ligne):
                print(" | ", end="")
            print("\n")
            back -= per_ligne

        for t in range(0, back):
            print(" O ", end="")
        print("\n")
        for t in range(0, back):
            print(" | ", end="")
