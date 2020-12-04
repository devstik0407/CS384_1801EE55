import time
from tkinter import *
import pathlib
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os
       
def newFile(event = None):
    global file
    root.title("Untitled - Notepad")
    file = None
    TextArea.delete(1.0, END)
    
def openFile():
    global file
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()


def saveFile(event = None):
    global file
    if file == None:
        file = asksaveasfilename(initialfile = 'Untitled.txt', 
                                 defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
        if file =="":
            file = None

        else:
            #Save as a new file
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")
            print("File Saved")
    else:
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()


def quitApp(event = None):
    root.destroy()
def modification_time():
    global file
    modificationTime = time.ctime(os.path.getmtime(file))
    showinfo("Modification time",modificationTime)
    
def creation_time():
    global file
    ctime = time.ctime(os.path.getctime(file))
    showinfo("Creation time:",ctime)
    
def cut(event = None):
    TextArea.event_generate(("<>"))

def copy(event = None):
    TextArea.event_generate(("<>"))

def paste(event = None):
    TextArea.event_generate(("<Paste>"))

def about():
    showinfo("Notepad", "Notepad by Swastik Dutta")
def charcount():
    text = TextArea.get(1.0,END)
    showinfo("Character Count",len(text) - 1)
def wordcount():
    text = TextArea.get(1.0,END)
    showinfo("Word Count",len(re.split("\s",text)) - 1)
def select_all(event=None):
    TextArea.tag_add('sel', '1.0', 'end')
    return "break"
def undo( event=None):
    TextArea.event_generate("<<Undo>>")
    return

def redo( event=None):
    TextArea.event_generate("<<Redo>>")
    return
if __name__ == '__main__':
    #Basic tkinter setup
    root = Tk()
    root.title("Untitled - Notepad")
    #root.wm_iconbitmap("1.ico")
    root.geometry("644x788")

    #Add TextArea
    TextArea = Text(root, font="lucida 13",undo = True)
    file = None
    TextArea.pack(expand=True, fill=BOTH)

    # Lets create a menubar
    MenuBar = Menu(root)

    #File Menu Starts
    FileMenu = Menu(MenuBar, tearoff=0)
    # To open new file
    FileMenu.add_command(label="New", command=newFile,accelerator = "Ctrl + N")

    #To Open already existing file
    FileMenu.add_command(label="Open", command = openFile)

    # To save the current file

    FileMenu.add_command(label = "Save", command = saveFile,accelerator = "Ctrl + S")
    FileMenu.add_separator()
    FileMenu.add_command(label = "Exit", command = quitApp,accelerator = "Ctrl + Q")
    MenuBar.add_cascade(label = "File", menu=FileMenu)
    root.bind("<Control-q>", quitApp)
    root.bind("<Control-n>", newFile)
    root.bind("<Control-s>", saveFile)
    # File Menu ends

    # Edit Menu Starts
    EditMenu = Menu(MenuBar, tearoff=0)
    #To give a feature of cut, copy and paste
    EditMenu.add_command(label = "Cut", command=cut,accelerator = "Ctrl + X")
    EditMenu.add_command(label = "Copy", command=copy,accelerator = "Ctrl + C")
    EditMenu.add_command(label = "Paste", command=paste,accelerator = "Ctrl + V")
    EditMenu.add_command(label='Select All', underline=7, accelerator='Ctrl+A', command=select_all)
    EditMenu.add_command(label = "Undo", command=TextArea.edit_undo,accelerator = "Ctrl + Z")
    EditMenu.add_command(label = "Redo", command=TextArea.edit_redo,accelerator = "Ctrl + R")
    MenuBar.add_cascade(label="Edit", menu = EditMenu)
    
   
    
    root.bind("<Control-X>", cut)
    root.bind("<Control-C>", copy)
    root.bind("<Control-V>", paste)
    root.bind("<Control-A>",select_all)
    root.bind("<Control-Z>", undo)
    root.bind("<Control-R>", redo)
    
    
    

    # Edit Menu Ends

    # Help Menu Starts
    HelpMenu = Menu(MenuBar, tearoff=0)
    HelpMenu.add_command(label = "About Notepad", command=about)
    MenuBar.add_cascade(label="Help", menu=HelpMenu)
    
    fram = Frame(root) 
  
    #adding label to search box 
    Label(fram,text='Text to find:').pack(side=LEFT)  
  
    #adding of single line text box 
    edit = Entry(fram)  
  
    #positioning of text box 
    edit.pack(side=LEFT, fill=BOTH, expand=1)  

    #setting focus 
    edit.focus_set()  
  
    #adding of search button 
    butt = Button(fram, text='Find')   
    butt.pack(side=RIGHT)  
    Label(fram, text = "Replace With ").pack(side = LEFT) 
  
    edit2 = Entry(fram) 
    edit2.pack(side = LEFT, fill = BOTH, expand = 1) 
    edit2.focus_set() 
  
    replace = Button(fram, text = 'FindNReplace') 
    replace.pack(side = LEFT)
    
    word_count = Button(fram,text = 'Word Count')
    word_count.pack(side = LEFT)
    fram.pack(side=TOP) 
  
    #text box in root window 
    text = TextArea  
  
    #text input area at index 1 in text window 
    #text.insert('1.0','''Type your text here''')  
    text.pack(side=BOTTOM) 
  
    def stats_find(): 
      
        #remove tag 'found' from index 1 to END 
        text.tag_remove('found', '1.0', END)  
        cnt = 0
        #returns to widget currently in focus 
        s = edit.get()  
        if s: 
            idx = '1.0'
            while 1: 
            #searches for desried string from index 1 
                idx = text.search(s, idx, nocase=1,  
                              stopindex=END)  
                if not idx: break
              
                #last index sum of current index and 
                #length of text 
                lastidx = '%s+%dc' % (idx, len(s))  
              
                #overwrite 'Found' at idx 
                text.tag_add('found', idx, lastidx) 
                cnt+=1
                idx = lastidx 
          
        #mark located string as red 
            text.tag_config('found', foreground='red')  
        edit.focus_set()
        return TextArea.get(1.0,END)
    #function to search string in text 
    def find(): 
      
        #remove tag 'found' from index 1 to END 
        text.tag_remove('found', '1.0', END)  
      
        #returns to widget currently in focus 
        s = edit.get()  
        if s: 
            idx = '1.0'
            while 1: 
            #searches for desried string from index 1 
                idx = text.search(s, idx, nocase=1,  
                              stopindex=END)  
                if not idx: break
              
                #last index sum of current index and 
                #length of text 
                lastidx = '%s+%dc' % (idx, len(s))  
              
                #overwrite 'Found' at idx 
                text.tag_add('found', idx, lastidx)  
                idx = lastidx 
          
        #mark located string as red 
            text.tag_config('found', foreground='red')  
        edit.focus_set() 

    def findNreplace():  
      
    # remove tag 'found' from index 1 to END  
        text.tag_remove('found', '1.0', END)  
      
    # returns to widget currently in focus  
        s = edit.get() 
        r = edit2.get() 
      
        if (s and r):  
            idx = '1.0'
            while 1:  
            # searches for desried string from index 1  
                idx = text.search(s, idx, nocase = 1,  
                            stopindex = END) 
                print(idx) 
                if not idx: break
              
            # last index sum of current index and  
            # length of text  
                lastidx = '% s+% dc' % (idx, len(s)) 
  
                text.delete(idx, lastidx) 
                text.insert(idx, r) 
  
                lastidx = '% s+% dc' % (idx, len(r)) 
              
            # overwrite 'Found' at idx  
                text.tag_add('found', idx, lastidx)  
                idx = lastidx  
  
        # mark located string as red 
            text.tag_config('found', foreground ='green', background = 'yellow') 
        edit.focus_set() 
  
                  
    #Find.config(command = find) 
    replace.config(command = findNreplace) 
  
    # mainloop function calls the endless  
    # loop of the window, so the window will 
    # wait for any user interaction till we 
    # close it  
    butt.config(command=find)
    word_count.config(command = stats_find)
    # Help Menu Ends

    root.config(menu=MenuBar)
    #Text.edit_undo(')
    #Text.edit_redo()
    #root.edit_redo()
    StatsMenu = Menu(MenuBar,tearoff = 0)
    StatsMenu.add_command(label = "word_count",command = wordcount)
    StatsMenu.add_command(label = "char_count",command = charcount)
    StatsMenu.add_command(label = "Creation time",command = creation_time)
    StatsMenu.add_command(label = "Modification time",command = modification_time)
    MenuBar.add_cascade(label="Stats", menu=StatsMenu)
    #top = tkinter.Tk.TopLevel()
    #top.title("The word count is")
    #msg = tkinter.Tk.Label(top,text = stats_find())
    #msg.pack()
    
    #Adding Scrollbar using rules from Tkinter lecture no 22
    Scroll = Scrollbar(TextArea)
    Scroll.pack(side=RIGHT,  fill=Y)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)

    root.mainloop()
print(file)