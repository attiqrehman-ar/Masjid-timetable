import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import os
import time
from datetime import datetime
import pytz
from hijri_converter import Hijri, Gregorian

# Percentage of the window's height that the image should cover
IMAGE_HEIGHT_PERCENTAGE = 1  # Adjust this value as needed
DEFAULT_IMAGE_FILENAME = "default_image.png"

def upload_image():
    # Open file dialog to select an image file
    filepath = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.gif")])
    if filepath:
        # Open the selected image
        img = Image.open(filepath)
        # Calculate the desired image height based on the percentage of the window's height
        target_height = int(window.winfo_screenheight() * IMAGE_HEIGHT_PERCENTAGE)
        # Resize the image to fit the window width and the calculated height
        img_resized = img.resize((window.winfo_screenwidth(), target_height))
        # Save the resized image to the "images" folder
        img_resized.save("images/" + os.path.basename(filepath))
        # Remove the existing default image if it exists
        if os.path.exists("images/" + DEFAULT_IMAGE_FILENAME):
            os.remove("images/" + DEFAULT_IMAGE_FILENAME)
        # Rename the uploaded image as the default image
        os.rename("images/" + os.path.basename(filepath), "images/" + DEFAULT_IMAGE_FILENAME)
        img_resized = ImageTk.PhotoImage(img_resized)
        background_label.config(image=img_resized)
        background_label.image = img_resized
        background_label.image_path = filepath

# Create the main window
window = tk.Tk()
window.title("Masjid Timetable")

# Function to update the background image when the window is resized
def update_background(event):
    if hasattr(background_label, "image_path"):  # Check if original image exists
        img = Image.open(background_label.image_path)
        img = img.resize((window.winfo_screenwidth(), int(window.winfo_screenheight() * IMAGE_HEIGHT_PERCENTAGE)))
        img = ImageTk.PhotoImage(img)
        background_label.config(image=img)
        background_label.image = img

# Bind the window resize event to the update_background function
window.bind("<Configure>", update_background)

# Create a label to display the background image
background_label = tk.Label(window)
background_label.pack(fill="both", expand=True)

# Check if the default image exists and display it
if os.path.exists("images/" + DEFAULT_IMAGE_FILENAME):
    default_img = Image.open("images/" + DEFAULT_IMAGE_FILENAME)
    default_img_resized = default_img.resize((window.winfo_screenwidth(), int(window.winfo_screenheight() * IMAGE_HEIGHT_PERCENTAGE)))
    default_img_resized = ImageTk.PhotoImage(default_img_resized)
    background_label.config(image=default_img_resized)
    background_label.image = default_img_resized

# Create a button to upload an image
upload_button = tk.Button(window, text="Upload Image",
                           command=upload_image, bg="#98FB98", font=("Arial", 12))  # Light green color, font size 12

upload_button.pack(side="bottom", pady=10)
upload_button.place(relx=0.16, rely=1.0, anchor="s")

# Create a label for the timer
timer_label = tk.Label(window, text="", font=("Arial", 35), highlightthickness=0,bg="#040720")
timer_label.place(relx=0.15, rely=0.37, anchor="center")  # Centered horizontally, 10% from the top


# Calculate Islamic month name and Hijri year
from datetime import datetime 
islamic_month_names = {
    1: "Muharram", 2: "Safar", 3: "Rabi' al-awwal", 4: "Rabi' al-sani",
    5: "Jumada al-awwal", 6: "Jumada al-thani", 7: "Rajab", 8: "Sha'ban",
    9: "Ramadan", 10: "Shawwal", 11: "Dhu al-Qi'dah", 12: "Dhu al-Hijjah"
}

islamic_day=""
islamic_month=""

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

# Create a label for the Islamic date and month
islamic_date_label = tk.Label(window, text="", font=("Arial", 18),bg="#040720", highlightthickness=0)
islamic_date_label.place(relx=0.22, rely=0.54, anchor="e")  # Aligned to the right, 13% from the top

