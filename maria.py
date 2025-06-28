import tkinter as tk
from tkinter import messagebox

def show_message():
    messagebox.showinfo("✨ maria+didi=love ✨", "Congrats on your LICENCE degree, Maria! You deserved it 💖")

# Window setup
window = tk.Tk()
window.title("🌸 maria l3ziizaaa 🌸")
window.geometry("550x400")
window.configure(bg="#fdf6f0")  # Soft cream background

# Top Pastel Hearts
hearts_top = tk.Label(window, 
                      text="♡ ♡ ♡ ♡ ♡", 
                      font=("Arial", 20), 
                      fg="#ffb6c1", 
                      bg="#fdf6f0")
hearts_top.pack(pady=10)

# Main Title
title = tk.Label(window, 
                 text="Congrats Maria!", 
                 font=("Helvetica", 22, "bold"), 
                 fg="#e75480", 
                 bg="#fdf6f0")
title.pack(pady=15)

# Soft Message
message = tk.Label(window, 
                   text="You got your LICENCE degree girl,\nYou truly deserved it. ♡", 
                   font=("Helvetica", 14), 
                   fg="#c71585", 
                   bg="#fdf6f0",
                   justify="center")
message.pack(pady=10)

# Button for more love
button = tk.Button(window, 
                   text="Click for a surprise ✨", 
                   command=show_message, 
                   bg="#f4a6c1", 
                   fg="white", 
                   font=("Helvetica", 12, "bold"),
                   padx=10, pady=5,
                   relief="flat")
button.pack(pady=25)

# Bottom Hearts, Subtle
hearts_bottom = tk.Label(window, 
                         text="♡ ♡ ♡ ♡ ♡", 
                         font=("Arial", 20), 
                         fg="#ffb6c1", 
                         bg="#fdf6f0")
hearts_bottom.pack(pady=10)

window.mainloop()
