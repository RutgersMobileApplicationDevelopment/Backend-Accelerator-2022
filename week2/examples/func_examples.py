# # # show_examples(0)
# def add_two_numbers(x, y):
#     return x + y

# def summation_1_to_n(n):
#     summation = 0
#     for i in range(1, n+1):
#         summation += i
#     return summation

# # show_examples(1)
# def half_all(input_list):
#     for i in range(len(input_list)):
#         input_list[i] //= 2

# ex_list = [1,2,3,4,5]
# half_all(ex_list)
# print(ex_list)

# # show_examples(2)
valid_logins = {
    "admin":"my_password",
    "ben":"1234567",
    "rumad":"ABcdEF"
}

def login(username, password):
    if username in valid_logins:
        print("valid username")
        if valid_logins[username] == password:
            print("valid password")
            return True
        else:
            print("invalid password")
    else:
        print("invalid username")

    return False

authenticated = login("admin","my_password")
print(authenticated)