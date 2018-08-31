from tkinter import *
import os
import sys

class SimpleGUI(object):

    def __init__(self, fields):

        #Configuration settings for GUI window
        self.root_window = Tk()
        self.tk_pack_directions = [LEFT, RIGHT, TOP, BOTTOM]

        #Names of text-entry fields
        self.fields = fields
        self.entries = [] #Contains an entry for each field name and text entry field

        #Results from user text-entry fields
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

    #Method to fetch entry field data; returns field name and data (None if empty) as well as a boolean event (True) for use with other modules/scripts
    def get_entries(self):
        for entry in self.entries:
            field = entry[0]
            text = entry[1].get()
            self.results.append([field, text])
            self.submit_form = True

    #Method to flush results if form is submitted; useful if you want multiple form submissions
    def flush_results(self):
        if self.submit_form is True:
            self.results = []
            self.submit_form = False

    #Method to create button which fetches entry field data
    def create_submit_button(root_window, entries, name, direction):
        if direction in self.tk_pack_directions:
            button = Button(root_window, text='{}'.format(name))
            button.pack(side=direction, padx=5, pady=5)
            button.bind(<'ButtonPress-1'>, self.get_entries)
        else:
            print('Direction must be: {}'.format(self.tk_pack_directions))

    #Quickly
