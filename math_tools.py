import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

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
