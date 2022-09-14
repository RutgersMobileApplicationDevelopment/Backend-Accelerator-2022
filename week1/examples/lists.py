# Lists[0]
my_ints = [1,2,3,4,5]
my_bools = [True,False,False]
my_any = [15,True,"apple"]

print(my_any[4])
# output: apple

if my_bools[0] == True:
    print(my_any)
    # output: [15, True, 'apple']

if my_any[2] == "apple":
    print(len(my_any))
    # output: 3

# Lists[1]
my_ints.append(6)
# "appends" 6 to end of the list
# my_ints: [1, 2, 3, 4, 5, 6]

print("apple" in my_any) # True
my_any.remove("apple")
# my_any: [15, True]
print("apple" in my_any) # False

del my_any[0]
# deletes the item at index=0
# my_any: [True]

# Lists[2] (extra.)
my_ints = [5,2,3,1,4]
print(my_ints[:3]) # [5, 2, 3]
# Sort simple lists and even more
# complex ones. (timsort)
my_sorted_ints = sorted(my_ints)
# my_sorted_ints: [1, 2, 3, 4, 5]

my_bools = [True,False,True,True,False]
# List comprehension is awesome and insanely useful!
# It's used below to create a sub-list of my_bools with only the true values.
true_bools = [b for b in my_bools if b == True]

# Returns true if there is any value that is true in the list
is_true_in_bools = any(my_bools)