# Update the Islamic date and month label every hour
def update_islamic_date():
    islamic_date = calculate_islamic_date()
    islamic_date_label.config(text=islamic_date)
    window.after(3600000, update_islamic_date)  # Schedule the function to run again after 1 hour (3600000 milliseconds)

update_islamic_date()  # Start updating the Islamic date and month

import calendar

# Function to get the current Gregorian date
def get_gregorian_date():
    current_date = datetime.now()
    day_name = calendar.day_name[current_date.weekday()]
    abbreviated_day_name = day_name[:3]  # Extract the first three letters
    return f"{abbreviated_day_name}, {current_date.strftime('%d %B %Y')}"

# Function to update the date label
def update_date_label():
    current_date = get_gregorian_date()
    date_label.config(text=current_date)
    window.after(60000, update_date_label)  # Update every minute

# Create a label to display the current date
date_label = tk.Label(window, text="", font=("Arial", 18) ,highlightthickness=0)
date_label.place(relx=0.07, rely=0.44, anchor="nw")

# Update the date label initially and start the update loop
update_date_label()

from tkinter import ttk  # Import ttk module


# Define the lists
prayer_list = ["الفجر Fajr", "الظهر Dhuhr", "العصر Asr", "المغرب Maghrib", "العشاء Isha"]
# beginning_list = ["5:00 AM", "12:00 PM", "3:30 PM", "6:00 PM", "8:00 PM"]
# start_list = ["5:15 AM", "12:15 PM", "3:45 PM", "6:15 PM", "8:15 PM"]
beginning_list = []
start_list = []

import csv

# Assuming the CSV file is named "prayer_timings.csv" and located in the same directory as this script
csv_file = "prayer_timings.csv"

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

# Define the initial position of the labels
label_position_x = 0.5  # 40% from the left
label_position_y = 0.21  # 18% from the top

# Define the vertical spacing between labels
vertical_spacing = 0.09  # Adjust this value as needed

# Define the horizontal spacing between labels
horizontal_spacing = 0.05  # Adjust this value as needed

# Create labels for headers
prayer_header_label = tk.Label(window, text="PRAYER", font=("Arial", 25))
prayer_header_label.place(relx=label_position_x, rely=label_position_y - vertical_spacing, anchor="ne")

beginning_header_label = tk.Label(window, text="BEGINNING", font=("Arial", 25))
beginning_header_label.place(relx=label_position_x + horizontal_spacing, rely=label_position_y - vertical_spacing, anchor="nw")

start_header_label = tk.Label(window, text="JAMAT", font=("Arial", 25))
start_header_label.place(relx=label_position_x + 0.25, rely=label_position_y - vertical_spacing, anchor="nw")
# Create labels to display the prayer timings if the lengths of beginning_list and start_list match the length of prayer_list
# Initialize lists to hold the labels for prayers, beginnings, and starts
prayers_labels = []
beginning_labels = []
start_labels = []
import sys
screen_timeout=1*60*1000
high_ligther="green"
interval=1 

try: 
    # Retrieve command-line arguments (screen timeout and background color)
   if int(sys.argv[1]):
         screen_timeout = int(sys.argv[1]) *60 *1000# Convert to integer

   if sys.argv[2]:
         high_ligther = sys.argv[2]
   if sys.argv[3]:
         interval = int(sys.argv[2])
except:
    # screen_timeout = int(sys.argv[1])  # Convert to integer
    #  ("screen:",screen_timeout)
    pass
    # pass
if len(beginning_list) == len(start_list) == len(prayer_list):
    for i in range(len(prayer_list)):
        # Create labels for prayers
        
        prayer_label = tk.Label(window, text=f"{prayer_list[i]}", font=("Arial", 25),bg="black")
        prayer_label.place(relx=label_position_x, rely=label_position_y + i * vertical_spacing, anchor="ne")
        prayers_labels.append(prayer_label)

        # Create labels for beginnings
        beginning_label = tk.Label(window, text=f" {beginning_list[i]}", font=("Arial", 25))
        beginning_label.place(relx=label_position_x + horizontal_spacing, rely=label_position_y + i * vertical_spacing, anchor="nw")
        beginning_labels.append(beginning_label)

        # Create labels for starts
        start_label = tk.Label(window, text=f" {start_list[i]}", font=("Arial", 25))
        start_label.place(relx=label_position_x + 0.25, rely=label_position_y + i * vertical_spacing, anchor="nw")
        start_labels.append(start_label)
