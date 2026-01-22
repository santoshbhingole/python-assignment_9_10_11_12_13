#11.1 Check whether number if prime or not
def PrimeNum(Num):
    if (Num <= 1):
        return (Num, "is not in the list of prime numbers")
    for i in range (2, Num):
        if (Num % 2) == 0:
            return (Num, "is not prime number")
    return (Num, "is prime the number")

#11.2 Get one number and print count of digit in that number
def Countofdigit(Num):
    NumStr = str(Num)
    lenData = len(NumStr)
    print (lenData)
    Data = []
    #count = 0
    for i in NumStr:
        Data.append(i)
    lenData = len(Data)
    #print (lenData)
    return lenData
        
    # for i in Data:
    #     count = count + Data(i)
    # return count

#11.3 Get one number and print sum of digit in that number
def SumOfDigit(Num):
    NumStr = str(Num)
    Data = []
    sum = 0
    for i in NumStr:
        Data.append(i)
            
    for i in Data:
        sum = sum + int(i)
    return sum

#11.4 Get one number and print the reverse of the digit
def ReverseDigit(Num):
    NumStr = str(Num)
    Data = []
    count = 0
    for i in NumStr:
        Data.append(i)

    return ''.join(Data)

    # for i in lenData:
    #     #print(int(i))
    #     i = i + 1
    #     print (count)

#11.5 Print if given number is panlindrome number
def Palindrom(Num):
    NumStr = str(Num)
    Data = []
    count = 0
    for i in NumStr:
        Data.append(i)

    #print (''.join(Data))
    #print (''.join(Data[::-1]))

    if (Data == Data[::-1]):
        return (Num, "It is palindrome number")
    
    return (Num, "It is not palindrome number")

def main():
    print ("-----------------------------------")
    
    result = PrimeNum(11)
    print (result)
    print ("-----------------------------------")

    result = Countofdigit(7421)
    print ("Count of digits in given number is :", result)
    print ("-----------------------------------")

    result = SumOfDigit(123)
    print ("Sum of the digits in given number is :",result)
    print ("-----------------------------------")

    result = ReverseDigit(4567)
    print ("Reverse of digits of given number is :", result)
    print ("-----------------------------------")

    result = Palindrom(121)
    print (result)
    print ("-----------------------------------")

if __name__ == "__main__":
    main()