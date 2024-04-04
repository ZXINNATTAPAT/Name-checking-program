# register.py

import tkinter as tk
from tkinter import messagebox
import csv

def is_student_id_duplicate(student_id):
    try:
        with open('student.csv', mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                if row and row[0] == student_id:
                    return True
    except FileNotFoundError:
        return False

    return False

def write_to_csv(data):
    file_name = 'student.csv'

    with open(file_name, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(data)

def register_student():
    student_id = student_id_entry.get()
    name = name_entry.get()
    last_name = last_name_entry.get()
    username = username_entry.get()
    password = password_entry.get()


    if student_id and name and last_name and username and password:
        if is_student_id_duplicate(student_id):
            messagebox.showerror("ข้อผิดพลาด", "รหัสนักศึกษาซ้ำกัน")
        else:
            data = [student_id, name, last_name, username, password, "มาเรียน"]
            write_to_csv(data)
            messagebox.showinfo("สำเร็จ", "สมัครเข้าเรียนสำเร็จ")
            student_id_entry.delete(0, tk.END)
            name_entry.delete(0, tk.END)
            last_name_entry.delete(0, tk.END)
            username_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)
    else:
        messagebox.showerror("ข้อผิดพลาด", "กรุณากรอกข้อมูลทุกช่อง")

# สร้างหน้าต่างลงทะเบียน
root = tk.Tk()
root.title("หน้าลงทะเบียน")

# สร้างกล่องข้อความแสดงคำอธิบาย
description_label = tk.Label(root, text="กรุณากรอกข้อมูลเพื่อลงทะเบียน")
description_label.pack()

# สร้างช่องป้อนข้อมูลสำหรับรหัสนักศึกษา
student_id_label = tk.Label(root, text="รหัสนักศึกษา: ")
student_id_label.pack()
student_id_entry = tk.Entry(root)
student_id_entry.pack()

# สร้างช่องป้อนข้อมูลสำหรับชื่อ
name_label = tk.Label(root, text="ชื่อ: ")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

# สร้างช่องป้อนข้อมูลสำหรับนามสกุล
last_name_label = tk.Label(root, text="นามสกุล: ")
last_name_label.pack()
last_name_entry = tk.Entry(root)
last_name_entry.pack()

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

# สร้างปุ่มสำหรับสมัครเข้าเรียน
register_button = tk.Button(root, text="สมัครเข้าเรียน", command=register_student)
register_button.pack()

# เริ่มการทำงานของหน้าต่างลงทะเบียน
root.mainloop()
