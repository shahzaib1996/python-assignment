para = input("Enter any String: ")

words = para.split()

wordFreq = {}

for val in words:
    keys = wordFreq.keys()
    if val in keys:
        wordFreq[val] += 1
    else:
        wordFreq[val] = 1

print(wordFreq)
for key,val in wordFreq.items():
    print(key+" : "+str(val))