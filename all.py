import math

#หาพื้นที่ด้วย ชอลเลสฟอมูล่า
#เเสดงผลกราฟ

#พื้นที่วงกลม
def CircleArea(radius,unit):
    area = 3.14 * (radius**2)
    return print("พท.วงกลม = ",area," ตาราง",unit)

# คำสั่งสะเเควรูท ==> math.sqrt(3)  
## พื้นที่สามเหลี่ยมด้านเท่า
def EquilateralTriangleArea(side,unit):
    area = math.sqrt(3)/4*(side)**2
    return print("พท.สามเหลี่ยมด้านเท่า =",area," ตาราง",unit)
#EquilateralTriangleArea(6)

## พื้นที่สามเหลี่ยมหน้าจั่ว 
def IsoscelesTriangleArea(base,hieght,unit):
    area = 1/2*base*hieght
    return print("พท.สามเหลี่ยมหน้าจั่ว=",area," ตาราง",unit)
#IsoscelesTriangleArea(6,3)

# พื้นที่สามเหลี่ยมด้านไม่เท่า (ใช้สูตรเฮรอน)
def ScaleneTriangleArea(sideA, sideB, sideC, unit):
    # คำนวณครึ่งหนึ่งของรอบรูป (semiperimeter)
    s = (sideA + sideB + sideC) / 2

    # ตรวจสอบว่าด้านทั้งสามสามารถสร้างสามเหลี่ยมได้หรือไม่
    if (sideA + sideB > sideC) and (sideA + sideC > sideB) and (sideB + sideC > sideA):
        # สูตรเฮรอน
        area = math.sqrt(s * (s - sideA) * (s - sideB) * (s - sideC))
        return print(f"พื้นที่สามเหลี่ยมด้านไม่เท่า = {area:.2f} ตาราง{unit}")
    else:
        return print("ไม่สามารถสร้างสามเหลี่ยมจากด้านที่ป้อนมา")

# พื้นที่รูปสี่เหลี่ยมจตุรัศ
def SquareArea(side,unit):
    area = side*side
    return print("พท.รูปสี่เหลี่ยมจตุรัศ=",area," ตาราง",unit)
#SquareArea(4)

# พื้นที่สี่เหลี่ยมผืนผ้า
def RectangleArea(length,width,unit):
    area = length*width
    return print("พื้นที่สี่เหลี่ยมผืนผ้า=",area," ตาราง",unit)
#RectangleArea(3,6)

#สี่เหลี่ยมคางหมู
def TrapezoidArea(base1, base2, height, unit):
    area = (base1 + base2) / 2 * height
    return print(f"พื้นที่สี่เหลี่ยมคางหมู = {area:.2f} ตาราง{unit}")

# พื้นที่ห้าเหลี่ยม
# perimeter = ความยาวด้าน
def PentagonArea(perimeter, apothem,unit):
    area = 1/2*perimeter*apothem
    return print("พท.ห้าเหลี่ยม =",area," ตาราง",unit)
#PentagonArea(4,4)

# พื้นที่หกเหลี่ยม
def HexagonArea(length,unit):
    area = (3*math.sqrt(3)*(length**2))/2
    return print("พท.หกเหลี่ยม =",area," ตาราง",unit)
#HexagonArea(6)

import matplotlib.pyplot as plt #ใช้วาดกราฟ

#ฟังชั่นตรวจสอบการป้อนค่า
array_units = [
    ['มิลลิเมตร',0.001],# 1 มม. = 0.001 เมตร
    ['เซนติเมตร',0.01],   # 1 ซม. = 0.01 เมตร
    ['นิ้ว',0.0254],# 1 นิ้ว = 0.0254 เมตร
    ['เมตร',1.0], # 1 เมตร = 1 เมตร
    ['วา',2.0], # 1 วา = 2 เมตร
    ['กิโลเมตร',1000.0] # 1 กม = 1000 เมตร
]

side_many = 0 #จำนวนด้าน
name_unit = 'ค่าเริ่มต้น' #ชื่อหน่วย
type_shap = 'ค่าเริ่มต้น' #ชนิดของรูปทรง
real_unit = 0 #ตัวเเปลงหน่วย เซนติเมตร 0.01

