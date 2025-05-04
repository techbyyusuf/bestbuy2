class Product:
    """
    A class representing a Product

    Attributes:
        name, price, quantity
    """

    def __init__(self, name: str, price: float, quantity: int):
        """
        Initializes a Product object.

        :param name: name of product (string)
        :param price: price of product (float)
        :param quantity: quantity of product (integer)
        """

        if not isinstance(name, str):
            raise TypeError("Invalid name: must be a string.")

        if not isinstance(price, (int, float)):
            raise TypeError("Invalid price: must be a number.")

        if price < 0:
            raise TypeError("No prices below zero.")

        if not isinstance(quantity, int):
            raise TypeError("Invalid quantity: must be an integer.")

        if quantity < 0:
            raise TypeError("No quantity below zero.")

        if name == "":
            raise TypeError("Empty names are not allowed!")

        self._name = name
        self._price = price
        self._quantity = quantity
        self._active = True

        self._promotion = None


    def get_quantity(self) -> int:
        """
        returns quantity of object
        """
        return self._quantity


    def activate(self):
        """
        activates product
        """
        self._active = True


    def deactivate(self):
        """
        deactivates product
        """
        self._active = False


    def get_price(self):
        """
        returns the price

        """
        return self._price

    def get_promotion(self):
        """
        returns the instance variable promotion
        """
        return self._promotion


    def set_promotion(self, promotion):
        """
        function gets a promotion and sets the instance promotion

        """
        self._promotion = promotion


    def set_quantity(self, quantity: int):
        """
        sets quantity of product

        :param quantity: quantity of product
        """
        self._quantity = quantity
        print(f"\nTotal amount of {self._name} is stocked to {self._quantity}.")
        if self._quantity <= 0:
            self.deactivate()


    def is_active(self) -> bool:
        """
        return the variable active to show if product is active or not
        """
        return self._active


    def show(self):
        """
        returns string of name, price and available quantity of product
        """
        promotion = self.get_promotion()
        return (f"{self._name}, Price: {self._price}, "
                f"Quantity: {self._quantity}, Promotion: {promotion}")


    def buy(self,  quantity: int) -> float:
        """
        return total price of the order if the ordered quantity is available,
        if not returns zero

        :param quantity: quantity of product, that is ordered
        """
        if self._quantity < quantity:
            raise ValueError("Not enough stock.")

        if self.get_promotion():
            total_price = self._promotion.apply_promotion(self, quantity)
        else:
            total_price: float = self._price * quantity

        self.set_quantity(self._quantity - quantity)

        if self._quantity == quantity:
            self.deactivate()

        return total_price



#Shipping
class LimitedProduct(Product):
    """
    Products that are only allowed to be purchased in a certain amount
    """
    def __init__(self, name, price, quantity, maximum):
        """
        gets name, price, quantity, maximum allowed purchase of prodcut in one
        order and creates the instances.
        """
        super().__init__(name, price, quantity)

        if not isinstance(maximum,(float, int)):
            raise TypeError("Enter a number for maximum amount of quantity!")
        if maximum <= 0:
            raise ValueError("Maximum purchase of product has to be over zero!")

        self._maximum = maximum

    def get_maximum(self):
        """
        returns the maximum available amount
        """
        return self._maximum

    def show(self):
        """
        return string of name, price, available quantity of product, maximum
        allowed amount of product in order
        """
        promotion = self.get_promotion()
        return (f"{self._name}, Price: {self._price}, Quantity: {self._quantity}, "
                f"Maximum: {self._maximum}, Promotion: {promotion}")


    def buy(self, quantity):
        """
        gets the quantity of purchased product, decrease the amount of product
        and return the total price of order
        """
        max_quantity = self.get_maximum()
        allowed_quantity = min(quantity, max_quantity)
        total_price = super().buy(allowed_quantity)
        return total_price


#Windows License
class NonStockedProduct(Product):
    """
    Products that are not stocked
    """

    def __init__(self, name, price):
        """
        gets name and price of non-stocked Product and sets the instances
        """
        super().__init__(name, price, quantity=0)
        self._active = True


    def show(self):
        """
        returns string of name and price
        """
        promotion = self.get_promotion()
        return f"{self._name}, Price: {self._price}, Promotion: {promotion}"



    def buy(self, quantity):
        """
        gets the quantity, checks if the product has a promotion. If it has
        a promotion applies the promotion and return the total price.
        """
        if self.get_promotion():
            total_price = self._promotion.apply_promotion(self, quantity)
        else:
            total_price: float = self._price * quantity

        return total_price