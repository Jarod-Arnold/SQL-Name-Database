import os
import tkinter as tk
import pygubu
from tkinter import ttk
from Database import Database
from Name import Name
import tkinter.messagebox as mb

PROJECT_PATH = os.path.dirname(__file__)
PROJECT_UI = os.path.join(PROJECT_PATH, "names_ui.ui")


class NamesApp:
    def __init__(self, master):
        self.__builder = builder = pygubu.Builder()
        builder.add_resource_paths(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        
        # Main widget
        self.__mainwindow = builder.get_object("top_frame", master)
        builder.connect_callbacks(self)


        # Save these 4 UI elements as properties so that we can access them when
        # the user clicks on the calculate button.
        self.__name_entry = builder.get_object('name_entry', master)
        self.__gender_var = tk.IntVar()
        

        #Sets the Radio buttons to be INT values. 
        #Solved the issue of clicking one radio button and both buttons
        #being highlighted
        self.__radio_male = builder.get_object('radio_male')
        self.__radio_male.config(variable=self.__gender_var, value=1)


        #Sets the Radio buttons to be INT values. 
        #Solved the issue of clicking one radio button and both buttons
        #being highlighted
        self.__radio_female = builder.get_object('radio_female')
        self.__radio_female.config(variable=self.__gender_var, value=0)


        # Hides the Treeview until the Retrieve button (get_data) method
        # is called
        self.__results_tree = builder.get_object("results_tree")
        self.__results_tree.grid_remove()


    def get_data(self):
        
        #Retrieves the name entry and capitalizes the name
        # if not already capital
        name = self.__name_entry.get().capitalize()


        #Sets the default value of the radio button to F
        gender = "M" if self.__gender_var.get() == 1 else "F"


        #retrieve information from database
        data = Database.readNames(name, gender)


        #Error message box that shows up if no info, or if there
        #is missing info from required data (name)
        if not data:
            mb.showerror(title="Data Error", message=
                         "Please input required data before proceeding.")
            return
        

        #convert data into name objects
        name_records = [Name.from_tuple(record) for record in data]

        #Populates the treeview with header names, and the fetched data
        results_tree = self.__builder.get_object("results_tree")
        results_tree["columns"] = ("name", "year", "name_count", "gender")
        results_tree.heading("name", text="Name")
        results_tree.heading("year", text="Year")
        results_tree.heading("name_count", text="Count")
        results_tree.heading("gender", text="Gender")

        
        #clear previous data in tree if running program 
        #again to populate more data.
        for child in results_tree.get_children():
            results_tree.delete(child)


        #Inserts data into the tree whether or not it is
        #the first instance or Nth instance of populating data
        for record in data:
            results_tree.insert("", "end", 
                                values=(record[0], record[1], record[2], record[3]))

        
        #Shows the treeview on the screen after the get_data method
        #is called. I did this for aesthetic reasons. 
        self.__results_tree.grid()


    def run(self):
        self.__mainwindow.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Name Statistics")
    app = NamesApp(root)
    app.run()
