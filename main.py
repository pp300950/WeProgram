from math_tools import ( #นำเข้าสูตรคำนวรพื้นที่ทั้งหดม
    CircleArea,
    TrapezoidArea,
    EquilateralTriangleArea,
    IsoscelesTriangleArea,
    ScaleneTriangleArea,
    SquareArea,
    RectangleArea,
    PentagonArea,
    HexagonArea
)
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
area = 0 #ตัวเเปรพื้น

#ฟังชั่นเเยกว่าต้องใช้สูตรหาพื้นที่ไหน
def choose(type_shap,name_unit):
    if type_shap == "วงกลม":
        while True:
            try:
                r = int(input("--> ป้อนรัศมี: "))
                area = CircleArea(r,name_unit)
                return area
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
                    area = ScaleneTriangleArea(sideA, sideB, sideC, name_unit)
                    return area
                elif number_input == 2:
                    print(">>> คุณเลือก: สามเหลี่ยมด้านเท่า")
                    side = float(input("--> ป้อนความยาวด้าน: "))
                    area = EquilateralTriangleArea(side, name_unit)
                    return area
                elif number_input == 3:
                    print(">>> คุณเลือก: สามเหลี่ยมหน้าจั่ว")
                    base = float(input("--> ป้อนฐาน: "))
                    height = float(input("--> ป้อนสูง: "))
                    area = IsoscelesTriangleArea(base, height, name_unit)
                    return area
                else:
                    print("กรุณาป้อนเฉพาะเลข 1, 2 หรือ 3 เท่านั้น")
                    break
            except ValueError:
                print("กรุณาป้อนตัวเลขจำนวนเต็มเท่านั้น")
    elif type_shap == "สี่เหลี่ยม":
        print("ลักษณะของสี่เหลี่ยมที่คุณต้องการคำนวณคือแบบไหน?")
        print("1. ด้านทุกด้านเท่ากัน")
        print("2. ด้านตรงข้ามเท่ากัน")
        print("3. มีฐานคู่ขนาน")

        while True:
            try:
                choice = int(input("--> ป้อนหมายเลข: "))
                if choice == 1:
                    print(">>> คุณเลือก: สี่เหลี่ยมจัตุรัส")
                    side = float(input("--> ป้อนความยาวด้าน: "))
                    area = SquareArea(side,name_unit)
                    return area
                elif choice == 2:
                    print(">>> คุณเลือก: สี่เหลี่ยมผืนผ้า")
                    length = float(input("--> ป้อนความยาว: "))
                    width = float(input("--> ป้อนความกว้าง: "))
                    area = RectangleArea(length,width,name_unit)
                    return area
                elif choice == 3:
                    print(">>> คุณเลือก: สี่เหลี่ยมคางหมู")
                    base1 = float(input("--> ป้อนความยาวฐานบน: "))
                    base2 = float(input("--> ป้อนความยาวฐานล่าง: "))
                    height = float(input("--> ป้อนความสูง: "))
                    area = TrapezoidArea(base1, base2, height, name_unit)
                    return area
                else:
                    print("กรุณาป้อนหมายเลข 1-3 เท่านั้น")
            except ValueError:
                print("กรุณาป้อนตัวเลขจำนวนเต็มเท่านั้น")
    elif type_shap == "ห้าเหลี่ยม":
        while True:
            try:
                perimeter = float(input("--> ความยาวด้าน: "))
                apothem = float(input("--> ระยะกึ่งกลาง: "))
                area = PentagonArea(perimeter, apothem,name_unit)
                return area
            except ValueError:
                print("กรุณาป้อนเเค่ตัวเลข")
    if type_shap == "หกเหลี่ยม":
        while True:
            try:
                length = float(input("--> ความยาวด้าน: "))
                area = HexagonArea(length,name_unit)
                return area
            except ValueError:
                print("กรุณาป้อนเเค่ตัวเลข")
    return area

