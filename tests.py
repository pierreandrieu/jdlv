from jdlv.jdlv import *
import inspect


def tests_initialisation():
    """
    Série de tests concernant le constructeur de la classe Jdlv
    """
    def test_empty_constructor():
        """
        Vérifie que le constructeur vide renvoie bien une exception TypeError
        :return:
        """
        try:
            jdlv = Jdlv()
            raise Exception("Le constructeur de Jdlv ne doit pas autoriser un constructeur vide")

        except TypeError:
            pass

    def test_constructor_has_exactly_one_string_argument():
        signature_construct = str(inspect.signature(Jdlv.__init__))
        # Recuperation de la signature du constructeur. Exemple de sortie : '(self, file_path: str)'
        args_construct = signature_construct.split(",")

        # Verification qu'il y a exactement deux arguments (1er = self) et que le 2e est de type string
        assert len(args_construct) == 2 and args_construct[-1].split(":")[-1].strip() == "str)"

    test_empty_constructor()
    test_constructor_has_exactly_one_string_argument()


def tests_nombre_cellules():
    """
    Tests concernant la possibilité pour l'utilisateur de récuperer le nombre de cellules vivantes dans la boite de
    petri
    """
    def nb_cellules_premier_fichier():
        jdlv: Jdlv = Jdlv(path_file="jdlv_1.txt")
        assert jdlv.n_cells == 3

    def nb_cellules_deuxieme_fichier():
        jdlv: Jdlv = Jdlv(path_file="jdlv_2.txt")
        assert jdlv.n_cells == 6

    nb_cellules_premier_fichier()
    nb_cellules_deuxieme_fichier()

def tests_mise_a_jour():
    pass


tests_initialisation()
tests_nombre_cellules()


