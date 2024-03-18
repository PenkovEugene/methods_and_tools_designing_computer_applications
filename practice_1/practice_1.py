from tkinter import *

def isDigit(string):
  numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]
  dot_count = 0
  for i in string:
    if i not in numbers:
      return False
    if i == ".":
      dot_count +=1
      if dot_count > 1:
        return False
  return True

def plus_function (event):
  first = first_number.get()
  first_is_digit = isDigit(first)
  second = second_number.get()
  second_is_digit = isDigit(second)
  if first_is_digit and second_is_digit:
    result = float(first) + float(second)
    result_of_calc[ "text" ] = round(result, 2)
  else:
    result_of_calc[ "text" ] = "Ошибка"
  
def minus_function (event):
  first = first_number.get()
  first_is_digit = isDigit(first)
  second = second_number.get()
  second_is_digit = isDigit(second)
  if first_is_digit and second_is_digit:
    result = float(first) - float(second)
    result_of_calc[ "text" ] = round(result, 2)
  else:
    result_of_calc[ "text" ] = "Ошибка"
  
def multiplication_function (event):
  first = first_number.get()
  first_is_digit = isDigit(first)
  second = second_number.get()
  second_is_digit = isDigit(second)
  if first_is_digit and second_is_digit:
    result = float(first) * float(second)
    result_of_calc[ "text" ] = round(result, 2)
  else:
    result_of_calc[ "text" ] = "Ошибка"
  
def division_function (event):
  first = first_number.get()
  first_is_digit = isDigit(first)
  second = second_number.get()
  second_is_digit = isDigit(second)
  if first_is_digit and second_is_digit and second != "0":
    result = float(first) / float(second)
    result_of_calc[ "text" ] = round(result, 2)
  else:
    result_of_calc[ "text" ] = "Ошибка"
  


root = Tk()

root.resizable( width=False, height=False )
root.geometry( "500x300" )
root[ "bg" ] = "grey"
root.title( "Practice 1" )
# root.iconbitmap( "app_logo.ico" )

first_number = Entry( width=20 )
second_number = Entry( width=20 )

plus_btn = Button( text="+", width=20 )
minus_btn = Button( text="-", width=20 )
multiplication_btn = Button( text="*", width=20 )
division_btn = Button( text="/", width=20 )

first_number_label = Label( 
  width=20, 
  bg="grey", 
  fg="white", 
  text="Введите первое число")
second_number_label = Label( 
  width=20, 
  bg="grey", 
  fg="white",
  text="Введите второе число" )
result_of_calc = Label( width=20, bg="#505F4E", fg="white" )

plus_btn.bind( "<Button-1>", plus_function )
minus_btn.bind( "<Button-1>", minus_function )
multiplication_btn.bind( "<Button-1>", multiplication_function )
division_btn.bind( "<Button-1>", division_function )

first_number_label.pack()
first_number.pack()
second_number_label.pack()
second_number.pack()
plus_btn.pack()
minus_btn.pack()
multiplication_btn.pack()
division_btn.pack()
result_of_calc.pack()

root.mainloop()