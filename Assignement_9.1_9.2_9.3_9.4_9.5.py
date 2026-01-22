#9.1 Display "Jay Ganesh" on console
def Display():
    print ("Jay Ganesh")

#9.2 Check greater number 
def ChkGreater(No1, No2):
    if No1 > No2:
        print (No1, "is greater")
    else:
        print (No2, "is greater")

#9.3 Square of number
def Square(No):
    sq = (No*No)
    return sq

#9.4 Cube of number
def Cube(No):
    Cube_Result = (No**3)
    return Cube_Result

#9.5 Divisible by 3 & 5
def Divisible(No):
    if (No % 5 == 0 and No % 3 == 0):
        print ("Provied number is divisible by 3 & 5")
    else:
        print ("Provied number is not divisible by 3 & 5")
    

def main():
    Display()
    
    ChkGreater(10,20)
    
    Result_sq = Square(5)
    print (Result_sq)

    No = int (input("Enter the number for cube operation :"))
    Result_Cube = Cube(No)
    print (Result_Cube)

    No = int (input("Enter the number for divisible by 3 & 5 :"))
    Divisible(No)


if __name__ == "__main__":
    main()