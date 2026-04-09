import tkinter as tk # Has window logic
from tkinter import ttk # Has widgets

textEntryString = "" # Create a String to hold the text entry value

total = '0'
firstNumber = '0'
currentOperation = ''
operationStarted = False # Flag to check if an operation has started.
DEBUG = False;

def opButtonClick(buttonText): # Function to handle button clicks
    global total
    global firstNumber
    global currentOperation
    global operationStarted

    if DEBUG:
        print('Operation = ', buttonText) # Print the button text to the console
        print('Total = ', total)

    if buttonText in '+':
        firstNumber = total
        currentOperation = buttonText
        operationStarted = True # Set the flag to true.

def numButtonClick(number):
    global total

    if total == '0':
        total = number # If the total is 0, replace it with the button value.
    else:
        total =total+str(number) # Update the text entry string with the button value.

    displayLabel.config(text=total) # Update the label with the text entry value.

calcWindow = tk.Tk() #create a window
calcWindow.title("Calculator") # Title of the window
calcWindow.geometry("300x325") # Size of the window
calcWindow.resizable(False, False)

displayLabel = tk.Label(calcWindow, text = "0", font=("Arial", 28), justify=tk.RIGHT) # Create the label for entering the numbers.
displayLabel.grid(column=0, row=0,  columnspan=4, sticky='e') # Telling the label where it needs to be.

for col in range(4):
    calcWindow.grid_columnconfigure(col, weight=1) # Make the columns expand equally

# Row 1 Buttons
clearButton = ttk.Button(calcWindow, text="\nC\n", command = lambda: opButtonClick('')) # Creating the button.
clearButton.grid(column=0, row=1) # Placing the button in a row and column.

parenthButton = ttk.Button(calcWindow, text="\n( )\n", command = lambda: opButtonClick('( )')) # Creating the button.
parenthButton.grid(column=1, row=1) # Placing the button in a row and column.

percentButton = ttk.Button(calcWindow, text="\n%\n", command = lambda: opButtonClick('%')) # Creating the button.
percentButton.grid(column=2, row=1) # Placing the button in a row and column.

slashButton = ttk.Button(calcWindow, text="\n/\n", command = lambda: opButtonClick('/')) # Creating the button.
slashButton.grid(column=3, row=1) # Placing the button in a row and column.

# Row 2 Buttons
sevenButton = ttk.Button(calcWindow, text="\n7\n", command = lambda: numButtonClick('7')) # Creating the button.
sevenButton.grid(column=0, row=2) # Placing the button in a row and column.

eightButton = ttk.Button(calcWindow, text="\n8\n", command = lambda: numButtonClick('8')) # Creating the button.
eightButton.grid(column=1, row=2) # Placing the button in a row and column.

nineButton = ttk.Button(calcWindow, text="\n9\n", command = lambda: numButtonClick('9')) # Creating the button.
nineButton.grid(column=2, row=2) # Placing the button in a row and column.

multiButton = ttk.Button(calcWindow, text="\nx\n", command = lambda: opButtonClick('*')) # Creating the button.
multiButton.grid(column=3, row=2) # Placing the button in a row and column.

# Row 3 Buttons
fourButton = ttk.Button(calcWindow, text="\n4\n", command = lambda: numButtonClick('4')) # Creating the button.
fourButton.grid(column=0, row=3) # Placing the button in a row and column.

fiveButton = ttk.Button(calcWindow, text="\n5\n", command = lambda: numButtonClick('5')) # Creating the button.
fiveButton.grid(column=1, row=3) # Placing the button in a row and column.

sixButton = ttk.Button(calcWindow, text="\n6\n", command = lambda: numButtonClick('6')) # Creating the button.
sixButton.grid(column=2, row=3) # Placing the button in a row and column.

minusButton = ttk.Button(calcWindow, text="\n-\n", command = lambda: opButtonClick('-')) # Creating the button.
minusButton.grid(column=3, row=3) # Placing the button in a row and column.

# Row 4 Buttons
oneButton = ttk.Button(calcWindow, text="\n1\n", command = lambda: numButtonClick('1')) # Creating the button.
oneButton.grid(column=0, row=4) # Placing the button in a row and column.

twoButton = ttk.Button(calcWindow, text="\n2\n", command = lambda: numButtonClick('2')) # Creating the button.
twoButton.grid(column=1, row=4) # Placing the button in a row and column.

threeButton = ttk.Button(calcWindow, text="\n3\n", command = lambda: numButtonClick('3')) # Creating the button.
threeButton.grid(column=2, row=4) # Placing the button in a row and column.

plusButton = ttk.Button(calcWindow, text="\n+\n", command = lambda: opButtonClick('+')) # Creating the button.
plusButton.grid(column=3, row=4) # Placing the button in a row and column.

# Row 5 Buttons
plusminusButton = ttk.Button(calcWindow, text="\n+/-\n", command = lambda: numButtonClick('+/-')) # Creating the button.
plusminusButton.grid(column=0, row=5) # Placing the button in a row and column.

zeroButton = ttk.Button(calcWindow, text="\n0\n", command = lambda: numButtonClick('0')) # Creating the button.
zeroButton.grid(column=1, row=5) # Placing the button in a row and column.

periodButton = ttk.Button(calcWindow, text="\n.\n", command = lambda: numButtonClick('.')) # Creating the button.
periodButton.grid(column=2, row=5) # Placing the button in a row and column.

equalsButton = ttk.Button(calcWindow, text="\n=\n", command = lambda: opButtonClick('=')) # Creating the button.
equalsButton.grid(column=3, row=5) # Placing the button in a row and column.


# Execute the window
calcWindow.mainloop() # Show the window