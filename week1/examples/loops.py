# Loops[0]
for i in range(6):
    print(i)
# 0
# 1
# 2
# 3
# 4
# 5

j = 5
while j >= 0:
    print(j, j >= 0)
    j -= 1
print("exited loop", j, j >= 0)
# Runs 6 times, ranging from 5 to 0

# 5 True
# 4 True
# 3 True
# 2 True
# 1 True
# 0 True
# exited loop -1 False