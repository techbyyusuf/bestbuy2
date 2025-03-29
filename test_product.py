import pytest
from products import Product
from store import Store


def test_create_object():
    adidas = Product(name="Adidas", price=50.0, quantity=100)
    assert isinstance(adidas, Product)

def test_create_object_with_empty_name():
    with pytest.raises(TypeError) as e:
        object_with_empty_name = Product(name = "", price=5, quantity= 100)
    assert "Empty names are not allowed!"

def test_create_object_with_negative_price():
    with pytest.raises(TypeError) as e:
        object_with_negative_price = Product(name="N", price=-5, quantity=250)
    assert "No prices below zero."

def test_zero_quantity_product_is_inactive():
    adidas = Product(name="Adidas", price=50.0, quantity=100)
    adidas.buy(100)
    assert adidas.is_active() == False

def test_create_object_with_zero_quantity():
    adidas = Product(name="Adidas", price=50.0, quantity=0)
    assert adidas.is_active() == False

def test_quantity_after_purchase():
    adidas = Product(name="Adidas", price=50.0, quantity=100)
    adidas.buy(10)
    assert adidas.get_quantity() == 90

def test_purchase_over_quantity():
    adidas = Product(name="Adidas", price=50.0, quantity=100)
    adidas.buy(200)
    assert adidas.get_quantity() == 100

pytest.main()