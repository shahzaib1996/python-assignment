class Mygenerator():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def generator(self):
        for val in range(self.x,(self.y+1)):
            if val%7 == 0:
                print(val)


obj = Mygenerator(0,21) #passing range from 0 to 21
obj.generator()