from tkinter import *
fields = 'Chords to Practice', 'Scales to Practice', 'PDF Destination'

def fetch(entries):
	toPrint = ""
	for entry in entries:
		toPrint += entry[1].get()
		toPrint += " 0000 "
	print(toPrint)
	
def makeform(root, fields):
   entries = []
   for field in fields:
      row = Frame(root)
      lab = Label(row, width=15, text=field, anchor='w')
      ent = Entry(row)
      row.pack(side=TOP, fill=X, padx=5, pady=5)
      lab.pack(side=LEFT)
      ent.pack(side=RIGHT, expand=YES, fill=X)
      entries.append((field, ent))
   return entries


if __name__ == '__main__':
   root = Tk()
   ents = makeform(root, fields)
   root.bind('<Return>', (lambda event, e=ents: fetch(e)))   
   b1 = Button(root, text='Create PDF',
          command=(lambda e=ents: fetch(e)))
   b1.pack(side=LEFT, padx=5, pady=5)
   b2 = Button(root, text='Quit', command=root.quit)
   b3 = Button(root, text= 'Help', command = root.quit)
   b2.pack(side=LEFT, padx=5, pady=5)
   b3.pack(side=LEFT, padx = 5, pady = 5)
   root.mainloop()