else:
    pass
# Define the positions for the labels at the bottom
bottom_label_position_x = 0.5  # 50% from the left
bottom_label_position_y = 0.90  # 5% from the bottom
bottom_label_spacing = 1  # Adjust this value as needed

# Create labels for "1st Juma," "2nd Juma," "Zawal," and "Sunrise"
juma1_label1 = tk.Label(window, text=" الجمعة الأولى ", font=("Arial", 16),bg="#051539",fg="white")
juma1_label1.place(relx=0.06, rely=0.8, anchor="s")
juma1_label = tk.Label(window, text=" 1st Juma ", font=("Arial", 16))
juma1_label.place(relx=0.06, rely=0.84, anchor="s")

juma2_label2 = tk.Label(window, text="الجمعة الثانية", font=("Arial", 16),bg="#051539",fg="white")
juma2_label2.place(relx=0.19, rely=0.8, anchor="s")
juma2_label = tk.Label(window, text="2nd Juma", font=("Arial", 16))
juma2_label.place(relx=0.19, rely=0.84, anchor="s")

zawal_label1 = tk.Label(window, text="الزوال", font=("Arial", 22),bg="#051539",fg="white")
zawal_label1.place(relx=0.05, rely=0.63, anchor="s")

zawal_label = tk.Label(window, text="Zawal", font=("Arial", 19))
zawal_label.place(relx=0.05, rely=0.678, anchor="s")

sunrise_label1 = tk.Label(window, text="الشروق", font=("Arial", 16),bg="#051539",fg="white")
sunrise_label1.place(relx=0.19, rely=0.63, anchor="s")
sunrise_label = tk.Label(window, text="Sunrise ", font=("Arial", 16),fg="green")
sunrise_label.place(relx=0.19, rely=0.674, anchor="s")

imsak_label = tk.Label(window, text="Imsak إمساك", font=("Arial", 16))
# imsak_label.place(relx=0.91, rely=bottom_label_position_y, anchor="s")

# Calculate Zawal time
# Get the Zuhr beginning time from the beginning list

zuhr_beginning_time = beginning_list[1]
zuhr_hour, zuhr_minute = map(int, zuhr_beginning_time.split(':'))
zawal_hour = zuhr_hour
zawal_minute = zuhr_minute - 10

if zawal_minute < 0:
    zawal_minute += 60
    zawal_hour -= 1
    if zawal_hour < 0:
        zawal_hour += 24
    elif zawal_hour == 0:
        zawal_hour =12
zawal_time = f"{zawal_hour:02d}:{zawal_minute:02d}"
zawal_time_label = tk.Label(window, text=zawal_time, font=("Arial", 18))
# zawal_time_label.place(relx=0.65, rely=bottom_label_position_y + 0.05, anchor="s")
zawal_time_label.place(relx=0.05, rely=0.72, anchor="s")


# Function to check if today is Friday and the time is between 13:00 and 13:45
def is_friday_and_time_between_1300_1345():
    # Get the current date and time
    now = datetime.now()

    # Check if today is Friday (weekday() returns 4 for Friday)
    if now.weekday() == 4:
        # Check if the time is between 13:00 and 13:45
        if datetime.time(13, 0) <= now.time() <= datetime.time(13, 45):
            window.destroy()
            subprocess(["python","posters.py",interval,screen_timeout])
    window.after(1000,is_friday_and_time_between_1300_1345)


def open_settings():
    # Open the settings page when the button is clicked
    subprocess.run(["python", "settings.py"])


# Create a button for settings
settings_button = ttk.Button(window, text="Settings", command=open_settings)
settings_button.place(relx=0.85, rely=0.98, anchor=tk.SE)

