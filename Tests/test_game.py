import unittest
from classes.Game import Game
from tkinter import *


class MyTestCase(unittest.TestCase):
    def test_something(self):
        game = Game(200, 2, 1)

        while game.winner == "":
            self.assertTrue(game.jeu_ordinateur() > 0)

    def test_something_2(self):
        game = Game(33, 2, 1)
        game.afficher_restant()

    def test_something_3(self):
        game = Game(1, 2, True)
        game.pc_play_first()
        self.assertEqual("humain", game.winner)

    def test_something_5(self):
        game = Game(1, 2, False)
        game.pc_play_first()
        self.assertEqual(game.nb_restantes, 1)

    def test_all(self):
        window = Tk()

        window.title("Welcome to LikeGeeks app")

        window.geometry('350x200')

        lbl = Label(window, text="Hello")

        lbl.grid(column=0, row=0)

        txt = Entry(window, width=10)

        txt.grid(column=1, row=0)

        def clicked():
            res = "Welcome to " + txt.get()

            lbl.configure(text=res)

        btn = Button(window, text="Click Me", command=clicked)

        btn.grid(column=2, row=0)

        window.mainloop()
        self.assertEqual(True,True)


if __name__ == '__main__':
    unittest.main()
