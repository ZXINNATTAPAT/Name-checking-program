import csv

# ระบุชื่อไฟล์ CSV ที่คุณต้องการสร้างหรือใช้งาน
file_name = 'รายชื่อนักเรียน.csv'

# เปิดไฟล์ CSV สำหรับเขียนโดยใช้คำสั่ง open() และระบุการใช้ UTF-8 ในการเขียน
with open(file_name, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)  # สร้างเครื่องมือสำหรับเขียน CSV

    # สร้างหัวของไฟล์ CSV
    header = ['ชื่อ', 'สถานะ']
    writer.writerow(header)

    while True:
        # แสดงเมนูตัวเลือก
        print("โปรดเลือกเพื่อทำรายการ:")
        print("1. สมัครเข้าเรียน")
        print("2. ลาเรียน")
        print("3. ลากิจ")
        print("4. สร้างรายงาน (CSV)")
        print("5. ออก")
        
        choice = input("กรุณาเลือกหมายเลข: ")
        
        if choice == '1':
            ชื่อ = input('ป้อนชื่อของนักเรียน: ')
            writer.writerow([ชื่อ, 'มาเรียน'])
        elif choice == '2':
            ชื่อ = input('ป้อนชื่อของนักเรียน: ')
            writer.writerow([ชื่อ, 'ลาเรียน'])
        elif choice == '3':
            ชื่อ = input('ป้อนชื่อของนักเรียน: ')
            writer.writerow([ชื่อ, 'ลากิจ'])
        elif choice == '4':
            print("สร้างรายงาน CSV สำเร็จ")
        elif choice == '5':
            break
        else:
            print("กรุณาเลือกหมายเลขที่ถูกต้อง")

print(f'ข้อมูลถูกบันทึกลงในไฟล์ CSV ชื่อ {file_name}')
