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
silent_label = Label(window, text="Witr", bg="#cdc874", fg="black" ,width="35", font=("Arial",35))
# Place the label just after the image
silent_label.place(relx=0.2, rely=0.03)

arabic_label = Label(window,bg="#cddec2", fg="black" , text="",height="200",width="85", font=("Arial",15))
# Place the label just after the image
arabic_label.place(relx=0.2, rely=0.14)
arabic_label = Label(window, bg="#cddec2", fg="black" , text="اَللَّهُمَّ اِنَّا نَسۡتَعِيۡنُكَ وَنَسۡتَغْفِرُكَ وَنُؤۡمِنُ بِكَ، ", font=("Arial",35))
# Place the label just after the image
arabic_label.place(relx=0.28, rely=0.25)

arabic_label = Label(window ,bg="#cddec2",  fg="black" ,text="وَنَتَوَكَّلُ عَلَيۡكَ وَنُثۡنِىۡ عَلَيۡكَ ٱلۡخَيۡرَ وَنَشۡكُرُكَ  ، ", font=("Arial",35))
# Place the label just after the image
arabic_label.place(relx=0.28, rely=0.33)

arabic_label = Label(window,bg="#cddec2", fg="black" ,  text="وَلَا نَكۡفُرُكَ وَنَخۡلَعُ وَنَتۡرُكُ مَنۡ يَّفۡجُرُكَ. اَللَّهُمَّ، ", font=("Arial",35))
# Place the label just after the image
arabic_label.place(relx=0.28, rely=0.40)

arabic_label = Label(window, bg="#cddec2", fg="black" , text="اِيَّاكَ نَعۡبُدُ وَلَكَ نُصَلِّئ وَنَسۡجُدُ وَاِلَيۡكَ نَسۡعٰى، ", font=("Arial",35))
# Place the label just after the image
arabic_label.place(relx=0.28, rely=0.47)

arabic_label = Label(window,bg="#cddec2" , fg="black" , text="ونَحۡفِدُ ونَرۡجُوۡا رَحۡمَتَكَ وَنَخۡشٰى عَذَابَكَ اِنَّ، ", font=("Arial",35))
# Place the label just after the image
arabic_label.place(relx=0.28, rely=0.54)

arabic_label = Label(window,bg="#cddec2", fg="black" , text="عَذَابَكَ بِالۡكُفَّارِ مُلۡحِقٌٌ، ", font=("Arial",35))
# Place the label just after the image
arabic_label.place(relx=0.28, rely=0.61)

arabic_label = Label(window,bg="#cddec2", fg="black" , text="---------------------------- ", font=("Arial",35))
# Place the label just after the image
arabic_label.place(relx=0.28, rely=0.69)

arabic_label = Label(window,bg="#cddec2", fg="black" , text="O Allah! We implore You for help and beg forgiveness of You and believe in You", font=("Arial",15))
# Place the label just after the image
arabic_label.place(relx=0.22, rely=0.75)

arabic_label = Label(window,bg="#cddec2", fg="black" , text=" and rely on You and extol You and we are thankful to You and are not ungrateful ", font=("Arial",15))
# Place the label just after the image
arabic_label.place(relx=0.22, rely=0.79)
arabic_label = Label(window,bg="#cddec2", fg="black" , text="to You and we alienate and forsake those who disobey You. O Allah! You alone do we worship and", font=("Arial",15))
# Place the label just after the image
arabic_label.place(relx=0.22, rely=0.83)
arabic_label = Label(window,bg="#cddec2", fg="black" , text="for You do we pray and prostrate and we betake to please You and present ourselves for the", font=("Arial",15))
# Place the label just after the image
arabic_label.place(relx=0.22, rely=0.87)
arabic_label = Label(window,bg="#cddec2", fg="black" , text="service in Your cause and we hope for Your mercy and fear Your chastisement.Undoubtedly, Your", font=("Arial",15))
# Place the label just after the image
arabic_label.place(relx=0.22, rely=0.91)
arabic_label = Label(window,bg="#cddec2", fg="black" , text="torment is going to overtake infidels O Allah! ", font=("Arial",15))
# Place the label just after the image
arabic_label.place(relx=0.22, rely=0.95)
arabic_label = Label(window,bg="#cddec2", fg="black" , text="torment is going to overtake infidels O Allah! ", font=("Arial",15))
# Place the label just after the image
arabic_label.place(relx=0.22, rely=0.95)

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

window.configure(bg="black")

if time_left_seconds <= 0:
    reset_screen()
else:
    window.mainloop()
