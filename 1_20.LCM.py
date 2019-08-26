#first we should set up the general framework
sum = 0
for i in range(1, 1001):
    if i % 3 is 0 or i % 5 is 0:
        sum = sum + i
print(sum)
