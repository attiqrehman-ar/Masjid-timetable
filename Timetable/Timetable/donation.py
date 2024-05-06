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
silent_label = Label(window, text=" (قال: رسول الله (صلى الله عليه وسلم",bg="black", fg="white", font=("Arial",35))
# Place the label just after the image
silent_label.place(relx=0.34, rely=0.06)

arabic_label = Label(window, text="ما نقصت صدقة من مال",bg="black" , fg="white", font=("Arial",35))
# Place the label just after the image
arabic_label.place(relx=0.37, rely=0.14)

arabic_label = Label(window, text="The messenger of Allah (saw) said:",bg="black", fg="white", font=("Arial",28))
# Place the label just after the image
arabic_label.place(relx=0.2, rely=0.28)
arabic_label = Label(window , text="\" Charity does not decrease wealth.\"",bg="black", fg="white", font=("Arial",35))
# Place the label just after the image
arabic_label.place(relx=0.2, rely=0.36)

arabic_label = Label(window , text="(PLease donate generously)",bg="black", fg="white", font=("Arial",25))
# Place the label just after the image
arabic_label.place(relx=0.2, rely=0.49)

arabic_label = Label(window , text="AL-SUNNAH MOSQUE",bg="black", fg="white", font=("Arial",25))
# Place the label just after the image
arabic_label.place(relx=0.26, rely=0.59)

arabic_label = Label(window , text="Account : 10117242",bg="black", fg="white", font=("Arial",25))
# Place the label just after the image
arabic_label.place(relx=0.26, rely=0.65)

arabic_label = Label(window , text="Sort code : 40-11-56",bg="black", fg="white", font=("Arial",25))
# Place the label just after the image
arabic_label.place(relx=0.26, rely=0.7)

arabic_label = Label(window , text="Contact : 0161 492 0699",bg="black", fg="white", font=("Arial",25))
# Place the label just after the image
arabic_label.place(relx=0.26, rely=0.8)

arabic_label = Label(window , text="Email : info@alsunnahmcr.org",bg="black", fg="white", font=("Arial",25))
# Place the label just after the image
arabic_label.place(relx=0.26, rely=0.86)

import sys


import subprocess
screen_timeout=int(sys.argv[4])

# Function to update the screen after 10 minutes
def reset_screen():
    subprocess.run(["python", "phone_off.py",str(sys.argv[1]),str(sys.argv[2]),str(sys.argv[3]),str(screen_timeout)])
    window.destroy()

# Simulate the passage of time
time_left_seconds = 10 * 60  # 10 minutes in seconds
def switch_to_main():
    subprocess.run(["python", "phone_off.py",str(sys.argv[1]),str(sys.argv[2]),str(sys.argv[3]),str(screen_timeout)])
    window.destroy()

# Schedule the function to switch back to main.py after 2 minutes (120 seconds)
# window.after(1 * 60*1000 , switch_to_main)
# Simulate the passage of time
# time_left_seconds = 600  # 10 minutes (change it to 0 for testing)
time_left_seconds = 10  # 10 minutes (change it to 0 for testing)

window.configure(bg="black")

window.after(screen_timeout, reset_screen)  # Run the reset_screen function after 40 seconds (40000 milliseconds)
# if time_left_seconds <= 0:
#     reset_screen()
# else:
    # Update the current prayer info
    # Show the "phone off" screen
window.mainloop()
