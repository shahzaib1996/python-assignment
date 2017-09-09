from operator import itemgetter

mytuple = []
print("Format i.e Shahzaib,20,95 | To terminate loop input blank")
while(1):
    utxt = input("Enter Name,Age,Height : ")
    if utxt == "":
        break;
    x = tuple(utxt.split(','))
    mytuple.append(x)
sortedList = list(sorted(mytuple, key=itemgetter(0,1,2)))
print(sortedList)