#ฟังชั่นเเยกว่าต้องใช้สูตรหาพื้นที่ไหน
def choose(type_shap,name_unit):
    if type_shap == "วงกลม":
        while True:
            try:
                r = int(input("--> ป้อนรัศมี: "))
                CircleArea(r,name_unit)
                break
            except ValueError:
                print("กรุณาป้อนตัวเลขจำนวนเต็มเท่านั้น")
    elif type_shap == "สามเหลี่ยม":
        print("สามเหลี่ยมที่คุณต้องการคำนวณ มีลักษณะอย่างไร?")
        print("1. ด้านทั้ง 3 ไม่เท่ากัน")
        print("2. ด้านทั้ง 3 เท่ากัน")
        print("3. ด้าน 2 ข้างเท่ากัน ฐานไม่เท่า")

        number_input = 0
        while True:
            try:
                number_input = int(input("--> ป้อนหมายเลข: "))

                if number_input == 1:
                    print(">>> คุณเลือก: สามเหลี่ยมด้านไม่เท่า")
                    sideA = float(input("--> ป้อนด้าน A: "))
                    sideB = float(input("--> ป้อนด้าน B: "))
                    sideC = float(input("--> ป้อนด้าน C: "))
                    ScaleneTriangleArea(sideA, sideB, sideC, name_unit)
                    break
                elif number_input == 2:
                    print(">>> คุณเลือก: สามเหลี่ยมด้านเท่า")
                    side = float(input("--> ป้อนความยาวด้าน: "))
                    EquilateralTriangleArea(side, name_unit)
                    break
                elif number_input == 3:
                    print(">>> คุณเลือก: สามเหลี่ยมหน้าจั่ว")
                    base = float(input("--> ป้อนฐาน: "))
                    height = float(input("--> ป้อนสูง: "))
                    IsoscelesTriangleArea(base, height, name_unit)
                    break
                else:
                    print("กรุณาป้อนเฉพาะเลข 1, 2 หรือ 3 เท่านั้น")
                    break
            except ValueError:
                print("กรุณาป้อนตัวเลขจำนวนเต็มเท่านั้น")
    elif type_shap == "สี่เหลี่ยม":
        print("ลักษณะของสี่เหลี่ยมที่คุณต้องการคำนวณคือแบบไหน?")
        print("1. ด้านทุกด้านเท่ากัน (สี่เหลี่ยมจัตุรัส)")
        print("2. ด้านตรงข้ามเท่ากัน (สี่เหลี่ยมผืนผ้า)")
        print("3. มีฐานคู่ขนาน (สี่เหลี่ยมคางหมู)")

        while True:
            try:
                choice = int(input("--> ป้อนหมายเลข: "))
                if choice == 1:
                    print(">>> คุณเลือก: สี่เหลี่ยมจัตุรัส")
                    side = float(input("--> ป้อนความยาวด้าน: "))
                    SquareArea(side,name_unit)
                    break
                elif choice == 2:
                    print(">>> คุณเลือก: สี่เหลี่ยมผืนผ้า")
                    length = float(input("--> ป้อนความยาว: "))
                    width = float(input("--> ป้อนความกว้าง: "))
                    RectangleArea(length,width,name_unit)
                    break
                elif choice == 3:
                    print(">>> คุณเลือก: สี่เหลี่ยมคางหมู")
                    base1 = float(input("--> ป้อนความยาวฐานบน: "))
                    base2 = float(input("--> ป้อนความยาวฐานล่าง: "))
                    height = float(input("--> ป้อนความสูง: "))
                    TrapezoidArea(base1, base2, height, name_unit)
                    break
                else:
                    print("กรุณาป้อนหมายเลข 1-3 เท่านั้น")
            except ValueError:
                print("กรุณาป้อนตัวเลขจำนวนเต็มเท่านั้น")
    elif type_shap == "ห้าเหลี่ยม":
        while True:
            try:
                perimeter = float(input("--> ความยาวด้าน: "))
                apothem = float(input("--> ระยะกึ่งกลาง: "))
                PentagonArea(perimeter, apothem,name_unit)
                break
            except ValueError:
                print("กรุณาป้อนเเค่ตัวเลข")
    if type_shap == "หกเหลี่ยม":
        while True:
            try:
                length = float(input("--> ความยาวด้าน: "))
                HexagonArea(length,name_unit)
                break
            except ValueError:
                print("กรุณาป้อนเเค่ตัวเลข")

# ใช้หาพื้นที่เเบบทั่วไป
def basic_area():
    name_unit = ''
    print("เลือกหน่วยของคุณ")
    for i in range(len(array_units)):
        if i < (len(array_units)-1):
            print(array_units[i][0], ",", end='')
        else:
            print(array_units[i][0])
    unit_input = input("--> ป้อนหน่วยของคุณ: ")

    # เเปลงหน่วยไปเป็นเมตรทั้งหมด 
    for i in range(len(array_units)):
        if unit_input == array_units[i][0]:
            real_unit = array_units[i][1] 
            name_unit = array_units[i][0] 

    # ตรวจสอบว่าป้อนหน่วยที่รองรับหรือไม่
    if name_unit == '':
        print("## หน่วยที่คุณป้อนไม่รองรับ ป้อนอีกครั้ง ##")
        return basic_area()
    print(f'>>> คุณเลือกหน่วย ตาราง{unit_input}')

    # ฟังชั่นระบุรูปทรง
    def what_shape(side_many,name_unit):
        try:
            side_many = int(input("--> ป้อนจำนวนด้าน: "))
        except ValueError:
            print("กรุณาป้อนเป็นตัวเลขจำนวนเต็มเท่านั้น")
            return what_shape(0,name_unit)
    
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
            return what_shape(0,name_unit)
        else:
            print("รองรับแค่ 0-6 ด้าน กรอกใหม่อีกครั้ง")
            return what_shape(0,name_unit)
        print(">>> คุณต้องการหาพื้นที่รูปทรง", type_shap)
        return choose(type_shap,name_unit)
    what_shape(0,name_unit)
        
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
