
utext = input("Enter Text: ")
mychar = list(utext)
mynew = mychar[::-1]
dtxt = ""

for val in range(0, len(mynew)):
    dtxt += mynew[val]

print(dtxt)


