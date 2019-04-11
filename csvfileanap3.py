from tkinter import messagebox as msg
from tkinter import *
from tkinter import filedialog
import pandas as pd
class csv_file_analisys():
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
        self.filename = filedialog.askopenfilename(initialdir="/",title="Select csv file",
                                                   filetypes=(("csv files","*.csv"),("all files","*.*")))
        pandascheck = pd.read_csv(self.filename)
        if pandascheck.duplicated().any() == True:
            self.ansford = "YES"
        else:
            self.ansford = "NO"
        
        if pandascheck.isnull().any == True:
            self.ansforn  = "YES"
        else:
            self.ansforn = "NO"
        msg.showinfo("FILE INFO","PATH:"+self.filename+
                     "\nEMPTY CELLS:"+self.ansforn+
                     "\nNAME AND TYPE OF COLUMNS:"+str(pandascheck.columns)+
                     "\nDUPLICATES:"+self.ansford+""+"\nSHAPE:"+str(pandascheck.shape)+
                     "\nINDEX:"+str(pandascheck.index))
def main():
    root=Tk()
    csvf = csv_file_analisys(root)
    root.mainloop()
    
if __name__=='__main__':
    main()