class employes:
    a=1
    def controcture(self):
        print("controcture of employes")

class employes2(employes):
    b=2
    def controcture1(self):
        print("controcture of employes2")

class employes3(employes2):
    c=3
    def controcture2(self):
        super().__init__()
        print("controcture of employes3")

a=employes()
print(a.a)
a.controcture()

a=employes2()
print(a.a,a.b)
a.controcture1()

a=employes3()
print(a.a,a.b,a.c)
a.controcture2()


# a.controcture()
# a.controcture1()
# a.controcture2()