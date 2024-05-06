import tkinter as tk
from tkinter import ttk, filedialog
import os
import subprocess

# Default values
default_screen_timeout = 1
default_background_color = "green"
default_interval = 1

# Function to save the settings
def save_settings():
    # Retrieve user input from the entry fields
    screen_timeout = screen_timeout_entry.get()
    background_color = color_entry.get()
    interval = interval_entry.get()
    print("back ",background_color)
    # Set default values if entries are empty
    if not screen_timeout:
        screen_timeout = default_screen_timeout
    if not background_color:
        background_color = default_background_color
    if not interval:
        interval = default_background_color
    
    # Close the settings window
    settings_window.destroy()
    
    # Pass the settings values to main.py using command-line arguments
    subprocess.run(["python", "main.py", str(screen_timeout), background_color,interval])
# Function to upload images
def upload_images():
    # Get the current posters
    current_posters = [f for f in os.listdir("posters") if f.endswith(".jpg")]
    
    # If there are already 5 posters, remove them
    if len(current_posters) == 5:
        for poster in current_posters:
            os.remove(os.path.join("posters", poster))
    
    # Ask user to select new images
    filenames = filedialog.askopenfilenames(title="Select 5 images", filetypes=(("Image files", "*.jpg;*.jpeg;*.png"),))
    if filenames:
        # Create a directory to store images if it doesn't exist
        os.makedirs("posters", exist_ok=True)
        # Save the selected images to the "posters" directory with names p1, p2, p3, ...
        for i, filename in enumerate(filenames, start=1):
            image_path = os.path.join("posters", f"p{i}.jpg")
            with open(filename, 'rb') as f_src, open(image_path, 'wb') as f_dst:
                f_dst.write(f_src.read())

# Create the main settings window
settings_window = tk.Tk()
settings_window.title("Settings")

# Create a frame to hold the settings widgets
settings_frame = ttk.Frame(settings_window, padding="20")
settings_frame.grid(row=0, column=0)

# Screen Timeout Label and Entry
screen_timeout_label = ttk.Label(settings_frame, text="Screen Timeout:")
screen_timeout_label.grid(row=0, column=0, padx=5, pady=5)
screen_timeout_entry = ttk.Entry(settings_frame)
screen_timeout_entry.grid(row=0, column=1, padx=5, pady=5)

# Background Color Label and Entry
color_label = ttk.Label(settings_frame, text="Highlighter Color:")
color_label.grid(row=1, column=0, padx=5, pady=5)
color_entry = ttk.Entry(settings_frame)
color_entry.grid(row=1, column=1, padx=5, pady=5)

interval_label = ttk.Label(settings_frame, text="Interaval time for posters:")
interval_label.grid(row=2, column=0, padx=5, pady=5)
interval_entry = ttk.Entry(settings_frame)
interval_entry.grid(row=2, column=1, padx=5, pady=5)

# Save Button
save_button = ttk.Button(settings_frame, text="Save Settings", command=save_settings)
save_button.grid(row=4, columnspan=2, padx=5, pady=10)

# Upload Images Button
upload_button = ttk.Button(settings_frame, text="Upload Posters", command=upload_images)
upload_button.grid(row=3, columnspan=2, padx=5, pady=10)

# Start the settings window
settings_window.mainloop()
