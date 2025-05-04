from abc import ABC, abstractmethod


class Promotion(ABC):
    """
    Abstract base class for all promotion types.
    Each promotion must implement the apply_promotion method.
    """

    def __init__(self, promotion):
        """
        Initialize the promotion with a description or identifier.
        """

        self._promotion = promotion


    @abstractmethod
    def apply_promotion(self, product, quantity) -> float:
        """
        Calculate the total price after applying the promotion.
        Must be implemented by all subclasses.
        """
        pass



class PercentDiscount(Promotion):
    """
    Promotion that applies a fixed percentage discount to all items.
    """

    def __init__(self, promotion, percent):
        """
        Initialize with a description and the discount percent.
        """
        super().__init__(promotion)

        if not isinstance(percent, (int, float)):
            raise TypeError("Discount percent must be a number.")

        if not (0 <= percent <= 100):
            raise ValueError("Discount percent must be between 0 and 100.")

        self._percent = percent


    def apply_promotion(self, product, quantity) -> float:
        """
        Apply percentage discount to the total price of the product.
        """
        product_price = product.get_price()
        new_product_price = product_price * ((100 - self._percent)/100)
        total_charge = new_product_price * quantity
        return total_charge


    def __str__(self):
        """
        string for the class

        """
        return "30% off!"


class SecondHalfPrice(Promotion):
    """
    Promotion where every second item is half price.
    """

    def apply_promotion(self, product, quantity) -> float:
        """
        Apply half price to every second product in the total quantity.
        """

        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0.")

        product_price = product.get_price()
        discounted_pairs = quantity // 2
        full_price_products  = quantity % 2
        total_charge = (discounted_pairs * product_price * 1.5) + (full_price_products * product_price)
        return total_charge


    def __str__(self):
        """
        string for class
        """
        return "Second Half Price!"



class ThirdOneFree(Promotion):
    """
    Promotion where every third item is free.
    """

    def apply_promotion(self, product, quantity) -> float:
        """
        For every three products, one is free. Calculate the total charge.
        """
        product_price = product.get_price()
        free_items = quantity // 3
        paid_items = quantity - free_items
        total_charge = paid_items * product_price
        return total_charge


    def __str__(self):
        """
        string for the class
        """
        return "Third One Free!"








