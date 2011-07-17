# http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

import math

# create a list with no even numbers (remember to add 2 back on at the end)
amount = 120000
amountroot = math.sqrt(amount)
numbers = range(3,amount+1,2)

i = 0
j = 0
while i < amountroot:
    while j < len(numbers):
        if j > i:
                if numbers[j] % numbers[i] == 0:
                    print(numbers[i])
                    print(numbers[j])
                    numbers.pop(j)
        j = j + 1
    i = i + 1
    j = 0

# add 2 back onto the start of the list
numbers.reverse()
numbers.append(2)
numbers.reverse()

print(len(numbers))
if len(numbers) > 10000:
    print(numbers[10000])
