from utils import greet
from math_tools import (
    CircleArea,
    TriangleArea,
    EquilateralTriangleArea,
    IsoscelesTriangleArea,
    ScaleneTriangleArea,
    SquareArea,
    RectangleArea,
    PentagonArea,
    HexagonArea,
    add
)

import matplotlib.pyplot as plt #ใช้วาดกราฟ

side,unit = 0,"เมตร"
#ฟังชั่นตรวจสอบการป้อนค่ากากๆ
def validate_input(side, unit):
    array_units_text = [] #เก็บชื่อหน่วยที่ใช้ได้
    array_units = [
        'มิลลิเมตร',
        'เซนติเมตร',
        'นิ้ว',
        'เมตร',
        'วา',
        'งาน',
        'ไร่',
        'กิโลเมตร'
    ]
    
    # ตรวจว่า value เป็นตัวเลข จำนวนเต็ม
    if side != int(side):
        return False, "ค่าที่ป้อนไม่ใช่ตัวเลข"

    #ตรวจว่าค่ามุมไม่ติดลบ
    if side < 0:
        return False, "มุมห้ามติดลบ"
    
    for i in range(len(array_units)):
        array_units_text.append(array_units[i])
    #ตรวจว่าหน่วยอยู่ในลิสที่อนุญาตให้ใช้
    if unit not in array_units:
        return False, f"หน่วยไม่ถูกต้อง: {unit} (ใช้ได้เเค่ {', '.join(array_units)})"
    return True, f"รับข้อมูลแล้ว: จน.มุม {side}, หน่วย {unit}"

is_valid, message = validate_input(side, unit)


validate_input(-5, 'กิโลเมตร')

print(message)
#วิธีการใช้งาน + เปิดโปรเเกรม
print("ยินดีต้อนรับสู่โปรเเกรมหาพื้นที่")

#รับหน่วยที่ใช้ ตาราง เมตร,ซม,นิ้ว,กิโลเมตร,วา,ไร่,งาน

#เเปลงหน่วยไปเป็นเมตรทั้งหมด

#รับจำนวนด้าน
Side_many = input("ป้อนจำนวนด้าน:")


