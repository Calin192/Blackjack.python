class UI:
    def __init__(self, serviceblackjack):
        self.__serviceblackjack = serviceblackjack
        self.__comenzi = {
            "play": self.__ui_blackjack,
        }

    def __ui_blackjack(self):
        comanda = "Afgksjdhfgsdhfgsdkhjs"
        l=0
        while True:
            try:
                valoare = input("Introdu o suma: ")
            except:
                continue
            if valoare == "":
                return
            else:
                valoare = int(valoare)
                if comanda == "stand" or l == 1:
                    comanda = "Afgksjdhfgsdhfgsdkhjs"
                try:
                    while comanda != "stand":
                        self.__serviceblackjack.pariu(valoare,comanda)
                        comanda = str(input(">>>"))
                        if comanda == "stand":
                            self.__serviceblackjack.pariu(valoare, comanda)
                except ValueError as ve:
                    l = 1
                    print(f"{ve}")

    def start_joc(self):
        while True:
            comanda = input(">>>")
            comanda.strip()
            if comanda == "exit":
                return
            if comanda == "":
                continue
            parti = comanda.split()
            if comanda in self.__comenzi:
                try:
                    self.__comenzi[comanda]()
                except ValueError:
                    print("ValueError")
            else:
                print("comanda invalida")
