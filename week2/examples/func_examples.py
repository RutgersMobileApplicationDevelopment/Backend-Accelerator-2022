# show_examples(0)
def add_two_numbers(x, y):
    return x + y

def summation_1_to_n(n):
    summation = 0
    for i in range(1, n+1):
        summation += i
    return summation

# show_examples(1)
def set_all_zero(input_list):
    for i in range(len(input_list)):
        input_list[i] = 0

ex_list = [1,2,3,4,5]
set_all_zero(ex_list) # [0, 0, 0, 0, 0]

# show_examples(2)
valid_logins = {
    "admin":"my_password",
    "ben":"1234567",
    "rumad":"ABcdEF"
}
def login(username, password):
    if username in valid_logins:
        if valid_logins[username] == password:
            return True

    return False