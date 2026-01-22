#10.1 multiplication table of provided number
def MultiplicationTable(No):
    mult = 0
    Data = []
    for i in range(1,11):
        mult = No * i
        Data.append(mult)
    return Data

#10.3 Factorial of given number
def factorial(No):
    fact = 1
    for i in range(1,No+1):
        fact = fact * i
        #print (fact)
    return fact

#10.4 Sum of N natural number
def MultNaturalNum(No):
    sum = 0
    for i in range (1,No+1):
        sum = sum + i
    return sum

#10.5 Accept number and print sum of odd and even number
def PrintEvenNumber(No):
    sum = 0
    Data = []   
    for i in range (1, No+1):
        if (i%2 == 0):
            Data.append(i)
    return Data
    
#10.6 Accept number and print sum of odd and even number
def PrintOddNumber(No):
    sum = 0
    Data = []   
    for i in range (1, No+1):
        if (i%2 != 0):
            Data.append(i)
    return Data

#10.7 Print if provided number is prime or not
def PrimeNumber(Num):
    if (Num <= 1):
        return (Num, " is not in list of prime number")
    
    for i in range (2, Num):
        if (Num % i) == 0:
            return (Num, "is not prime number")
            
    return (Num, "is prime number")
       
def main():
    print ("-----------------------------------")
    No = int (input("Enter the number of multiplication table :"))
    Result = MultiplicationTable(No)
    print ("Mulitplcation table of given number is :", Result)
    print ("-----------------------------------")
    
    result_Fact = factorial(5)
    print ("Factorial of given number is :", result_Fact)
    print ("-----------------------------------")

    result_natural = MultNaturalNum(5)
    print ("Sum of N natural number is :", result_natural)
    print ("-----------------------------------")

    NoEven = int (input("Enter the Even number :"))
    result_Even = PrintEvenNumber(NoEven)
    print ("All even number till the provided even number is:", result_Even)
    print ("-----------------------------------")

    NumOdd = int (input("Enter the Odd number :"))
    result_Odd = PrintOddNumber(NumOdd)
    print ("All odd numbers till provided odd number is:", result_Odd)
    print ("-----------------------------------")

    Num = int (input("Enter number for prime number validation :"))
    result_prime = PrimeNumber(Num)
    print (result_prime)
    print ("-----------------------------------")


if __name__ == "__main__":
    main()