import tkinter as tk
import os

def shutdown():
    # Issue the shutdown command
    # /s: shutdown
    # /t 0: no timeout (immediate)
    os.system("shutdown /s /t 0")

# Create the main application window
root = tk.Tk()
root.title("Shutdown Button")
root.geometry("200x100")  # Optional: set the window size

# Create the Shutdown button
shutdown_button = tk.Button(root, text="Shutdown", command=shutdown, fg="white", bg="red")
shutdown_button.pack(expand=True, fill="both", padx=20, pady=20)

# Run the Tkinter event loop
root.mainloop()
