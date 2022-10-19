# Conditions[0]
# username = "admin"
# password = "password"

# username2 = "rumad"
# password2 = "rumad_password"

# my_username = "ben"
# my_password = "abcdefgh"
# # Condition syntax
# if my_username == username and my_password == password:
#     print("Logged into admin")
# elif my_username == username and my_password == password2:
#     print("Logged into rumad")
# else:
#     print("Failed to log in")


# Conditions[1]
# You can write this...
# if my_username == username and my_password == password:
#     logged_in = True
# else:
#     logged_in = False

# # or simply write this!
# logged_in = my_username == username and my_password == password

# Slide 3
# prod_1 = 9*7    # 63
# prod_2 = 3*15   # 45

# if prod_1 > prod_2:
#     print("prod_1 greater than prod_2")
# elif prod_2 == prod_2:
#     print("prod_1 equal to prod_2")
# else:
#     print("prod_1 less than prod_2")

cash_in_wallet = 80
price = 75

can_purchase = cash_in_wallet >= price
print(can_purchase)