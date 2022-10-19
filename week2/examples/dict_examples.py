my_car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
}

# for key in my_car.keys():
#     print(key)
#     print(my_car[key])
# ['brand', 'model', 'year']
# for value in my_car.values():
#     print(value)
# ['Ford', 'Mustand', 1964]
for (key, value) in my_car.items():
    print(key, value)
# [('Brand','Ford'),('Model','Mustang'),('Year',1964)   ]

# my_cars = {}
# car_properties = [["Ford","Mustang",1964],["Chevy","Malibu",1999]]

# for (brand, model, year) in car_properties:
#     # brand = car[0]
#     # model = car[1]
#     # year = car[2]

#     if my_cars.get(brand):
#         continue

#     my_cars[brand] = {
#         "brand": brand,
#         "model": model,
#         "year": year
#     }

# print(my_cars)

# my_car["brand"]     # Ford
# my_car.get("brand") # Ford

# my_car["brnad"]     # KeyError: 'brnad'
# brand = my_car.get("brnad") # None
# print(brand)



# my_car["brand"] = "Chevy"
# my_car["model"] = "Malibu"
# my_car["year"] = 2022

# my_car["mileage"] = 29