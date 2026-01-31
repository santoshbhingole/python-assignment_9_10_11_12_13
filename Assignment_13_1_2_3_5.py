#Program to accpet the lenth and width of rectanle and print area
def RectangleArea(Length, Width):
    Area = Length * Width
    return Area

def CicleArea(Radius):
    Area = (Radius * Radius)
    return Area

def PerfectNum(Num):
    sum = 0
    Data = []
    for i in range(1, Num):
        if ( Num % i == 0):
            sum = sum + i
            Data.append(i)
            #print(Data)
            #print(sum)
    if (sum == Num):
        return "Enetered Number", Num ,"is Perfect Number"
    else: 
        return "Enetered Number", Num ,"is not Perfect Number"

def Display(Marks):
    if (Marks >= 75):
        return "You are PASSED in Distinction"
    if (Marks >= 60):
        return "You are PASSED in First Class"
    if (Marks >= 50):
        return "You are PASSED in Second Class"
    if (Marks <= 50):
        return "You are FAILED"
            
def main():
    Length = int (input("Enter Length for rectanle :"))
    Width = int (input("Enter Width for rectanle :"))
    Result = RectangleArea(Length,Width)
    print("Area of rectangle is :", Result)

    Radius = int (input("Enter radius of cicle :"))
    Result = CicleArea(Radius)
    print("Area of rectangle is :", Result)

    Number = int (input("Enter for perfect number validation :"))
    Result = PerfectNum(Number)
    print (Result)

    Marks = int (input("Enter the marks for grade validation :"))
    Result = Display(Marks)
    print (Result)

if __name__ == "__main__":
    main()

