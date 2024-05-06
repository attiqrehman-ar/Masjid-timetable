from tkinter import Tk, Label, PhotoImage
from datetime import datetime
import sys
# Create the main window
window = Tk()
# window.geometry("1000 x 1000")
window.attributes('-fullscreen', True)
screen_timeout=int(sys.argv[4])

# Load the "phone off" image
phone_off_image = PhotoImage(file="phone_off.png")

# Create a label widget to display the "phone off" image
phone_off_label = Label(window, image=phone_off_image)

# Place the image label at coordinates (10% from top, 40% from left)
phone_off_label.place(relx=0.3, rely=0.2, width=400, height=350)


# Create a label for "Silent your phone" text
# silent_label = Label(window, text="Silent your phone", font=("Arial",25))
# # Place the label just after the image
# silent_label.place(relx=0.4, rely=0.72)

# Create a label for "Silent your phone" text
timer1 = Label(window, text="Timer", font=("Arial",25),bg="black", fg="white")
# Place the label just after the image
timer1.place(relx=0.4, rely=0.72)

# Function to toggle color between red and white
def toggle_color():
    current_color = timer1.cget("fg")
    if current_color == "white":
        timer1.config(fg="red")
    else:
        timer1.config(fg="white")

# Function to update label text and toggle color
def update_and_toggle():
    toggle_color()
    window.after(1000, update_and_toggle)  # Schedule the function to run again after 1 second

# Start the update_and_toggle function
update_and_toggle()
import sys

# Function to update the screen after 10 minutes
def reset_screen(v1,v2,v3): 
    subprocess.run(["python", "current_nmaz_time.py",v1,v2,v3,str(screen_timeout)])
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

islamic_month_names = {
    1: "Muharram", 2: "Safar", 3: "Rabi' al-awwal", 4: "Rabi' al-sani",
    5: "Jumada al-awwal", 6: "Jumada al-thani", 7: "Rajab", 8: "Sha'ban",
    9: "Ramadan", 10: "Shawwal", 11: "Dhu al-Qi'dah", 12: "Dhu al-Hijjah"
}
islamic_day=""
islamic_month=""

from hijri_converter import Hijri, Gregorian

def calculate_islamic_date():
   current_date = datetime.now()
   h = Gregorian(current_date.year, current_date.month, current_date.day).to_hijri()
  
   islamic_month = islamic_month_names[h.month]
   islamic_year = h.year
   islamic_day=h.day
   return f"{h.day} {islamic_month} {islamic_year} "
# Test the function

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
    elif nmaz_index=="3" and islamic_month=="Ramadan":
        subprocess(["python","ramadan_day_calculator.py"])
        window.destroy()
    elif nmaz_index=="4" and islamic_month=="Ramadan":
        subprocess(["python","taraweeh.py"])
        window.destroy()

    else:
        return False

def update_jamat_left_timer():
    # Get the current time in seconds, ensuring it's within the same day
    current_time = datetime.now().time()
    current_time_seconds = (current_time.hour * 3600 + current_time.minute * 60 + current_time.second) % 86400

    # Convert prayer timings to seconds for easier comparison
    prayer_timings_seconds = []
    for i, t in enumerate(start_list):
         hour, minute = map(int, t.split(':'))
    # Convert 12-hour format to 24-hour format for Zuhr, Asr, Maghrib, and Isha
         if i in [1, 2, 3, 4]:  # Check if the current prayer is Zuhr, Asr, Maghrib, or Isha
            # if i == 1 and hour != 12:  # Check if it's Zuhr (index 1) and hour is not already 12
            if i == 1 and hour > 12:  # Check if it's Zuhr (index 1) and hour is not already 12
                hour += 12  # Add 12 hours to convert to 24-hour format
            elif hour == 12:
                hour = 12  # Keep the hour as 12 (no need to add additional 12 hours)
            elif hour > 12:
                hour = hour  # Keep the hour as 12 (no need to add additional 12 hours)
            elif hour < 12:
                hour += 12  # Keep the hour as 12 (no need to add additional 12 hours)
                # hour += 12  # Add 12 hours to convert to 24-hour format
            prayer_timings_seconds.append(hour * 3600 + minute * 60)
         else:
            prayer_timings_seconds.append(hour * 3600 + minute * 60)


    # Find the index of the next upcoming prayer
    next_prayer_index = next((i for i, t in enumerate(prayer_timings_seconds) if t > current_time_seconds), None)
    
    if next_prayer_index is not None:
        # Get the timing of the next prayer
        next_prayer_time_seconds = prayer_timings_seconds[next_prayer_index]
        
        # Calculate the time left until the next prayer
        time_left_seconds = next_prayer_time_seconds - current_time_seconds

        # Check if the time left is less than or equal to 0

      
        if time_left_seconds <= 0:
            time_left_seconds += 24 * 3600  # Add 24 hours in seconds
      
        elif time_left_seconds == 1:
            # Show the "phone off" image
            # beepnow()
            nmaz_index=str(next_prayer_index)
            next_prayertime=str(start_list[next_prayer_index])
            # subprocess.run(["python", "current_nmaz_time.py",nmaz_index,next_prayertime,str(sys.argv[3])])
            subprocess.run(["python", "current_nmaz_time.py",str(nmaz_index),next_prayertime,str(sys.argv[3])])
            # subprocess.run(["python", "phone_off.py",nmaz_index,next_prayertime])
            window.destroy()
         
            # phone_off_label.place(x=100, y=100)  # Adjust the coordinates as per your UI layout
  
        # Check if the time left is less than or equal to 10 minutes
        elif time_left_seconds  <= 180:  # 600 seconds = 10 minutes
            # Convert time left to hours, minutes, and seconds
            hours_left = time_left_seconds // 3600
            minutes_left = (time_left_seconds % 3600) // 60
            seconds_left = time_left_seconds % 60

            # Format the time left string
            time_left_str = f"{minutes_left:02d}:{seconds_left:02d}"

            
            timer1.config(text=f"{time_left_str}")
        else:
            # If more than 3 minutes left, hide the timer label
            timer1.config(text="")
    
    # Schedule the function to run again after 1 second
    window.after(1000, update_jamat_left_timer)

update_jamat_left_timer()

if today_weekday==4 and nmaz_index==2:
    reset_screen(nmaz_index,nmaz_index,str(sys.argv[3]))


# Function to update the current prayer time and name
def update_prayer_info():

    if nmaz_index=="0":
        prayer_label.config(text="صلاة الفجر " )
        prayer_label2.config(text="Fajr Prayer " )
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
prayer_label.place(relx=0.4, rely=0.12)

# Create a label to display current prayer name and time
prayer_label2 = Label(window,font=("Arial",25))
# Place the label just after the "Silent your phone" label
prayer_label2.place(relx=0.4, rely=0.05)

# Create a label to display current prayer name and time
# prayer__time_label = Label(window,font=("Arial",25),text=nmaz_time)
# # Place the label just after the "Silent your phone" label
# prayer__time_label.place(relx=0.4, rely=0.9)



# Simulate the passage of time
time_left_seconds = 10 * 60  # 10 minutes in seconds
def switch_to_main():
    if islamic_day_check()==False:
        subprocess.run(["python", "current_nmaz_time.py",str(screen_timeout)])
        window.destroy()

        
# Schedule the function to switch back to main.py after 2 minutes (120 seconds)
window.after(screen_timeout, switch_to_main)
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
