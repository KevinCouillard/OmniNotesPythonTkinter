from tkinter import *
from PIL import ImageTk, Image

#set up main gui window
root = Tk()
root.title('OmniNotesPython')
root.configure(background="gray")
root.geometry("1200x800")
root.rowconfigure(1,weight=0)
root.columnconfigure(1,weight=1)

#create toolbar frame and configure toolbar frame grid
toolbarFrame = LabelFrame(root, bg="blue")
toolbarFrame.grid(row=0,column=1,columnspan=2,sticky="NWE")

#create note frame and configure note frame grid
noteFrame = LabelFrame(root, bg="gray",width=800)
noteFrame.grid(row=1,column=1,columnspan=2,sticky="NWES")

#configure grid system on note frame
noteFrame.columnconfigure(1, weight=1)
noteFrame.rowconfigure(10, weight=1)

#Add elements to the toolbar frame
toolbarLabel = Label(toolbarFrame, text="ToolBar", bd=1, bg="blue")

#Add toolbar label
toolbarLabel.grid(row=0,column=0,columnspan=1,sticky="WE")

#Add elements to the note frame
#create empty grid elements
row1Label = Label(noteFrame, bg="gray", bd=1, height=5,width=5)
row2Label = Label(noteFrame, bg="gray", bd=1, height=5,width=5)
row3Label = Label(noteFrame, bg="gray", bd=1, height=10,width=5)
row5Label = Label(noteFrame, bg="gray", bd=1, height=0,width=5)
row7Label = Label(noteFrame, bg="gray", bd=1, height=5,width=5)
row8Label = Label(noteFrame, bg="gray", bd=1, height=5,width=5)
row9Label = Label(noteFrame, bg="gray", bd=1, height=5,width=5)
row10Label = Label(noteFrame, bg="gray", bd=1,height=5,width=5)

#create grid elements
noteImg = ImageTk.PhotoImage(Image.open("resources/no_notesImg.png"))
imgLabel = Label(noteFrame, bg="gray", bd=1, image=noteImg)
noteLabel = Label(noteFrame, text="Nothing Here!", fg="blue", bg="gray", bd=1, height=3,width=5,font=(0,30))

addNote = Menubutton(noteFrame, text="Add Note!", relief=RAISED)
addNote.menu = Menu(addNote,tearoff=0)
addNote["menu"] = addNote.menu

addNoteImg = ImageTk.PhotoImage(Image.open("resources/add_noteImg.png"))
addNote.configure(width=0,height=1, bg="gray", highlightbackground="blue")

#add elements to grid
row1Label.grid(row=1, column=1, columnspan=1, sticky="WE")
row2Label.grid(row=2, column=1, columnspan=1, sticky="WE")
row3Label.grid(row=3, column=1, columnspan=1, sticky="WE")
row5Label.grid(row=5, column=1, columnspan=1, sticky="WE")
row7Label.grid(row=7, column=1, columnspan=1, sticky="WE")
row8Label.grid(row=8, column=1, columnspan=1, sticky="WE")
row9Label.grid(row=9, column=1, columnspan=1, sticky="WE")
row10Label.grid(row=10, column=1, columnspan=1,sticky="WES")

addNote.grid(row=8, column=1, columnspan=1, sticky="WE")
imgLabel.grid(row=4, column=1, columnspan=1, sticky="WE")
noteLabel.grid(row=6, column=1, columnspan=1, sticky="WE")

#Create Functions

