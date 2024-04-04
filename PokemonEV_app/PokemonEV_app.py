from tkinter import *
#from tkinter import Tk, ttk, Label, Canvas, Scrollbar, Frame, VERTICAL, N, S, E, W

#class tkinter.Tk(screenName=None, baseName=None, className='Tk', useTk=True, sync=False, use=None)
#This line opens the file Pokedex_EVs.txt in read mode ('r'). 
#The with statement ensures that the file is properly closed after it is no longer needed.
#with open('Pokedex_EVs.csv', 'r') as file:
#    reader = csv.reader(file)   #This line creates a csv.reader object that can iterate over lines in the CSV file.
#    data = list(reader) #This line reads all lines from the CSV file and stores them in the data variable as a list of lists.

#Create the GUI, this line creates a new Tkinter window. root is a common name for the main window in a Tkinter application.
root = Tk()

# Create a canvas on the root window and a vertical scrollbar
canvas = Canvas(root)
scrollbar = Scrollbar(root, orient=VERTICAL, command=canvas.yview)
canvas.configure(yscrollcommand=scrollbar.set)

# Create a frame on the canvas to hold the labels
frame = Frame(canvas)
canvas.create_window((0, 0), window=frame, anchor='nw')

#This line starts a loop that goes through each row in the data list.
#enumerate is a built-in function that returns both the index of the current item and the item itself.
for i, row in enumerate(data):  
    for j, cell in enumerate(row):
#This line creates a new Tkinter Label widget. The label is added to the root window and its text is set to the current cell's value.
        label = Label(root, text=cell) 
#This line positions the label in the root window.
#The grid method arranges widgets in a grid, and the row and column options specify the label's position in the grid.
        label.grid(row=i, column=j)
        
# Update the scrollregion after the canvas and labels have been displayed
frame.update_idletasks()
canvas.configure(scrollregion=canvas.bbox('all'))

# Layout the canvas and the scrollbar
canvas.grid(column=0, row=0, sticky=N+S+E+W)
scrollbar.grid(column=1, row=0, sticky=N+S)

#This line starts the Tkinter event loop. This loop is what makes the window appear on the screen and respond to user actions.
root.mainloop()