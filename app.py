import tkinter as tk
from tkinter import messagebox
import webbrowser

# --- PASSWORD SETTING ---
REAL_PASSWORD = "1989"

def check_password():
    entered = entry_pass.get()
    if entered == REAL_PASSWORD:
        messagebox.showinfo("Success", "✅ Login Successful! Welcome Raunak!")
        root.destroy() # login window band karo
        open_main_website() # main website kholo
    else:
        messagebox.showerror("Error", "❌ Galat Password! Sahi password 1989 hai")

def open_main_website():
    # Yaha tumhari hacking wali website khulegi
    main = tk.Tk()
    main.title("Raunak Web - Welcome")
    main.geometry("800x600")
    main.configure(bg="black")

    tk.Label(main, text="WELCOME TO MY WEBSITE", fg="#00ff00", bg="black", font=("Courier", 22, "bold")).pack(pady=30)
    tk.Label(main, text="Is website ko banane wala Raunak Singh hai", fg="white", bg="black", font=("Courier", 14)).pack(pady=10)

    # Form jaisa look
    tk.Label(main, text="Name: Raunak Singh", fg="#00ff00", bg="black", font=("Courier", 12)).pack(pady=20)
    tk.Label(main, text="Email: Raunakkashyap1989@gmail.com", fg="#00ff00", bg="black", font=("Courier", 12)).pack()

    tk.Button(main, text="OPEN MY ORIGINAL WEBSITE", bg="#00ff00", fg="black", font=("Arial", 12, "bold"), command=lambda: webbrowser.open("https://raunakweb.onrender.com")).pack(pady=40)
    main.mainloop()

# --- LOGIN WINDOW (Hacking Style) ---
root = tk.Tk()
root.title("Login - Raunak Web")
root.geometry("400x400")
root.configure(bg="black")

# Beech me lane ke liye
frame = tk.Frame(root, bg="black")
frame.place(relx=0.5, rely=0.5, anchor="center")

tk.Label(frame, text="🔒 SECURE LOGIN", fg="#00ff00", bg="black", font=("Courier", 18, "bold")).pack(pady=15)
tk.Label(frame, text="Welcome to Raunak's Website", fg="white", bg="black", font=("Arial", 10)).pack(pady=5)

# Password kaha dalna hai
tk.Label(frame, text="Password yaha dalo:", fg="#00ff00", bg="black", font=("Arial", 11)).pack(pady=(20,5))

entry_pass = tk.Entry(frame, show="*", width=25, font=("Arial", 12), justify="center", bg="#111", fg="#00ff00", insertbackground="#00ff00")
entry_pass.pack(pady=5)

# BLUE Login Button - Bich me Niche
btn_login = tk.Button(frame, text="LOGIN", bg="blue", fg="white", width=15, font=("Arial", 12, "bold"), command=check_password)
btn_login.pack(pady=20)

tk.Label(frame, text="Hint: Password = 1989", fg="#555", bg="black", font=("Arial", 8)).pack()

root.mainloop()
