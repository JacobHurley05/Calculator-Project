#Demo Video: https://youtube.com/shorts/PEYfRcS95Ow?feature=share

import tkinter as tk # Has window logic
from tkinter import ttk # Has widgets

import math

textEntryString = "" # Create a String to hold the text entry value

total = '0'
firstNumber = '0'
currentOperation = ''
operationStarted = False # Flag to check if an operation has started.
secondMode = False
DEBUG = False;

def opButtonClick(buttonText): # Function to handle button clicks
    global total
    global firstNumber
    global currentOperation
    global operationStarted
    global operationFinished
    global secondMode

    if DEBUG:
        print('Operation = ', buttonText) # Print the button text to the console
        print('Total = ', total)

    if buttonText == '2nd':
        secondMode = True # Turns secondMode on or off.

    if buttonText in '+-*/%+/-':
        firstNumber = total
        currentOperation = buttonText
        operationStarted = True # Set the flag to true.

    elif buttonText == '=':
        operationFinished = True
        print(firstNumber, currentOperation, total) # Print the first number, operations and total.
        # Making the operations work so that when you do a number plus a operations it actually does the operations.
        if currentOperation == '+':
            total = str(float(firstNumber) + float(total))
        elif currentOperation == '-':
            total = str(float(firstNumber) - float(total))
        elif currentOperation == '*':
            total = str(float(firstNumber) * float(total))
        elif currentOperation == '/':
            if float(total) != 0:
                total = str(float(firstNumber) / float(total))
            else:
                total = "Error"
        elif currentOperation == '%':
            total = str((float(firstNumber) / 100) * float(total))
        elif currentOperation == '+/-':
            if secondMode == False:
                total = str(float(total))
            elif secondMode == True:
                total = str(-float(total))

    elif buttonText == 'Clear':
        total = '0' # Reset total to 0.
        firstNumber = '0' # Reset first number to 0.
        currentOperation = '' # Reset operation
        operationStarted = False # Reset the flag.

    elif buttonText == 'Clear Entry':
        total = '0' # Reset total to 0.

    elif buttonText == 'Backspace':
        total = total[:-1] # Removing the last number typed.
        if total == '': # Checking if total is blank.
            total = '0'

    elif buttonText == 'sin(x)':
        if secondMode == False:
            total = str(math.sin(float(total))) # Calculate the sine of the total.
        elif secondMode == True:
            if -1 <= float(total) <= 1:
                total = str(math.asin(float(total))) # Calculate the sine of the total.
            else:
                total = "Error"

    elif buttonText == 'cos(x)':
        if secondMode == False:
            total = str(math.cos(float(total))) # Calculate the sine of the total.
        elif secondMode == True:
            if -1 <= float(total) <= 1:
                total = str(math.acos(float(total))) # Calculate the sine of the total.
            else:
                total = "Error"

    elif buttonText == 'tan(x)':
        if secondMode == False:
            total = str(math.tan(float(total))) # Calculate the sine of the total.
        elif secondMode == True:
            if -1 <= float(total) <= 1:
                total = str(math.atan(float(total))) # Calculate the sine of the total.
            else:
                total = "Error"

    elif buttonText == '1/x':
        total = str(1 / float(total))
        if float(total) != 0:
            total = str(1 / float(total))
        else:
            total = "Error"

    elif buttonText == 'x^2':
        total = str(math.pow(float(total), 2))

    elif buttonText == 'sqrt(x)':
        total = str(math.sqrt(float(total)))

    displayLabel.config(text=total) # Update the label with the new total.



def numButtonClick(number):
    global total
    global operationStarted
    global operationFinished
    global secondMode

    if (total == '0' or operationStarted) or operationFinished == True:
        total = number # If the total is 0, replace it with the button value.
        operationStarted= False # Resetting the flag.
        operationFinished= False # Resetting the flag.
        secondMode= False # Resetting the flag.
    else:
        if not (number == '.' and '.' in total):
            total =total+str(number) # Update the text entry string with the button value.

    displayLabel.config(text=total) # Update the label with the text entry value.


calcWindow = tk.Tk() #create a window
calcWindow.title("Calculator") # Title of the window

topDisplayLabel = tk.Label(calcWindow, text = "0", font=("Arial", 28), justify=tk.RIGHT) # Create the label for entering the numbers.
topDisplayLabel.grid(column=0, row=0,  columnspan=4, sticky='e') # Telling the label where it needs to be.


displayLabel = tk.Label(calcWindow, text = "0", font=("Arial", 28), justify=tk.RIGHT) # Create the label for entering the numbers.
displayLabel.grid(column=0, row=0,  columnspan=4, sticky='e') # Telling the label where it needs to be.

style = ttk.Style()
style.theme_use("clam")


for col in range(4):
    calcWindow.grid_columnconfigure(col, weight=1) # Make the columns expand equally


# Row 1 Buttons
percentButton = ttk.Button(calcWindow, text="\n%\n", command = lambda: opButtonClick('%')) # Creating the button.
percentButton.grid(column=0, row=1) # Placing the button in a row and column.

clearButton = ttk.Button(calcWindow, text="\nCE\n", command = lambda: opButtonClick("Clear Entry")) # Creating the button.
clearButton.grid(column=1, row=1) # Placing the button in a row and column.

deleteButton = ttk.Button(calcWindow, text="\nC\n", command = lambda: opButtonClick("Clear")) # Creating the button.
deleteButton.grid(column=2, row=1) # Placing the button in a row and column.

