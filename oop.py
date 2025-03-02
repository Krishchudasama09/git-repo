class programmer:
    company= "microsoft"
    def __init__(self,name,salary,pincode):
        self.name=name
        self.salary=salary
        self.pincode=pincode
    
k = programmer ("krish", 12000, 232434)

# Corrected print statement
print(k.name,k.salary,k.pincode,k.company)