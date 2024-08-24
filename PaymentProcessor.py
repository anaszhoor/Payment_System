from PaymentMethod import PaymentMethod, CreditCard, PayPal, Crypto
from Discount import Discount, PercentageDiscount, FixedAmountDiscount
from CurrencyConverter import CurrencyConverter, USDconverter, JODconverter
import logging

logging.basicConfig(filename="my_app.log",
                    filemode="a", 
                    format="(%(asctime)s) => | %(name)s | %(levelname)s => `%(message)s`",
                    datefmt="%d - %B - %Y, %H:%M:%S")

my_logger = logging.getLogger("ANAS ZHOUR")

class PaymentProcessor:
    def __init__(self, payment_method: PaymentMethod, discount: Discount = None, currency_converter: CurrencyConverter = None):
        self.payment_method = payment_method
        self.discount = discount
        self.currency_converter = currency_converter
        
    def process(self, amount, user_name, password):
        my_logger.critical(f"USER NAME : {user_name}")
        if not self.payment_method.validate(user_name, password):
            my_logger.error("Invalid payment details")
            raise print("Invalid payment details")
        
        success = self.payment_method.process_payment(amount)
        
        if self.discount:
            amount = self.discount.apply_discount(amount)

        if self.currency_converter:
            amount = self.currency_converter.converter(amount)

        if success:
            my_logger.critical(f"Payment Method : {self.payment_method} \n Final Amount (*amount after discount and convertion) : {amount}")
        else :
            my_logger.error("Something went wrong.")

        return success

# Test Case 1

test_payment = CreditCard()
test_discount = PercentageDiscount(15)
test_currency_converter = USDconverter()

Test = PaymentProcessor(test_payment, test_discount, test_currency_converter)
Test.process(4700, "Asem Saleh", 834857530)

# Test case 2

test2_payment = PayPal()
test2_discount = PercentageDiscount(25)
test2_currency_converter = JODconverter()

Test = PaymentProcessor(test2_payment, test2_discount, test2_currency_converter)
Test.process(4700, "Dana", 834857530)






