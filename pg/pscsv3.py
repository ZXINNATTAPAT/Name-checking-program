import csv
import tkinter as tk
from tkinter import messagebox

def is_student_id_duplicate(student_id):
    # อ่านข้อมูลจากไฟล์ CSV และตรวจสอบรหัสนักศึกษาซ้ำ
    try:
        with open('รายชื่อนักศึกษา.csv', mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                if row and row[2] == student_id:
                    return True
    except FileNotFoundError:
        return False  # ถ้าไฟล์ CSV ยังไม่มี

    return False

def write_to_csv(data):
    # ระบุชื่อไฟล์ CSV ที่คุณต้องการสร้างหรือใช้งาน
    file_name = 'รายชื่อนักศึกษา.csv'

    # เปิดไฟล์ CSV สำหรับเขียนโดยใช้คำสั่ง open() และระบุการใช้ UTF-8 ในการเขียน
    with open(file_name, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)  # สร้างเครื่องมือสำหรับเขียน CSV

        for row in data:
            writer.writerow(row)

def register_student():
    รหัสนักศึกษา = student_id_entry.get()
    ชื่อ = name_entry.get()
    นามสกุล = last_name_entry.get()
    ชื่อผู้ใช้ = username_entry.get()
    รหัสผ่าน = password_entry.get()
    
    if รหัสนักศึกษา and ชื่อ and นามสกุล and ชื่อผู้ใช้ and รหัสผ่าน:
        if is_student_id_duplicate(รหัสนักศึกษา):
            messagebox.showerror("ข้อผิดพลาด", "รหัสนักศึกษาซ้ำกัน")
        else:
            data = [รหัสนักศึกษา, ชื่อ, นามสกุล, ชื่อผู้ใช้, รหัสผ่าน, "มาเรียน"]
            write_to_csv([data])
            messagebox.showinfo("สำเร็จ", "สมัครเข้าเรียนสำเร็จ")
            student_id_entry.delete(0, tk.END)
            name_entry.delete(0, tk.END)
            last_name_entry.delete(0, tk.END)
            username_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)
    else:
        messagebox.showerror("ข้อผิดพลาด", "กรุณากรอกข้อมูลทุกช่อง")


def open_check_in_form():
    root.destroy()  # ปิดหน้าต่างหลักหลังจากเข้าสู่ระบบสำเร็จ
    check_in_form()  # เมื่อเข้าสู่ระบบสำเร็จให้เปิดหน้าต่างเช็คชื่อ

# สร้างหน้าต่างเช็คชื่อ
def check_in_form():
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
        student_id = entered_student_id.get()
        selected_status = status_var.get()

        if student_id:
            # บันทึกข้อมูลลงใน report.csv
            data = [student_id, selected_status]
            write_to_report_csv(data)
            messagebox.showinfo("บันทึกสถานะสำเร็จ", "บันทึกสถานะเรียบร้อยแล้ว")
        else:
            messagebox.showerror("ข้อผิดพลาด", "กรุณาป้อนรหัสนักศึกษา")

    save_button = tk.Button(check_in_root, text="บันทึก", command=save_check_in)
    save_button.pack()

    # สร้างช่องป้อนข้อมูลสำหรับรหัสนักศึกษา
    student_id_label = tk.Label(check_in_root, text="รหัสนักศึกษา:")
    student_id_label.pack()

    entered_student_id = tk.Entry(check_in_root)
    entered_student_id.pack()

    check_in_root.mainloop()
    
# สร้างหน้าต่างหลักของ tkinter
root = tk.Tk()
root.title("โปรแกรมเช็คชื่อนักศึกษา")

# สร้างกล่องข้อความแสดงคำอธิบาย
description_label = tk.Label(root, text="ป้อนข้อมูลสำหรับการสมัครเข้าเรียน:")
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

# สร้างปุ่มสำหรับออกจากโปรแกรม
quit_button = tk.Button(root, text="ออก", command=root.quit)
quit_button.pack()

# เริ่มการทำงานของหน้าต่าง tkinter
root.mainloop()
