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

    def next_generation(self) -> str:
        return ""
