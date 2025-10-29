import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os

class ImageToPDFConverter:
    def __init__(self, root):
        self.root = root
        self.image_paths = []
        self.output_pdf_name = tk.StringVar()
        self.save_directory = tk.StringVar(value=os.getcwd())

        # --- Auto-detect background image from same folder ---
        folder = os.path.dirname(os.path.abspath(__file__))
        possible_files = ["background.png", "background.jpg", "background.png.jpg"]
        self.background_image_path = None

        for file in possible_files:
            path = os.path.join(folder, file)
            if os.path.exists(path):
                self.background_image_path = path
                break

        # --- Initialize UI ---
        self.initialize_ui()

    def initialize_ui(self):
        self.root.title("✨ Image to PDF Converter ✨")
        self.root.geometry("600x750")

        # ---------- Background Image ----------
        if self.background_image_path:
            bg_image = Image.open(self.background_image_path)
            bg_image = bg_image.resize((600, 750))
            self.bg_photo = ImageTk.PhotoImage(bg_image)

            bg_label = tk.Label(self.root, image=self.bg_photo)
            bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        else:
            self.root.configure(bg="#f3e5f5")

        # ---------- Overlay Frame ----------
        overlay = tk.Frame(self.root, bg="#ffffff")  # semi-transparent overlay
        overlay.place(relx=0.5, rely=0.5, anchor="center", width=500, height=650)

        # ---------- Heading ----------
        title_label = tk.Label(
            overlay,
            text="🖼️ Image ➜ PDF Converter",
            font=("Algerian", 22, "bold"),
            fg="#4A148C",
            bg="#ffffff"
        )
        title_label.pack(pady=15)

        # ---------- Buttons Frame ----------
        button_frame = tk.Frame(overlay, bg="#ffffff")
        button_frame.pack(pady=5)

        select_btn = tk.Button(
            button_frame,
            text="📸 Select Images",
            command=self.select_images,
            font=("Comic Sans MS", 12, "bold"),
            bg="#7E57C2",
            fg="white",
            width=15
        )
        select_btn.grid(row=0, column=0, padx=5)

        clear_btn = tk.Button(
            button_frame,
            text="🧹 Clear",
            command=self.clear_selection,
            font=("Comic Sans MS", 12, "bold"),
            bg="#BA68C8",
            fg="white",
            width=10
        )
        clear_btn.grid(row=0, column=1, padx=5)

        # ---------- Selected Images ----------
        tk.Label(overlay, text="Selected Images:", bg="#ffffff", font=("Arial", 11, "bold")).pack(pady=(10,0))
        self.listbox = tk.Listbox(overlay, width=50, height=8, font=("Arial", 10))
        self.listbox.pack(pady=5)

        # ---------- Save Directory ----------
        tk.Label(overlay, text="Save PDF To:", bg="#ffffff", font=("Arial", 11, "bold")).pack(pady=(10, 0))
        path_frame = tk.Frame(overlay, bg="#ffffff")
        path_frame.pack(pady=5)

        path_entry = tk.Entry(path_frame, textvariable=self.save_directory, width=35, font=("Arial", 10))
        path_entry.grid(row=0, column=0, padx=5)

        browse_btn = tk.Button(
            path_frame,
            text="📁 Browse",
            command=self.browse_directory,
            font=("Comic Sans MS", 10, "bold"),
            bg="#9575CD",
            fg="white"
        )
        browse_btn.grid(row=0, column=1)

        # ---------- PDF Name ----------
        tk.Label(overlay, text="PDF File Name:", bg="#ffffff", font=("Arial", 11, "bold")).pack(pady=(10,0))
        name_entry = tk.Entry(overlay, textvariable=self.output_pdf_name, width=30, font=("Arial", 11))
        name_entry.pack(pady=(0,10))

        # ---------- Convert Button ----------
        convert_btn = tk.Button(
            overlay,
            text="✨ Convert to PDF ✨",
            command=self.convert_to_pdf,
            font=("Comic Sans MS", 13, "bold"),
            bg="#6A1B9A",
            fg="white",
            width=20
        )
        convert_btn.pack(pady=15)

        # ---------- Footer ----------
        tk.Label(
            overlay,
            text="© Created by You | Powered by Lunar Orbit 💜",
            bg="#ffffff",
            fg="#4A148C",
            font=("Courier New", 10, "italic")
        ).pack(side="bottom", pady=10)

    # ---------- Select Images ----------
    def select_images(self):
        file_paths = filedialog.askopenfilenames(
            title="Select Images",
            filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp *.gif")]
        )
        self.image_paths = list(file_paths)
        self.listbox.delete(0, tk.END)
        for path in self.image_paths:
            self.listbox.insert(tk.END, os.path.basename(path))
        if self.image_paths:
            messagebox.showinfo("Images Selected", f"{len(self.image_paths)} image(s) selected!")

    # ---------- Clear Selection ----------
    def clear_selection(self):
        self.image_paths.clear()
        self.listbox.delete(0, tk.END)
        messagebox.showinfo("Cleared", "Image selection cleared!")

    # ---------- Browse Save Location ----------
    def browse_directory(self):
        directory = filedialog.askdirectory(title="Select Save Location")
        if directory:
            self.save_directory.set(directory)

    # ---------- Convert to PDF ----------
    def convert_to_pdf(self):
        if not self.image_paths:
            messagebox.showerror("Error", "Please select images first!")
            return

        pdf_name = self.output_pdf_name.get().strip()
        if not pdf_name:
            messagebox.showerror("Error", "Please enter a PDF file name!")
            return

        pdf_path = os.path.join(self.save_directory.get(), pdf_name + ".pdf")
        images = [Image.open(img).convert("RGB") for img in self.image_paths]
        images[0].save(pdf_path, save_all=True, append_images=images[1:])
        messagebox.showinfo("Success", f"PDF created successfully!\n\nSaved at:\n{pdf_path}")

# ---------- Main Function ----------
def main():
    root = tk.Tk()
    app = ImageToPDFConverter(root)
    root.mainloop()

if __name__ == "__main__":
    main()
