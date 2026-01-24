#12.1 print entered char is vowel or consonent
def CharVowel(Char):
    if (Char == "a" or Char == "e" or Char == "i" or Char == "o" or Char == "u" or Char == "A" or Char == "E" or Char == "I" or Char == "O" or Char == "U"):
        return (Char, "is Vowel alphabet")
    
    return (Char, "is Consonent alphabet ")

#12.2 Find the factors of provided number
def Factors(Num):
    Data = []
    
    for i in range(1,Num+1):
        if (Num % i) == 0:
            Data.append(i)
            #print (Data)
    return (Data)

#12.3 Accepts two number and do the addition, Substraction, Multiplcation and Division
#Addition
Addition = lambda A,B : A+B
#Substration
Substraction = lambda A,B : A-B
#Multiplication
Multiplication = lambda A,B : A*B
#Division
Division = lambda A,B : A/B

#12.4 Take number and print all the number start from 1
def printNumber(Num):
    Data = []
    for i in range(1,Num+1):
        print (i)
        Data.append(str(i))
    return ' '.join(Data)

#12.5 Take number and print all the number till 1 in reverse order
def printNumberReverse(Num):
    Data = []
    for i in range(1,Num+1):
        #print (i)
        Data.append(str(i))
    return ' '.join(Data[::-1])

def main():
    print ("----------------------------------")
    Char = str (input(("Enter the alphabet for Vowel & Consonent check :")))
    result = CharVowel(Char)
    print (result)
    print ("----------------------------------")
    
    Num = int(input("Enter the number for factor calculation :"))
    result = Factors(Num)
    print (result)
    print ("----------------------------------")

    print ("----------------------------------")
    No1 = int (input("Enter first Number :"))
    No2 = int (input("Enter second Number :"))
    print ("----------------------------------")

    if (No1 < No2):
        print ("Substraction and Division would invalid or negative")
        No2 = int (input("Enter second number less than No1:"))
        
    result = Addition(No1,No2)
    print ("Addition of two number is :",result)
    print ("----------------------------------")

    result = Substraction(No1,No2)
    print ("Substraction of two number is :",result)
    print ("----------------------------------")

    result = Multiplication(No1,No2)
    print ("Multiplication of two number is :",result)
    print ("----------------------------------")

    result = Division(No1,No2)
    print ("Division of two number is :",result)
    print ("----------------------------------")

    Num = int(input("Enter the number :"))
    result = printNumber(Num)
    print("All the numbers starting from 1 till the number is :",result)
    print ("----------------------------------")

    Num = int(input("Enter the number :"))
    result = printNumberReverse(Num)
    print("All the numbers in reverse order for the the number till 1 is :",result)
    print ("----------------------------------")

if __name__ == "__main__":
    main()