is_friday_and_time_between_1300_1345()
# Calculate Sunrise time
# sunrise_time = "06:30"  # Example time
sunrise_time_label = tk.Label(window, text=sunrise_time, font=("Arial", 18))
sunrise_time_label.place(relx=0.19, rely=0.71, anchor="s")

fajar_start_time = start_list[0]
imsak_hour, imsak_minute = map(int, fajar_start_time.split(':'))
imsak_hour = imsak_hour
imsak_minute = imsak_minute - 10
if imsak_minute < 0:
    imsak_minute += 60
    imsak_hour -= 1
    if imsak_hour < 0:
        imsak_hour += 24
imsk_time = f"{imsak_hour:02d}:{imsak_minute:02d}"

imsak_time_label = tk.Label(window, text=imsk_time, font=("Arial", 18))
# imsak_time_label.place(relx=0.91, rely=0.94, anchor="s")

# Get the Jumu'ah beginning time from the beginning list (assuming it's the third prayer)
jumuah_beginning_time = beginning_list[1]
jumuah_time_label = tk.Label(window, text=jumuah_beginning_time, font=("Arial", 18))
jumuah_time_label.place(relx=0.05, rely=0.88, anchor="s")

jumuah_time_label2 = tk.Label(window, text=jumuah_beginning_time, font=("Arial", 18))
jumuah_time_label2.place(relx=0.18, rely=0.9, anchor="s")

# Define the position for the timer
timer_position_x = 0.1  # 50% from the left
timer_position_y = 0.45  # 15% from the top

# Create a label for the timer
left_timer_label = tk.Label(window, text="", font=("Arial", 18))
left_timer_label.place(relx=0.55, rely=0.19, anchor="n")

import winsound

from tkinter import Label, PhotoImage

# Load the "phone off" image
phone_off_image = PhotoImage(file="phone_off.png")  # Replace "phone_off.png" with the actual path to your image file

# Create a label widget to display the "phone off" image
phone_off_label = Label(window, image=phone_off_image)

time_left_sec = 1
import time

def hide_phone():
    phone_off_label.place_forget()

import subprocess

current_nmaz=""
begin_time=1
start_time=1

def update_left_timer():
    # Get the current time in seconds, ensuring it's within the same day
    current_time = datetime.now().time()
    current_time_seconds = (current_time.hour * 3600 + current_time.minute * 60 + current_time.second) % 86400

    # Convert prayer timings to seconds for easier comparison
    prayer_timings_seconds = []
    for i, t in enumerate(beginning_list):
         hour, minute = map(int, t.split(':'))
    # Convert 12-hour format to 24-hour format for Zuhr, Asr, Maghrib, and Isha
         if i in [1, 2, 3, 4]:  # Check if the current prayer is Zuhr, Asr, Maghrib, or Isha
            if i == 1 and hour <= 12:  # Check if it's Zuhr (index 1) and hour is not already 12
            # if i == 1 and hour != 12:  # Check if it's Zuhr (index 1) and hour is not already 12
                hour += 12  # Add 12 hours to convert to 24-hour format
            elif hour == 12:
                hour = 12  # Keep the hour as 12 (no need to add additional 12 hours)
            elif hour > 12:
                hour = hour  # Keep the hour as 12 (no need to add additional 12 hours)
            elif hour < 12:
                hour += 12 
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
            # next_jmat(next_prayer_index)
        elif time_left_seconds == 1:
            # Show the "phone off" image
            begin_time=0
            beepnow()
            subprocess.run(["python", "azan_dua.py"])
            window.destroy()

        else:
            # Hide the "phone off" image
            update_jamat_left_timer()
            # pass

        # Check if the time left is less than or equal to 10 minutes
        if time_left_seconds <= 120 :  # 600 seconds = 10 minutes
            # Convert time left to hours, minutes, and seconds
            hours_left = time_left_seconds // 3600
            minutes_left = (time_left_seconds % 3600) // 60
            seconds_left = time_left_seconds % 60

            # Format the time left string
            time_left_str = f"{minutes_left:02d}:{seconds_left:02d}"

            # Update the timer label with the time left until the next prayer
            if next_prayer_index == 0:
                left_timer_label.config(text=f"Fajr in: {time_left_str}")
            elif next_prayer_index == 1:
                left_timer_label.config(text=f"Zohar in: {time_left_str}")
            elif next_prayer_index == 2:
                left_timer_label.config(text=f"Asr in: {time_left_str}")
            elif next_prayer_index == 3:
                left_timer_label.config(text=f"Magrib in: {time_left_str}")
            else:
                left_timer_label.config(text=f"Isha in: {time_left_str}")
        # else:
        #     # If more than 3 minutes left, hide the timer label
        #     left_timer_label.config(text="")
        
        # Highlight the current prayer in green
        for i in range(len(start_list)):
            if i == next_prayer_index and next_prayer_index>0:
                prayers_labels[i-1].config(fg="green")  # Change the text color to green for the current prayer
                start_labels[i-1].config(fg="green")  # Change the text color to green for the current prayer
                beginning_labels[i-1].config(fg="green")  # Change the text color to green for the current prayer
                prayers_labels[i-1].config(bg="#fef9f2")  # Change the text color to green for the current prayer
                beginning_labels[i-1].config(bg="#fef9f2")  # Change the text color to green for the current prayer
                start_labels[i-1].config(bg="#fef9f2")  # Change the text color to green for the current prayer
            elif i == next_prayer_index and next_prayer_index==0:
                prayers_labels[i].config(fg=high_ligther)  # Change the text color to green for the current prayer
                start_labels[i].config(fg=high_ligther)  # Change the text color to green for the current prayer
                beginning_labels[i].config(fg=high_ligther)  # Change the text color to green for the current prayer
                # prayers_labels[i].config(bg="systemTransparent")  # Change the text color to green for the current prayer

           
    
    # Schedule the function to run again after 1 second
    window.after(1000, update_left_timer)

