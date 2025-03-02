class code:
    company="microsoft"
    name="krish"
    salary=123333
    def coding(self):
        print(f"this is name of empolees {self.name},company {self.company},and salary{self.salary}")

class coder:
    lang="python"    
    def coding2(self): 
        print(f"the most uses lang in world{self.lang}")

    
class lang(code,coder):
    company="infosys"
    def coding3(self): 
        print(f"the most famous company in world{self.company}")

    
a=code()
b=coder()
c=lang()

#print(a.company,a.name,a.salary,b.company,c.lang)
a.coding()
b.coding2()
c.coding3()
