
#now I need to make that iterate over all numbers from one to 1 billion.
#then I need to figure out how to compare each digit to ensure it's odd (how do I add the number now that I know EVERY digit is odd?)
#then I think that's it.
def isNumberReversible(number):

#this is where we take a number as input, and convert it into a string.
    numberAsString = str(number)
    reversedStringNumber = str()

#this is how I decided to reverse the string, go from the negative index
    for i in range(1, len(numberAsString)+1):
        reversedStringNumber = reversedStringNumber + numberAsString[-i]

#then I go ahead and add the two together to get the sum, as per the problem
    numbersCombined = number + int(reversedStringNumber)

#turn into string to work with it
    stringCombinedNumber = str(numbersCombined)

#set up a boolean value to change if the digit is ever odd, it doesn't count number as having all odd digits
    isAllOdd = True

#This block does one thing: if we see a single odd number, give up, otherwise, check next number.

    for i in range(0,len(stringCombinedNumber)):
        if isAllOdd is True:
            if int(stringCombinedNumber[i]) % 2 is 1:
                isAllOdd = True
                continue
            else:
                isAllOdd = False
                break
        else:
            break

    if reversedStringNumber[0] is "0":
        isAllOdd = False

    return(isAllOdd)
    print(isAllOdd)
#This is the end of the reversibility check!

#this is how many reversible numbers are under a birrion.
numRev = 0
for i in range(1, 1000000000):
    if isNumberReversible(i) is True:
        numRev = numRev + 1
#    numberOfReversible = numberOfReversible + isNumberReversible(i)
print(numRev)