from datetime import datetime, timedelta

# Get today's date
today = datetime.today().date()

# Calculate the number of days until the next Friday (assuming today is not Friday)
days_until_friday = (4 - today.weekday()) % 7
# Add the number of days until Friday to today's date
next_friday = today + timedelta(days=days_until_friday)

next_friday_coming = next_friday.strftime("%d-%b")

# Get the day of the month
# day_of_month = next_friday.strftime("%d")


# Calculate the next Friday from the coming Friday
next_friday_after = next_friday + timedelta(days=(12 - next_friday.weekday()))
# Format the next Friday after coming Friday
next_friday_after_formatted = next_friday_after.strftime("%d-%b")
coming_friday_time=""
next_coming_friday_time=""
# Open the CSV file

with open('prayer_timings.csv', 'r') as file:
    # Create a CSV reader object
    reader = csv.DictReader(file)
    
    # Iterate over each row in the CSV file
    for row in reader:
        # Check if the row's 'Date' column matches next Friday's date
        if row['Date'] == str(next_friday_coming):
            # Print the value of the 'DHUHR start' column
            coming_friday_time=row['DHUHR start']
            break  # Exit the loop after finding the matching row

 # Iterate over each row in the CSV file
    for row in reader:
        if row['Date'] == str(next_friday_after_formatted):
             next_coming_friday_time=row['DHUHR start']
             break  # Exit the loop after finding the matching row
        
jumuah_time_label.config(text=coming_friday_time)
# Start the Tkinter event loop


jumuah_time_label2.config(text="1:14")

todaydat = datetime.now().date()

# Calculate tomorrow's date
tomorrows = todaydat + timedelta(days=1)
formatted_tomorrow_date = tomorrows.strftime("%d-%b")


differing_times=[]
differing_index=[]
with open(csv_file, newline='') as file:
    reader = csv.DictReader(file)
    # Initialize the index counter
    i = 0
    # Iterate over each row in the CSV file
    for row in reader:
        # Check if the row date matches the formatted tomorrow's date
        if row["Date"] == formatted_tomorrow_date:
            # Iterate over the start times in the row
            for column_name in ["FAJR prayer", "DHUHR prayer", "ASR prayer", "M/RIB prayer", "ISHA prayer"]:
                # Get the start time from the row
                row_start_time = row[column_name]
                # Get the corresponding start time from the start_list
                list_start_time = start_list[i]
                # Compare the start times
                if row_start_time != list_start_time:
                    # If the start times differ, store the index i
                    differing_index.append(i)
                    differing_times.append(row_start_time)
                # Increment the index counter
                else:
                    differing_times.append(-1)
                    differing_index.append(-1)

                i += 1

