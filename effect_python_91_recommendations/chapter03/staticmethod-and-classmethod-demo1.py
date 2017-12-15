class Fruit(object):
    total = 0

    def __init__(self, area="", category="", batch=""):
        self.area = area
        self.category = category
        self.batch = batch

    @classmethod
    def Init_Product(cls, product_info):
        area, category, batch = map(int, product_info.split('-'))
        fruit = cls(area, category, batch)
        return fruit 

    @classmethod
    def print_total(cls):
        print(cls.total)
        print(id(Fruit.total))
        print(id(cls.total))

    @classmethod
    def set(cls, value):
        print("calling class_method(%s, %s)" % (cls, value))
        cls.total = value

    @staticmethod
    def is_input_valid(product_info):
        area, category, batch = map(int, product_info.split('-'))
        try:
            assert 0 <= area <= 10
            assert 0 <= category <= 15
            assert 0 <= batch <= 99
        except AssertionError:
            return False
        return True


class Apple(Fruit):
    pass


class Orange(Fruit):
    pass

'''
app1 = Apple()
app1.set(200)
app2 = Apple()
org1 = Orange()
org1.set(300)
org2 = Orange()
app1.print_total()
org1.print_total()
'''

app1 = Apple(2, 5, 10)
org1 = Orange.Init_Product("3-3-9")
print("app1 is instance of Apple: " + str(isinstance(app1, Apple)))
print("org1 is instance of Orange: " + str(isinstance(org1, Orange)))
