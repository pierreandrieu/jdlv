from jdlv.jdlv import *
import inspect


def tests_initialisation():
    def test_empty_constructor():
        try:
            jdlv = Jdlv()
            raise Exception("Le constructeur de Jdlv ne doit pas autoriser un constructeur vide")

        except TypeError:
            pass

    def test_constructor_has_exactly_one_string_argument():
        signature_construct = str(inspect.signature(Jdlv.__init__))
        args_construct = signature_construct.split(",")
        assert len(args_construct) == 2 and args_construct[-1].split(":")[-1].strip() == "str)"

    test_empty_constructor()
    test_constructor_has_exactly_one_string_argument()


def tests_nombre_cellules():
    pass


def tests_mise_a_jour():
    pass


tests_initialisation()

