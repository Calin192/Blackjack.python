class RepoJucator:

    def __init__(self):
        self.__carti_jucator = []

    def adauga_carte(self, carte):
        self.__carti_jucator.append(carte)

    def get_all(self):
        return self.__carti_jucator

    def goleste(self):
        self.__carti_jucator = []
