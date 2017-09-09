
utxt = input("Enter any String: ")

myfreq = {}

for val in utxt:
    keys = myfreq.keys()
    if val in keys:
        myfreq[val] += 1
    else:
        myfreq[val] = 1

for key,val in myfreq.items():
    print(""+key+" , "+str(val))