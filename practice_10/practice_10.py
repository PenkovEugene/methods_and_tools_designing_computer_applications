from tkinter import *

def move_towards_target(x_target, y_target):
  x1, y1, x2, y2 = c.coords(ball)
  if x1 < x_target:
      c.move(ball, 1, 0)
  elif x1 > x_target:
      c.move(ball, -1, 0)
  if y1 < y_target:
      c.move(ball, 0, 1)
  elif y1 > y_target:
      c.move(ball, 0, -1)
  if (x1, y1) != (x_target, y_target):
      root.after(10, lambda: move_towards_target(x_target, y_target))

def handle_click(event):
  move_towards_target(event.x, event.y)

root = Tk()
root.title("practice_10")

c = Canvas(root, width=300, height=200, bg="white")
c.pack()

ball = c.create_oval(0, 100, 40, 140, fill='green')

c.bind('<Button-1>', handle_click)

root.mainloop()