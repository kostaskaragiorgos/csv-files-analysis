from tkinter import messagebox as msg
from tkinter import *
from tkinter import filedialog
import pandas as pd
class csv_file_analisys1():
    def __init__(self,master):
        self.master = master
        self.master.title("CSV FILE ANALYSIS")
        self.master.geometry("300x60")
        self.master.resizable(False,False)
        self.welcomemes = Label(self.master,text="Welcome to csv file analysis\n"+
                                   "Import a csv file and examine it")
        self.welcomemes.pack()
        self.open_csv_file = Button(self.master,text = "IMPORT CSV FILE",
                                       command = self.importfile)
        self.open_csv_file.pack()
    def importfile(self):
        global filed
        global ansfordup 
        global ansfornull
        filed = filedialog.askopenfilename(initialdir="/",title="Select csv file",
                                                   filetypes=(("csv files","*.csv"),("all files","*.*")))
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
class csv_Main():
    def __init__(self,master):
        self.master =master
        self.master.title("CSV FILE ANALYSIS")
        self.master.geometry("200x150")
        self.showinfob = Button(self.master,text = "SHOW INFO",command=self.showinfobf)
        self.showinfob.pack()
        self.showh=Button(self.master,text ="SHOW FIVE FIRST COLUMNS"
                          ,command = self.show5fcol)
        self.showh.pack()
        self.show5last = Button(self.master,text = "SHOW FIVE LAST COLUMNS"
                                ,command = self.show5last)
        self.show5last.pack()
        self.showftocol = Button(self.master, text = "SHOW FROM TO COLUMNS",command = self.showfto)
        self.showftocol.pack()
    def showfto(self):
        pass
    
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