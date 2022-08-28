from tkinter import *
from random_lines import text
import random




random_texts=random.choice(text)
print(len(random_texts))





# creating timer
def countdown():

   start_timer(60)
def start_timer(count):
   timer_left.config(text=f":{count}")
   if count > 0:
      window.after(1000,start_timer, count-1)
   elif count==0:
      total_words = len(typing_box.get("1.0",END))
      WPM = total_words / 5
      WPM_count.config(text=f"{WPM}")

# creating GUI
window=Tk()
window.title("The Typing speed testing machine")
window.config(width=800, height=500)

button=Button(text="Restart", highlightthickness=0, command=countdown)
button.place(x=400, y=150)
WPM_count=Label(text="00")
WPM_count.place(x=360, y=150)


timer_left=Label(text=f":60")
timer_left.place(x=220, y=150)
typing_box=Text(width=50, height=60)
typing_box.place(x=150, y= 270)

start_timer(60)
WPM_label=Label(text="WPM")
WPM_label.place(x=320, y=150)
timer=Label(text="Time left")
timer.place(x=150, y=150)
lines_Label=Label(text=random_texts)
lines_Label.place(x=10, y=200)






window.mainloop()