class StrCarti:
    def __init__(self):
        pass

    def transforma_in_litere(self, valoare):
        if valoare == 1:
            return "A "
        if valoare <= 9:
            return f"{valoare} "
        if valoare == 10:
            return "10"
        if valoare == 11:
            return " J"
        if valoare == 12:
            return " Q"
        if valoare == 13:
            return " K"


    def carti_1(self, valoare, model,puncte):
        valoare = str(self.transforma_in_litere(valoare))

        return f'''________ 
|{valoare}    |
|   {model}  |
|    {valoare}|
‾‾‾‾‾‾‾‾
{puncte}'''

    def carti_2(self,valoare,model,valoare1,model1,puncte):
        valoare = self.transforma_in_litere(valoare)
        valoare1 = self.transforma_in_litere(valoare1)

        return  f'''________   ________
|{valoare}    |   |{valoare1}    | 
|   {model}  |   |   {model1}  |  
|    {valoare}|   |    {valoare1}|  
‾‾‾‾‾‾‾‾   ‾‾‾‾‾‾‾‾
{puncte}'''

    def carti_3(self,valoare,model,valoare1,model1,valoare2,model2,puncte):
        valoare = self.transforma_in_litere(valoare)
        valoare1 = self.transforma_in_litere(valoare1)
        valoare2 = self.transforma_in_litere(valoare2)

        return f'''________   ________   ________
|{valoare}    |   |{valoare1}    |   |{valoare2}    | 
|   {model}  |   |   {model1}  |   |   {model2}  |  
|    {valoare}|   |    {valoare1}|   |    {valoare2}|  
‾‾‾‾‾‾‾‾   ‾‾‾‾‾‾‾‾   ‾‾‾‾‾‾‾‾
{puncte}'''

    def carti_4(self, valoare, model, valoare1, model1, valoare2, model2, valoare3, model3,puncte):
        valoare = self.transforma_in_litere(valoare)
        valoare1 = self.transforma_in_litere(valoare1)
        valoare2 = self.transforma_in_litere(valoare2)
        valoare3 = self.transforma_in_litere(valoare3)

        return f'''________   ________   ________   ________
|{valoare}    |   |{valoare1}    |   |{valoare2}    |   |{valoare3}    |
|   {model}  |   |   {model1}  |   |   {model2}  |   |   {model3}  |  
|    {valoare}|   |    {valoare1}|   |    {valoare2}|   |    {valoare3}| 
‾‾‾‾‾‾‾‾   ‾‾‾‾‾‾‾‾   ‾‾‾‾‾‾‾‾   ‾‾‾‾‾‾‾‾
{puncte}'''

    def carti_5(self, valoare, model, valoare1, model1, valoare2, model2, valoare3, model3,valoare4,model4,puncte):
        valoare = self.transforma_in_litere(valoare)
        valoare1 = self.transforma_in_litere(valoare1)
        valoare2 = self.transforma_in_litere(valoare2)
        valoare3 = self.transforma_in_litere(valoare3)
        valoare4 = self.transforma_in_litere(valoare4)

        return f'''________   ________   ________   ________   ________
|{valoare}    |   |{valoare1}    |   |{valoare2}    |   |{valoare3}    |   |{valoare4}    |
|   {model}  |   |   {model1}  |   |   {model2}  |   |   {model3}  |   |   {model4}  |  
|    {valoare}|   |    {valoare1}|   |    {valoare2}|   |    {valoare3}|   |    {valoare4}| 
‾‾‾‾‾‾‾‾   ‾‾‾‾‾‾‾‾   ‾‾‾‾‾‾‾‾   ‾‾‾‾‾‾‾‾   ‾‾‾‾‾‾‾‾
{puncte}'''

    def carti_6(self, valoare, model, valoare1, model1, valoare2, model2, valoare3, model3,valoare4,model4,valoare5,model5,puncte):
        valoare = self.transforma_in_litere(valoare)
        valoare1 = self.transforma_in_litere(valoare1)
        valoare2 = self.transforma_in_litere(valoare2)
        valoare3 = self.transforma_in_litere(valoare3)
        valoare4 = self.transforma_in_litere(valoare4)
        valoare5 = self.transforma_in_litere(valoare5)

        return f'''________   ________   ________   ________   ________   ________
|{valoare}    |   |{valoare1}    |   |{valoare2}    |   |{valoare3}    |   |{valoare4}    |   |{valoare5}    |
|   {model}  |   |   {model1}  |   |   {model2}  |   |   {model3}  |   |   {model4}  |   |   {model5}  |  
|    {valoare}|   |    {valoare1}|   |    {valoare2}|   |    {valoare3}|   |    {valoare4}|   |    {valoare5}| 
‾‾‾‾‾‾‾‾   ‾‾‾‾‾‾‾‾   ‾‾‾‾‾‾‾‾   ‾‾‾‾‾‾‾‾   ‾‾‾‾‾‾‾‾   ‾‾‾‾‾‾‾‾
{puncte}'''

    def carti_7(self, valoare, model, valoare1, model1, valoare2, model2, valoare3, model3, valoare4, model4,valoare5,model5,valoare6, model6, puncte):
        valoare = self.transforma_in_litere(valoare)
        valoare1 = self.transforma_in_litere(valoare1)
        valoare2 = self.transforma_in_litere(valoare2)
        valoare3 = self.transforma_in_litere(valoare3)
        valoare4 = self.transforma_in_litere(valoare4)
        valoare5 = self.transforma_in_litere(valoare5)
        valoare6 = self.transforma_in_litere(valoare6)

        return f'''________   ________   ________   ________   ________   ________   ________
|{valoare}    |   |{valoare1}    |   |{valoare2}    |   |{valoare3}    |   |{valoare4}    |   |{valoare5}    |   |{valoare6}    |
|   {model}  |   |   {model1}  |   |   {model2}  |   |   {model3}  |   |   {model4}  |   |   {model5}  |   |   {model6}  |  
|    {valoare}|   |    {valoare1}|   |    {valoare2}|   |    {valoare3}|   |    {valoare4}|   |    {valoare5}|   |    {valoare6}| 
‾‾‾‾‾‾‾‾   ‾‾‾‾‾‾‾‾   ‾‾‾‾‾‾‾‾   ‾‾‾‾‾‾‾‾   ‾‾‾‾‾‾‾‾   ‾‾‾‾‾‾‾‾   ‾‾‾‾‾‾‾‾
{puncte}'''

    def carti_dealer_1(self,valoare,model,puncte):
        valoare = self.transforma_in_litere(valoare)

        return f'''________   ________
|      |   |{valoare}    | 
|  ?   |   |   {model}  |  
|      |   |    {valoare}|  
‾‾‾‾‾‾‾‾   ‾‾‾‾‾‾‾‾
{puncte}'''