import threading

current_prayer_index=0

# Function to execute witr_dua.py after 3 minutes
def execute_witr_dua():
    # Execute witr_dua.py
    subprocess.run(["python", "witr_dua.py"])
counter=0
nmaz_index=0
# Function to check if the current prayer is Isha and start the timer
def check_and_execute():
    # current_prayer_index = 4  # Assuming Isha is at index 4 in the start_list
    try:
        if sys.argv[1] == "4":  # Check if the current prayer is Isha
        # if sys.argv[1] == "4" and counter==0:  # Check if the current prayer is Isha
        # Start a timer for 3 minutes
            counter =1
            # threading.Timer(180.0, execute_witr_dua).start()  # 180 seconds = 3 minutes
            execute_witr_dua()  # 180 seconds = 3 minutes
    except:
        return
# Call the function to check and execute
check_and_execute()

# Define a flag to control the execution of next_jmat
stop_flag = threading.Event()

left_timer_label.config(fg="green")
def next_jmat(index):
    if not stop_flag.is_set():
        # Iterate over differing_index to find the matching index
        for diff in differing_index:
            if diff == index:  # Check if the current differing_index matches the index
                # Convert index to integer to handle comparisons properly
                index = int(index)
                if index == 1:
                    left_timer_label.config(text=f"Dhuhar Jamat for tomorrow is: {differing_times[diff-2]}")
                elif index == 2:
                    left_timer_label.config(text=f"Asr Jamat for tomorrow is: {differing_times[diff-2]}")
                elif index == 3:
                    left_timer_label.config(text=f"Magrib Jamat for tomorrow is: {differing_times[diff-2]}")
                elif index == 4:
                    left_timer_label.config(text=f"Isha Jamat time change tomorrow: {differing_times[diff-2]}")
                break  # Exit the loop after finding the matching index
                
        # Set the stop flag after 1 minute (60 seconds)
        threading.Timer(180,stop).start()

def stop():
    stop_flag.set()
    left_timer_label.config(text="")

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
            beepnow()
            # next_jmat(next_prayer_index)
            nmaz_index=str(next_prayer_index)
            next_prayertime=str(start_list[next_prayer_index])
            subprocess.run(["python", "donation.py",nmaz_index,next_prayertime, start_list[next_prayer_index],screen_timeout])
            # subprocess.run(["python", "phone_off.py",nmaz_index,next_prayertime])
            # window.destroy()
        elif time_left_seconds <= 180:
            nmaz_index=str(next_prayer_index)
            next_prayertime=str(start_list[next_prayer_index])
            # next_jmat(next_prayer_index)
            subprocess.run(["python", "donation.py",nmaz_index,next_prayertime, start_list[next_prayer_index],str(screen_timeout)])
            # window.destroy()     
            # phone_off_label.place(x=100, y=100)  # Adjust the coordinates as per your UI layout

        # elif time_left_seconds <= 240 and islamic_day_check() and time_left_seconds >= 120:
            # nmaz_index=str(next_prayer_index)
            # next_prayertime=str(start_list[next_prayer_index])
            # next_jmat(next_prayer_index)
            # subprocess.run(["python", "donation.py",nmaz_index,next_prayertime, start_list[next_prayer_index]])
            # window.destroy()     
            # phone_off_label.place(x=100, y=100)  # Adjust the coordinates as per your UI layout

        # else:
            # Hide the "phone off" image
            # print("Time left:",time_left_seconds)    
       
    # Schedule the function to run again after 1 second
    window.after(1000, update_jamat_left_timer)

update_jamat_left_timer()
update_left_timer()



current_time2 = datetime.now().strftime("%H:%M")

# Define the sunrise time

