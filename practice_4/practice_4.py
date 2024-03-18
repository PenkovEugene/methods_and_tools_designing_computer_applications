from tkinter import *

def open_file():
  file_data.delete( 1.0, END )
  file_path = file_getter.get()
  file = open( f'practice_4/{file_path}' )
  file_lines = file.readlines()
  for line in file_lines:
    file_data.insert( END, line )
  file.close()

def save_file():
  data_for_save = file_data.get( 1.0, END )
  file_path = file_getter.get()
  with open ( f'practice_4/{file_path}', 'wt' ) as file:
    file.writelines(data_for_save) 

root = Tk()

root.resizable( width=False, height=False )
root.title( "Practice_4" )
root.geometry( "600x400" )
root[ "bg" ] = "grey"

first_line_frame = Frame()
first_line_frame.pack()

file_getter = Entry( first_line_frame, width=25 )
file_getter.pack( side=LEFT, padx=3 )

Button( 
  first_line_frame,
  width=10,
  text="Открыть",
  command=( open_file )
 ).pack( side=LEFT )

Button( 
  first_line_frame,
  width=10,
  text="Сохранить",
  command=( save_file )
 ).pack( side=LEFT )

file_data = Text()
file_data.pack()

root.mainloop()