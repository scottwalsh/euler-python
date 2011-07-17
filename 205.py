import random

peterWin = 0
colinWin = 0

for i in range(10000000):
    print(i)
    peter = random.randint(1,4)
    colin = random.randint(1,6)

    if peter > colin:
        peterWin = peterWin + 1
    else:
        colinWin = colinWin + 1

print(peterWin)
