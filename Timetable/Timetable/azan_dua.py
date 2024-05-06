from tkinter import Tk, Label, PhotoImage
from datetime import datetime

# Create the main window
window = Tk()
# window.geometry("1000 x 1000")
window.attributes('-fullscreen', True)

# Load the "phone off" image
phone_off_image = PhotoImage(file="after_azan_dua.png")

phone_off_image_resized = phone_off_image.subsample(5)  # Resize by a factor of 5

# Create a label widget to display the "phone off" image
phone_off_label = Label(window, image=phone_off_image)

# Place the image label at coordinates (10% from top, 40% from left)
# phone_off_label.place(relx=0.3, rely=0.15, width=400, height=350)

# Create a label for "Silent your phone" text
silent_label = Label(window, text="Dua after Athan",width="20", bg="#b4bca8",font=("Arial",30))
# Place the label just after the image
silent_label.place(relx=0.35, rely=0.03, anchor="nw")

arabic_label = Label(window, text="دعاء الأذان",bg="#d0cc74", width="20",font=("Arial",30))
# Place the label just after the image
arabic_label.place(relx=0.35, rely=0.1,anchor="nw")

arabic_label = Label(window, text="اللَّهُمَّ رَبَّ هَذِهِ الدَّعْوَةِ التَّامَّةِ، وَالصَّلَاةِ الْقَائِمَةِ، ", bg="#75b53d", font=("Arial",35))
# Place the label just after the image
arabic_label.place(relx=0.28, rely=0.25)
arabic_label = Label(window , text="آتِ مُحَمَّداً الْوَسِيلَةَ وَالْفَضِيلَةَ، وَابْعَثْهُ مَقَاماً  ، ", bg="#75b53d",font=("Arial",35))
# Place the label just after the image
arabic_label.place(relx=0.28, rely=0.33)
arabic_label = Label(window,  text=" مَحْمُوداً الَّذِي وَعَدْتَهُ، إَنَّكَ لَا تُخْلِفُ الْمِيعَادَ، ", bg="#75b53d",font=("Arial",35))
# Place the label just after the image
arabic_label.place(relx=0.28, rely=0.40)

import sys

import subprocess

# Function to update the screen after 10 minutes
def reset_screen():
    subprocess.run(["python", "main.py"])
    window.destroy()

# Simulate the passage of time
time_left_seconds = 10 * 60  # 10 minutes in seconds
def switch_to_main():
    subprocess.run(["python", "main.py"])
    window.destroy()

# Schedule the function to switch back to main.py after 2 minutes (120 seconds)
window.after(2 * 60 * 1000, switch_to_main)

# Simulate the passage of time
# time_left_seconds = 600  # 10 minutes (change it to 0 for testing)

time_left_seconds = 10  # 10 minutes (change it to 0 for testing)

window.configure(bg="#75b53d")

if time_left_seconds <= 0:
    reset_screen()
else:
    window.mainloop()
