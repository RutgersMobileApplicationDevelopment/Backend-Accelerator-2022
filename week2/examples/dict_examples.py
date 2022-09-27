my_car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

my_car["brand"]     # Ford
my_car.get("brand") # Ford

my_car["brnad"]     # KeyError: 'brnad'
my_car.get("brnad") # None

my_car["brand"] = "Chevy"
my_car["model"] = "Malibu"
my_car["year"] = 2022

my_car["mileage"] = 29

my_car.keys()
# ['brand', 'model', 'year']
my_car.values()
# ['Ford', 'Mustand', 1964]
my_car.items()
# [('Brand','Ford'),('Model','Mustang'),('Year',1964)   ]