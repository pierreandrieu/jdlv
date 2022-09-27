class Jdlv:
    """
    Class for GL TP2 : jeu de la vie
    """
    def __init__(self, path_file: str):
        # private attribute
        self.__nb_cells = 3

    @property
    def n_cells(self) -> int:
        return self.__nb_cells
