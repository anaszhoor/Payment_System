from abc import ABC, abstractmethod

class CurrencyConverter(ABC):
    @abstractmethod
    def converter(self, amount):
        pass

# Convert from shekel to dollar if the user wants to pay in dollars, considering that the basic currency of the system is shekel .
# You can add any another convert function 
class USDconverter(CurrencyConverter):
    shekel_per_dolar = 3.7

    def converter(self, amount):
        return str(round(amount/self.shekel_per_dolar, 4)) + " USD"
    
# Convert from shekel to dinar if the user wants to pay in dinar, considering that the basic currency of the system is shekel
class JODconverter(CurrencyConverter):
    shekel_per_dinar = 5.0

    def converter(self, amount):
        return str(round(amount/self.shekel_per_dinar)) + " JOD"

# Unit Test 
test1 = USDconverter()
print(test1.converter(2500))

test2 = JODconverter()
print(test2.converter(2500))
