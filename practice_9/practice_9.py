from tkinter import *

root = Tk()
root.title("practice_9")
root.resizable(width=False, height=False)

c = Canvas(root, width=400, height=340, bg='white')
c.pack()

c.create_oval(290, 50, 350, 110, width=1, fill='orange', outline='orange')
c.create_polygon(200, 70, 70, 170, 320, 170, fill="lightblue", outline="lightblue")
c.create_polygon((110, 170), (280, 170),
 (280, 310), (110, 310),
 fill='lightblue', outline='lightblue')

start_x = 10
start_y = 450
end_x = 280
end_y = 230
start_angle = 180
extent_angle = -40
spacing = -260

for i in range(35):
  c.create_arc(start_x + i * (end_x + spacing), start_y,
               end_x + i * (end_x + spacing), end_y,
               start = start_angle, extent = extent_angle,
               style=ARC, outline = 'green', width = 5)

root.mainloop()