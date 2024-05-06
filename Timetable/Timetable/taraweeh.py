from tkinter import Tk, Label, PhotoImage
from datetime import datetime

# Create the main window
window = Tk()
# window.geometry("1000 x 1000")
window.attributes('-fullscreen', True)

# Load the "phone off" image
phone_off_image = PhotoImage(file="")

phone_off_image_resized = phone_off_image.subsample(5)  # Resize by a factor of 5

# Create a label widget to display the "phone off" image
phone_off_label = Label(window, image=phone_off_image)

# Place the image label at coordinates (10% from top, 40% from left)
# phone_off_label.place(relx=0.3, rely=0.15, width=400, height=350)

# Create a label for "Silent your phone" text
silent_label = Label(window, text="E&S Islamic Society",bg="black", fg="white", font=("Arial",24))
# Place the label just after the image
silent_label.place(relx=0.34, rely=0.06)

arabic_label = Label(window, text="Taraweeh Prayer",bg="black" , fg="white", font=("Arial",26))
# Place the label just after the image
arabic_label.place(relx=0.34, rely=0.14)
arabic_label = Label(window, text="صلاة التراويح",bg="black" , fg="white", font=("Arial",26))
# Place the label just after the image
arabic_label.place(relx=0.34, rely=0.19)

timer_label = Label(window, text="",bg="black", fg="red", font=("Arial",28))
# Place the label just after the image
timer_label.place(relx=0.34, rely=0.28)




import time
# Update the timer label every second
def update_timer():
    # current_time_24hr = time.strftime("%H:%M:%S") #24 hour formate
    current_time = time.strftime("%H:%M")
    # current_time = time.strftime("%I:%M:%S %p", time.strptime(current_time_24hr, "%H:%M:%S"))

    timer_label.config(text=current_time)
    window.after(1000, update_timer)  # Schedule the function to run again after 1000ms (1 second)

update_timer()  # Start the timer


arabic_label = Label(window , text="Turn off / silence your phone",bg="black", fg="white", font=("Arial",35))
# Place the label just after the image
arabic_label.place(relx=0.2, rely=0.36)

arabic_label = Label(window , text="(PLease donate generously)",bg="black", fg="white", font=("Arial",20))
# Place the label just after the image
arabic_label.place(relx=0.2, rely=0.46)

# Load the "phone off" image
phone_off_image = PhotoImage(file="phone_off2.png")

# Create a label widget to display the "phone off" image
phone_off_label = Label(window, image=phone_off_image)

# Place the image label at coordinates (10% from top, 40% from left)
phone_off_label.place(relx=0.31, rely=0.55, width=100, height=100)

arabic_label = Label(window , text="AL-SUNNAH MOSQUE",bg="black", fg="white", font=("Arial",25))
# Place the label just after the image
arabic_label.place(relx=0.26, rely=0.7)

arabic_label = Label(window , text="Account : 10117242",bg="black", fg="white", font=("Arial",25))
# Place the label just after the image
arabic_label.place(relx=0.26, rely=0.76)

arabic_label = Label(window , text="Sort code : 40-11-56",bg="black", fg="white", font=("Arial",25))
# Place the label just after the image
arabic_label.place(relx=0.26, rely=0.82)


import sys


import subprocess


# Function to update the screen after 10 minutes
def reset_screen():
    subprocess.run(["python", "phone_off.py",str(sys.argv[1]),str(sys.argv[2]),str(sys.argv[3])])
    window.destroy()

# Simulate the passage of time
time_left_seconds = 10 * 60  # 10 minutes in seconds
def switch_to_main():
    subprocess.run(["python", "phone_off.py",str(sys.argv[1]),str(sys.argv[2]),str(sys.argv[3])])
    window.destroy()

# Schedule the function to switch back to main.py after 2 minutes (120 seconds)
# window.after(1 * 60*1000 , switch_to_main)
# Simulate the passage of time
# time_left_seconds = 600  # 10 minutes (change it to 0 for testing)
time_left_seconds = 10  # 10 minutes (change it to 0 for testing)

window.configure(bg="black")

window.after(2000, reset_screen)  # Run the reset_screen function after 40 seconds (40000 milliseconds)
# if time_left_seconds <= 0:
#     reset_screen()
# else:
    # Update the current prayer info
    # Show the "phone off" screen
window.mainloop()
