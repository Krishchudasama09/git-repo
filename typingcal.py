from time import time
import random as r

def mistek(peratest, usertest):
    error = 0  # Start from 0 instead of 1
    min_length = min(len(peratest), len(usertest))

    for i in range(min_length):
        if peratest[i] != usertest[i]:
            error += 1

    # Add remaining extra characters as errors
    error += abs(len(peratest) - len(usertest))
    
    return error

def speed_time(time_s, time_e, userinput):
    time_delay = time_e - time_s
    if time_delay == 0:  # Prevent division by zero
        return 0
    speed = len(userinput) / time_delay
    return round(speed)



test = [

    "Syntans are made by treating aromatic substances like phenols",
    "Cresols, naphthalenes, formaldehyde, and sulfuric acid",
    "They can vary in ingredients, quantities",
    "Manufacturing methods they can produce white or",
    "Buff-colored leather that darkens when exposed to light."]

test1 = r.choice(test)
print("******* Typing Speed Test *********")
print(test1)
print("\n")

time_1 = time()
testinput = input("Enter: ")
time_2 = time()

print("\nSpeed:", speed_time(time_1, time_2, testinput), "characters per second")
print("Errors:", mistek(test1, testinput))









# 


