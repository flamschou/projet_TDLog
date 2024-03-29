# Purpose: This file is used to scale the GUI to the screen size of the user.

import tkinter as tk


def get_scale_factor():
    try:
        root = tk.Tk()
        # screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        root.destroy()
        return screen_height / 600 * 0.85  # Adjust this calculation as needed
    except tk.TclError as e:
        # Handle the case when there's no available display
        # Useful for running the tests
        print(
            f"Error: {e}. No display available or $DISPLAY environment variable not set."
        )
        return None  # Or handle the absence of display in an appropriate way


scale = get_scale_factor()

# For the tests, the scale factor becomes 1
if scale is None:
    scale = 1
