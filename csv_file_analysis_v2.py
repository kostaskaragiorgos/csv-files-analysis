"""
Csv_File_Analysis
"""
from tkinter import Tk, Menu, filedialog
from tkinter import messagebox as msg
import pandas as pd
def helpmenu():
    """ help menu funciton """
def aboutmenu():
    """ about menu function """
    msg.showinfo("About", "Version 2.0")
class Csv_File_Analysis():
    """ Csv_File_Analysis Class"""
    def __init__(self, master):
        self.master = master
        self.master.title("Csv_File_Analysis")
        self.master.geometry("250x120")
        self.master.resizable(False, False)
        self.filename = ""
        self.menu = Menu(self.master)
        self.file_menu = Menu(self.menu, tearoff=0)
        self.file_menu.add_command(label="Insert a csv file", accelerator='Ctrl+O', command=self.insertfile)
        self.file_menu.add_command(label="Close file", accelerator='Ctrl+F4', command=self.closefile)
        self.file_menu.add_command(label="Save analysis")
        self.file_menu.add_command(label="Exit", accelerator='Alt+F4', command=self.exitmenu)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.show_menu = Menu(self.menu, tearoff=0)
        self.show_menu.add_command(label="Show analysis", accelerator='Ctrl+F5', command=self.show_analysis)
        self.menu.add_cascade(label="Show", menu=self.show_menu)
        self.about_menu = Menu(self.menu, tearoff=0)
        self.about_menu.add_command(label="About", accelerator='Ctrl+I', command=aboutmenu)
        self.menu.add_cascade(label="About", menu=self.about_menu)
        self.help_menu = Menu(self.menu, tearoff=0)
        self.help_menu.add_command(label="Help", accelerator='Ctrl+F1', command=helpmenu)
        self.menu.add_cascade(label="Help", menu=self.help_menu)
        self.master.config(menu=self.menu)
        self.master.bind('<Control-o>', lambda event: self.insertfile())
        self.master.bind('<Control-F4>', lambda event: self.closefile())
        self.master.bind('<Control-F5>', lambda event: self.show_analysis())
        self.master.bind('<Alt-F4>', lambda event: self.exitmenu())
        self.master.bind('<Control-F1>', lambda event: helpmenu())
        self.master.bind('<Control-i>', lambda event: aboutmenu())
    def print_analysis(self):
        msg.showinfo("CSV FILE ANALYSIS", "PATH:"+self.filename + 
                "\nEMPTY CELLS:"+("Yes" if  self.df.isnull().any else "NO") +
                "\nDUPLICATES"+("Yes" if self.df.duplicated().any else "NO")+
                "\nSHAPE:"+ str(self.df.shape) +"\nINDEX:"+str(self.df.index))
    def show_analysis(self):
        """ shows analysis """
        if not ".csv" in self.filename:
            msg.showerror("ERROR", "NO CSV TO CLOSE")
        else:
            self.print_analysis()

    def closefile(self):
        """ closes the csv file """
        if not ".csv" in self.filename:
            msg.showerror("ERROR", "NO CSV TO CLOSE")
        else:
            self.filename = ""
            msg.showinfo("SUSSESS", "YOUR CSV FILE HAS SUCCESFULLY CLOSED")

    def insertfile(self):
        """ inserts the csv file """
        if ".csv" in self.filename:
            msg.showerror("ERROR", "A CSV FILE IS ALREADY OPEN")
        else:
            self.filename = filedialog.askopenfilename(initialdir="/", title="Select csv file",
                                                       filetypes=(("csv files", "*.csv"), ("all files", "*.*")))
            if self.filename.endswith('.csv'):
                self.df = pd.read_csv(self.filename)
                msg.showinfo("SUCCESSFUL INSERTION", "YOUR CSV FILE HAS SUCCESFULLY INSERTED")
            else:
                msg.showerror("INSERT A CSV", "YOU HAVE TO INSERT A CSV FILE")

    def exitmenu(self):
        """ exit menu function """
        if msg.askokcancel("Quit?", "Really quit?"):
            self.master.destroy()
def main():
    """ main function """
    root = Tk()
    Csv_File_Analysis(root)
    root.mainloop()
if __name__ == '__main__':
    main()