def sunrize_zawal_show():
# Check if the current time is equal to the sunrise time
    current_time2 = datetime.now().strftime("%H:%M")


    # Convert times to datetime objects
    sunrise_time_obj = datetime.strptime(sunrise_time, "%H:%M")
    current_time2_obj = datetime.strptime(current_time2, "%H:%M")

    # Format times with leading zeros using strftime
    current_time2_formatted = datetime.strptime(current_time2, "%H:%M")
    sunrise_time_formatted = datetime.strptime(sunrise_time, "%H:%M")
    zawal_time_formatted = datetime.strptime(zawal_time, "%H:%M")

    # Calculate the difference between current_time2 and sunrise_time
    time_difference = sunrise_time_formatted - current_time2_formatted
    time_difference2 = zawal_time_formatted - current_time2_formatted

# Check if current_time2 is less than sunrise_time and the time difference is less than 2 minutes
    if current_time2_formatted <= sunrise_time_formatted and time_difference < timedelta(minutes=2):
             subprocess.run(["python", "sunrize_zawal.py","Sunrize",str(sunrise_time)])
        # window.destroy()
    elif current_time2_formatted <= zawal_time_formatted and time_difference2 < timedelta(minutes=2):
        subprocess.run(["python", "sunrize_zawal.py","Zawal",str(zawal_time)])
        # window.destroy()    
    window.after(1000, sunrize_zawal_show)

today_date = datetime.now().date()
current_time = datetime.now().time()

# Check if today is Friday (weekday 4)
if today_date.weekday() == 4:
    # Define the start and end times for the specified range
    start_time = datetime.strptime("13:00", "%H:%M").time()
    end_time = datetime.strptime("13:45", "%H:%M").time()

    # Check if the current time is within the specified range
    if start_time <= current_time <= end_time:
        # If yes, show posters.py file
        import subprocess
        subprocess.run(["python", "posters.py"])

sunrize_zawal_show()
def beepnow():
    if begin_time==0:
        update_jamat_left_timer()
    winsound.Beep(1200, 1500)  # Beep at 1000 Hz for 1000 milliseconds (1 second)




color_string="white"
newfg=high_ligther
color_fg="black" 
new_color="#051539"

prayer_header_label.config(bg="#101d3f",fg="white")  # Change the text color to green for the current prayer
start_header_label.config(bg="#101d3f",fg="white")  # Change the text color to green for the current prayer
beginning_header_label.config(bg="#101d3f",fg="white")  # Change the text color to green for the current prayer
# time_left_sec.config(bg="black",fg="white")  # Change the text color to green for the current prayer
timer_label.config(bg=new_color,fg=color_fg)  # Change the text color to green for the current prayer
zawal_label.config(bg=new_color,fg=newfg)  # Change the text color to green for the current prayer
zawal_time_label.config(bg=new_color,fg=color_string)  # Change the text color to green for the current prayer
sunrise_label.config(bg=new_color,fg=newfg)  # Change the text color to green for the current prayer
sunrise_time_label.config(bg=new_color,fg=color_string)  # Change the text color to green for the current prayer
juma1_label.config(bg=new_color,fg=newfg)  # Change the text color to green for the current prayer
juma2_label.config(bg=new_color,fg=newfg)  # Change the text color to green for the current prayer
jumuah_time_label.config(bg=new_color,fg=color_string)  # Change the text color to green for the current prayer
jumuah_time_label2.config(bg=new_color,fg=color_string)  # Change the text color to green for the current prayer
imsak_label.config(bg=new_color,fg=color_string)  # Change the text color to green for the current prayer
imsak_time_label.config(bg=new_color,fg=color_string)  # Change the text color to green for the current prayer
date_label.config(bg=new_color,fg="white")  # Change the text color to green for the current prayer
islamic_date_label.config(bg=new_color,fg="white")  # Change the text color to green for the current prayer

update_jamat_left_timer()
import sys

try:
    if sys.argv[1]:
        next_jmat(sys.argv[2])
except:
    pass

