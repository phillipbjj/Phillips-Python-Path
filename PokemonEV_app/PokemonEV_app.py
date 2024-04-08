from tkinter import *
from tkinter import ttk
from PokemonEV_reader import pokemon_data
from evDisplayFunction import evDisplay

#evDisplay(pokemon_data, 'Venusaur')
#class tkinter.Tk(screenName=None, baseName=None, className='Tk', useTk=True, sync=False, use=None)
#Create the GUI, this line creates a new Tkinter window. root is a common name for the main window in a Tkinter application.
root = Tk(className='PokemonEV App')
# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
# Set the window size to the screen size
root.geometry(f"{screen_width}x{screen_height}")
# Create a canvas on the root window and a vertical scrollbar
canvas = Canvas(root)
scrollbar = Scrollbar(root, orient=VERTICAL, command=canvas.yview)
#This line configures the canvas to update the scrollbar whenever the view in the canvas changes.
canvas.configure(yscrollcommand=scrollbar.set)

# Create a frame on the canvas to hold the labels
frame = Frame(canvas)
#The (0, 0) argument is the position of the window, window=frame makes the frame the content of the window,
#and anchor='nw' positions the window's top-left corner at the given position.
canvas.create_window((0, 0), window=frame, anchor='nw')
        
#places the canvas to the left and makes it fill the window both horizontally and vertically.
canvas.pack(side='left', fill='both', expand=True) 
#places the scrollbar to the right and makes it fill the window vertically.
scrollbar.pack(side='right', fill='y')

# Update the scrollregion after the canvas and labels have been displayed
frame.update_idletasks() #This is necessary to calculate the correct scroll region for the canvas.
canvas.configure(scrollregion=canvas.bbox('all'))

#This line starts the Tkinter event loop. This loop is what makes the window appear on the screen and respond to user actions.
root.mainloop()