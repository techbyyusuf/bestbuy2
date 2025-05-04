from products import Product


class Store:
    """
    A class representing a Store

    Attributes:
        list of products(name, price, quantity)
    """

    def __init__(self, product_list:list):
        """
        Initializes Store object.

        :param product_list: list of products with tuples as elements
        """
        for product in product_list:
            if not isinstance(product, Product):
                raise TypeError(f"Invalid item in product list: {product}")

        self._product_list = product_list


    def add_product(self, product):
        """
        Adds a new product to the list of products, if it's not already there (by name)
        """
        if any(p.name == product.name for p in self._product_list):
            print(f"{product.name} is already in the store.")
        else:
            self._product_list.append(product)
            print(f"Added {product.name} to the store.")


    def remove_product(self, product):
        """
        Removes a product from the list by matching the name
        """
        for p in self._product_list:
            if p.name == product.name:
                self._product_list.remove(p)
                print(f"Removed {product.name} from the store.")
                return
        print(f"Error: {product.name} is not in the store.")


    def get_total_quantity(self) -> int:
        """
        returns total quantity of offered products
        """
        return sum([product.get_quantity() for product in self._product_list])


    def get_all_products(self) -> list[Product]:
        """
        return list of offered products, that are available
        """
        return [product for product in self._product_list if product.is_active()]


    def order(self, shopping_list: list[tuple]) -> float:
        """
        gets a shopping list made of a tuples in a list and returns
        total price of order
        """
        total_price: float = 0

        for product, quantity in shopping_list:
            total_price += product.buy(quantity)

        return total_price


