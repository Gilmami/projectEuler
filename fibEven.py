#Find sum of even fibbonacci numbers under 4,000,000.
#first generate fibbonacci sequence
#then check if they are even
#then sum the numbers I find.
n1 = 1
n2 = 2
nth = 0
fib = [1, 2]
for i in range(1, 1000):
    if n1 + n2 <= 4000000:
        nth = n1 + n2
        fib.append(nth)
        n1 = n2
        n2 = nth
sumOfEvens = 0
for num in fib:
    if num % 2 is 0:
        sumOfEvens = sumOfEvens + num
print(sumOfEvens)
