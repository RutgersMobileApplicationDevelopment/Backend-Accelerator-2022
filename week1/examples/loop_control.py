# loop_control[0]
my_any = [15, True, "apple"]

for item in my_any:
    print(item)

# 15
# True
# apple

my_any = ["cherry", 9, False, 15, True, "apple"]
for item in my_any:
    if item == True:
        break
    print(item)

# cherry
# 9
# False
# 15

# loop_control[1]
for item in my_any:
    if item == False or item == 15:
        continue
    print(item)

# cherry
# 9
# True
# apple