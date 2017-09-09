import math
pos = [0,0]
while(1):
    x = input("Enter Direction Steps: ")
    if x == "":
        break;
    moveList = x.split(" ")
    direct = moveList[0]
    step = int(moveList[1])
    if direct == 'up':
        pos[1] += step
    elif direct == 'down':
        pos[1] -= step
    elif direct == 'left':
        pos[0] -= step
    elif direct == 'right':
        pos[0] += step

ans = round(math.sqrt((pos[0]**2)+(pos[1]**2)))
print(ans)

