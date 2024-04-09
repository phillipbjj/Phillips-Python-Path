from tkinter import *
from tkinter import ttk
import tkinter as tk
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




# Create a Listbox and a Scrollbar
listbox = Listbox(root, width=200, height=100)
scrollbar = Scrollbar(root, orient=VERTICAL, command=listbox.yview)
# Configure the Listbox to update the Scrollbar
listbox.configure(yscrollcommand=scrollbar.set)

# Add items to the Listbox
for pokemon_name, pokemon in pokemon_data.items():
    listbox.insert(END, repr(pokemon))

# Grid the Listbox and the Scrollbar
listbox.grid(row=0, column=0, sticky='ns')
scrollbar.grid(row=0, column=1, sticky='ns')
# Configure the grid to expand properly
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
# This line starts the Tkinter event loop. This loop is what makes the window appear on the screen and respond to user actions.
root.mainloop()