from tkinter import Label, Tk
import time
def speak(str):
 from win32com.client import Dispatch
 speak = Dispatch("SAPI.SpVoice")
 speak.Speak(str)

if __name__ == '__main__':



 app_window = Tk()
app_window.title("The Current time is ")
speak("This is the Current time that you can see on your Output Screen")
app_window.geometry("420x150")
app_window.resizable(1,1)

text_font= ("Digital", 68, 'bold')
background = "#f2e750"
foreground= "#363529"
border_width = 25

label = Label(app_window, font=text_font, bg=background, fg=foreground, bd=border_width)
label.grid(row=0, column=1)

def digital_clock():
   time_live = time.strftime("%H:%M:%S")
   label.config(text=time_live)

   label.after(200, digital_clock)

digital_clock()
app_window.mainloop()