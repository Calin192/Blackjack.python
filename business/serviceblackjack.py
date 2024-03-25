import random
from domain.carte import Carte
from business.carti import StrCarti


class ServiceBlackjack:
    def __init__(self,repo_dealer,repo_jucator):
        self.__repo_dealer = repo_dealer
        self.__repo_jucator = repo_jucator
        self.__suma = 5000
        self.__carti = [0]+[3]*52
        self.__simboluri = ["♥", "♠", "♦", "♣"]
        self.__puncte = 0
        self.__contor_carti_jucator = 0
        self.__str_carti = StrCarti()

    def pariu(self, valoare, comanda):
        self.check_balance(valoare)
        if comanda == "Afgksjdhfgsdhfgsdkhjs":
            nr_carte = self.trage_carte()
            carte = self.determina_carte(nr_carte)
            self.__repo_dealer.adauga_carte(carte)
            puncte_dealer = self.__calcueaza_puncte_dealer()
            print("Dealer:")
            print(self.afiseaza_carti_dealer(puncte_dealer))

        nr_carte = self.trage_carte()
        carte = self.determina_carte(nr_carte)
        if comanda == "hit" or comanda == "Afgksjdhfgsdhfgsdkhjs":
            self.__repo_jucator.adauga_carte(carte)

        if comanda == "stand":
            puncte_dealer = self.__calcueaza_puncte_dealer()
            puncte_player = self.__calcueaza_puncte_jucator()
            l = 2

            while puncte_dealer < 17:
                nr_carte = self.trage_carte()
                carte = self.determina_carte(nr_carte)
                self.__repo_dealer.adauga_carte(carte)
                puncte_dealer = self.__calcueaza_puncte_dealer()
            if puncte_dealer <= 21 and puncte_player <= 21 and puncte_player > puncte_dealer:
                self.__suma += valoare
                l = 1
            elif puncte_dealer <= 21 and puncte_player <= 21 and puncte_player < puncte_dealer:
                self.__suma -= valoare
                l = 0
            elif puncte_dealer <= 21 and puncte_player > 21:
                self.__suma -= valoare
                l = 0
            elif puncte_dealer > 21 and puncte_player <= 21:
                self.__suma += valoare
                l = 1
            elif puncte_dealer == puncte_player and puncte_dealer <= 21:
                pass
            elif puncte_dealer == puncte_player and puncte_dealer > 21:
                self.__suma -= valoare
                l = 0



            puncte_dealer = self.__calcueaza_puncte_dealer()
            print("Dealer:")
            print(self.afiseaza_carti_dealer(puncte_dealer))

            puncte = self.__calcueaza_puncte_jucator()
            print("Jucator:")
            print(self.afiseaza_carti(puncte))

            print("Banii tai:",self.__suma)

            if l == 2:
                print("Egalitate")
            elif l == 1:
                print("Ai castigat!")
            else:
                print("Ai pierdut")

            self.__repo_jucator.goleste()
            self.__repo_dealer.goleste()
            return

        if comanda != "Afgksjdhfgsdhfgsdkhjs":
            puncte_dealer = self.__calcueaza_puncte_dealer()
            print("Dealer:")
            print(self.afiseaza_carti_dealer(puncte_dealer))

        puncte = self.__calcueaza_puncte_jucator()
        print("Jucator:")
        print(self.afiseaza_carti(puncte))

        if puncte == 21 and comanda == "stand":
            self.__suma += valoare*3/2

        if puncte > 21:
            self.__suma -= valoare
            print("Banii tai:", self.__suma)
            self.__repo_jucator.goleste()
            self.__repo_dealer.goleste()
            raise ValueError("Ai trecut de 21")

    def afiseaza_carti(self,puncte):
        carti = self.__repo_jucator.get_all()
        lungime = len(carti)

        if lungime == 1:
            valoare = carti[0].get_nr_carte()
            model = carti[0].get_simbol()
            return self.__str_carti.carti_1(valoare, model,puncte)

        if lungime == 2:
            valoare = carti[0].get_nr_carte()
            model = carti[0].get_simbol()
            valoare1 = carti[1].get_nr_carte()
            model1 = carti[1].get_simbol()
            return self.__str_carti.carti_2(valoare, model, valoare1, model1,puncte)

        if lungime == 3:
            valoare = carti[0].get_nr_carte()
            model = carti[0].get_simbol()
            valoare1 = carti[1].get_nr_carte()
            model1 = carti[1].get_simbol()
            valoare2 = carti[2].get_nr_carte()
            model2 = carti[2].get_simbol()
            return self.__str_carti.carti_3(valoare, model, valoare1, model1, valoare2, model2,puncte)

        if lungime == 4:
            valoare = carti[0].get_nr_carte()
            model = carti[0].get_simbol()
            valoare1 = carti[1].get_nr_carte()
            model1 = carti[1].get_simbol()
            valoare2 = carti[2].get_nr_carte()
            model2 = carti[2].get_simbol()
            valoare3 = carti[3].get_nr_carte()
            model3 = carti[3].get_simbol()
            return self.__str_carti.carti_4(valoare, model, valoare1, model1, valoare2, model2, valoare3, model3,puncte)

        if lungime == 5:
            valoare = carti[0].get_nr_carte()
            model = carti[0].get_simbol()
            valoare1 = carti[1].get_nr_carte()
            model1 = carti[1].get_simbol()
            valoare2 = carti[2].get_nr_carte()
            model2 = carti[2].get_simbol()
            valoare3 = carti[3].get_nr_carte()
            model3 = carti[3].get_simbol()
            valoare4 = carti[4].get_nr_carte()
            model4 = carti[4].get_simbol()
            return self.__str_carti.carti_5(valoare, model, valoare1, model1, valoare2, model2, valoare3, model3,valoare4, model4,puncte)

        if lungime == 6:
            valoare = carti[0].get_nr_carte()
            model = carti[0].get_simbol()
            valoare1 = carti[1].get_nr_carte()
            model1 = carti[1].get_simbol()
            valoare2 = carti[2].get_nr_carte()
            model2 = carti[2].get_simbol()
            valoare3 = carti[3].get_nr_carte()
            model3 = carti[3].get_simbol()
            valoare4 = carti[4].get_nr_carte()
            model4 = carti[4].get_simbol()
            valoare5 = carti[5].get_nr_carte()
            model5 = carti[5].get_simbol()
            return self.__str_carti.carti_6(valoare, model, valoare1, model1, valoare2, model2, valoare3, model3,valoare4, model4,valoare5,model5,puncte)

        if lungime == 7:
            valoare = carti[0].get_nr_carte()
            model = carti[0].get_simbol()
            valoare1 = carti[1].get_nr_carte()
            model1 = carti[1].get_simbol()
            valoare2 = carti[2].get_nr_carte()
            model2 = carti[2].get_simbol()
            valoare3 = carti[3].get_nr_carte()
            model3 = carti[3].get_simbol()
            valoare4 = carti[4].get_nr_carte()
            model4 = carti[4].get_simbol()
            valoare5 = carti[5].get_nr_carte()
            model5 = carti[5].get_simbol()
            valoare6 = carti[6].get_nr_carte()
            model6 = carti[6].get_simbol()
            return self.__str_carti.carti_7(valoare, model, valoare1, model1, valoare2, model2, valoare3, model3,valoare4, model4,valoare5,model5,valoare6,model6,puncte)

    def afiseaza_carti_dealer(self,puncte):
        carti = self.__repo_dealer.get_all()
        lungime = len(carti)

        if lungime == 1:
            valoare = carti[0].get_nr_carte()
            model = carti[0].get_simbol()
            return self.__str_carti.carti_dealer_1(valoare, model,puncte)

        if lungime == 2:
            valoare = carti[0].get_nr_carte()
            model = carti[0].get_simbol()
            valoare1 = carti[1].get_nr_carte()
            model1 = carti[1].get_simbol()
            return self.__str_carti.carti_2( valoare1, model1,valoare, model,puncte)

        if lungime == 3:
            valoare = carti[0].get_nr_carte()
            model = carti[0].get_simbol()
            valoare1 = carti[1].get_nr_carte()
            model1 = carti[1].get_simbol()
            valoare2 = carti[2].get_nr_carte()
            model2 = carti[2].get_simbol()
            return self.__str_carti.carti_3( valoare1, model1,valoare, model, valoare2, model2,puncte)

        if lungime == 4:
            valoare = carti[0].get_nr_carte()
            model = carti[0].get_simbol()
            valoare1 = carti[1].get_nr_carte()
            model1 = carti[1].get_simbol()
            valoare2 = carti[2].get_nr_carte()
            model2 = carti[2].get_simbol()
            valoare3 = carti[3].get_nr_carte()
            model3 = carti[3].get_simbol()
            return self.__str_carti.carti_4( valoare1, model1,valoare, model, valoare2, model2, valoare3, model3,puncte)

        if lungime == 5:
            valoare = carti[0].get_nr_carte()
            model = carti[0].get_simbol()
            valoare1 = carti[1].get_nr_carte()
            model1 = carti[1].get_simbol()
            valoare2 = carti[2].get_nr_carte()
            model2 = carti[2].get_simbol()
            valoare3 = carti[3].get_nr_carte()
            model3 = carti[3].get_simbol()
            valoare4 = carti[4].get_nr_carte()
            model4 = carti[4].get_simbol()
            return self.__str_carti.carti_5( valoare1, model1,valoare, model, valoare2, model2, valoare3, model3,valoare4, model4,puncte)

        if lungime == 6:
            valoare = carti[0].get_nr_carte()
            model = carti[0].get_simbol()
            valoare1 = carti[1].get_nr_carte()
            model1 = carti[1].get_simbol()
            valoare2 = carti[2].get_nr_carte()
            model2 = carti[2].get_simbol()
            valoare3 = carti[3].get_nr_carte()
            model3 = carti[3].get_simbol()
            valoare4 = carti[4].get_nr_carte()
            model4 = carti[4].get_simbol()
            valoare5 = carti[5].get_nr_carte()
            model5 = carti[5].get_simbol()
            return self.__str_carti.carti_6( valoare1, model1,valoare, model, valoare2, model2, valoare3, model3,valoare4, model4,valoare5,model5,puncte)


        if lungime == 7:
            valoare = carti[0].get_nr_carte()
            model = carti[0].get_simbol()
            valoare1 = carti[1].get_nr_carte()
            model1 = carti[1].get_simbol()
            valoare2 = carti[2].get_nr_carte()
            model2 = carti[2].get_simbol()
            valoare3 = carti[3].get_nr_carte()
            model3 = carti[3].get_simbol()
            valoare4 = carti[4].get_nr_carte()
            model4 = carti[4].get_simbol()
            valoare5 = carti[5].get_nr_carte()
            model5 = carti[5].get_simbol()
            valoare6 = carti[6].get_nr_carte()
            model6 = carti[6].get_simbol()
            return self.__str_carti.carti_7( valoare1, model1,valoare, model, valoare2, model2, valoare3, model3,valoare4, model4,valoare5,model5,valoare6,model6,puncte)


    def check_balance(self, valoare):
        if valoare > self.__suma:
            raise ValueError("Balanta insuficienta")

    def trage_carte(self):
        while True:
            nr_carte = random.randint(1,52)
            if self.__carti[nr_carte] == 0:
                continue
            self.__carti[nr_carte] -= 1
            return nr_carte

    def determina_carte(self,nr_carte):
        nr = 0
        while nr_carte > 13:
            nr_carte = nr_carte - 13
            nr += 1
        simbol = self.__simboluri[nr]
        self.creste_contor_jucator()
        carte = Carte(nr_carte, simbol)
        return carte

    def creste_contor_jucator(self):
        self.__contor_carti_jucator += 1

    def get_contor_jucator(self):
        return self.__contor_carti_jucator

    def __calcueaza_puncte_jucator(self):
        carti = self.__repo_jucator.get_all()
        puncte = 0
        nr_asi = 0
        for carte in carti:
            nr_carte = carte.get_nr_carte()
            if nr_carte == 1:
                nr_asi += 1
            else:
                if nr_carte >= 10:
                    puncte += 10
                else:
                    puncte += nr_carte
        for i in range (nr_asi):
            if puncte + 11 > 21:
                puncte += 1
            else:
                puncte += 11
        return puncte

    def __calcueaza_puncte_dealer(self):
        carti = self.__repo_dealer.get_all()
        puncte = 0
        nr_asi = 0
        for carte in carti:
            nr_carte = carte.get_nr_carte()
            if nr_carte == 1:
                nr_asi += 1
            else:
                if nr_carte >= 10:
                    puncte += 10
                else:
                    puncte += nr_carte
        for i in range (nr_asi):
            if puncte + 10 > 21:
                puncte += 1
            else:
                puncte += 11
        return puncte