backSpaceButton = ttk.Button(calcWindow, text="\nBackspace\n", command = lambda: opButtonClick('Backspace')) # Creating the button.
backSpaceButton.grid(column=3, row=1) # Placing the button in a row and column.

# Row 2 Buttons
secondButton = ttk.Button(calcWindow, text="\n2nd\n", command = lambda: opButtonClick('2nd')) # Creating the button.
secondButton.grid(column=0, row=2) # Placing the button in a row and column.

eightButton = ttk.Button(calcWindow, text="\nsin(x)\n", command = lambda: opButtonClick('sin(x)')) # Creating the button.
eightButton.grid(column=1, row=2) # Placing the button in a row and column.

nineButton = ttk.Button(calcWindow, text="\ncos(x)\n", command = lambda: opButtonClick('cos(x)')) # Creating the button.
nineButton.grid(column=2, row=2) # Placing the button in a row and column.

multiButton = ttk.Button(calcWindow, text="\ntan(x)\n", command = lambda: opButtonClick('tan(x)')) # Creating the button.
multiButton.grid(column=3, row=2) # Placing the button in a row and column.

# Row 2 Buttons
sevenButton = ttk.Button(calcWindow, text="\n1/x\n", command = lambda: opButtonClick('1/x')) # Creating the button.
sevenButton.grid(column=0, row=3) # Placing the button in a row and column.

eightButton = ttk.Button(calcWindow, text="\nx^2\n", command = lambda: opButtonClick('x^2')) # Creating the button.
eightButton.grid(column=1, row=3) # Placing the button in a row and column.

nineButton = ttk.Button(calcWindow, text="\nsqrt(x)\n", command = lambda: opButtonClick('sqrt(x)')) # Creating the button.
nineButton.grid(column=2, row=3) # Placing the button in a row and column.

multiButton = ttk.Button(calcWindow, text="\n/\n", command = lambda: opButtonClick('/')) # Creating the button.
multiButton.grid(column=3, row=3) # Placing the button in a row and column.

# Row 2 Buttons
sevenButton = ttk.Button(calcWindow, text="\n7\n", command = lambda: numButtonClick('7')) # Creating the button.
sevenButton.grid(column=0, row=4) # Placing the button in a row and column.

eightButton = ttk.Button(calcWindow, text="\n8\n", command = lambda: numButtonClick('8')) # Creating the button.
eightButton.grid(column=1, row=4) # Placing the button in a row and column.

nineButton = ttk.Button(calcWindow, text="\n9\n", command = lambda: numButtonClick('9')) # Creating the button.
nineButton.grid(column=2, row=4) # Placing the button in a row and column.

multiButton = ttk.Button(calcWindow, text="\nx\n", command = lambda: opButtonClick('*')) # Creating the button.
multiButton.grid(column=3, row=4) # Placing the button in a row and column.

# Row 3 Buttons
fourButton = ttk.Button(calcWindow, text="\n4\n", command = lambda: numButtonClick('4')) # Creating the button.
fourButton.grid(column=0, row=5) # Placing the button in a row and column.

fiveButton = ttk.Button(calcWindow, text="\n5\n", command = lambda: numButtonClick('5')) # Creating the button.
fiveButton.grid(column=1, row=5) # Placing the button in a row and column.

sixButton = ttk.Button(calcWindow, text="\n6\n", command = lambda: numButtonClick('6')) # Creating the button.
sixButton.grid(column=2, row=5) # Placing the button in a row and column.

minusButton = ttk.Button(calcWindow, text="\n-\n", command = lambda: opButtonClick('-')) # Creating the button.
minusButton.grid(column=3, row=5) # Placing the button in a row and column.

# Row 4 Buttons
oneButton = ttk.Button(calcWindow, text="\n1\n", command = lambda: numButtonClick('1')) # Creating the button.
oneButton.grid(column=0, row=6) # Placing the button in a row and column.

twoButton = ttk.Button(calcWindow, text="\n2\n", command = lambda: numButtonClick('2')) # Creating the button.
twoButton.grid(column=1, row=6) # Placing the button in a row and column.

threeButton = ttk.Button(calcWindow, text="\n3\n", command = lambda: numButtonClick('3')) # Creating the button.
threeButton.grid(column=2, row=6) # Placing the button in a row and column.

plusButton = ttk.Button(calcWindow, text="\n+\n", command = lambda: opButtonClick('+')) # Creating the button.
plusButton.grid(column=3, row=6) # Placing the button in a row and column.

# Row 5 Buttons
plusminusButton = ttk.Button(calcWindow, text="\n+/-\n", command = lambda: opButtonClick('+/-')) # Creating the button.
plusminusButton.grid(column=0, row=7) # Placing the button in a row and column.

zeroButton = ttk.Button(calcWindow, text="\n0\n", command = lambda: numButtonClick('0')) # Creating the button.
zeroButton.grid(column=1, row=7) # Placing the button in a row and column.

periodButton = ttk.Button(calcWindow, text="\n.\n", command = lambda: numButtonClick('.')) # Creating the button.
periodButton.grid(column=2, row=7) # Placing the button in a row and column.

equalsButton = ttk.Button(calcWindow, text="\n=\n", command = lambda: opButtonClick('=')) # Creating the button.
equalsButton.grid(column=3, row=7) # Placing the button in a row and column.



# Execute the window
calcWindow.mainloop() # Show the window