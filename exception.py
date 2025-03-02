# a = int(input("Enter your 1st number: "))

while True:
    a= int(input("Enter your 1st number: "))
    b = int(input("Enter your 2nd number: "))
    
    try:
        print("Result:", a / b)
        
    except ZeroDivisionError:
        print("Error: Division by zero")

print("Done")
