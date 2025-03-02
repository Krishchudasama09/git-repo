while True:
    try:
        a = int(input("Enter your 1st number: "))
        b = int(input("Enter your 2nd number: "))
        print("Result:", a / b)
        break  # Exit loop on successful division
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed. Please enter a non-zero denominator.")
    except ValueError:
        print("Error: Please enter valid integer numbers.")
    except Exception as e:
        print(f"Unexpected error: {e}")

print("Done")
