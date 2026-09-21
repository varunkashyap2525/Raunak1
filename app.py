import tkinter as tk
from tkinter import messagebox
import time
import threading
import random

class TermuxPrank:
    def __init__(self, root):
        self.root = root
        self.root.title("Termux Interface")
        self.root.geometry("350x600")
        self.root.configure(bg="#000000")  # Black background like Termux
        
        # Font style for that terminal look
        self.terminal_font = ("Courier", 12)
        
        # Step 1: Main Termux Screen
        self.setup_termux_screen()

    def setup_termux_screen(self):
        """Main screen with the 'Click' button"""
        frame = tk.Frame(self.root, bg="#000000")
        frame.pack(fill="both", expand=True)
        
        # Terminal prompt look
        label = tk.Label(frame, text="$", font=("Courier", 20), fg="#00ff00", bg="#000000")
        label.pack(pady=20, anchor="w")
        
        btn = tk.Button(frame, text="Click", font=("Courier", 16), bg="#333333", fg="#00ff00",
                        command=self.show_password_screen, activebackground="#555555", activeforeground="#00ff00")
        btn.pack(pady=50)
        
        # Some fake terminal text
        txt = tk.Label(frame, text="Welcome to Termux\nType 'click' to start...", 
                       font=("Courier", 10), fg="#aaaaaa", bg="#000000", anchor="w")
        txt.pack(anchor="w", padx=10, pady=10)

    def show_password_screen(self):
        """Window asking for password"""
        # Hide main window temporarily
        self.root.withdraw()
        
        pw_window = tk.Toplevel(self.root)
        pw_window.title("Password")
        pw_window.geometry("300x200")
        pw_window.configure(bg="#000000")
        pw_window.attributes("-topmost", True) # Keep on top

        label = tk.Label(pw_window, text="Enter Password:", font=("Courier", 12), fg="#00ff00", bg="#000000")
        label.pack(pady=20)

        entry = tk.Entry(pw_window, font=("Courier", 14), show="*", bg="#222222", fg="#ffffff")
        entry.pack(pady=10)

        def check_password():
            pwd = entry.get()
            if pwd == "1989":
                pw_window.destroy()
                self.start_hacking_sequence()
            else:
                entry.delete(0, tk.END)
                entry.insert(0, "Wrong Password")
                entry.config(fg="red")
                self.root.after(1000, lambda: entry.config(fg="#ffffff"))

        btn = tk.Button(pw_window, text="Submit", command=check_password, bg="#00ff00", fg="#000000", font=("Courier", 12))
        btn.pack(pady=20)

    def start_hacking_sequence(self):
        """5-second hacking animation"""
        hack_window = tk.Toplevel(self.root)
        hack_window.title("Hacking...")
        hack_window.geometry("400x300")
        hack_window.configure(bg="#000000")
        hack_window.attributes("-topmost", True)

        label = tk.Label(hack_window, text="HACKING SERVER...", font=("Courier", 16, "bold"), fg="#00ff00", bg="#000000")
        label.pack(pady=50)

        # Progress bar
        progress = tk.Progressbar(hack_window, length=300, mode='determinate')
        progress.pack(pady=10)
        
        count = 0
        def update_progress():
            nonlocal count
            if count < 100:
                progress['value'] = count
                count += 5
                hack_window.after(100, update_progress)
            else:
                hack_window.destroy()
                self.show_welcome_page()

        update_progress()

    def show_welcome_page(self):
        """The final prank page with Instagram form"""
        self.root.deiconify() # Bring main window back
        self.root.title("Welcome My Web")
        
        # Clear previous widgets
        for widget in self.root.winfo_children():
            widget.destroy()

        # Header
        header = tk.Label(self.root, text="Welcome My Web", font=("Courier", 18, "bold"), fg="#00ff00", bg="#000000")
        header.pack(pady=20)

        frame = tk.Frame(self.root, bg="#111111")
        frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Instagram Account Section
        tk.Label(frame, text="IG ACCOUNT BEN PRANK", font=("Courier", 12, "bold"), fg="#ff0050", bg="#111111").pack(anchor="w", pady=5)
        
        tk.Label(frame, text="Username:", font=("Courier", 10), fg="#aaaaaa", bg="#111111").pack(anchor="w")
        user_entry = tk.Entry(frame, font=("Courier", 10), bg="#333333", fg="#ffffff")
        user_entry.pack(fill="x", pady=2)
        
        # Fake result label for username
        user_result_label = tk.Label(frame, text="", font=("Courier", 9), fg="#ffff00", bg="#111111)
        user_result_label.pack(anchor="w")

        tk.Label(frame, text="Phone Number:", font=("Courier", 10), fg="#aaaaaa", bg="#111111").pack(anchor="w", pady=5)
        phone_entry = tk.Entry(frame, font=("Courier", 10), bg="#333333", fg="#ffffff")
        phone_entry.pack(fill="x", pady=2)

        # Fake result label for phone
        phone_result_label = tk.Label(frame, text="", font=("Courier", 9), fg="#ffff00", bg="#111111)
        phone_result_label.pack(anchor="w")

        tk.Label(frame, text="(Data hidden from user)", font=("Courier", 8), fg="#666666", bg="#111111").pack(anchor="e", pady=10)

        submit_btn = tk.Button(frame, text="GENERATE", command=lambda: self.generate_data(user_entry.get(), phone_entry.get(), user_result_label, phone_result_label),
                               bg="#00ff00", fg="#000000", font=("Courier", 12))
        submit_btn.pack(pady=20)

    def generate_data(self, user, phone, user_lbl, phone_lbl):
        """Logic to show 24 Grants and Hardoi UP"""
        if user:
            # Show 24 granted time
            user_lbl.config(text="[GRANTED] 24:00:00 HOURS REMAINING", fg="#00ff00")
        
        if phone:
            # Show Hardoi UP
            phone_lbl.config(text="LOCATION: HARDOI, UP", fg="#00ff00")
            
        # Final success message
        tk.Message(self.root, text="Account Ben Prank Processed Successfully.", 
                   font=("Courier", 10), fg="#ffffff", bg="#000000").pack(pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    app = TermuxPrank(root)
    root.mainloop()
