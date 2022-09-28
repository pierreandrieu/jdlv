from typing import List


class Jdlv:

    """
    Class for GL TP2 : jeu de la vie
    """
    def __init__(self, path_file: str):
        # private attribute
        self.__nb_cells: int = 0
        with open(path_file, 'r') as fichier:
            lignes: List[str] = fichier.read().split("\n")
            # recuperation de la 1e ligne d'en-tête formatée int int
            en_tete: List[str] = lignes[0].split(" ")
            # 1e valeur : le n et 2e valeur: le m
            self.__n: int = int(en_tete[0])
            self.__m: int = int(en_tete[1])

            self.__matrix: List[str] = []
            for ligne in lignes[1:]:
                if len(ligne) == self.__m:
                    self.__matrix.append(ligne)
                    self.__nb_cells += ligne.count("*")

    def __repr__(self) -> str:
        return "\n".join(self.__matrix)

    def __str__(self) -> str:
        return self.__repr__()

    @property
    def n_cells(self) -> int:
        return self.__nb_cells

    def __petri_vide(self) -> List[List[str]]:
        """
        fonction qui renvoie une liste de n listes contenant chacune m fois la chaîne "."
        n nombre de lignes
        m nombre de colonnes
        :return: List[List[str]]
        """
        list_new_lines: List = []
        for i in range(self.__n):
            list_new_lines.append([])
            for j in range(self.__m):
                list_new_lines[i].append(".")
        return list_new_lines

    @staticmethod
    def __from_list_list_str_to_str(petri: List[List[str]]) -> str:
        """
        :param petri: Liste de Liste de str
        :return: str suivant : les List[str] sont concaténées en str et séparées entre elles par "\n"
        """
        return "\n".join(["".join(petri[i]) for i in range(len(petri))])

    def next_generation(self) -> str:
        """
        fonction qui renvoie une chaine de caractères correspondant à la prochaine étape du jeu de la vie
        :return: str
        """
        # initialisation de la boite de petri à vide
        list_new_lines: List[List[str]] = self.__petri_vide()

        # on considère l'état précédent
        for i in range(self.__n):
            for j in range(self.__m):
                if self.__matrix[i][j] == "*":
                    list_new_lines[i][j] = "*"
        # on renvoie la "version string"
        return Jdlv.__from_list_list_str_to_str(list_new_lines)
