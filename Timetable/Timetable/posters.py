from tkinter import Tk, Label, PhotoImage
from PIL import Image, ImageTk  # Import PIL library
import os
import sys
import subprocess
from datetime import datetime

# Create the main window
window = Tk()
window.attributes('-fullscreen', True)

window.config(bg="black")

# Load the "phone off" image
phone_off_image = PhotoImage(file="phone_off2.png")

# Create a label widget to display the "phone off" image
phone_off_label = Label(window, image=phone_off_image)
phone_off_label.place(relx=0.28, rely=0.75, width=100, height=100)

# Create a label for "Silent your phone" text
# poster_label2 = Label(window, text="Poster", font=("Arial",25), bg="black", fg="white")
# poster_label2.place(relx=0.23, rely=0.1)

timer2 = Label(window, text="E & S society", font=("Arial",25), bg="black", fg="#cdc874")
timer2.place(relx=0.26, rely=0.62)


timer3 = Label(window, text="Turn off / silence your phone", font=("Arial",25), bg="black", fg="#cdc874")
timer3.place(relx=0.26, rely=0.69)

timer4 = Label(window, text="", font=("Arial",25), bg="black", fg="white")
timer4.place(relx=0.26, rely=0.88)

timer5 = Label(window, text="Jummah 13:15", font=("Arial",25), bg="black", fg="white")
timer5.place(relx=0.26, rely=0.94)

poster_label = Label(window, text="Poster", font=("Arial",25), bg="black", fg="white")
poster_label.place(relx=0.26, rely=0.12)

# Get the list of poster image files
poster_files = sorted([f for f in os.listdir("posters") if f.endswith(".jpg")])

# Function to show posters
def show_posters():
    global poster_index
    # Check if there are posters to show
    if poster_index < len(poster_files):
        # Open the image file
        poster_image = Image.open(os.path.join("posters", poster_files[poster_index]))
        # Resize the image to fit the label
        poster_image = poster_image.resize((400, 350))
        # Convert image to Tkinter PhotoImage
        poster_photo = ImageTk.PhotoImage(poster_image)
        # Update the label with the new image
        poster_label.config(image=poster_photo)
        poster_label.image = poster_photo
        # Increment the poster index
        poster_index += 1
        # Schedule the next poster
        window.after(interval * 1000, show_posters)
    else:
        # If all posters are shown, destroy the window
        poster_index = 0

# Simulate the passage of time
time_left_seconds = 10 * 60  # 10 minutes in seconds

# Function to switch back to main.py
def switch_to_main():
    window.destroy()
    subprocess.run(["python", "main.py"])

screen_timeout=30

try:
    screen_timeout=sys.argv[2]
except:
    pass
# Schedule the function to switch back to main.py after screen_timeout
window.after(screen_timeout * 60 * 1000, switch_to_main)

# Get interval for showing posters
interval = int(sys.argv[1]) if len(sys.argv) >= 1 else 2  # Default interval is 2 seconds

# Set initial poster index
poster_index = 0

# Start showing posters
show_posters()

# Function to update the current time every second
def update_time():
    current_time = datetime.now().strftime("%H:%M:%S")
    timer4.config(text=current_time)
    window.after(1000, update_time)  # Schedule the function to run after 1000 milliseconds (1 second)

# Start updating the time
update_time()


# Start the main window
window.mainloop()
