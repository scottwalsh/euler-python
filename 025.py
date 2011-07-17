last = 1
current = 1
count = 2

while True:
    next = last + current
    print(next)
    count = count + 1
    if len(str(next)) == 1000:
        print(next)
        break

    last = current
    current = next
print(count)