# Update the timer label every second
def update_timer():
    # current_time_24hr = time.strftime("%H:%M:%S") #24 hour formate
    current_time = time.strftime("%H:%M:%S")
    # current_time = time.strftime("%I:%M:%S %p", time.strptime(current_time_24hr, "%H:%M:%S"))

    timer_label.config(text=current_time)
    update_jamat_left_timer()
    window.after(1000, update_timer)  # Schedule the function to run again after 1000ms (1 second)

update_timer()  # Start the timer


from datetime import datetime

# Get today's day of the week (0 = Monday, 1 = Tuesday, ..., 6 = Sunday)
today_weekday = datetime.now().weekday()

# Check if today is Thursday (index 3 represents Thursday)

# Assuming start_list[1] contains the Dhuhar start time in 12-hour format like "10:30 AM"
# Convert it to 24-hour format
if today_weekday == 4:
    start_time_str = start_list[1]
    start_time_obj = datetime.strptime(start_time_str, "%I:%M")
    hour = start_time_obj.hour
    if hour != 12 and hour < 12:
        hour += 12
        start_time_obj = start_time_obj.replace(hour=hour)
    start_list[1] = start_time_obj.strftime("%H:%M")  # Convert datetime object to 24-hour format string

# Get the current time
current_time = datetime.now().time()

# Check if today is Thursday (index 3 represents Thursday) and the current time has passed the start time of Jumu'ah prayer
# Or if today is Friday (index 4 represents Friday) and the current time has not passed the start time of Jumu'ah prayer
if (today_weekday == 3 and current_time >= datetime.strptime(start_list[1], "%H:%M").time()) or (today_weekday == 4 and current_time <= datetime.strptime(start_list[1], "%H:%M").time()):
        # Update the corresponding label to display "Juma"
        prayers_labels[1].config(text="الجمعة Juma")
else:    # Update the corresponding label to display "Juma"
        # prayers_labels[1].config(text="Dhuhar")
        pass

for lab in prayers_labels:
    lab.config(fg="black", bg="white")
for lab in start_labels:
    lab.config(fg="black", bg="white")
for lab in beginning_labels:
    lab.config(fg="black", bg="white")

# else:
#     prayers_labels[1].config(text="الظهر Dhuhar")
# window.configure(bg="white")  # Change "white" to your window's background color
# window.wm_attributes("-transparentcofolor", 'green')

# Create a canvas to display the background image
canvas = tk.Canvas(window, width=window.winfo_screenwidth(), height=window.winfo_screenheight())
canvas.pack(fill="both", expand=True)

# Load and display the default image
if os.path.exists("images/" + DEFAULT_IMAGE_FILENAME):
    default_img = Image.open("images/" + DEFAULT_IMAGE_FILENAME)
    default_img_resized = default_img.resize((window.winfo_screenwidth(), int(window.winfo_screenheight() * IMAGE_HEIGHT_PERCENTAGE)))
    default_img_resized = ImageTk.PhotoImage(default_img_resized)
    background_image = canvas.create_image(0, 0, anchor="nw", image=default_img_resized)
    canvas.image = default_img_resized

import schedule
import time
 
def check_dates():
    # Get today's date and date after 5 days
    today_date = datetime.now().strftime("%d-%b")
    date_after_5_days = (datetime.now() + timedelta(days=5)).strftime("%d-%b")

    # Read the latest.csv file and check if the dates exist
    date_exists = False
    with open("latest.csv", newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["Date"] in [ date_after_5_days]:
                date_exists = True
                break
    # Print result
    if date_exists:
     
        pass
    else:
        left_timer_label.config(text="Please upload data in timetable sheet with in 4 days")

check_dates()
# Schedule the task to run daily at a specific time
# schedule.every().day.at("08:00").do(check_dates)

# Infinite loop to keep the script running
# while True:
#     schedule.run_pending()
#     time.sleep(60)  # Check every minute

# prayers_labels[2].config(bg="white", fg="black")  # Change the text color to green for the current prayer
# Get the background color of the window
window_bg_color = window.cget("background")

timer_label.config(fg="white",bg="#051539")

# Change the background of labels to match the window background color
# for label in prayers_labels:
#     label.config(bg=window_bg_color)

window.mainloop()
