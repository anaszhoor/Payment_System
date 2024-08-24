from abc import ABC, abstractmethod

class Discount(ABC):
    @abstractmethod
    def apply_discount(self, amount):
        pass
    
class PercentageDiscount(Discount):
    def __init__(self, percentage):
        self.percentage = percentage

    def apply_discount(self, amount):
        return amount - (amount * self.percentage / 100)

class FixedAmountDiscount(Discount):
    def __init__(self, discount_amount):
        self.discount_amount = discount_amount

    def apply_discount(self, amount):
        return max(0, amount - self.discount_amount)
    
# Unit Test1
test3 = PercentageDiscount(10)
print(test3.apply_discount(3000))

# Unit Test2
test4 = FixedAmountDiscount(760)
print(test4.apply_discount(3000))