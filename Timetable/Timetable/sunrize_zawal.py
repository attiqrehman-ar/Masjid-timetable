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

import sys

which_time=sys.argv[1]
# which_time="Zawal"
arabic=""

if which_time=="Zawal":
    arabic="وقت الزوال"
else:
    arabic="وقت المشروق"

# Create a label for "Silent your phone" text
silent_label = Label(window, text=arabic,bg="lightgrey", width="28",fg="black", font=("Arial",25))
# Place the label just after the image
silent_label.place(relx=0.34, rely=0.06)

silent_label = Label(window, text=which_time,width="20",bg="#cdc874", fg="black", font=("Arial",35))
# Place the label just after the image
silent_label.place(relx=0.34, rely=0.15)

arabic_label = Label(window , text=which_time , bg="black", fg="white", font=("Arial",68))
# Place the label just after the image
arabic_label.place(relx=0.35, rely=0.45)
timer1 = Label(window , text="which_time" , bg="black", fg="white", font=("Arial",48))
# Place the label just after the image
timer1.place(relx=0.35, rely=0.6)






import sys


import subprocess

# Function to update the screen after 10 minutes
def reset_screen():
    subprocess.run(["python", "main.py"])

# Simulate the passage of time
time_left_seconds = 10 * 60  # 10 minutes in seconds
def switch_to_main():
    subprocess.run(["python", "main.py"])
    window.destroy()

# Schedule the function to switch back to main.py after 2 minutes (120 seconds)
window.after(1 * 60 * 1000, switch_to_main)
# Simulate the passage of time
# time_left_seconds = 600  # 10 minutes (change it to 0 for testing)
time_left_seconds = 10  # 10 minutes (change it to 0 for testing)



# Create a label for "Silent your phone" text
# timer1 = Label(window, text="Timer", font=("Arial",25),bg="black", fg="white")
# # Place the label just after the image
# timer1.place(relx=0.4, rely=0.72)



# # Function to toggle color between red and white
# def toggle_color():
#     current_color = timer1.cget("fg")
#     if current_color == "white":
#         timer1.config(fg="red")
#     else:
#         timer1.config(fg="white")

# Function to update label text and toggle color
# def update_and_toggle():
    # toggle_color()
    # window.after(1000, update_and_toggle)  # Schedule the function to run again after 1 second
# 
# Start the update_and_toggle function
# update_and_toggle()
import sys

# Function to update the screen after 10 minutes
def reset_screen(): 
    subprocess.run(["python", "main.py"])
    # subprocess.run(["python", "current_nmaz_time.py",v1,v2,v3])

# Retrieve command-line arguments
nmaz_index = sys.argv[1]  # value1
nmaz_time = sys.argv[2]  # value2

beginning_list = []
start_list = []

import csv

# Assuming the CSV file is named "prayer_timings.csv" and located in the same directory as this script
csv_file = "prayer_timings.csv"
# csv_file = "latest.csv"
import subprocess
today_weekday = datetime.now().weekday()

# Get today's date in the format "1-Jan"
today_date = datetime.now().strftime("%d-%b")
sun_rise=""
sunrise_time=""
fajr_time=""
# Read the data from the CSV file and append only the data for today's date to beginning_list and start_list
with open(csv_file, newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row["Date"] == today_date:
            beginning_list.append(row["FAJR start"])
            start_list.append(row["FAJR prayer"])
            sunrise_time=row["SUN RISE"]
            fajr_time=row["FAJR prayer"]

            beginning_list.append(row["DHUHR start"])
            start_list.append(row["DHUHR prayer"])
            
            beginning_list.append(row["ASR start"])
            start_list.append(row["ASR prayer"])
            
            beginning_list.append(row["M/RIB start"])
            start_list.append(row["M/RIB prayer"])
            
            beginning_list.append(row["ISHA start"])
            start_list.append(row["ISHA prayer"])
def update_jamat_left_timer(counter=120):
    # Decrease the counter by 1 second
    counter -= 1

    # Calculate minutes and seconds from the counter
    minutes_left = counter // 60
    seconds_left = counter % 60

    # Format the time left string
    time_left_str = f"{minutes_left:02d}:{seconds_left:02d}"

    # Update the timer label with the time left
    timer1.config(text=time_left_str)

    # If counter reaches 0, stop the timer
    if counter == 0:
        subprocess(["python","main.py"])
        # Add your code here to execute when the counter reaches 0
        pass
    else:
        # Schedule the function to run again after 1 second
        window.after(1000, update_jamat_left_timer, counter)

# Start the 2-minute countdown timer
update_jamat_left_timer()



window.configure(bg="black")

if time_left_seconds <= 0:
    reset_screen()
else:
    # Update the current prayer info
    # Show the "phone off" screen
    window.mainloop()
