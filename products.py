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

        self.name = name
        self.price = price
        self.quantity = quantity
        if quantity == 0:
            self.active = False
        else:
            self.active = True


    def get_quantity(self) -> int:
        """
        returns quantity of object
        """
        return self.quantity


    def activate(self):
        """
        activates product
        """
        self.active = True


    def deactivate(self):
        """
        deactivates product
        """
        self.active = False


    def set_quantity(self, quantity: int):
        """
        sets quantity of product

        :param quantity: quantity of product
        """
        self.quantity = quantity
        print(f"\nTotal amount of {self.name} is stocked to {self.quantity}.")
        if self.quantity <= 0:
            self.deactivate()


    def is_active(self) -> bool:
        """
        return the variable active to show if product is active or not
        """
        return self.active


    def show(self):
        """
        prints name, price and available quantity of product
        """
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"


    def buy(self,  quantity: int) -> float:
        """
        return total price of the order if the ordered quantity is available,
        if not returns zero

        :param quantity: quantity of product, that is ordered
        """
        if self.quantity >= quantity:
            new_quantity = self.quantity - quantity
            self.set_quantity(new_quantity)
            total_price: float = self.price * quantity

            if self.quantity == 0:
                self.deactivate()
            return total_price

        print(f"Error while making order. Quantity of {self.name} larger then exists")
        return 0
