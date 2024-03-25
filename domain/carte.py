class Carte:
    def __init__(self,nr_carte,simbol):
        self.__nr_carte = nr_carte
        self.__simbol = simbol

    def get_nr_carte(self):
        return self.__nr_carte

    def get_simbol(self):
        return self.__simbol