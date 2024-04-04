import csv

# ระบุชื่อไฟล์ CSV ที่คุณต้องการสร้างหรือใช้งาน
file_name = 'ข้อมูล.csv'

# เปิดไฟล์ CSV สำหรับเขียนโดยใช้คำสั่ง open() และระบุการใช้ UTF-8 ในการเขียน
with open(file_name, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)  # สร้างเครื่องมือสำหรับเขียน CSV

    # สร้างหัวของไฟล์ CSV (หากต้องการ)
    header = ['ชื่อ', 'อายุ', 'เพศ']
    writer.writerow(header)

    while True:
        # รับข้อมูลจากผู้ใช้
        ชื่อ = input('ป้อนชื่อ (หรือพิมพ์ "จบ" เพื่อออก): ')
        if ชื่อ.lower() == 'จบ':
            break
        อายุ = input('ป้อนอายุ: ')
        เพศ = input('ป้อนเพศ: ')

        # เขียนข้อมูลลงในไฟล์ CSV
        writer.writerow([ชื่อ, อายุ, เพศ])

print(f'ข้อมูลถูกบันทึกลงในไฟล์ CSV ชื่อ {file_name}')

 
# filecsv = datacheck.csv
# with open(filecsv, mode='w', newline='', encoding='utf-8') as file: