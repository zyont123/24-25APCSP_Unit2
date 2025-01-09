#   a214_simple_window1.py
#   A program creates a window on your screen using Tkinter.
import tkinter as tk

# main window
root = tk.Tk()
root.wm_geometry("200x200")

# create empty frame
frame_login = tk.Frame(root)

# activiate the grid in our new frames
frame_login.grid()

# widgets for frame login
lbl_login = tk.Label(frame_login, text="Login")
lbl_username.pack()

# text box for username
ent_username = tk.Entry(frame_login, bd=3)
ent_username.pack()

root.mainloop()
