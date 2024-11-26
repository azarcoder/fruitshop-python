all_fruits_data = [
    {"fruitName": "apple", "price": 67, "unit": "kg", "imported_from": "USA"},
    {"fruitName": "banana", "price": 30, "unit": "dozen", "imported_from": "India"},
    {"fruitName": "grapes", "price": 120, "unit": "kg", "imported_from": "Chile"},
    {"fruitName": "orange", "price": 80, "unit": "kg", "imported_from": "Spain"},
    {"fruitName": "mango", "price": 150, "unit": "kg", "imported_from": "Mexico"},
]


class Fruits:
    all_fruits = []

    def __init__(self, name, price, unit, imported_from):
        self.fruitName = name
        self.price = price
        self.isAvail = True
        self.unit = unit
        self.imported_from = imported_from
        Fruits.all_fruits.append(
            {
                "fruitName": self.fruitName,
                "price": self.price,
                "unit": self.unit,
                "availability": self.isAvail,
                "imported_from": self.imported_from,
            }
        )

    # view all fruits
    @classmethod
    def view_all_fruits(cls):
        for f in cls.all_fruits:
            print(f)

    # imported_from search
    @classmethod
    def search_by_import(cls, country):
        f = False
        data = ""
        for i in cls.all_fruits:
            if i["imported_from"] == country:
                f = True
                data = i
                break
        print(data if f else f"no fruits imported from {country}")

    # make unavailable
    @classmethod
    def make_unavail(cls, fruitName):
        for f in cls.all_fruits:
            if f["fruitName"] == fruitName:
                f["availability"] = False

    @classmethod
    def available_fruits(cls):
        for f in cls.all_fruits:
            if f["availability"]:
                print(f)
    
    @classmethod
    def price_range(cls, minValue, maxValue):
        for i in cls.all_fruits:
            if i['price'] >= minValue and i['price'] <= maxValue:
                print(i)



# load all fruits data to Fruits class's all_fruits
for i in all_fruits_data:
    Fruits(
        name=i["fruitName"],
        price=i["price"],
        unit=i["unit"],
        imported_from=i["imported_from"],
    )


# Fruits.make_unavail('banana')
# Fruits.available_fruits()
# Fruits.view_all_fruits()
# Fruits.search_by_import(Fruits, "UK")
