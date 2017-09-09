heads = int(input("Enter Heads: "))
legs = int(input("Enter Legs: "))
chicken = 0;
rabbit = 0;

for a in range(0,(heads)) :
    b = heads - a
    x = (a*2)+(b*4)
    if x == legs:
        chicken = a;
        rabbit = b;

print("Chickens: "+str(chicken)+" , Rabbits: "+str(rabbit))