from utils import greet
"""from math_tools import (
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
)"""

import matplotlib.pyplot as plt #ใช้วาดกราฟ

side,unit = 0,"เมตร" #ค่าเริ่มต้น

#ฟังชั่นตรวจสอบการป้อนค่า
array_units = [
    [['มิลลิเมตร'],[0.001]],  # 1 มม. = 0.001 เมตร
    [['เซนติเมตร'],[0.01]],   # 1 ซม. = 0.01 เมตร
    [['นิ้ว'],[0.0254]],      # 1 นิ้ว = 0.0254 เมตร
    [['เมตร'],[1.0]],    # 1 เมตร = 1 เมตร
    [['วา'],[2.0]],   # 1 วา = 2 เมตร
    [['กิโลเมตร'],[1000.0]] # 1 กม. = 1000 เมตร
]

def validate_input(side, unit):
    array_units_text = [] #เก็บชื่อหน่วยที่ใช้ได้
    
    #ตรวจว่า side เป็นตัวเลข จำนวนเต็ม
    if side != int(side) and side != float(side):
        return False, "ค่าที่ป้อนไม่ใช่ตัวเลข"
    elif side == float(side):
        return False, "ค่าที่ป้อนต้องเป็นจำนวนเต็ม"
    elif side < 1:
        return False, "ป้อนเป็นจำนวนเต็มบวก"

    #ตรวจว่าค่ามุมไม่ติดลบ
    if side < 0:
        return False, "มุมห้ามติดลบ"
    
    for i in range(len(array_units)):
        array_units_text.append(array_units[i])
    #ตรวจว่าหน่วยอยู่ในลิสที่อนุญาตให้ใช้
    if unit not in array_units:
        return False, f"หน่วยไม่ถูกต้อง: {unit} (ใช้ได้เเค่ {', '.join(array_units)})"
    return True, f"รับข้อมูลแล้ว: จน.มุม {side}, หน่วย {unit}"

# validate_input(-5, 'กิโลเมตร')
# is_valid, message = validate_input(side, unit)
# print(message)


# ใช้หาพื้นที่เเบบทั่วไป
# ใช้หาพื้นที่เเบบทั่วไป
def basic_area():
    print("เลือกหน่วยของคุณ")
    for i in range(len(array_units)):
        if i < (len(array_units)-1):
            print(array_units[i][0][0], ",", end='')
        else:
            print(array_units[i][0][0])

    name_unit = ''
    unit_input = input("--> ป้อนหน่วยของคุณ: ")

    # เเปลงหน่วยไปเป็นเมตรทั้งหมด 
    for i in range(len(array_units)):
        if unit_input == array_units[i][0][0]:
            real_unit = array_units[i][1][0] 
            name_unit = array_units[i][0][0] 

    # ตรวจสอบว่าป้อนหน่วยที่รองรับหรือไม่
    if name_unit == '':
        print("## หน่วยที่คุณป้อนไม่รองรับ ป้อนอีกครั้ง ##")
        return basic_area()
    
    print(f'>>> คุณเลือกหน่วย ตาราง{unit_input}')

    type_shap = ""
    # ฟังชั่นระบุรูปทรง
    def what_shape(side_many):
        try:
            side_many = int(input("--> ป้อนจำนวนด้าน: "))
        except ValueError:
            print("กรุณาป้อนเป็นตัวเลขจำนวนเต็มเท่านั้น")
            return what_shape(0)
    
        type_shap = ''
    
        if side_many == 0:
            type_shap = "วงกลม"
        elif side_many == 3:
            type_shap = "สามเหลี่ยม"
        elif side_many == 4:
            type_shap = "สี่เหลี่ยม"
        elif side_many == 5:
            type_shap = "ห้าเหลี่ยม"
        elif side_many == 6:
            type_shap = "หกเหลี่ยม"
        elif side_many == 1 or side_many == 2:
            print("ไม่มีรูปทรงที่มีจำนวนด้านแค่ 1 และ 2 กรอกใหม่อีกครั้ง")
            return what_shape(0)
        else:
            print("รองรับแค่ 0-6 ด้าน กรอกใหม่อีกครั้ง")
            return what_shape(0)

        print(">>> คุณต้องการหาพื้นที่รูปทรง", type_shap)
        return type_shap
    
    what_shape(0)
        

#วิธีการใช้งาน + เปิดโปรเเกรม
print("ยินดีต้อนรับสู่โปรเเกรมหาพื้นที่\nหาพื้นที่เเบบไหนดี?\n1. พิกัดจุด/2. ปกติ")

def start_program():
    while True:
        try:
            type_calculator = int(input("--> ป้อนเลขตัวเลือก: "))
            if type_calculator == 1:
                print(">>> คุณเลือกการคำนวณแบบ พิกัดจุด")
                print("***** ทำงานการคำนวณพิกัดจุด *****")
                break
            elif type_calculator == 2:
                print(">>> คุณเลือกการคำนวณแบบ ทั่วไป")
                basic_area()
                break
            else:
                print("โปรดป้อนเป็นตัวเลข 1 หรือ 2 เท่านั้น")
        except ValueError: #ถ้าเออเร่อจะโยนออกมาที่ทันที
            print("กรุณาป้อนเป็นตัวเลข ไม่ใช่ตัวอักษรหรือสัญลักษณ์")

start_program() #เริ่มทำงานทั้งหมด