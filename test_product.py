import pytest
from products import Product
import promotions


def test_create_object():
    adidas = Product(name="Adidas", price=50.0, quantity=100)
    assert isinstance(adidas, Product)
    assert adidas.get_quantity() == 100
    assert adidas.get_price() == 50.0

def test_create_object_with_empty_name():
    with pytest.raises(TypeError) as e:
        Product(name = "", price=5, quantity= 100)
    assert "Empty names are not allowed!" in str(e.value)

def test_create_object_with_negative_price():
    with pytest.raises(TypeError):
        Product(name="N", price=-5, quantity=250)
    assert "No prices below zero."

def test_zero_quantity_product_is_inactive():
    adidas = Product(name="Adidas", price=50.0, quantity=100)
    adidas.buy(100)
    assert adidas.get_quantity() == 0
    assert adidas.is_active() == False

def test_quantity_after_purchase():
    adidas = Product(name="Adidas", price=50.0, quantity=100)
    adidas.buy(10)
    assert adidas.get_quantity() == 90

def test_purchase_over_quantity():
    adidas = Product(name="Adidas", price=50.0, quantity=100)
    with pytest.raises(ValueError) as e:
        adidas.buy(200)
    assert "Not enough stock" in str(e.value)

def test_second_half_price_promotion():
    promo = promotions.SecondHalfPrice("Second for half!")
    product = Product(name="Notebook", price=10.0, quantity=10)
    product.set_promotion(promo)

    total = product.buy(2)
    assert total == 15.0  # 10 + 5


pytest.main()