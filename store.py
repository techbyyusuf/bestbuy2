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

        self.product_list = product_list


    def add_product(self, product):
        """
        adds new product to list of products
        """
        if product in self.product_list:
            print(f" {product.name} is already in the store.")
        else:
            print(f"Added {product.name} to the store.")
            self.product_list.append(product)


    def remove_product(self, product):
        """
        removes product from list of products
        """
        if product in self.product_list:
            self.product_list.remove(product)
            print(f"Removed {product.name} from the store.")
        else:
            print(f"Error: {product.name} is not in the store.")


    def get_total_quantity(self) -> int:
        """
        returns total quantity of offered products
        """
        return sum([product.get_quantity() for product in self.product_list])


    def get_all_products(self) -> list[Product]:
        """
        return list of offered products, that are available
        """
        return [product for product in self.product_list if product.is_active()]


    def order(self, shopping_list: list[tuple]) -> float:
        """
        gets a shopping list made of a tuples in a list and returns
        total price of order
        """
        total_price: float = 0

        for product, quantity in shopping_list:
            total_price += product.buy(quantity)

        return total_price
