import os
from tkinter import filedialog, messagebox, ttk
import tkinter as tk
import matplotlib.pyplot as plt
import mysql.connector
import pandas as pd
from PIL import Image, ImageTk

def get_connection():
    """Establishes connection to MySQL server using NCERT standard syntax."""
    try:
        connection = mysql.connector.connect(
            host="localhost", user="root", password="password", database="lenslog_db"
        )
        return connection
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Failed to connect: {err}")
        return None

class LensLogApp:
    def __init__(self, root):
        self.root = root
        self.root.title("LensLog - Photography Portfolio Management System")
        self.root.geometry("1100x650")
        self.selected_file_path = ""
        # Setup GUI Sections
        self.create_header()
        self.create_form_frame()
        self.create_table_frame()
        self.create_preview_frame()
        # Load Data on Startup
        self.fetch_all_records()

    def create_header(self):
        header = tk.Frame(self.root, bg="#1e293b", height=50)
        header.pack(fill="x")
        title_label = tk.Label(
            header,
            text="LENSLOG PORTFOLIO MANAGER",
            font=("Arial", 16, "bold"),
            fg="white",
            bg="#1e293b",
        )
        title_label.pack(pady=10)
    def create_form_frame(self):
        form_frame = tk.LabelFrame(
            self.root,
            text=" Photograph Metadata ",
            font=("Arial", 10, "bold"),
            padx=10,
            pady=10,
        )
        form_frame.place(x=10, y=60, width=320, height=570)
        fields = [
            ("Title:", "entry_title"),
            ("Category:", "entry_cat"),
            ("Location:", "entry_loc"),
            ("Date (YYYY-MM-DD):", "entry_date"),
            ("Camera Used:", "entry_cam"),
            ("Lens Used:", "entry_lens"),
            ("ISO:", "entry_iso"),
            ("Shutter Speed:", "entry_shutter"),
            ("Aperture:", "entry_aperture"),
        ]
        self.inputs = {}
        row_idx = 0
        for label_text, attr_name in fields:
            tk.Label(form_frame, text=label_text, anchor="w").grid(
                row=row_idx, column=0, sticky="w", pady=2
            )
            entry = tk.Entry(form_frame, width=22)
            entry.grid(row=row_idx, column=1, pady=2)
            self.inputs[attr_name] = entry
            row_idx += 1

        # Rating Combo
        tk.Label(form_frame, text="Rating (1-5):", anchor="w").grid(
            row=row_idx, column=0, sticky="w", pady=2
        )
        self.rating_cb = ttk.Combobox(
            form_frame, values=[1, 2, 3, 4, 5], width=19, state="readonly"
        )
        self.rating_cb.set(5)
        self.rating_cb.grid(row=row_idx, column=1, pady=2)
        row_idx += 1

        # Status Combo
        tk.Label(form_frame, text="Status:", anchor="w").grid(
            row=row_idx, column=0, sticky="w", pady=2
        )
        self.status_cb = ttk.Combobox(
            form_frame,
            values=["Unedited", "In Progress", "Final"],
            width=19,
            state="readonly",
        )
        self.status_cb.set("Final")
        self.status_cb.grid(row=row_idx, column=1, pady=2)
        row_idx += 1

        # Image Upload Button
        btn_img = tk.Button(
            form_frame,
            text="Select Image File",
            command=self.browse_image,
            bg="#0284c7",
            fg="white",
        )
        btn_img.grid(row=row_idx, columnspan=2, sticky="ew", pady=6)
        row_idx += 1

        # Action Buttons
        btn_add = tk.Button(
            form_frame,
            text="Add Record",
            command=self.add_record,
            bg="#16a34a",
            fg="white",
            font=("Arial", 9, "bold"),
        )
        btn_add.grid(row=row_idx, columnspan=2, sticky="ew", pady=2)
        row_idx += 1
        btn_update = tk.Button(
            form_frame,
            text="Update Selected",
            command=self.update_record,
            bg="#eab308",
            fg="black",
        )
        btn_update.grid(row=row_idx, columnspan=2, sticky="ew", pady=2)
        row_idx += 1
        btn_delete = tk.Button(
            form_frame,
            text="Delete Selected",
            command=self.delete_record,
            bg="#dc2626",
            fg="white",
        )
        btn_delete.grid(row=row_idx, columnspan=2, sticky="ew", pady=2)
        row_idx += 1

        btn_clear = tk.Button(
            form_frame, text="Clear Form", command=self.clear_entries
        )
        btn_clear.grid(row=row_idx, columnspan=2, sticky="ew", pady=2)

    def create_table_frame(self):
        table_frame = tk.Frame(self.root)
        table_frame.place(x=340, y=60, width=740, height=330)
        columns = (
            "id",
            "title",
            "cat",
            "loc",
            "date",
            "cam",
            "lens",
            "rating",
            "status",
        )
        self.tree = ttk.Treeview(
            table_frame, columns=columns, show="headings"
        )
        headers = [
            ("id", "ID", 30),
            ("title", "Title", 110),
            ("cat", "Category", 80),
            ("loc", "Location", 90),
            ("date", "Date", 80),
            ("cam", "Camera", 100),
            ("lens", "Lens", 90),
            ("rating", "Rating", 50),
            ("status", "Status", 75),
        ]
        for col_id, text, width in headers:
            self.tree.heading(col_id, text=text)
            self.tree.column(col_id, width=width, anchor="center")
        scrollbar = ttk.Scrollbar(
            table_frame, orient="vertical", command=self.tree.yview
        )
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # BINDINGS: Single click loads preview, Double click opens image on PC
        self.tree.bind("<<TreeviewSelect>>", self.on_record_select)
        self.tree.bind("<Double-1>", self.open_full_image)

    def create_preview_frame(self):
        preview_box = tk.LabelFrame(
            self.root,
            text=" Image Preview & Controls (Double-click box to open photo on PC) ",
            font=("Arial", 10, "bold"),
        )
        preview_box.place(x=340, y=400, width=740, height=230)

        # Interactive Preview Box
        self.image_label = tk.Label(
            preview_box, text="No Image Selected", bg="#f1f5f9", cursor="hand2"
        )
        self.image_label.place(x=10, y=10, width=280, height=180)

        # BINDING: Double click preview box opens full image on PC
        self.image_label.bind("<Double-1>", self.open_full_image)

        # Control Panel inside Preview
        ctrl_frame = tk.Frame(preview_box)
        ctrl_frame.place(x=310, y=10, width=410, height=180)
        btn_open_pic = tk.Button(
            ctrl_frame,
            text="Open Full Photo on PC",
            command=self.open_full_image,
            bg="#2563eb",
            fg="white",
            font=("Arial", 9, "bold"),
        )
        btn_open_pic.pack(fill="x", pady=3)
        btn_analytics = tk.Button(
            ctrl_frame,
            text="Generate Analytics & Charts",
            command=self.show_analytics,
            bg="#4f46e5",
            fg="white",
            font=("Arial", 9, "bold"),
        )
        btn_analytics.pack(fill="x", pady=3)
        btn_export = tk.Button(
            ctrl_frame,
            text="Export Portfolio to CSV",
            command=self.export_csv,
            bg="#059669",
            fg="white",
        )
        btn_export.pack(fill="x", pady=3)

        # Search Controls
        search_frame = tk.LabelFrame(ctrl_frame, text=" Quick Search ")
        search_frame.pack(fill="x", pady=5)
        self.search_entry = tk.Entry(search_frame, width=18)
        self.search_entry.pack(side="left", padx=5, pady=5)
        btn_search = tk.Button(
            search_frame, text="Search Category", command=self.search_records
        )
        btn_search.pack(side="left", padx=2)
        btn_reset = tk.Button(
            search_frame, text="Reset Table", command=self.fetch_all_records
        )
        btn_reset.pack(side="left", padx=2)

    def browse_image(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp")]
        )
        if file_path:
            # Standardize path slashes using raw forward slashes
            self.selected_file_path = os.path.normpath(file_path).replace(
                "\\", "/"
            )
            self.display_image(self.selected_file_path)

    def display_image(self, file_path):
        if file_path and os.path.exists(file_path):
            try:
                img = Image.open(file_path)
                img = img.resize((280, 180), Image.Resampling.LANCZOS)
                self.tk_img = ImageTk.PhotoImage(img)
                self.image_label.config(image=self.tk_img, text="")
                return
            except Exception:
                pass

        self.image_label.config(image="", text="Image File Not Found / No Path")

    def open_full_image(self, event=None):
        """Launches the actual image file on PC using Windows Photos."""
        target_path = getattr(self, "selected_file_path", "")
        if target_path:
            # Clean up slashes without duplicating relative working directory paths
            clean_path = os.path.normpath(target_path)
            if os.path.exists(clean_path):
                os.startfile(clean_path)
            else:
                messagebox.showerror(
                    "File Error",
                    f"Image file not found at location:\n{clean_path}",
                )
        else:
            messagebox.showinfo(
                "Info", "No image file attached to this record."
            )

        
    def fetch_all_records(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        conn = get_connection()
        if not conn:
            return
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM photographs")
        rows = cursor.fetchall()
        for r in rows:
            self.tree.insert(
                "",
                "end",
                values=(
                    r[0],
                    r[1],
                    r[2],
                    r[3],
                    r[4],
                    r[5],
                    r[6],
                    r[10],
                    r[11],
                ),
            )

        cursor.close()
        conn.close()

    def add_record(self):
        title = self.inputs["entry_title"].get().strip()
        category = self.inputs["entry_cat"].get().strip()
        if not title or not category:
            messagebox.showwarning(
                "Input Error", "Title and Category are required!"
            )
            return
        conn = get_connection()
        if not conn:
            return
        cursor = conn.cursor()

        query = """
        INSERT INTO photographs 
        (title, category, location, date_taken, camera_used, lens_used, iso, shutter_speed, aperture, rating, editing_status, image_path)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        vals = (
            title,
            category,
            self.inputs["entry_loc"].get().strip(),
            self.inputs["entry_date"].get().strip() or None,
            self.inputs["entry_cam"].get().strip(),
            self.inputs["entry_lens"].get().strip(),
            int(self.inputs["entry_iso"].get() or 100),
            self.inputs["entry_shutter"].get().strip(),
            self.inputs["entry_aperture"].get().strip(),
            int(self.rating_cb.get()),
            self.status_cb.get(),
            self.selected_file_path,
        )

        try:
            cursor.execute(query, vals)
            conn.commit()
            messagebox.showinfo("Success", "Photograph record added!")
            self.clear_entries()
            self.fetch_all_records()
        except mysql.connector.Error as err:
            messagebox.showerror("Execution Error", str(err))
        finally:
            cursor.close()
            conn.close()

    def on_record_select(self, event):
        selected = self.tree.selection()
        if not selected:
            return
        item = self.tree.item(selected[0])
        photo_id = item["values"][0]
        conn = get_connection()
        if not conn:
            return
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM photographs WHERE photo_id = %s", (photo_id,)
        )
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        if row:
            self.clear_entries()
            self.selected_photo_id = row[0]
            self.inputs["entry_title"].insert(0, row[1])
            self.inputs["entry_cat"].insert(0, row[2])
            self.inputs["entry_loc"].insert(0, row[3] or "")
            self.inputs["entry_date"].insert(0, str(row[4]) if row[4] else "")
            self.inputs["entry_cam"].insert(0, row[5] or "")
            self.inputs["entry_lens"].insert(0, row[6] or "")
            self.inputs["entry_iso"].insert(0, str(row[7]) if row[7] else "")
            self.inputs["entry_shutter"].insert(0, row[8] or "")
            self.inputs["entry_aperture"].insert(0, row[9] or "")
            self.rating_cb.set(row[10])
            self.status_cb.set(row[11])
            self.selected_file_path = row[12] or ""
            self.display_image(self.selected_file_path)

    def update_record(self):
        if not hasattr(self, "selected_photo_id"):
            messagebox.showwarning(
                "Selection Error", "Select a record from table to update!"
            )
            return
        conn = get_connection()
        if not conn:
            return
        cursor = conn.cursor()
        query = """
        UPDATE photographs 
        SET title=%s, category=%s, location=%s, date_taken=%s, camera_used=%s, lens_used=%s,
            iso=%s, shutter_speed=%s, aperture=%s, rating=%s, editing_status=%s, image_path=%s
        WHERE photo_id=%s
        """
        vals = (
            self.inputs["entry_title"].get().strip(),
            self.inputs["entry_cat"].get().strip(),
            self.inputs["entry_loc"].get().strip(),
            self.inputs["entry_date"].get().strip() or None,
            self.inputs["entry_cam"].get().strip(),
            self.inputs["entry_lens"].get().strip(),
            int(self.inputs["entry_iso"].get() or 100),
            self.inputs["entry_shutter"].get().strip(),
            self.inputs["entry_aperture"].get().strip(),
            int(self.rating_cb.get()),
            self.status_cb.get(),
            self.selected_file_path,
            self.selected_photo_id,
        )
        cursor.execute(query, vals)
        conn.commit()
        cursor.close()
        conn.close()
        messagebox.showinfo("Success", "Record updated!")
        self.fetch_all_records()

    def delete_record(self):
        if not hasattr(self, "selected_photo_id"):
            messagebox.showwarning(
                "Selection Error", "Select a record from table to delete!"
            )
            return
        if messagebox.askyesno(
            "Confirm Delete", "Are you sure you want to delete this record?"
        ):
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "DELETE FROM photographs WHERE photo_id=%s",
                (self.selected_photo_id,),
            )
            conn.commit()
            cursor.close()
            conn.close()
            self.clear_entries()
            self.fetch_all_records()

    def search_records(self):
        cat = self.search_entry.get().strip()
        if not cat:
            return
        for item in self.tree.get_children():
            self.tree.delete(item)

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM photographs WHERE category LIKE %s", (f"%{cat}%",)
        )
        rows = cursor.fetchall()
        for r in rows:
            self.tree.insert(
                "",
                "end",
                values=(
                    r[0],
                    r[1],
                    r[2],
                    r[3],
                    r[4],
                    r[5],
                    r[6],
                    r[10],
                    r[11],
                ),
            )
        cursor.close()
        conn.close()

    def show_analytics(self):
        conn = get_connection()
        df = pd.read_sql("SELECT * FROM photographs", conn)
        conn.close()
        if df.empty:
            messagebox.showinfo("Analytics", "No data available!")
            return
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
        df["category"].value_counts().plot(
            kind="bar", ax=ax1, color="#0284c7", edgecolor="black"
        )
        ax1.set_title("Photographs per Category")
        df["rating"].value_counts().plot(
            kind="pie", ax=ax2, autopct="%1.1f%%", startangle=90
        )
        ax2.set_title("Rating Distribution")
        plt.tight_layout()
        plt.show()

    def export_csv(self):
        conn = get_connection()
        df = pd.read_sql("SELECT * FROM photographs", conn)
        conn.close()
        df.to_csv("portfolio_backup.csv", index=False)
        messagebox.showinfo("Export", "Saved as 'portfolio_backup.csv'!")

    def clear_entries(self):
        for entry in self.inputs.values():
            entry.delete(0, tk.END)
        self.rating_cb.set(5)
        self.status_cb.set("Final")
        self.selected_file_path = ""
        self.image_label.config(image="", text="No Image Selected")
        if hasattr(self, "selected_photo_id"):
            del self.selected_photo_id

if __name__ == "__main__":
    root = tk.Tk()
    app = LensLogApp(root)
    root.mainloop()
