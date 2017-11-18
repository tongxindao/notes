class Customer(object):
    def __init__(self, name, gender, phone):
        self.name = name
        self.gender = gender
        self.phone = phone
    def __str__(self):
        return "Customer({self.name}, {self.gender}, {self.phone})".format(self=self)


print(str(Customer("Lisa", "Female", "67889")))

print("=" * 30)

weather=[("Monday", "rain"),
         ("Tuesday", "sunny"),
         ("Wednesday", "sunny"),
         ("Thursday", "rain"),
         ("Friday", "cloudy")]
formatter = "Weather of '{0[0]}' is '{0[1]}'".format

for item in map(formatter, weather):
    print(item)
