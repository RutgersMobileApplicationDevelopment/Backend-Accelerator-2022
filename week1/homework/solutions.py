my_int = 10
# Problem 1.
if my_int + 5 == 15:
    print("1. OK")
else:
    print("1. INCOMPLETE")




# Problem 2.
my_list = ["abc","def","hij","klm","nop"]
is_def_in_list = False

# Solution A. (Great! Very pythonic)
is_def_in_list = "def" in my_list

# Solution B. (Good solution, not bad.)
if "def" in my_list:
    is_def_in_list = True

# Solution C. (Works, but python makes it so much easier than this!)
for string in my_list:
    if string == "def":
        is_def_in_list = True
        break

if is_def_in_list:
    print("2. OK")
else:
    print("2. INCOMPLETE")




# Problem 3.
for item in my_list:
    print(item)

for i in range(len(my_list)):
    print(my_list[i])




# Problem 4.
my_list = [1,2,3,4,5]

# Solution A. (Great!)
my_list.extend([6,7])

# Solution B. (Okay.)
my_list.append(6)
my_list.append(7)




# Problem 5:
my_solution = ["Any","list","is","okay!"]
print(my_solution)