import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

#หาพื้นที่ด้วย ชอลเลสฟอมูล่า
#เเสดงผลกราฟ

#พื้นที่วงกลม
def CircleArea(radius):
    area = 3.14 * (radius**2)
    return print("พท.วงกลมนะ = ",area)
CircleArea(5)

#พื้นที่สามเหลี่ยมทั่วไป
def TriangleArea(base, height):
    area = 1/2 *base*height
    return print("พท.สามเหลี่ยมทั่วไป =",area)
TriangleArea(4,5)

# คำสั่งสะเเควรูท ==> math.sqrt(3)  
## พื้นที่สามเหลี่ยมด้านเท่า
def EquilateralTriangleArea(side):
    area = math.sqrt(3)/4*(side)**2
    return print("พท.สามเหลี่ยมด้านเท่า =",area)
EquilateralTriangleArea(6)

## พื้นที่สามเหลี่ยมหน้าจั่ว 
def IsoscelesTriangleArea(base,hieght):
    area = 1/2*base*hieght
    return print("พท.สามเหลี่ยมหน้าจั่ว=",area)
IsoscelesTriangleArea(6,3)

## พื้นที่สามเหลี่ยมด้านไม่เท่า
def ScaleneTriangleArea(sideA, sideB, sideC):
    
    return print("ไม่มีอะไร",sideA, sideB, sideC)


# พื้นที่รูปสี่เหลี่ยมจตุรัศ
def SquareArea(side):
    area = side*side
    return print("พท.รูปสี่เหลี่ยมจตุรัศ=",area)
SquareArea(4)

# พื้นที่สี่เหลี่ยมผืนผ้า
def RectangleArea(length,width):
    area = length*width
    return print("พื้นที่สี่เหลี่ยมผืนผ้า=",area)
RectangleArea(3,6)

# พื้นที่ห้าเหลี่ยม
# perimeter = ความยาวด้าน
def PentagonArea(perimeter, apothem):
    area = 1/2*perimeter*apothem
    return print("พท.ห้าเหลี่ยม=",area)
PentagonArea(4,4)

# พื้นที่หกเหลี่ยม
def HexagonArea(length):
    area = (3*math.sqrt(3)*(length**2))/2
    return print("พท.หกเหลี่ยม=",area)
HexagonArea(6)