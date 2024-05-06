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

arabic_label0 = Label(window, text="",bg="#ccddc1" , fg="black", font=("Arial",26))
# Place the label just after the image
arabic_label0.place(relx=0.34, rely=0.14)

arabic_label1 = Label(window , text="",bg="#ccddc1", fg="black", font=("Arial",30))
# Place the label just after the image
arabic_label1.place(relx=0.2, rely=0.36)

arabic_label2 = Label(window , text="",bg="#ccddc1", fg="green", font=("Arial",56))
# Place the label just after the image
arabic_label2.place(relx=0.4, rely=0.46)


from datetime import datetime, timedelta

# Get today's date
today = datetime.today().date()

# Calculate the number of days until the next Friday (assuming today is not Friday)
days_until_friday = (4 - today.weekday()) % 7
# Add the number of days until Friday to today's date
next_friday = today + timedelta(days=days_until_friday)

next_friday_coming = next_friday.strftime("%d-%b")

# Calculate the next Friday from the coming Friday
next_friday_after = next_friday + timedelta(days=(12 - next_friday.weekday()))
# Format the next Friday after coming Friday
next_friday_after_formatted = next_friday_after.strftime("%d-%b")

coming_friday_time=""
next_coming_friday_time=""

import csv

with open('prayer_timings.csv', 'r') as file:
    # Create a CSV reader object
    reader = csv.DictReader(file)
    
    # Iterate over each row in the CSV file
    for row in reader:
        # Check if the row's 'Date' column matches next Friday's date
        if row['Date'] == str(next_friday_coming):
            # Print the value of the 'DHUHR start' column
            coming_friday_time=row['DHUHR start']
            print("DHUHR start on next Friday:", row['DHUHR start'])
            pass  # Exit the loop after finding the matching row
        if row['Date'] == str(next_friday_after_formatted):
             next_coming_friday_time=row['DHUHR start']
             print("DHUHR start on next Friday:", row['DHUHR start'])
             break  # Exit the loop after finding the matching row
        
todaydat = datetime.now().date()

# Calculate tomorrow's date
tomorrows = todaydat + timedelta(days=1)
formatted_tomorrow_date = tomorrows.strftime("%d-%b")


beginning_list = []
start_list = []

import csv

# Assuming the CSV file is named "prayer_timings.csv" and located in the same directory as this script
# csv_file = "prayer_timings.csv"
csv_file = "latest.csv"

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
import sys 
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


# Function to update the screen after 10 minutes
def reset_screen():
    subprocess.run(["python", "main.py",screen_timeout])
    window.destroy()


if all(time == -1 for time in differing_times):
    reset_screen()

def next_jmat(index):
        # Iterate over differing_index to find the matching index
        for diff in differing_index:
            if diff == index:  # Check if the current differing_index matches the index
                # Convert index to integer to handle comparisons properly
                index = int(index)
                if index == 0:
                    arabic_label0.config(text=f"جماعة الفجر تتغير غدا")
                    arabic_label1.config(text=f"Dhuhar Jamat time change tomorrow")
                    arabic_label2.config(text=f"{differing_times[diff-2]}")
                elif index == 1:
                    arabic_label0.config(text=f"جماعة الظهر تتغير غدا")
                    arabic_label1.config(text=f"Dhuhar Jamat time change tomorrow")
                    arabic_label2.config(text=f"{differing_times[diff-2]}")
                elif index == 2:
                    arabic_label0.config(text=f"جماعة العصر تتغير غدا")
                    arabic_label1.config(text=f"Asr Jamat time change tomorrow")
                    arabic_label2.config(text=f"{differing_times[diff-2]}")
                elif index == 3:
                    arabic_label0.config(text=f"جماعة المغرب تتغير غدا")
                    arabic_label1.config(text=f"Magrib Jamat time change tomorrow")
                    arabic_label2.config(text=f"{differing_times[diff]}")
                elif index == 4:
                    arabic_label0.config(text=f"جماعة العشاء تتغير غدا")
                    arabic_label1.config(text=f"Isha Jamat time change tomorrow")
                    arabic_label2.config(text=f"{differing_times[diff-2]}")
                break  # Exit the loop after finding the matching index
        # Set the stop flag after 1 minute (60 seconds)
        # threading.Timer(180,stop).start()

# nmaz_index=sys.argv[1]
nmaz_index=3
next_jmat(nmaz_index)
import sys

import subprocess

# screen_timeout=int(sys.argv[2])
screen_timeout=1


# Simulate the passage of time
time_left_seconds = 10 * 60  # 10 minutes in seconds
def switch_to_main():
    window.destroy()
    subprocess.run(["python", "main.py",str(sys.argv[2])])

# Schedule the function to switch back to main.py after 2 minutes (120 seconds)
# window.after(1 * 60*1000 , switch_to_main)
# Simulate the passage of time
# time_left_seconds = 600  # 10 minutes (change it to 0 for testing)
time_left_seconds = 10  # 10 minutes (change it to 0 for testing)

window.configure(bg="#ccddc1")

window.after(screen_timeout, reset_screen)  # Run the reset_screen function after 40 seconds (40000 milliseconds)
# if time_left_seconds <= 0:
#     reset_screen()
# else:
    # Update the current prayer info
    # Show the "phone off" screen
window.mainloop()
