import tkinter as tk
from tkinter import messagebox
import csv

# Test data in csv 
# import random
# # สร้างข้อมูลสุ่มสำหรับนักศึกษา 20 รายการ
# data = []
# for i in range(20):
#     student_id = f"ID{i+1}"
#     name = f"Name{i+1}"
#     last_name = f"LastName{i+1}"
#     username = f"User{i+1}"
#     password = f"Password{i+1}"
#     status = random.choice(["มาเรียน", "ลา", "ลากิจ"])
#     data.append([student_id, name, last_name, username, password, status])
# # บันทึกข้อมูลลงในไฟล์ student.csv
# with open('student.csv', mode='w', newline='', encoding='utf-8') as file:
#     writer = csv.writer(file)
#     writer.writerow(["รหัสนักศึกษา", "ชื่อ", "นามสกุล", "ชื่อผู้ใช้", "รหัสผ่าน", "สถานะ"])
#     writer.writerows(data)
# print("สร้างข้อมูลนักศึกษาสำเร็จ")

def write_to_report_csv(data):
    file_name = 'report.csv'
    with open(file_name, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(data)

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
        student_id = find_student_id_by_username(entered_username)
        messagebox.showinfo("เข้าสู่ระบบสำเร็จ", "เข้าสู่ระบบสำเร็จ")
        open_check_in_form(student_id)  # เมื่อเข้าสู่ระบบสำเร็จให้เปิดหน้าเช็คชื่อโดยส่งรหัสนักศึกษาไปด้วย
        
        # ปิดหน้าต่างล็อกอินหลังจากเข้าสู่ระบบสำเร็จ

        # open_check_in_form()

def find_student_id_by_username(username):
    # อ่านไฟล์ CSV และค้นหารหัสนักศึกษาจาก username
    with open('student.csv', mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # ข้ามหัวของไฟล์ CSV
        for row in reader:
            if row[3] == username:
                return row[0]  # รหัสนักศึกษาถูกพบ

    return None  # หากไม่พบ username ในไฟล์ CSV

def register_student(student_id_entry, name_entry, last_name_entry, username_entry, password_entry):
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
            open_register_form.root.destroy()
            # open_login_form()  # เมื่อสมัครเสร็จให้

def open_login_form():
    if not hasattr(open_login_form, "root"):
        open_login_form.root = tk.Toplevel()
        open_login_form.root.title("หน้าล็อกอิน")
        description_label = tk.Label(open_login_form.root, text="กรุณาป้อนชื่อผู้ใช้และรหัสผ่านเพื่อเข้าสู่ระบบ")
        description_label.pack()
        username_label = tk.Label(open_login_form.root, text="ชื่อผู้ใช้: ")
        username_label.pack()
        username_entry = tk.Entry(open_login_form.root)
        username_entry.pack()
        password_label = tk.Label(open_login_form.root, text="รหัสผ่าน: ")
        password_label.pack()
        password_entry = tk.Entry(open_login_form.root, show='*')
        password_entry.pack()
        login_button = tk.Button(open_login_form.root, text="เข้าสู่ระบบ", command=login)
        login_button.pack()

def open_register_form():
    open_register_form.root = tk.Toplevel()
    open_register_form.root.title("หน้าลงทะเบียน")
    
    description_label = tk.Label(open_register_form.root, text="กรุณากรอกข้อมูลเพื่อลงทะเบียน")
    description_label.pack()
    
    student_id_label = tk.Label(open_register_form.root, text="รหัสนักศึกษา: ")
    student_id_label.pack()
    student_id_entry = tk.Entry(open_register_form.root)
    student_id_entry.pack()
    
    name_label = tk.Label(open_register_form.root, text="ชื่อ: ")
    name_label.pack()
    name_entry = tk.Entry(open_register_form.root)
    name_entry.pack()
    
    last_name_label = tk.Label(open_register_form.root, text="นามสกุล: ")
    last_name_label.pack()
    last_name_entry = tk.Entry(open_register_form.root)
    last_name_entry.pack()
    
    username_label = tk.Label(open_register_form.root, text="ชื่อผู้ใช้: ")
    username_label.pack()
    username_entry = tk.Entry(open_register_form.root)
    username_entry.pack()
    
    password_label = tk.Label(open_register_form.root, text="รหัสผ่าน: ")
    password_label.pack()
    password_entry = tk.Entry(open_register_form.root, show='*')
    password_entry.pack()
    
    register_button = tk.Button(open_register_form.root, text="สมัครเข้าเรียน", command=lambda: register_student(student_id_entry, name_entry, last_name_entry, username_entry, password_entry))
    register_button.pack()

# สร้างหน้าต่างเช็คชื่อ
def open_check_in_form(student_id):
    check_in_root = tk.Tk()
    check_in_root.title("หน้าเช็คชื่อ")

    # สร้างเลือกสถานะ (มา, ลากิจ, ลาป่วย)
    status_label = tk.Label(check_in_root, text="เลือกสถานะ:")
    status_label.pack()

    status_var = tk.StringVar()
    status_var.set("มา")  # ตั้งค่าสถานะเริ่มต้นเป็น "มา"

    status_options = ["มา", "ลากิจ", "ลาป่วย"]
    status_menu = tk.OptionMenu(check_in_root, status_var, *status_options)
    status_menu.pack()

    # สร้างปุ่มบันทึก
    def save_check_in():
        selected_status = status_var.get()

        if student_id:
            # บันทึกข้อมูลลงใน report.csv
            data = [student_id, selected_status]
            write_to_report_csv(data)
            messagebox.showinfo("บันทึกสถานะสำเร็จ", "บันทึกสถานะเรียบร้อยแล้ว")
            root.destroy();
            check_in_root.destroy()  # ปิดหน้าต่างเช็คชื่อหลังจากบันทึกสถานะสำเร็จ
        else:
            messagebox.showerror("ข้อผิดพลาด", "ไม่พบรหัสนักศึกษา")

    save_button = tk.Button(check_in_root, text="บันทึก", command=save_check_in)
    save_button.pack()

    check_in_root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("โปรแกรมเช็คชื่อนักศึกษา")

    # สร้าง GUI หลักในนี้ (ปุ่มเรียกใช้งานหน้าอื่น ๆ)
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

    # สร้างปุ่มสำหรับลงทะเบียน
    register_button = tk.Button(root, text="ลงทะเบียน", command=open_register_form)
    register_button.pack()

    root.mainloop()







