from tkinter import *
import os
import sys

class Simple_GUI(object):

    def __init__(self, fields):

        #Configuration settings for GUI window
        self.root_window = Tk()
        self.tk_pack_directions = [LEFT, RIGHT, TOP, BOTTOM]
        self.default_button_name = 'Submit'
        self.close_window_after_submit = True

        #Names of text-entry fields
        self.fields = fields
        self.entries = [] #Contains an entry for each field name and text entry field

        #Results from user text-entry fields
        self.results = []
        self.submit_form = False

    #Method to provide a way to close GUI within the scope of the methods of the class
    def quit(self):
        self.root_window.destroy()

    #Method to fetch entry field data; returns field name and data (None if empty) as well as a boolean event (True) for use with other modules/scripts
    def get_entries(self):
        for entry in self.entries:
            field = entry[0]
            text = entry[1].get()
            self.results.append([field, text])
            self.submit_form = True
        if self.close_window_after_submit is True:
            self.quit()

    #Method to flush results if form is submitted; useful if you want multiple form submissions
    def flush_results(self):
        if self.submit_form is True:
            self.results = []
            self.submit_form = False

    #Method to create user text-entry form
    def create_form(self):
        for field in self.fields:
            row = Frame(self.root_window)
            lab = Label(row, width=15, text=field, anchor='w')
            ent = Entry(row)
            row.pack(side=TOP, fill=X, padx=5, pady=5)
            lab.pack(side=LEFT)
            ent.pack(side=RIGHT, expand=YES, fill=X)
            self.entries.append((field, ent))

    #Method to create button which fetches entry field data
    def create_submit_button(self, name, direction):
        if direction in self.tk_pack_directions:
            button = Button(self.root_window, text='{}'.format(name))
            button.pack(side=direction, padx=5, pady=5)
            button.bind('<ButtonPress-1>', self.get_entries)
        else:
            print('Direction must be: {}'.format(self.tk_pack_directions))

    #Quickly create a generic menu with text-entry fields and a submit button; provide method w/ False to prevent window from closing on completion
    def create_gui(self, close_window):
        self.create_form()
        self.create_submit_button()
        if close_window is False:
            self.close_window_after_submit = False
