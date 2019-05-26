from tkinter import messagebox as msg
from tkinter import *
from tkinter import simpledialog
from tkinter import filedialog

import pandas as pd
"""
no file input msg
"""
class csv_file_analisys1():
    def __init__(self,master):
        self.master = master
        self.master.title("CSV FILE ANALYSIS")
        self.master.geometry("300x60")
        self.master.resizable(False,False)
        self.menu = Menu(self.master)
        
        self.file_menu = Menu(self.menu,tearoff = 0)
        self.file_menu.add_command(label="Exit",accelerator = 'Alt+F4',command = self.exitmenu)
        self.menu.add_cascade(label = "File",menu=self.file_menu)
        
        self.about_menu = Menu(self.menu,tearoff = 0)
        self.about_menu.add_command(label = "About",accelerator = 'Ctrl+I',command=self.aboutmenu)
        self.menu.add_cascade(label="About",menu=self.about_menu)
        
        self.help_menu = Menu(self.menu,tearoff = 0)
        self.help_menu.add_command(label = "Help",accelerator = 'Ctrl+F1',command=self.helpmenu)
        self.menu.add_cascade(label="Help",menu=self.help_menu)

        self.master.config(menu=self.menu)
        
        self.master.bind('<Alt-F4>',lambda event: self.exitmenu())
        self.master.bind('<Control-F1>',lambda event: self.helpmenu())
        self.master.bind('<Control-i>',lambda event:self.aboutmenu())
        
        
        self.welcomemes = Label(self.master,text="Welcome to csv file analysis\n"+
                                   "Import a csv file and examine it")
        self.welcomemes.pack()
        self.open_csv_file = Button(self.master,text = "IMPORT CSV FILE",
                                       command = self.importfile)
        self.open_csv_file.pack()
    
    def exitmenu(self):
        if msg.askokcancel("Quit?", "Really quit?"):
            self.master.destroy()
    def aboutmenu(self):
        msg.showinfo("About CSV FILES ANALYSIS","Version 0.1\nAnalyzes your csv files")
    def helpmenu(self):
        msg.showinfo("Help" , "1.Import a csv file\n2.Analyze the csv file")
    
    def importfile(self):
        global filed
        global ansfordup 
        global ansfornull
        filed = filedialog.askopenfilename(initialdir="/",title="Select csv file",
                                                   filetypes=(("csv files","*.csv"),("all files","*.*")))
        if ".csv" in filed:
            pandascheck = pd.read_csv(filed)
            if pandascheck.duplicated().any() == True:
                ansfordup = "YES"
            else:
                ansfordup = "NO"
            if pandascheck.isnull().any == True:
                ansfornull  = "YES"
            else:
                ansfornull = "NO"
            msg.showinfo("FILE INFO","PATH:"+filed+
                     "\nEMPTY CELLS:"+ansfornull+
                     "\nNAME AND TYPE OF COLUMNS:"+str(pandascheck.columns)+
                     "\nDUPLICATES:"+ansfordup+""+"\nSHAPE:"+str(pandascheck.shape)+
                     "\nINDEX:"+str(pandascheck.index))
            root2 = Toplevel()
            makeacc = csv_Main(root2)
        
        else:
            msg.showerror("ERROR","NO FILE INSERTED\nINSERT A CSV FILE ")
class csv_Main():
    def __init__(self,master):
        self.master =master
        self.master.title("CSV FILE ANALYSIS")
        self.master.geometry("360x70")
        self.showh=Button(self.master,text ="SHOW FIVE FIRST COLUMNS"
                          ,command = self.show5fcol)
        self.showh.grid(row = 0 ,column =0 )
        self.show5last = Button(self.master,text = "SHOW FIVE LAST COLUMNS"
                                ,command = self.show5last)
        self.show5last.grid(row = 0,column = 1)
        self.showftocol = Button(self.master, text = "SHOW FROM TO COLUMNS",command = self.showfto)
        self.showftocol.grid(row = 1 ,column = 0)
        self.showinfob = Button(self.master,text = "SHOW INFO",command=self.showinfobf)
        self.showinfob.grid(row = 1,column = 1)
    def showfto(self):
        pandascheck = pd.read_csv(filed)
        print(str(pandascheck.index.size))
        fromb = simpledialog.askinteger("From","Enter from value",parent = self.master, minvalue = 0 , maxvalue =int(pandascheck.index.size)-1 )
        while fromb == None:
            fromb = simpledialog.askinteger("From","Enter from value",parent = self.master, minvalue = 0 , maxvalue =int(pandascheck.index.size)-1 )    
        tob = simpledialog.askinteger("To" , "Enter to value",parent = self.master,minvalue = fromb , maxvalue = int(pandascheck.index.size))
        while tob == None:
            tob = simpledialog.askinteger("To" , "Enter to value",parent = self.master,minvalue = fromb , maxvalue = int(pandascheck.index.size))
    def show5fcol(self):
        pandascheck = pd.read_csv(filed)
        msg.showinfo("FIVE FIRST COLUMNS",str(pandascheck.head()))
    def show5last(self):
        pandascheck = pd.read_csv(filed)
        msg.showinfo("FIVE FIRST COLUMNS",str(pandascheck.tail()))
    def showinfobf(self):
        pandascheck = pd.read_csv(filed)
        msg.showinfo("FILE INFO","PATH:"+filed+
                     "\nEMPTY CELLS:"+ansfornull+
                     "\nNAME AND TYPE OF COLUMNS:"+str(pandascheck.columns)+
                     "\nDUPLICATES:"+ansfordup+""+"\nSHAPE:"+str(pandascheck.shape)+
                     "\nINDEX:"+str(pandascheck.index))
def main(): 
    root=Tk()
    csvf = csv_file_analisys1(root)
    root.mainloop()
    
if __name__=='__main__':
    main()
