from time import time
import random as r
from tkinter import Tk, Label, Entry, Button, Text, END, messagebox

# Function to calculate errors
def mistek(peratest, usertest):
    error = 0
    min_length = min(len(peratest), len(usertest))

    for i in range(min_length):
        if peratest[i] != usertest[i]:
            error += 1

    error += abs(len(peratest) - len(usertest))
    return error

# Function to calculate typing speed
def speed_time(time_s, time_e, userinput):
    time_delay = time_e - time_s
    if time_delay == 0:
        return 0
    speed = len(userinput) / time_delay
    return round(speed)

# Function to start the test
def start_test():
    global test1, time_1
    test1 = r.choice(test)
    test_label.config(text=test1)
    input_entry.delete(0, END)
    result_text.delete(1.0, END)
    time_1 = time()

# Function to evaluate the test
def evaluate_test():
    time_2 = time()
    user_input = input_entry.get()
    speed = speed_time(time_1, time_2, user_input)
    errors = mistek(test1, user_input)

    result_text.delete(1.0, END)
    result_text.insert(END, f"Speed: {speed} characters per second\n")
    result_text.insert(END, f"Errors: {errors}")

    if errors == 0:
        messagebox.showinfo("Result", "Congratulations! You made no errors!")
    else:
        messagebox.showwarning("Result", f"You made {errors} errors. Try again!")

# List of test sentences
test = [
    "Syntans are made by treating aromatic substances like phenols",
    "Cresols, naphthalenes, formaldehyde, and sulfuric acid",
    "They can vary in ingredients, quantities",
    "Manufacturing methods they can produce white or",
    "Buff-colored leather that darkens when exposed to light."
]

# Create the main window
root = Tk()
root.title("Typing Speed Test")
root.geometry("500x400")
root.configure(bg="#f0f0f0")  # Set background color for the window

# Styling variables
FONT = ("Arial", 12)
BUTTON_BG = "#4CAF50"  # Green
BUTTON_FG = "white"
LABEL_BG = "#f0f0f0"
ENTRY_BG = "white"
TEXT_BG = "white"

# Label to display the test sentence
test_label = Label(
    root,
    text="",
    wraplength=400,
    font=FONT,
    bg=LABEL_BG,
    fg="black"
)
test_label.pack(pady=20)

# Entry widget for user input
input_entry = Entry(
    root,
    font=FONT,
    width=50,
    bg=ENTRY_BG,
    fg="black"
)
input_entry.pack(pady=10)

# Button to start the test
start_button = Button(
    root,
    text="Start Test",
    command=start_test,
    font=FONT,
    bg=BUTTON_BG,
    fg=BUTTON_FG,
    padx=10,
    pady=5
)
start_button.pack(pady=10)

# Button to evaluate the test
evaluate_button = Button(
    root,
    text="Evaluate",
    command=evaluate_test,
    font=FONT,
    bg=BUTTON_BG,
    fg=BUTTON_FG,
    padx=10,
    pady=5
)
evaluate_button.pack(pady=10)

# Text widget to display results
result_text = Text(
    root,
    height=5,
    width=50,
    font=FONT,
    bg=TEXT_BG,
    fg="black"
)
result_text.pack(pady=20)

# Run the application
root.mainloop()