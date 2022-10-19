# Lists[0]
my_bools = [True,False,False]
if my_bools[0] == True:
    print("Hello World!")
# output: Hello World!

# my_any = [15,True,"apple"]
# print(my_any[2])
# # output: apple
# if my_any[2] == "apple":
#     print(len(my_any))
#     # output: 3

# # Lists[1]
# my_ints = [1,2,3,4,5]
# my_ints.append(6)
# # "appends" 6 to end of the list
# # my_ints: [1, 2, 3, 4, 5, 6]

# my_any = [15,True,"apple"]
# print("apple" in my_any) # True
# my_any.remove("apple")
# # my_any: [15, True]
# print("apple" in my_any) # False

# del my_any[0]
# # deletes the item at index=0
# # my_any: [True]

# # Lists[2] (extra.)

# my_ints = [5,2,3,1,4]
# print(my_ints[:3]) # [5, 2, 3]
# # Sort simple lists and even more
# # complex ones. (timsort)
# my_sorted_ints = sorted(my_ints)
# # my_sorted_ints: [1, 2, 3, 4, 5]

# # List comprehension is awesome and insanely useful!
# # List comprehensions run faster than regular for loops, and can look so much cleaner!
# comprehension = [i for i in my_ints if i >= 3]

# # compared to the normal way of writing it...
# regular = []
# for i in my_ints:
#     if i >= 3:
#         regular.append(3)
