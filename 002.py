last = 1
current = 1
total = 0

while current < 4000000:
    next = last + current
    if next % 2 == 0:
        total = total + next
        print(next)

    last = current
    current = next
print(total)
