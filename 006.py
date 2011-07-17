sumofsquaresTotal = 0
sumTotal = 0
for i in range(101): # remember python starts at 0
	sumofsquaresTotal = sumofsquaresTotal + (i * i)
	sumTotal = sumTotal + (i)

squareofsumTotal = sumTotal * sumTotal

print(squareofsumTotal - sumofsquaresTotal)
