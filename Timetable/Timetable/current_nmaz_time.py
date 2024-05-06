from tkinter import Tk, Label, PhotoImage
from datetime import datetime
import sys

# Create the main window
window = Tk()
# window.geometry("1000 x 1000")
window.attributes('-fullscreen', True)

# Load the "phone off" image
phone_off_image = PhotoImage(file="phone_off.png")

# Create a label widget to display the "phone off" image
phone_off_label = Label(window, image=phone_off_image)

# Place the image label at coordinates (10% from top, 40% from left)
phone_off_label.place(relx=0.3, rely=0.12, width=400, height=350)
today_date = datetime.now().strftime("%H-%M")

import sys

# Retrieve command-line arguments
nmaz_index = sys.argv[1]  # value1
nmaz_time = sys.argv[2]  # value2
now_time= datetime.now().strftime("%H:%M")

screen_timeout=int(sys.argv[4])

  # value2

# Create a label for "Silent your phone" text
# silent_label = Label(window, text="Silent your phone", font=("Arial",25))
# # Place the label just after the image
# silent_label.place(relx=0.4, rely=0.72)

# Create a label for "Silent your phone" text
# timer1 = Label(window, text=sys.argv[3], font=("Arial",25), fg="green")
timer1 = Label(window, text=now_time, font=("Arial",25), fg="green")
# Place the label just after the image
timer1.place(relx=0.4, rely=0.72)



beginning_list = []
start_list = []

import csv

# Assuming the CSV file is named "prayer_timings.csv" and located in the same directory as this script
# csv_file = "prayer_timings.csv"
csv_file = "latest.csv"
import subprocess
today_date = datetime.now().strftime("%d-%b")

# Get today's date in the format "1-Jan"
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



# Function to update the current prayer time and name
def update_prayer_info():

    if nmaz_index=="0":
        prayer_label.config(text="صلاة الفجر " )
        prayer_label2.config(text="Fajr Prayer " )
    elif nmaz_index=="1" and datetime.now().weekday()==4:
        prayer_label.config(text="صلاة الجمعة ")
        prayer_label2.config(text="Jumm'a Prayer ")
    elif nmaz_index=="1":
        prayer_label.config(text="صلاة الظهر ")
        prayer_label2.config(text="Dhuhar Prayer ")
    elif nmaz_index=="2":
        prayer_label.config(text="صلاة العصر")
        prayer_label2.config(text="Asr Prayer")
    elif nmaz_index=="3":
        prayer_label.config(text=" صلاة المغرب")
        prayer_label2.config(text="Magrib Prayer")
    elif nmaz_index=="4":
        prayer_label.config(text="صلاة العشاء")
        prayer_label2.config(text="Isha Prayer")

# Create a label to display current prayer name and time
prayer_label = Label(window,font=("Arial",25))
# Place the label just after the "Silent your phone" label
prayer_label.place(relx=0.4, rely=0.63)

# Create a label to display current prayer name and time
prayer_label2 = Label(window,font=("Arial",25))
# Place the label just after the "Silent your phone" label
prayer_label2.place(relx=0.4, rely=0.05)

# Create a label to display current prayer name and time
# prayer__time_label = Label(window,font=("Arial",25),text=nmaz_time)
# # Place the label just after the "Silent your phone" label
# prayer__time_label.place(relx=0.4, rely=0.9)

# Function to update the screen after 10 minutes
def reset_screen():
    if nmaz_index=="4":
        subprocess.run(["python", "witr_dua.py"])
        window.destroy()
    else:
        subprocess.run(["python", "time_change.py",nmaz_index,screen_timeout])
        window.destroy()



islamic_day=""
islamic_month=""
from hijri_converter import Gregorian 

islamic_month_names = {
    1: "Muharram", 2: "Safar", 3: "Rabi' al-awwal", 4: "Rabi' al-sani",
    5: "Jumada al-awwal", 6: "Jumada al-thani", 7: "Rajab", 8: "Sha'ban",
    9: "Ramadan", 10: "Shawwal", 11: "Dhu al-Qi'dah", 12: "Dhu al-Hijjah"
}


def calculate_islamic_date():
   current_date = datetime.now()
   h = Gregorian(current_date.year, current_date.month, current_date.day).to_hijri()
  
   islamic_month = islamic_month_names[h.month]
   islamic_year = h.year
   islamic_day=h.day
   return f"{h.day} {islamic_month} {islamic_year} "
# Test the function
calculate_islamic_date()

def islamic_day_check():
    if islamic_day==27 and islamic_month=="Ramadan":
        subprocess(["python","zakat_ul_fitr.py"])
        window.destroy()
    elif islamic_day==28 and islamic_month=="Ramadan":
        subprocess(["python","zakat_ul_fitr.py"])
        window.destroy()
    elif islamic_day==29 and islamic_month=="Ramadan":
        subprocess(["python","zakat_ul_fitr.py"])
        window.destroy()


# Simulate the passage of time
time_left_seconds = 10 * 60  # 10 minutes in seconds
def switch_to_main():
    # subprocess.run(["python", "main.py","1", str(nmaz_index)])
     if nmaz_index=="4":
        subprocess.run(["python", "witr_dua.py",screen_timeout])
        window.destroy()
     elif nmaz_index=="4" and islamic_month=="Ramadan":
        subprocess.run(["python", "taraweeh.py",screen_timeout])
        window.destroy()
     else:
        subprocess.run(["python", "main.py"])
        window.destroy()

# Schedule the function to switch back to main.py after 2 minutes (120 seconds)
window.after(screen_timeout * 60 * 100, switch_to_main)
# Simulate the passage of time
# time_left_seconds = 600  # 10 minutes (change it to 0 for testing)
time_left_seconds = 10  # 10 minutes (change it to 0 for testing)

window.configure(bg="black")

if time_left_seconds <= 0:
    reset_screen()
else:
    # Update the current prayer info
    update_prayer_info()
    # Show the "phone off" screen
    window.mainloop()
