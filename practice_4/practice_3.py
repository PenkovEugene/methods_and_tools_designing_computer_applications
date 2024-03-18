from tkinter import *

def insert_color(color):
  if color == "red":
    color_name[ "text" ] = ( "красный ")
    color_code.insert( END, red_button["bg"] )
  if color == "orange":
    color_name[ "text" ] = ( "оранжевый" )
    color_code.delete( 0, END )
    color_code.insert( END, orange_button["bg"] )
  if color == "yellow":
    color_name[ "text" ] = ( "жёлтый" )
    color_code.delete( 0, END )
    color_code.insert( END, yellow_button["bg"] )
  if color == "green":
    color_name[ "text" ] = ( "зелёный" )
    color_code.delete( 0, END )
    color_code.insert( END, green_button["bg"] )
  if color == "light_blue":
    color_name[ "text" ] = ( "голубой" )
    color_code.delete( 0, END )
    color_code.insert( END, light_blue_button["bg"] )
  if color == "blue":
    color_name[ "text" ] = ( "синий" )
    color_code.delete( 0, END )
    color_code.insert( END, blue_button["bg"] )
  if color == "purple":
    color_name[ "text" ] = ( "фиолетовый" )
    color_code.delete( 0, END )
    color_code.insert( END, purple_button["bg"] )

root = Tk()
root.title( "Practice_3" )
root[ "bg" ] = "lightgrey"
root.resizable( width=False, height=False )

color_name = Label( width=30, bg="lightgrey", justify="center" )
color_code = Entry( width=20, bg="white", justify="center" )

colors_frame = Frame( root )

red_button = Button( colors_frame, width=2, bg="#ff0000", command=lambda: insert_color("red") )
orange_button = Button( colors_frame, width=2, bg="#ff7d00", command=lambda: insert_color("orange") )
yellow_button = Button( colors_frame, width=2, bg="#ffff00", command=lambda: insert_color("yellow") )
green_button = Button( colors_frame, width=2, bg="#00ff00", command=lambda: insert_color("green") )
light_blue_button = Button( colors_frame, width=2, bg="#007dff", command=lambda: insert_color("light_blue") )
blue_button = Button( colors_frame, width=2, bg="#0000ff", command=lambda: insert_color("blue") )
purple_button = Button( colors_frame, width=2, bg="#7d00ff", command=lambda: insert_color("purple") )

color_name.pack()
color_code.pack( pady=5 )
colors_frame.pack( side=BOTTOM )
red_button.pack( side=LEFT, padx=1 )
orange_button.pack( side=LEFT, padx=1 )
yellow_button.pack( side=LEFT, padx=1 )
green_button.pack( side=LEFT, padx=1 )
light_blue_button.pack( side=LEFT, padx=1 )
blue_button.pack( side=LEFT, padx=1 )
purple_button.pack( side=LEFT, padx=1 )

root.mainloop()

