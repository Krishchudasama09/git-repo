class Employes:
    a = 1
    
    def __init__(self):
        print("Constructor of Employes")

class Employes2(Employes):
    b = 2

    def __init__(self):
        super().__init__()  # Call parent constructor
        print("Constructor of Employes2")

class Employes3(Employes2):
    c = 3

    def __init__(self):
        super().__init__()  # Call parent constructor
        print("Constructor of Employes3")

# Creating an instance of Employes3
a = Employes3()
print(a.a, a.b, a.c)  # Accessing inherited attributes
