import tkinter
import os
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
import io

#Creating a class
class Project:
    
    #Creating root window
    root=Tk()

    #Specifying window width
    width=300
    text_area=Text(root)
    menu_bar=Menu(root)
    file_menu=Menu(menu_bar, tearoff=0)
    help_menu=Menu(menu_bar, tearoff=0)

    #Adding scrollbar
    scrollbar=Scrollbar(text_area)
    __file=None
    def __init__(self,**kwargs): 
  
        #Setting icon 
        try: 
                self.root.wm_iconbitmap("Python.ico")  
        except: 
                pass
  
        #Setting window size 
  
        try: 
            self.width = kwargs['width'] 
        except KeyError: 
            pass
  
        try: 
            self.__thisHeight = kwargs['height'] 
        except KeyError: 
            pass
  
        #Setting the window text 
        self.root.title("Untitled - Editor")
        buffer = io.StringIO()

        print("def local_function():", file=buffer)
        print("    ", file=buffer)
        

        output = buffer.getvalue()
        self.text_area.insert(END, output)
       
        #Centering the window 
        screenWidth = self.root.winfo_screenwidth() 
        screenHeight = self.root.winfo_screenheight() 
      
        #For left-allign 
        left = (screenWidth / 2) - (self.width / 2)  
          
        #For right-allign 
        top = (screenHeight / 2) - (self.__thisHeight /2)  
          
        #For top and bottom 
        self.root.geometry('%dx%d+%d+%d' % (self.width, 
                                              self.__thisHeight, 
                                              left, top))  
  
        #Making the textarea auto resizable 
        self.root.grid_rowconfigure(0, weight=1) 
        self.root.grid_columnconfigure(0, weight=1) 
  
        #Adding widgets 
        self.text_area.grid(sticky = N + E + S + W) 
          
        #To open a new file 
        self.file_menu.add_command(label="New", 
                                        command=self.__newFile)

        #To open an already existing file 
        self.file_menu.add_command(label="Open", 
                                        command=self.__openFile) 
          
        #To save current file 
        self.file_menu.add_command(label="Save", 
                                        command=self.__saveFile)
        
        #To run current file
        self.file_menu.add_command(label="Run", command=self.__runFile)    
  
        #To exit from the current file        
        self.file_menu.add_separator()                                          
        self.file_menu.add_command(label="Exit", 
                                        command=self.__quitApplication) 
        self.menu_bar.add_cascade(label="File", 
                                       menu=self.file_menu)      
          
          
        #To create menubar options 
        self.help_menu.add_command(label="About", 
                                        command=self.__showAbout)  
        self.menu_bar.add_cascade(label="Help", 
                                        menu=self.help_menu) 
  
        self.root.config(menu=self.menu_bar) 
  
        self.scrollbar.pack(side=RIGHT,fill=Y)                     
          
        #Scrollbar will adjust automatically according to the content         
        self.scrollbar.config(command=self.text_area.yview)      
        self.text_area.config(yscrollcommand=self.scrollbar.set) 

    #Closing the window
    def __quitApplication(self): 
        self.root.destroy()  
  
    #Showing the about section
    def __showAbout(self): 
        showinfo("Python Project","Made By: \nDebanjan,Debjit,Sreeparno,Shamik,Sukanya")
  
    #To open file
    def __openFile(self): 
          
        self.__file = askopenfilename(defaultextension=".py", 
                                      filetypes=[("All Files","*.*"), 
                                        ("Python Files","*.py"), ("C Files","*.c")]) 
  
        if self.__file == "": 
              
            #No file to open 
            self.__file = None
        else: 
              
            #Try to open the file 
            self.root.title(os.path.basename(self.__file) + " - Script") 
            self.text_area.delete(1.0,END) 
  
            file = open(self.__file,"r") 
  
            self.text_area.insert(1.0,file.read())

            file.close() 
  
    #Funtion to create a new file      
    def __newFile(self): 
        self.root.title("Untitled - Editor") 
        self.__file = None
        self.text_area.delete(1.0,END)
        buffer = io.StringIO()

        print("def local_function():", file=buffer)
        print("    ", file=buffer)
        output = buffer.getvalue()
        self.text_area.insert(END, output) 

    #Function to run the input file
    def __runFile(self):
        os.system('final_py_project.py')
  
         
        self.root.title(os.path.basename('fhi.txt') + " - Output") 
        self.text_area.delete(1.0,END) 
  
        file = open('fhi.txt',"r") 
  
        self.text_area.insert(1.0,file.read()) 
  
        file.close() 
        
        
        
    #Function to save the file
    def __saveFile(self): 
  
        if self.__file == None: 
            #Save as new file 
            self.__file = asksaveasfilename(initialfile='Untitled.py', 
                                            defaultextension=".py", 
                                            filetypes=[("All Files","*.*"), 
                                                ("Python Files","*.py"), ("C files", "*.c")]) 
  
            if self.__file == "": 
                self.__file = None
            else: 
                  
                #Try to save the file 
                file = open(self.__file,"w") 
                file.write(self.text_area.get(1.0,END)) 
                file.close() 
                file.close() 
                
                #Change the window title 
                self.root.title(os.path.basename(self.__file) + " - Script") 
                  
              
        else: 
            file = open(self.__file,"w") 
            file.write(self.text_area.get(1.0,END)) 
            file.close() 
  
    def run(self): 
        #Run main application 
        self.root.mainloop() 

python_pr = Project(width=600,height=400) 
python_pr.run()