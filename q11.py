def checkValidity(upass):
    chkSm = 0;
    chkCa = 0;
    chkDi = 0;
    chSc = 0;
    chLen = 0;
    x = list(upass)
    lenght = len(x)
    if lenght <= 12 and lenght >= 6:
        chLen = 1

    for val in x:
        cnum = int(ord(val))
        if cnum <= 122 and cnum >= 97:
            chkSm = 1;
        if cnum <= 90 and cnum >= 65:
            chkCa = 1;
        if cnum <= 57 and cnum >= 48:
            chkDi = 1;
        if (cnum == 36 or cnum == 35 or cnum == 64) and (cnum != 32):
            chSc = 1;

    if chkSm == 1 and chkCa == 1 and chkDi == 1 and chSc == 1 and chLen == 1:
        print(upass+" Valid Password")


password = input("Enter Sequence of Password Seperated By Comma: ")
passList = password.split(',')
for value in range(len(passList)):
    checkValidity(passList[value])


