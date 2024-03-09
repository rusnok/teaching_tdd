import pytest
class Product:
    def __init__(self, name: str, volume: float):
        self.name = name
        self.volume = volume


class Warehouse:
    def __init__(self, capacity: float):
        self.capacity = capacity
        self.products = []

    def __calculate_free_space(self):
        sum_od_products = sum([x.volume for x in self.products])
        return self.capacity - sum_od_products

    def add(self, product: Product):
        rest_space = self.__calculate_free_space()
        if rest_space >= product.volume:
            self.products.append(product)
            return rest_space - product.volume
        else:
            return -1


@pytest.fixture
def produkty():
    a = Product("kniha", 4.5)
    b = Product("auto", 10)
    return a, b

@pytest.fixture
def sklad():
    return Warehouse(8.5)

def test_Warehouse_add(produkty, sklad):
    produkt1, produkt2 = produkty
    zbytek1 = sklad.add(produkt1)
    zbytek2 = sklad.add(produkt2)
    zbytek1_expected = 4.0
    zbytek2_expected = -1
    assert zbytek1 == zbytek1_expected
    assert zbytek2 == zbytek2_expected

@pytest.fixture
def products():
    return [Product("name1", 24.30), Product("name2", 42), Product("name3", 75.98)]


@pytest.mark.parametrize("capacity, result", [(100, -1), (142.28, 0), (150, 7.72)])
def test_warehouses(capacity, result, products):
    w = Warehouse(capacity)
    last_result = None
    for product in products:
        last_result = w.add(product)

    assert round(last_result, 2) == result