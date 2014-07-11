import Tkinter

def OnKeyPress(event):
 value = event.widget.get()
 string="value of %s is '%s'" % (event.widget._name, value)
 status.configure(text=string)

root = Tkinter.Tk()

entry1 = Tkinter.Entry(root, name="entry1")
entry2 = Tkinter.Entry(root, name="entry2")
entry3 = Tkinter.Entry(root, name="entry3")

entry1.bindtags(('.entry1', 'Entry', '.', 'all'))
entry2.bindtags(('Entry', '.entry1', '.', 'all'))
entry3.bindtags(('.entry1','Entry','post-class-bindings', '.', 'all'))

btlabel1 = Tkinter.Label(text="bindtags: %s" % " ".join(entry1.bindtags()))
btlabel2 = Tkinter.Label(text="bindtags: %s" % " ".join(entry2.bindtags()))
btlabel3 = Tkinter.Label(text="bindtags: %s" % " ".join(entry3.bindtags()))
status = Tkinter.Label(anchor="w")

entry1.grid(row=0,column=0)
btlabel1.grid(row=0,column=1, padx=10, sticky="w")
entry2.grid(row=1,column=0)
btlabel2.grid(row=1,column=1, padx=10, sticky="w")
entry3.grid(row=2,column=0)
btlabel3.grid(row=2,column=1, padx=10)
status.grid(row=3, columnspan=2, sticky="w")
entry1.bind("<KeyPress>", OnKeyPress)
entry2.bind("<KeyPress>", OnKeyPress)
entry3.bind_class("post-class-bindings", "<KeyPress>", OnKeyPress)

root.mainloop()
