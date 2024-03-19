from tkinter import *

def tel_number_changer(tel_number):
  person_tel_number[ "text" ] = tel_number

class Person:
  def __init__( self, name, tel_number, person_id):
    Radiobutton( 
      text=name,
      command=lambda i=tel_number: tel_number_changer(i),
      variable=person_radio_changer,
      value=person_id,
      indicatoron=0,
      width=12,
      height=3
     ).pack()

root = Tk()
root.title( "Practice_5" )
root.resizable( width=False, height=False )

frame = Frame()
frame.pack( side=RIGHT )

person_radio_changer = IntVar()
person_radio_changer.set(0)
Person( "Вася", "8-800-555-35-35", 1 )
Person( "Петя", "8-980-111-00-00", 2 )
Person( "Маша", "8-999-888-88-88", 3 )

person_tel_number = Label( frame, width=25, height=10, bg="white" )

person_tel_number.pack(side=RIGHT)

root.mainloop()