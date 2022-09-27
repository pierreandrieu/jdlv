class Jdlv:
    """
    Class for GL TP2 : jeu de la vie
    """
    def __init__(self, path_file: str):
        # private attribute
        self.__nb_cells = 0
        with open(path_file, 'r') as fichier:
            lignes = fichier.read().split("\n")
            # recuperation de la 1e ligne d'en-tête formatée int int
            en_tete = lignes[0].split(" ")

            # 1e valeur : le n et 2e valeur: le m
            self.__n = int(en_tete[0])
            self.__m = int(en_tete[1])
            self.__matrix = []
            for ligne in lignes[1:]:
                if len(ligne) == self.__m:
                    self.__matrix.append(ligne)
                    self.__nb_cells += ligne.count("*")
        print(self.__matrix)
    @property
    def n_cells(self) -> int:
        return self.__nb_cells
