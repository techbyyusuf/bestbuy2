import sys
from store import Store
from products import Product, NonStockedProduct, LimitedProduct
import promotions


def display_menu() -> None:
    """
    prints the help menu
    """
    print("\n\tStore Menu\n\t----------")
    print("1. List all products in the store\n2. Show total amount in store\n"
          "3. Make an order\n4. Quit")


def display_products(best_buy, products: list) -> None:
    """
    gets a list and prints the list
    """
    print("______")
    for index, product in enumerate(products):
        print(f"{index + 1}. {product.show()}")
    print("______")


def display_total_amount(best_buy, products) -> None:
    """
    gets the store object and returns the total quantity of the items in the store.
    """
    print(f"\nTotal of {best_buy.get_total_quantity()} items in store.\n")


def get_choice_for_order(products) -> list[tuple]:
    """
    gets a list of products, asks for product and amount, that want to be ordered
    and creates tuples of name and amount of the chosen product returns the choice in a list
    """
    order: list[tuple] = []

    while True:
        try:
            product_choice = input("\nEnter the number of the product: ")

            if product_choice == "":
                break

            index = int(product_choice) -1
            product = products[index]
            order_amount = input("What amount do you want? ")

            if order_amount == "":
                break

            if int(order_amount) <= 0:
                print("Enter an amount over zero!")
                continue

            if type(product) == LimitedProduct:
                if int(order_amount) > product.get_maximum():
                    print(f"Only {product.get_maximum()} per order!")
                    continue

            if type(product) != NonStockedProduct:
                if product.get_quantity() < int(order_amount):
                    print(f"Available quantity: {product.get_quantity()}.")
                    continue

            order.append((product, int(order_amount)))
            print("Product added to list!")

        except ValueError:
            print("Error adding product!")
        except IndexError:
            print("Choose an offered product from the store!")

    return order


def get_order(best_buy, products) -> None:
    """
    gets store abject and list of products and prints the total price of the order
    """
    display_products(best_buy, products)
    print("When you want to finish order, enter empty text.")

    order = get_choice_for_order(products)

    if not order:
        print("No products were ordered.")
        return

    total_price = best_buy.order(order)
    print(f"\n********\nOrder made! Total payment: ${total_price}")


def main():
    """
    creates a store object with product objects and enables user to make order
    """
    try:
        product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                        Product("Google Pixel 7", price=500, quantity=250),
                        NonStockedProduct("Windows License", price=125),
                        LimitedProduct(name="Shipping", price= 10, quantity=250, maximum=1)
                        ]

        best_buy = Store(product_list)

        second_half_price = promotions.SecondHalfPrice("Second Half Price!")
        third_one_free = promotions.ThirdOneFree("Third One Free!")
        thirty_percent = promotions.PercentDiscount("30% off!", percent=30)

        product_list[0].set_promotion(second_half_price)
        product_list[1].set_promotion(third_one_free)
        product_list[3].set_promotion(thirty_percent)

    except TypeError as e:
        print("Store initialization failed", e)
        sys.exit()


    dict_for_choice = {1: display_products,
                       2: display_total_amount,
                       3: get_order,
                       4: sys.exit
                       }

    while True:
        display_menu()
        try:
            choice = int(input("Please choose a number: "))

            if choice < 1 or choice > 4:
                continue

            elif choice == 4:
                dict_for_choice[choice]()

            products = best_buy.get_all_products()
            dict_for_choice[choice](best_buy, products)

        except ValueError:
            print("Error with your choice! Try again!")


if __name__ == "__main__":
    main()