# ใช้หาพื้นที่เเบบทั่วไป
def basic_area():
    global area, name_unit
    name_unit = ''
    
    print("เลือกหน่วยของคุณ")
    for i in range(len(array_units)):
        if i < (len(array_units)-1):
            print(array_units[i][0], ",", end='')
        else:
            print(array_units[i][0])
            
    unit_input = input("--> ป้อนหน่วยของคุณ: ")

    for i in range(len(array_units)):
        if unit_input == array_units[i][0]:
            real_unit = array_units[i][1] 
            name_unit = array_units[i][0] 

    if name_unit == '':
        print("## หน่วยที่คุณป้อนไม่รองรับ ป้อนอีกครั้ง ##")
        return basic_area()
    
    print(f'>>> คุณเลือกหน่วย ตาราง{unit_input}')

    def what_shape(side_many, name_unit):
        try:
            side_many = int(input("--> ป้อนจำนวนด้าน: "))
        except ValueError:
            print("กรุณาป้อนเป็นตัวเลขจำนวนเต็มเท่านั้น")
            return what_shape(0,name_unit)
    
        shapes = {
            0: "วงกลม",
            3: "สามเหลี่ยม",
            4: "สี่เหลี่ยม",
            5: "ห้าเหลี่ยม",
            6: "หกเหลี่ยม"
        }

        if side_many in shapes:
            type_shap = shapes[side_many]
        elif side_many in (1, 2):
            print("ไม่มีรูปทรงที่มีจำนวนด้านแค่ 1 และ 2 กรอกใหม่อีกครั้ง")
            return what_shape(0, name_unit)
        else:
            print("รองรับแค่ 0-6 ด้าน กรอกใหม่อีกครั้ง")
            return what_shape(0, name_unit)
        
        print(">>> คุณต้องการหาพื้นที่รูปทรง", type_shap)
        return choose(type_shap, name_unit)
    
    area = what_shape(0, name_unit) 
    after_stare() 

#วิธีการใช้งาน + เปิดโปรเเกรม
def start_program():
    print("ยินดีต้อนรับสู่โปรเเกรมหาพื้นที่\nหาพื้นที่เเบบไหนดี?\n1. พิกัดจุด/2. ปกติ")
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

#ฟังก์ชันสำหรับแสดงหน่วยวัดที่มีให้เลือก ยกเว้นหน่วยปัจจุบัน
def show_available_units(current_unit):
    for i, unit_info in enumerate(array_units):
        unit_name = unit_info[0]
        if unit_name != current_unit:
            print(f"{i+1}. {unit_name}")

area = 0 #ตัวเเปรพื้นที่ที่ผู้ใช้ต้องการเเปลง

#ฟังก์ชันสำหรับจัดการหลังจากคำนวณพื้นที่เสร็จ
def after_stare():
    print("คุณยังต้องการอะไรอีกไหม?\n1. กลับไปหน้าเริ่มต้น\n2. ต้องการเเปลงหน่วย\n3. หาปริมาตร")
    while True:
        try:
            choice = int(input("--> ป้อนหมายเลข: "))
            if choice == 1:
                print(">>> คุณเลือก: กลับไปหน้าเริ่มต้น")
                start_program()
                break
            elif choice == 2:
                print(f">>> คุณเลือก: ต้องการเเปลงหน่วย\nคุณจะเเปลงหน่วยจาก ตาราง {name_unit} เป็นหน่วยอะไร?")
                show_available_units(name_unit)
                new_unit_index = int(input("--> ป้อนหมายเลขของหน่วยใหม่: ")) - 1
                if 0 <= new_unit_index < len(array_units):
                    old_multiplier = None
                    new_multiplier = array_units[new_unit_index][1]
                    new_unit_name = array_units[new_unit_index][0]
    
                    #หน่วยเดิม = multiplier
                    for unit_name, multiplier in array_units:
                        if unit_name == name_unit:
                            old_multiplier = multiplier
                            break
    
                    if old_multiplier is not None:
                        #คำนวนพื้นที่ทีแปงแล้ว
                        New_area = area * (old_multiplier ** 2) / (new_multiplier ** 2)
    
                        print(f">>> คุณได้แปลงพื้นที่จาก ตาราง{name_unit} เป็น {New_area:.4f} ตาราง{new_unit_name}")
                        after_stare()
                    else:
                        print("ไม่พบหน่วยเดิม")
                else:
                    print("คุณป้อนหมายเลขไม่ถูกต้อง")
                break
            
            elif choice == 3:
                print(">>> คุณเลือก: หาปริมาตร")
                heigth = float(int(input("--> ป้อนความสูง: ")))
                print(f'>>> ปริมาตรที่ได้คือ {area * heigth:.4f} ลูกบาศก์{name_unit}')
                after_stare()
                break
            else:
                print("กรุณาป้อนหมายเลข 1-3 เท่านั้น")
        except ValueError:
            print("กรุณาป้อนตัวเลขจำนวนเต็มเท่านั้น")
            