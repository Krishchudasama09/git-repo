class calclutor:
    def __init__(self,n):
        self.n=n
    
    def squre(self):
        print(f"this a squre{self.n*self.n}")
    def cube(self):
        print(f"this a cube{self.n*self.n*self.n}")
    def squreroot(self):
        print(f"this a squreroot{self.n**1/2}")


a=calclutor(4)
a.squre()
a.cube()
a.squreroot()