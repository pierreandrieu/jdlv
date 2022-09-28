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
    """
    Fonctions de test pour la mise à jour des cellules
    """

    def test_comparaison(path_file: str):
        jdlv = Jdlv(path_file=path_file)
        jdlv_output = Jdlv(path_file=path_file[:-4]+"_expected_next.txt")
        assert jdlv.next_generation() == str(jdlv_output)

    def test_vide():
        """
        Teste le cas suivant : si aucune cellule vivante, aucune vivante à l'étape suivante
        Assertion error si le test échoue
        """
        test_comparaison(path_file="jdlv_3.txt")

    def test_point_fixe_non_vide():
        """
        Teste le cas suivant : chaque cellule vivante doit rester en vie a l'étape suivante et aucune reproduction
        C'est un point fixe : aucun changement
        Assertion error si le test échoue
        """
        test_comparaison(path_file="jdlv_4.txt")

    def test_cellule_meurt():
        """
        Teste la mort de la cellule. Une cellule vivante meurt ssi + de 3 voisins ou - de 2 voisins
        """
        test_comparaison(path_file="jdlv_5.txt")

    test_vide()
    test_point_fixe_non_vide()
    test_cellule_meurt()


tests_initialisation()
tests_nombre_cellules()
tests_mise_a_jour()


