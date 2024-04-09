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

# Create a Treeview
treeview = ttk.Treeview(root, columns=('name'), show='headings')
"""# Set the column headings
treeview.heading('name', text='Name')
treeview.heading('type', text='Type')"""
"""# Create a Listbox and a Scrollbar
name_listbox = Listbox(root, width=20, height=100, font=('Arial', 12))
hp_listbox = Listbox(root, width=10, height=100, font=('Arial', 12))
attack_listbox = Listbox(root, width=10, height=100, font=('Arial', 12))
defense_listbox = Listbox(root, width=10, height=100, font=('Arial', 12))
sp_attack_listbox = Listbox(root, width=10, height=100, font=('Arial', 12))
sp_defense_listbox = Listbox(root, width=10, height=100, font=('Arial', 12))
speed_listbox = Listbox(root, width=10, height=100, font=('Arial', 12))
total_listbox = Listbox(root, width=10, height=100, font=('Arial', 12))"""

scrollbar = Scrollbar(root, width=30, orient=VERTICAL, command=treeview.yview)
# Configure the Listbox to update the Scrollbar
treeview.configure(yscrollcommand=scrollbar.set)
# Add items to the Treeview
for pokemon_name, pokemon in pokemon_data.items():
    treeview.insert('', 'end', values=(pokemon.name))
# Add items to the Listbox
"""for pokemon_name, pokemon in pokemon_data.items():
    name_listbox.insert(END, f"{pokemon.name}")
    hp_listbox.insert(END, f"{pokemon.hp}")
    attack_listbox.insert(END, f"{pokemon.attack}")
    defense_listbox.insert(END, f"{pokemon.defense}")
    sp_attack_listbox.insert(END, f"{pokemon.sp_attack}")
    sp_defense_listbox.insert(END, f"{pokemon.sp_defense}")
    speed_listbox.insert(END, f"{pokemon.speed}")
    total_listbox.insert(END, f"{pokemon.total}")"""
"""# Create a dictionary that maps attribute names to listboxes
listboxes = {
    'name': name_listbox,
    'hp': hp_listbox,
    'attack': attack_listbox,
    'defense': defense_listbox,
    'sp_attack': sp_attack_listbox,
    'sp_defense': sp_defense_listbox,
    'speed': speed_listbox,
    'total': total_listbox,
}"""
"""# Loop over the pokemon data and the listboxes
for pokemon_name, pokemon in pokemon_data.items():
    for attr, listbox in listboxes.items():
        listbox.insert(END, getattr(pokemon, attr))  """ 
         
"""# Grid the Listbox and the Scrollbar
name_listbox.grid(row=0, column=0, sticky='ns')
hp_listbox.grid(row=0, column=1, sticky='ns')
attack_listbox.grid(row=0, column=2, sticky='ns')
defense_listbox.grid(row=0, column=3, sticky='ns')
sp_attack_listbox.grid(row=0, column=4, sticky='ns')
sp_defense_listbox.grid(row=0, column=5, sticky='ns')
speed_listbox.grid(row=0, column=6, sticky='ns')
total_listbox.grid(row=0, column=7, sticky='ns')
scrollbar.grid(row=0, column=8, sticky='ns')"""

"""# Configure the grid to expand properly
root.grid_rowconfigure(0, weight=1)
for box in range(9):
    root.grid_columnconfigure(box, weight=0)"""
# Grid the Treeview
treeview.grid(row=0, column=0, sticky='nsew')
scrollbar.grid(row=0, column=1, sticky='ns')
# Configure the grid to expand properly
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
# This line starts the Tkinter event loop. This loop is what makes the window appear on the screen and respond to user actions.
root.mainloop()