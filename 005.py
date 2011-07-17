success = False
number = 0
while ( success == False ):
    number = number + 20
    for i in reversed(xrange(1,20)):
        print(i)
    	if number % i != 0:
            break
        if i == 2:
            success = True
print(number)
