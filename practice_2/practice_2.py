from tkinter import *

def insert_color(color):
  if color == "red":
    color_name.delete( 0, END )
    color_name.insert( END, "красный ",  )
    color_code.insert( END, red_button["bg"] )
  if color == "orange":
    color_name.delete( 0, END )
    color_name.insert( END, "оранжевый " )
    color_code.delete( 0, END )
    color_code.insert( END, orange_button["bg"] )
  if color == "yellow":
    color_name.delete( 0, END )
    color_name.insert( END, "жёлтый " )
    color_code.delete( 0, END )
    color_code.insert( END, yellow_button["bg"] )
  if color == "green":
    color_name.delete( 0, END )
    color_name.insert( END, "зелёный " )
    color_code.delete( 0, END )
    color_code.insert( END, green_button["bg"] )
  if color == "light_blue":
    color_name.delete( 0, END )
    color_name.insert( END, "голубой " )
    color_code.delete( 0, END )
    color_code.insert( END, light_blue_button["bg"] )
  if color == "blue":
    color_name.delete( 0, END )
    color_name.insert( END, "синий " )
    color_code.delete( 0, END )
    color_code.insert( END, blue_button["bg"] )
  if color == "purple":
    color_name.delete( 0, END )
    color_name.insert( END, "фиолетовый " )
    color_code.delete( 0, END )
    color_code.insert( END, purple_button["bg"] )

root = Tk()
root.resizable( width=False, height=False )
root.geometry( "500x300" )
root[ "bg" ] = "grey"
root.title( "Practice 2" )



color_name = Entry( width=50, bg="grey", justify="center" )
color_code = Entry( width=50, bg="white", justify="center" )

red_button = Button( width=40, bg="#ff0000", command=lambda: insert_color("red") )
orange_button = Button( width=40, bg="#ff7d00", command=lambda: insert_color("orange") )
yellow_button = Button( width=40, bg="#ffff00", command=lambda: insert_color("yellow") )
green_button = Button( width=40, bg="#00ff00", command=lambda: insert_color("green") )
light_blue_button = Button( width=40, bg="#007dff", command=lambda: insert_color("light_blue") )
blue_button = Button( width=40, bg="#0000ff", command=lambda: insert_color("blue") )
purple_button = Button( width=40, bg="#7d00ff", command=lambda: insert_color("purple") )

color_name.pack()
color_code.pack()
red_button.pack()
orange_button.pack()
yellow_button.pack()
green_button.pack()
light_blue_button.pack()
blue_button.pack()
purple_button.pack()


root.mainloop()