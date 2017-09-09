utxt = input("Enter a sentence: ")
num = ['0','1','2','3','4','5','6','7','8','9']
words=utxt.split()
mydigits = []
for val in words:
    check = 0;
    for val1 in val:
        if val1 in num:
            check = 1;
        else:
            check = 0;
            break;
    if check == 0:
        continue
    else:
        mydigits.append(val)
print(mydigits)
