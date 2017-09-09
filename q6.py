def numDivideByZero(x):
    try:
        print(x / 0)
    except ZeroDivisionError:
        print("Cannot divided by zero")

num =  int(input("Enter Number to divide by zero: "))
numDivideByZero(num)