class RepoDealer:

    def __init__(self):
        self.__carti_dealer = []

    def adauga_carte(self,carte):
        self.__carti_dealer.append(carte)

    def get_all(self):
        return self.__carti_dealer

    def goleste(self):
        self.__carti_dealer = []

