import tkinter as tk #has window logic
from tkinter import ttk #has widgets

textEntryString = "" #create a String to hold the text entry value

def btn_click():
    print("Button clicked!")
    textEntryString = textEntry.get() #get the value from the text entry widget
    label.config(text=textEntryString) #update the label with the text entry value

window = tk.Tk() #create a window
window.title("My first GUI") #title of the window
window.geometry("500x300") #size of the window

#label widget
label = ttk.Label(window, text="Hello World!") #create a label widget
label.pack(pady=10) #add the label to the window with padding

textEntry = ttk.Entry(window, textvariable = textEntryString ) #create a text entry widget
textEntry.pack(pady=10) #add the text entry to the window with padding

button = ttk.Button(window, text="Click Me!",command=lambda: btn_click()) #create a button widget
button.pack(pady=10) #add the button to the window with padding

#execute the window
window.mainloop() #show the window