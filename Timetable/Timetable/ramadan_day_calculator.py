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


# Create a label for "Silent your phone" text
silent_label = Label(window, text=f"Ramadan {islamic_day}", bg="black", fg="red" , font=("Arial",35))
# Place the label just after the image
silent_label.place(relx=0.4, rely=0.03)

arabic_label = Label(window, text="ذَهَبَ الظَّمَأُ وَابْتَلَّتِ الْعُرُوقُ ",bg="black", fg="white" , font=("Arial",35))
# Place the label just after the image
arabic_label.place(relx=0.3, rely=0.18)
arabic_label = Label(window, text=" وَثَبَتَ الأَجْرُ إِنْ شَاءَ اللَّهُ ",bg="black", fg="white" , font=("Arial",35))
# Place the label just after the image
arabic_label.place(relx=0.3, rely=0.26)

arabic_label = Label(window, bg="black", fg="white" , text="          ---------------------", font=("Arial",30))
arabic_label.place(relx=0.3, rely=0.48)

arabic_label = Label(window, bg="black", fg="white" , text="The prophet (S.A.W) said when he broke his fast:", font=("Arial",25))
arabic_label.place(relx=0.28, rely=0.58)


arabic_label = Label(window, bg="black", fg="white" , text="\" Thirst is gone, the veins are moistened", font=("Arial",30))
arabic_label.place(relx=0.3, rely=0.65)

arabic_label = Label(window, bg="black", fg="white" , text="and the reward is certain if Allah wills. \"", font=("Arial",30))
arabic_label.place(relx=0.3, rely=0.72)


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
window.after(1 * 60 * 1000, switch_to_main)

# Simulate the passage of time
# time_left_seconds = 600  # 10 minutes (change it to 0 for testing)

time_left_seconds = 10  # 10 minutes (change it to 0 for testing)

window.configure(bg="black")

if time_left_seconds <= 0:
    reset_screen()
else:
    window.mainloop()
