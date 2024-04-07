from tkinter import *

def change_size():
  try:
    width = int(width_value.get())
    height = int(height_value.get())

    squeare_for_changer.config(width=width, height=height)
  except ValueError:
    pass

def change_background(event):
  if str(event.type) == "FocusIn":
    squeare_for_changer.config(bg="white")
  elif str(event.type) == "FocusOut":
    squeare_for_changer.config(bg="lightgrey")

def focus_next_widget(event):
  event.widget.tk_focusNext().focus_set()
  return "break"

def focus_previos_widget(event):
  event.widget.tk_focusPrev().focus_set()
  return "break"

root = Tk()
root.title("Practice_8")

top_frame = Frame()
top_frame.pack()

w_h_frame = Frame(top_frame)
w_h_frame.grid(row=0, column=0)

width_frame = Frame(w_h_frame)
width_frame.pack()

width_label = Label(width_frame, text="W: ")
width_label.pack(side=LEFT)
width_value = Entry(width_frame, width=5)
width_value.pack(side=LEFT)

height_frame = Frame(w_h_frame)
height_frame.pack()

height_label = Label(height_frame, text="H: ")
height_label.pack(side=LEFT)
height_value = Entry(height_frame, width=5)
height_value.pack(side=TOP)

change_button = Button(top_frame, text="Изменить", command=change_size)
change_button.bind("<Return>", lambda event: change_size())
change_button.grid(row=0, column=1)

squeare_for_changer = Text(width=35, height=10)
squeare_for_changer.pack()
squeare_for_changer.bind("<FocusIn>", change_background)
squeare_for_changer.bind("<FocusOut>", change_background)
squeare_for_changer.focus_set()
squeare_for_changer.config(takefocus=True)

root.bind("<Tab>", focus_next_widget)
root.bind("<Shift-Tab>", focus_previos_widget)
root.bind("<Control-Tab>", focus_next_widget)

root.mainloop()