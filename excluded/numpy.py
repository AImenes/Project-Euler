from Tkinter import *

root = Tk()

topDiv = Frame(root)
topDiv.pack()
bottomDiv = Frame(root)
bottomDiv.pack(side=BOTTOM);

button1 = Button(topDiv, text="Button 1", fg="red");
button2 = Button(topDiv, text="Button 2", fg="red");
button3 = Button(bottomDiv, text="Button 3", fg="blue");

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack()


root.mainloop();