#Create Text Note Functions
def createTextNote():
    #create add note window
    noteWindow = Toplevel(root, bg="gray")
    noteWindow.title("Text Note Window")
    noteWindow.geometry("1200x800")
    noteWindow.rowconfigure(1,weight=0)
    noteWindow.columnconfigure(1,weight=1)

    #create toolbar
    toolbarFrame = LabelFrame(noteWindow, bg="blue")
    toolbarFrame.grid(row=0,column=1,columnspan=2,sticky="WE")
    toolbarLabel = Label(toolbarFrame, text="ToolBar", bd=1, bg="blue")
    toolbarLabel.grid(row=0,column=0,columnspan=1,sticky="WE")

    #create add note frame
    addNoteFrame = LabelFrame(noteWindow, bg="gray")
    addNoteFrame.grid(row=1,column=1,columnspan=2,rowspan=2,sticky="WES")

    #set up new window layout
    addNoteFrame.columnconfigure(1, weight=1)
    addNoteFrame.rowconfigure(10, weight=0)

    #Grid Placeholders
    row1Label = Label(addNoteFrame, bg="gray", bd=1, height=5,width=5)
    row2Label = Label(addNoteFrame, text="Create Your Note:", fg="blue", bg="gray", bd=1, height=5,width=5,font=(0,30))
    row4Label = Label(addNoteFrame, bg="gray", bd=1, height=5,width=5)
    row5Label = Label(addNoteFrame, bg="gray", bd=1, height=5,width=5)
    row7Label = Label(addNoteFrame, bg="gray", bd=1, height=5,width=5)
    #row8Label = Label(addNoteFrame, bg="gray", bd=1, height=5,width=5)
    row9Label = Label(addNoteFrame, bg="gray", bd=1, height=5,width=5)
    row10Label = Label(addNoteFrame, bg="gray", bd=1, height=5,width=5)

    row1Label.grid(row=1, column=1, columnspan=1, sticky="WE")
    row2Label.grid(row=2, column=1, columnspan=1, sticky="WE")
    row4Label.grid(row=4, column=1, columnspan=1, sticky="WE")
    row5Label.grid(row=5, column=1, columnspan=1, sticky="WE")
    row7Label.grid(row=7, column=1, columnspan=1, sticky="WE")
    #row8Label.grid(row=8, column=1, columnspan=1, sticky="WE")
    row9Label.grid(row=9, column=1, columnspan=1, sticky="WE")
    row10Label.grid(row=10, column=1, columnspan=1, sticky="WE")

    noteTitle = Entry(addNoteFrame)
    noteTitle.insert(0, "Note Title Here!")
    noteTitle.grid(row=3,column=1, columnspan=1, sticky="WE", padx=15, pady=15)

    noteContent = Entry(addNoteFrame)
    noteContent.insert(0, "Note Content Here!")
    noteContent.grid(row=6,column=1, columnspan=1, sticky="WE", padx=15, pady=15)

    #add new note to main window (needs a lot of work/adds note to text note window that shoud be destroyed?)
    def addNewNote():
        # print(test)
        # if(test == 50):
        #     rowPH = 0
        rowPH = 0
        title = noteTitle.get()
        content = noteContent.get()
        imgLabel.destroy()
        noteLabel.destroy()
        Button(noteFrame, bg="blue", bd=1, text=title, height=5).grid(row=rowPH, column=1, columnspan=1, sticky="WE",padx=15)
        noteWindow.destroy()
        rowPH += 1 #don't know how to define with code structure so can properly increment w.out resetting variable
        #noteButton = Button(noteFrame, bg="blue", bd=1, text=title, height=5)
        #noteButton.grid(row=4, column=1, columnspan=1, sticky="WE",padx=15)

    #Finish note button
    finishNote = Button(addNoteFrame, command=addNewNote, text="Finish Note")
    finishNote.grid(row=8,column=1, columnspan=1, sticky="WE", padx=15, pady=15)

#create list note window
def createListNote():
    noteFrame = Toplevel(root)
    noteFrame.title("List Note Window")

#create canvas note window
def createCanvasNote():
    noteFrame = Toplevel(root)
    noteFrame.title("Canvas Note Window")

    #canvas functions
    def clear_all(noteFrame):
        noteFrame.canvas.delete("all")

    def print_points(noteFrame):
        if noteFrame.points_recorded:
            noteFrame.points_recorded.pop()
            noteFrame.points_recorded.pop()
        noteFrame.canvas.create_line(noteFrame.points_recorded, fill = "yellow")
        noteFrame.points_recorded[:] = []

    def tell_me_where_you_are(noteFrame, event):
        noteFrame.previous_x = event.x
        noteFrame.previous_y = event.y

    def draw_from_where_you_are(noteFrame, event):
        if noteFrame.points_recorded:
            noteFrame.points_recorded.pop()
            noteFrame.points_recorded.pop()

        noteFrame.x = event.x
        noteFrame.y = event.y
        noteFrame.canvas.create_line(noteFrame.previous_x, noteFrame.previous_y,
                                noteFrame.x, noteFrame.y,fill="yellow")
        noteFrame.points_recorded.append(noteFrame.previous_x)
        noteFrame.points_recorded.append(noteFrame.previous_y)
        noteFrame.points_recorded.append(noteFrame.x)
        noteFrame.points_recorded.append(noteFrame.x)
        noteFrame.previous_x = noteFrame.x
        noteFrame.previous_y = noteFrame.y

    noteFrame.previous_x = noteFrame.previous_y = 0
    noteFrame.x = noteFrame.y = 0
    noteFrame.points_recorded = []
    noteFrame.canvas = Canvas(noteFrame, width=400, height=400, bg = "black", cursor="cross")
    noteFrame.canvas.pack(side="top", fill="both", expand=True)
    noteFrame.button_print = Button(noteFrame, text = "Display points", command = print_points)
    noteFrame.button_print.pack(side="top", fill="both", expand=True)
    noteFrame.button_clear = Button(noteFrame, text = "Clear", command = clear_all)
    noteFrame.button_clear.pack(side="top", fill="both", expand=True)
    noteFrame.canvas.bind("<Motion>", tell_me_where_you_are)
    noteFrame.canvas.bind("<B1-Motion>", draw_from_where_you_are)

