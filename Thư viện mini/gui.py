# gui.py

import tkinter as tk
from tkinter import messagebox
from sach import Sach

class QuanLySachGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Quản Lý Sách Cơ Bản")
        self.danh_sach = []

        # Form nhập
        tk.Label(root, text="Mã sách:").grid(row=0, column=0, sticky="e")
        tk.Label(root, text="Tên sách:").grid(row=1, column=0, sticky="e")
        tk.Label(root, text="Tác giả:").grid(row=2, column=0, sticky="e")
        tk.Label(root, text="Năm XB:").grid(row=3, column=0, sticky="e")

        self.ent_ma = tk.Entry(root)
        self.ent_ten = tk.Entry(root)
        self.ent_tacgia = tk.Entry(root)
        self.ent_nam = tk.Entry(root)

        self.ent_ma.grid(row=0, column=1, padx=5, pady=2)
        self.ent_ten.grid(row=1, column=1, padx=5, pady=2)
        self.ent_tacgia.grid(row=2, column=1, padx=5, pady=2)
        self.ent_nam.grid(row=3, column=1, padx=5, pady=2)

        tk.Button(root, text="Thêm sách", command=self.them_sach).grid(row=4, column=0, columnspan=2, pady=5)

        # Danh sách hiển thị
        self.lst_sach = tk.Listbox(root, width=50, height=10)
        self.lst_sach.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

    def them_sach(self):
        ma = self.ent_ma.get()
        ten = self.ent_ten.get()
        tac_gia = self.ent_tacgia.get()
        try:
            nam = int(self.ent_nam.get())
        except ValueError:
            messagebox.showerror("Lỗi", "Năm xuất bản phải là số!")
            return

        sach = Sach(ma, ten, tac_gia, nam)
        self.danh_sach.append(sach)
        self.lst_sach.insert(tk.END, str(sach))

        # Xoá nội dung các ô nhập
        self.ent_ma.delete(0, tk.END)
        self.ent_ten.delete(0, tk.END)
        self.ent_tacgia.delete(0, tk.END)
        self.ent_nam.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = QuanLySachGUI(root)
    root.mainloop()
