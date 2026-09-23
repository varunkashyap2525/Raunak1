import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import qrcode
import io

# Bikeebo Brand Name
APP_NAME = "Bikeebo"

class BikeeboApp:
    def __init__(self, root):
        self.root = root
        self.root.title(APP_NAME)
        self.root.geometry("800x600")
        self.root.configure(bg="#f0f0f0")

        # Header
        self.header = tk.Label(root, text=APP_NAME, font=("Arial", 24, "bold"), bg="#f0f0f0", fg="#ff5722")
        self.header.pack(pady=10)

        # Phone Data
        self.phones = [
            {"name": "iPhone 17", "img": "https://via.placeholder.com/150?text=iPhone+17"},
            {"name": "iPhone 16", "img": "https://via.placeholder.com/150?text=iPhone+16"},
            {"name": "iPhone 15", "img": "https://via.placeholder.com/150?text=iPhone+15"},
            {"name": "iPhone 14", "img": "https://via.placeholder.com/150?text=iPhone+14"},
            {"name": "Android Flagship", "img": "https://via.placeholder.com/150?text=Android+2026"},
            {"name": "Android Budget X", "img": "https://via.placeholder.com/150?text=Android+Budget"}
        ]

        self.container = tk.Frame(root, bg="#f0f0f0")
        self.container.pack(pady=10)

        # Create Cards
        self.cards = []
        for i, phone in enumerate(self.phones):
            card = tk.Frame(self.container, bg="white", bd=1, relief="solid", width=200, height=300)
            card.grid(row=i // 2, column=i % 2, padx=10, pady=10)
            card.pack_propagate(False)
            
            # Image Placeholder (Using text for demo, you can replace with actual ImageTk.PhotoImage)
            img_label = tk.Label(card, text="📱", font=("Arial", 40), bg="white")
            img_label.pack(pady=5)
            
            name_label = tk.Label(card, text=phone["name"], font=("Arial", 12, "bold"), bg="white")
            name_label.pack()

            price_label = tk.Label(card, text="₹500", font=("Arial", 14, "bold"), fg="green", bg="white")
            price_label.pack()

            buy_btn = tk.Button(card, text="BUY NOW", command=lambda p=phone: self.open_buy_window(p), bg="#ff5722", fg="white", font=("Arial", 10, "bold"))
            buy_btn.pack(pady=5)

            self.cards.append(card)

    def open_buy_window(self, phone):
        buy_win = tk.Toplevel(self.root)
        buy_win.title(f"Buy {phone['name']}")
        buy_win.geometry("400x500")
        buy_win.configure(bg="#f0f0f0")

        tk.Label(buy_win, text=phone["name"], font=("Arial", 16, "bold"), bg="#f0f0f0").pack(pady=10)
        tk.Label(buy_win, text="Price: ₹500", font=("Arial", 12), bg="#f0f0f0").pack()

        # Form Fields
        fields = ["Full Name", "Phone Number", "City", "Address"]
        entries = []
        for field in fields:
            tk.Label(buy_win, text=f"{field}:", font=("Arial", 10), bg="#f0f0f0").pack(anchor="w", padx=20, pady=2)
            entry = tk.Entry(buy_win, font=("Arial", 10), width=30)
            entry.pack(padx=20, pady=2)
            entries.append(entry)

        def submit():
            details = [e.get() for e in entries]
            if any(not d for d in details):
                messagebox.showwarning("Missing Info", "Please fill all fields.")
                return
            
            # Show Scanner Page
            show_scanner(buy_win, phone["name"], details)

        tk.Button(buy_win, text="Confirm & Scan", command=submit, bg="#2196f3", fg="white", font=("Arial", 10, "bold")).pack(pady=20)

    def show_scanner(self, win, phone_name, details):
        # Clear current window content
        for widget in win.winfo_children():
            widget.destroy()

        tk.Label(win, text="Scanner", font=("Arial", 20, "bold"), bg="#f0f0f0").pack(pady=20)
        
        # Generate QR Code Data
        qr_data = f"Order: {phone_name}\nName: {details[0]}\nNum: {details[1]}\nCity: {details[2]}\nAddr: {details[3]}\nAmount: ₹500"
        
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(qr_data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")

        # Save to a buffer to display in Tkinter
        buffer = io.BytesIO()
        img.save(buffer, format="PNG")
        buffer.seek(0)
        
        # Load image for Tkinter
        try:
            from PIL import ImageTk
            img_tk = ImageTk.PhotoImage(Image.open(buffer))
            tk.Label(win, image=img_tk, bg="#f0f0f0").pack(pady=10)
            win.image = img_tk # Keep reference
        except Exception as e:
            tk.Label(win, text="QR Code Generated (Check Console)", bg="#f0f0f0").pack()
            print(qr_data)

        tk.Label(win, text="Scan to Pay ₹500", font=("Arial", 12), bg="#f0f0f0").pack()
        tk.Button(win, text="Back", command=lambda: [win.destroy()], bg="#ff5722", fg="white").pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = BikeeboApp(root)
    root.mainloop()
