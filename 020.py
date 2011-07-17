total = 1
n = 100

while (n != 0):
    print(n)
    print(total)
    total = n * total
    n = n - 1

print(total)

numeralTotal = sum(int(each_numeral) for each_numeral in str(total))
print(numeralTotal)
