# Import Module
from tkinter import *
from tkinter import messagebox  # Import messagebox module
import webbrowser  # Import webbrowser module

# create root window
root = Tk()

# root window title and dimension
root.title("Welcome to The Fallen Gaze")
# Set geometry (widthxheight)
root.geometry('1150x800')

# Set dark theme colors
root.configure(bg='black')

# Create a frame for the navigation bar
nav_frame = Frame(root, bg='darkgray')
nav_frame.pack(side=TOP, fill=X)

# Create a menu bar
menu_bar = Menu(root)

# Function to display messages (placeholder for actual functionality)
def show_message(option):
    print(f"{option} selected")

# Function to show about dialog
def show_about():
    messagebox.showinfo("About", "The Fallen Gaze is the C2 framework that is made to control all the agents and helps evade the firewall.")

# Create Gaze dropdown menu
gaze_menu = Menu(menu_bar, tearoff=0)
gaze_menu.add_command(label="Team Server", command=lambda: show_message("Team Server"))
gaze_menu.add_command(label="Quit", command=root.quit)  # Updated to call root.quit()
menu_bar.add_cascade(label="Gaze", menu=gaze_menu)

# Create View dropdown menu
view_menu = Menu(menu_bar, tearoff=0)
view_menu.add_command(label="Graph View", command=lambda: show_message("Graph View"))
view_menu.add_command(label="Line View", command=lambda: show_message("Line View"))
menu_bar.add_cascade(label="View", menu=view_menu)

# Create Attack dropdown menu
attack_menu = Menu(menu_bar, tearoff=0)
attack_menu.add_command(label="Listener", command=lambda: show_message("Listeners"))
attack_menu.add_command(label="Payload", command=lambda: show_message("Payload"))
menu_bar.add_cascade(label="Attack", menu=attack_menu)

# Create Help dropdown menu
help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label="Help Contents", command=lambda: webbrowser.open("https://github.com/aayushpnth/The-Fallen-Gaze/blob/main/README.md"))  # Link added here
help_menu.add_command(label="About", command=show_about)  # Updated to call show_about function
menu_bar.add_cascade(label="Help", menu=help_menu)

# Configure the root window to use the menu bar
root.config(menu=menu_bar)

# Execute Tkinter
root.mainloop()
