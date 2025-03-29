from abc import ABC, abstractmethod


class Promotion(ABC):
    def __init__(self, promotion):
        self._promotion = promotion


    @abstractmethod
    def apply_promotion(self, product, quantity) -> float:
        pass



class PercentDiscount(Promotion):
    def __init__(self, promotion, percent):
        super().__init__(promotion)
        self._percent = percent

    def apply_promotion(self, product, quantity) -> float:
        product_price = product.get_price()
        new_product_price = product_price * ((100 - self._percent)/100)
        total_charge = new_product_price * quantity
        return total_charge

    def __str__(self):
        return "30% off!"



class SecondHalfPrice(Promotion):
    def apply_promotion(self, product, quantity) -> float:
        product_price = product.get_price()
        pairs = quantity // 2
        leftover = quantity % 2
        total_charge = (pairs * product_price * 1.5) + (leftover * product_price)
        return total_charge

    def __str__(self):
        return "Second Half Price!"



class ThirdOneFree(Promotion):
    def apply_promotion(self, product, quantity) -> float:
        product_price = product.get_price()
        free_items = quantity // 3
        paid_items = quantity - free_items
        total_charge = paid_items * product_price
        return total_charge


    def __str__(self):
        return "Third One Free!"








