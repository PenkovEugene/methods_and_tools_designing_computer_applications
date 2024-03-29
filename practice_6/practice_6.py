from tkinter import *

def item_to_right():
  select = list(leftbox.curselection())
  select.reverse()
  for i in select:
    value = leftbox.get(i)
    rightbox.insert(END, value)
    leftbox.delete(i)

def item_to_left():
  select = list(rightbox.curselection())
  select.reverse()
  for i in select:
    value = rightbox.get(i)
    leftbox.insert(END, value)
    rightbox.delete(i)

root = Tk()
root.title("practice_6")

leftbox = Listbox(selectmode=EXTENDED)
leftbox.pack(side=LEFT)

for i in ('apple', 'bananas', 'carrot', 'bread', 'butter', 'meat', 'potato', 'pineapple'):
  leftbox.insert(END, i)

f = Frame()
f.pack(side=LEFT, padx=10)

Button(f, text=">>>", command=item_to_right).pack(fill=X)
Button(f, text="<<<", command=item_to_left).pack(fill=X)

rightbox = Listbox(selectmode=EXTENDED)
rightbox.pack(side=RIGHT)

root.mainloop()