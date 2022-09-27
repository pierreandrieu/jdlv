from jdlv.jdlv import *


def tests_initialisation():
    def test_empty_constructor():
        try:
            jdlv = Jdlv()
            raise Exception("Le constructeur de Jdlv ne doit pas autoriser un constructeur vide")

        except TypeError:
            pass
    test_empty_constructor()


def tests_nombre_cellules():
    pass


def tests_mise_a_jour():
    pass


tests_initialisation()

