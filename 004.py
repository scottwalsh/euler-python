def palindrome(number):
    string = str(number)
    stringReversed = string[::-1]
    length = len(string)
    if length != 0:
        if length % 2 == 0:
            #even
            halflength = length / 2
            #if the first half is equal to the second half reversed
            if string[0:halflength] == stringReversed[0:halflength]:
                return True
            else:
                return False
        else:
            #odd
            halflength = (length - 1) / 2
            #if the first half is equal to the last half reversed
            if string[0:halflength] == stringReversed[0:halflength]:
                return True
            else:
                return False
    else:
        return False

palindromes = []

for i in reversed(range(100,1000)):
    for j in reversed(range(100,1000)):
        result = i * j
        if palindrome(result):
             palindromes.append(result)

palindromes.sort()
print(palindromes[-1])
