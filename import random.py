import random
n=random.randint
a=-1
gusses=0
while(a!=n):
    gusses+=1
    a=int(input("gusses the number"))
    if(a >n):
         print("enter the lower number")
    else:
         print("enter the larger number")
         
