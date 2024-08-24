from abc import ABC, abstractmethod
import logging

logging.basicConfig(filename="my_app.log",
                    filemode="a", 
                    format="(%(asctime)s) => | %(name)s | %(levelname)s => `%(message)s`",
                    datefmt="%d - %B - %Y, %H:%M:%S")

my_logger = logging.getLogger("ANAS ZHOUR")

# Strategy Pattern
class PaymentMethod(ABC):
    @abstractmethod
    def validate(self, user_name, password):
        pass

    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCard(PaymentMethod):
    def validate (self, user_name, password):
        print("Validating credit card details")
        # validation logic 
        my_logger.critical("Validating credit card details")
        return True
    
    def process_payment(self, amount):
        print(f"Processing credit card payment of {amount} ILS")
        my_logger.critical(f"Processing credit card payment of {amount} ILS")
        return True

class PayPal(PaymentMethod):
    def validate (self, user_name, password):
        print("Validating PayPal details")
        # validation logic 
        my_logger.critical("Validating PayPal details")
        return True
    
    def process_payment(self, amount):
        print(f"Processing PayPal payment of {amount} ILS")
        my_logger.critical(f"Processing PayPal payment of {amount} ILS")
        return True

class Crypto(PaymentMethod):
    def validate (self, user_name, password):
        print("Validating cryptocurrency details")
        # validation logic 
        my_logger.critical("Validating cryptocurrency details")
        return True

    def process_payment(self, amount):
        print(f"Processing cryptocurrency payment of {amount} ILS")
        my_logger.critical(f"Processing cryptocurrency payment of {amount} ILS")
        return True
   
# Unit Test 

# T1 = CreditCard()
# print(T1.validate("Anas", 84747549))
# print(T1.process_payment(4000))

# T2 = PayPal()
# print(T2.validate("Asem", 84847589))
# print(T2.process_payment(3500))

# T3 = Crypto()
# print(T3.validate("Mohammad", 756484984))
# print(T3.process_payment(7400))
    
