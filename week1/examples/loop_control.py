# loop_control[0]
my_any = [15, True, "apple"]

for item in my_any:
    print(item)
# 15
# True
# apple

my_any = ["cherry", 9, False, 15, True, "apple"]
for item in my_any:
    if item == "cherry":
        break # ends the loop
    print(item)
# no output

# loop_control[1]
for item in my_any:
    if item == 9 or item == 15:
        continue # skip item and jump to next
    print(item)
# cherry
# True
# apple