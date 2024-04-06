from tkinter import *

def item_to_list(event):
  value = one_line_enter.get()
  listbox.insert(END, value)
  one_line_enter.delete(0, END)

def copy_to_one_line(event):
  select = list(listbox.curselection())
  select.reverse()
  for i in select:
    value = listbox.get(i)
    one_line_enter.delete(0, END)
    one_line_enter.insert(END, value)

root = Tk()
root.resizable(width=False, height=False)
root.title("Practice_7")
root.geometry( "300x250" )
root[ "bg" ] = "grey"

entry_name = Label(text="Введите значение", bg="grey", fg="white")
entry_name.pack()

one_line_enter = Entry(width=35)
one_line_enter.bind('<Return>', item_to_list)

one_line_enter.pack()

listbox_name = Label(text="Лист:", bg="grey", fg="white")
listbox_name.pack()

listbox = Listbox(width=35)
listbox.bind("<Double-Button-1>", copy_to_one_line)
listbox.pack()

root.mainloop()