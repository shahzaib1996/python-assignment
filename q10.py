def f(x):
    if x != 0:
        return f(x-1) + 100
    else:
        return 0

num = int(input("Enter a Number : "))
print(f(num))


