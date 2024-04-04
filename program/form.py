# form.py

import tkinter as tk
import login
import register

# สร้างหน้าหลัก
root = tk.Tk()
root.title("โปรแกรมเช็คชื่อนักศึกษา")

def open_login_form():
    login.login()
    
def open_register_form():
    register.register_student()

# สร้างปุ่มเรียกใช้หน้าล็อกอิน
login_button = tk.Button(root, text="เข้าสู่ระบบ", command=open_login_form)
login_button.pack()

# สร้างปุ่มเรียกใช้หน้าลงทะเบียน
register_button = tk.Button(root, text="ลงทะเบียน", command=open_register_form)
register_button.pack()

# เริ่มการทำงานของหน้าหลัก
root.mainloop()
