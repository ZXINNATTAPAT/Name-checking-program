# login.py

import tkinter as tk
from tkinter import messagebox
import csv

def is_valid_login(username, password):
    with open('student.csv', mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # ข้ามหัวของไฟล์ CSV
        for row in reader:
            if row[3] == username and row[4] == password:
                return True
    return False

def login():
    entered_username = username_entry.get()
    entered_password = password_entry.get()

    if is_valid_login(entered_username, entered_password):
        messagebox.showinfo("เข้าสู่ระบบสำเร็จ", "เข้าสู่ระบบสำเร็จ")
        root.destroy()  # ปิดหน้าต่างล็อกอินหลังจากเข้าสู่ระบบสำเร็จ
    else:
        messagebox.showerror("ข้อผิดพลาด", "ชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง")
        username_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)

# สร้างหน้าต่างล็อกอิน
root = tk.Tk()
root.title("หน้าล็อกอิน")

# สร้างกล่องข้อความแสดงคำอธิบาย
description_label = tk.Label(root, text="กรุณาป้อนชื่อผู้ใช้และรหัสผ่านเพื่อเข้าสู่ระบบ")
description_label.pack()

# สร้างช่องป้อนข้อมูลสำหรับชื่อผู้ใช้
username_label = tk.Label(root, text="ชื่อผู้ใช้: ")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

# สร้างช่องป้อนข้อมูลสำหรับรหัสผ่าน
password_label = tk.Label(root, text="รหัสผ่าน: ")
password_label.pack()
password_entry = tk.Entry(root, show='*')
password_entry.pack()

# สร้างปุ่มสำหรับเข้าสู่ระบบ
login_button = tk.Button(root, text="เข้าสู่ระบบ", command=login)
login_button.pack()

# เริ่มการทำงานของหน้าต่างล็อกอิน
root.mainloop()