#opens settings window
def openSettings():
    settingsWindow = Toplevel(root)
    settingsWindow.title("Settings")

#opens about window
def openAbout():
    aboutWindow = Toplevel(root)
    aboutWindow.title("About")

    aboutWindow.rowconfigure(1,weight=0)
    aboutWindow.columnconfigure(1,weight=1)

    #create toolbar
    toolbarFrame = LabelFrame(aboutWindow, bg="blue")
    toolbarFrame.grid(row=0,column=0,columnspan=2,sticky="WE")
    toolbarLabel = Label(toolbarFrame, text="ToolBar", bd=1, bg="blue")
    toolbarLabel.grid(row=0,column=0,columnspan=2,sticky="WE")


    #create about frame
    labelFrame = LabelFrame(aboutWindow, bg="gray")
    labelFrame.grid(row=1,column=0,columnspan=2,rowspan=2,sticky="NWES")

    #create about message
    aboutLabel = Label(labelFrame, text="""This is a basic note taking application that was created as a way for me to learn Python. \n The current state is far from incomplete. \n To learn more about the current state of the application see the github repository documentation.""", fg="blue", bg="gray", bd=1,font=(0,20))
    aboutLabel.grid(row=0,column=0,rowspan=2,sticky="NSEW")

#Add commands to dropdown note options
addNote.menu.add_command(label="Text Note", command=createTextNote)
addNote.menu.add_command(label="List Note", command=createListNote)
addNote.menu.add_command(label="Canvas Note", command=createCanvasNote)

min_w = 50 # Minimum width of the frame
max_w = 200 # Maximum width of the frame
cur_width = min_w # Increasing width of the frame
expanded = False # Check if it is completely exanded

#sidebar functions
def expand():
    global cur_width, expanded
    cur_width += 10 # Increase the width by 10
    rep = root.after(5,expand) # Repeat this func every 5 ms
    frame.config(width=cur_width) # Change the width to new increase width
    if cur_width >= max_w: # If width is greater than maximum width
        expanded = True # Frame is expended
        root.after_cancel(rep) # Stop repeating the func
        fill()

def contract():
    global cur_width, expanded
    cur_width -= 10 # Reduce the width by 10
    rep = root.after(5,contract) # Call this func every 5 ms
    frame.config(width=cur_width) # Change the width to new reduced width
    if cur_width <= min_w: # If it is back to normal width
        expanded = False # Frame is not expanded
        root.after_cancel(rep) # Stop repeating the func
        fill()

def fill():
    if expanded: # If the frame is exanded
        # Show a text, and remove the image
        home_b.config(text='Home',image='',font=(0,21))
        set_b.config(text='Settings',image='',font=(0,21))
        about_b.config(text='About',image='',font=(0,21))
    else:
        # Bring the image back
        home_b.config(image=home,font=(0,21))
        set_b.config(image=settings,font=(0,21))
        about_b.config(image=about,font=(0,21))

# Define the icons to be shown and resize it
home = ImageTk.PhotoImage(Image.open('resources/home.png').resize((40,40),Image.ANTIALIAS))
settings = ImageTk.PhotoImage(Image.open('resources/settings.png').resize((40,40),Image.ANTIALIAS))
about = ImageTk.PhotoImage(Image.open('resources/about.png').resize((40,40),Image.ANTIALIAS))

root.update() # For the width to get updated
frame = Frame(root,bg='orange',width=50,height=root.winfo_height())
frame.grid(row=0,column=0,rowspan=2,sticky="NSE")

# Make the buttons with the icons to be shown
home_b = Button(frame,image=home,bg='orange',relief='flat')
set_b = Button(frame,image=settings,bg='orange',relief='flat', command=openSettings)
about_b = Button(frame,image=about,bg='orange',relief='flat', command=openAbout)

# Put them on the frame
home_b.grid(row=0,column=0,pady=10)
set_b.grid(row=1,column=0,pady=50)
about_b.grid(row=2,column=0,pady=10)

# Bind to the frame, if entered or left
frame.bind('<Enter>',lambda e: expand())
frame.bind('<Leave>',lambda e: contract())

# So that it does not depend on the widgets inside the frame
frame.grid_propagate(False)


root.mainloop()
