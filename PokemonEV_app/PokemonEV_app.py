from tkinter import *
from tkinter import ttk
import tkinter as tk
from pokemonevs import Pokemon
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

# Create a Treeview
style = ttk.Style()
treeview = ttk.Treeview(root, columns=('name'), show='headings')
style.configure("Treeview", foreground='white', background="#15292B", font=('Arial', 12))

scrollbar = Scrollbar(root, width=30, orient=VERTICAL, command=treeview.yview)
# Configure the Listbox to update the Scrollbar
treeview.configure(yscrollcommand=scrollbar.set, show='headings')
# Add columns, headers, & items to the Treeview
treeview['columns'] = ('Name', 'HP', 'Attack', 'Defense', 'Special Attack', 'Special Defense', 'Speed', 'Total') 
for column in treeview['columns']:
    treeview.heading(column, text=column)

for pokemon_name, pokemon in pokemon_data.items():
    treeview.insert('', 'end', values=(pokemon.name, pokemon.hp, pokemon.attack, pokemon.defense, pokemon.sp_attack, pokemon.sp_defense, pokemon.speed, pokemon.total))
    
# Grid the Treeview
treeview.grid(row=0, column=0, sticky='nsew')
scrollbar.grid(row=0, column=1, sticky='ns')
# Configure the grid to expand properly
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
# This line starts the Tkinter event loop. This loop is what makes the window appear on the screen and respond to user actions.
root.mainloop()