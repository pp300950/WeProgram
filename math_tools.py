import matplotlib.pyplot as plt
import math

array_units = [
    ['มิลลิเมตร', 0.001],
    ['เซนติเมตร', 0.01],
    ['นิ้ว', 0.0254],
    ['เมตร', 1.0],
    ['วา', 2.0],
    ['กิโลเมตร', 1000.0]
]

#การคำนวณประเภทพิกัดจุด ด้วยคู่อันดับ
def plot_polygon_simple(vertices,unit):
    x_coords = [] # สร้างลิสต์ว่างสำหรับเก็บพิกัด X
    y_coords = [] # สร้างลิสต์ว่างสำหรับเก็บพิกัด Y

    # วนลูปผ่านแต่ละจุดยอดในลิสต์ vertices
    #เช่น [[1,2], [3,4], [5,6]]
    #          v     v+1   v+2
    # v[1,2]  -->  v[0] = 1

    for v in vertices: #ลูปเเยกอาเรย์ของเเกน X = 1,3,5 | Y = 2,4,6
        x_coords.append(v[0])
        y_coords.append(v[1]) # เพิ่มพิกัด Y ของจุดยอดปัจจุบันเข้าไปใน y_coords

    # เพิ่มพิกัดของจุดยอดแรกเข้าไปในลิสต์เป็นตัวสุดท้าย เพื่อให้รูปปิด
    # vertices = [(1, 2), (4, 2), (3, 5), (1, 4)]
    # vertices[2] = (3,5)
    # vertices[2][1] = 5

    # ( 1,2 )
    x_coords.append(vertices[0][0]) # (index,X ตัวเเรก) => 1
    y_coords.append(vertices[0][1]) # (index,Y ตัวเเรก) => 2

    # วนลูปเพื่อคำนวณผลรวมของการคูณลงและคูณขึ้น

    sum_down = 0  # ผลรวมของการคูณลง
    sum_up = 0    # ผลรวมของการคูณขึ้น

    num_vertices = len(vertices) # เก็บจำนวนจุดยอดไว้ในตัวแปรเพื่อความสะดวก

    for i in range(len(vertices)):
        # กำหนดดัชนีของจุดยอดถัดไป
        next_i = i + 1

        # ถ้า next_i เกินขอบเขตของลิสต์ (คือถึงจุดสุดท้ายแล้ว)
        # ให้วนกลับไปใช้จุดยอดแรกสุด (ดัชนี 0)
        if next_i == num_vertices:
            next_i = 0

        # การคูณลง: x_i * y_{i+1}
        sum_down += vertices[i][0] * vertices[next_i][1]

        # การคูณขึ้น: y_i * x_{i+1}
        sum_up += vertices[i][1] * vertices[next_i][0]

    area = 0.5 * abs(sum_down - sum_up)
    print(f"พท.รูปหลายเหลี่ยม = {area:.2f} ตาราง{unit}")

    # วาดรูปหลายเหลี่ยม
    plt.plot(x_coords, y_coords, 'o-')

    # เพิ่ม label ให้กับจุดยอด
    # vertices = [(1,2),(4,5),(6,7)]
    # enumerate(vertices) = (1,2) = เเล้วเอาไปยัดลง (x,y)
    # ควรทราบว่า คำสั่งมันส่งค่าออกเเบบนี้
    # (index, (x_coord, y_coord))
    for i, (x, y) in enumerate(vertices):
        plt.text(x + 0.1, y + 0.1, f'({x},{y})', fontsize=10, color='red')

    # กำหนดชื่อกราฟ แสดงพื้นที่ และตั้งค่าแกน
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.show()
    return area


def convert_unit_to_english(unit_th, array_units):
    """แปลงชื่อหน่วยวัดจากภาษาไทยเป็นอังกิด
    พารมิเต้อ
    unit_th (str): ชื่อหน่วยวัดภาษาไทย (เช่น 'เมตร')
    array_units(list): รายการของหน่วยวัดแต่ละหน่วย

    โยนค่าคืน
    tuple: (ชื่อหน่วยภาษาอังกฤษ, ค่าตัวเลขสำหรับแปลงหน่วย) ถ้าพบหน่วยนั้น
           (None, None) ถ้าไม่พบหน่วยนั้น
    """
    
    unit_map = {
        'มิลลิเมตร': ('millimeter', 0.001),
        'เซนติเมตร': ('centimeter', 0.01),
        'นิ้ว': ('inch', 0.0254),
        'เมตร': ('meter', 1.0),
        'วา': ('wa', 2.0),
        'กิโลเมตร': ('kilometer', 1000.0)
    }

    if unit_th in unit_map:
        return unit_map[unit_th]

#unit_thai = "เมตร"
#english_unit, value = convert_unit_to_english(unit_thai, array_units)

# พื้นที่วงกลม
def CircleArea(radius, unit):
    unit_thai = unit
    english_unit, value = convert_unit_to_english(unit_thai, array_units)

    area = 3.14 * (radius**2)
    
    # สร้างกราฟวงกลม
    fig, ax = plt.subplots()
    circle = plt.Circle((0, 0), radius, fill=False, color='blue')
    ax.add_artist(circle)
    
    plt.plot([0, radius], [0, 0], 'r--')
    plt.text(radius/2, 0.2, f'Radius: {radius} {english_unit}', ha='center', color='red')
    
    plt.xlim(-radius - 1, radius + 1)
    plt.ylim(-radius - 1, radius + 1)
    plt.gca().set_aspect('equal', adjustable='box')
    print(f"พท.วงกลมนะ = {area:.2f} ตาราง{unit}")
    plt.show()
    return area
#CircleArea(5, "เมตร")

# math.sqrt(3)==> คำสั่งสเเควรูท
# พื้นที่สามเหลี่ยมด้านเท่า
def EquilateralTriangleArea(side, unit):
    unit_thai = unit
    english_unit, value = convert_unit_to_english(unit_thai, array_units)

    area = (math.sqrt(3) / 4) * (side**2)
    
    #จุดยอด
    h = (math.sqrt(3) / 2) * side # หาสูง
    points = [(-side/2, 0), (side/2, 0), (0, h)]
    
    #กราฟ
    fig, ax = plt.subplots()
    polygon = plt.Polygon(points, closed=True, fill=False, edgecolor='blue')
    ax.add_patch(polygon)
    
    #ความยาวด้าน
    plt.text(0, -0.5, f"Side: {side} {english_unit}", ha='center')
    plt.gca().set_aspect('equal', adjustable='box')
    print(f"พท.สามเหลี่ยมด้านเท่า = {area:.2f} ตาราง{unit}")
    plt.show()
    return area

# พื้นที่สามเหลี่ยมหน้าจั่ว
def IsoscelesTriangleArea(base, height, unit):
    unit_thai = unit
    english_unit, value = convert_unit_to_english(unit_thai, array_units)
    area = 0.5 * base * height
    
    #จุดยอด
    points = [(-base/2, 0), (base/2, 0), (0, height)]
    
    fig, ax = plt.subplots()
    polygon = plt.Polygon(points, closed=True, fill=False, edgecolor='blue')
    ax.add_patch(polygon)
    
    #ความยาวด้าน
    plt.text(0, -0.5, f"Base: {base} {english_unit}", ha='center')
    plt.plot([0, 0], [0, height], 'r--')
    plt.text(0.5, height/2, f"Height: {height} {unit}", ha='left')
    
    plt.gca().set_aspect('equal', adjustable='box')
    print(f"พท.สามเหลี่ยมหน้าจั่ว = {area:.2f} ตาราง{unit}")
    plt.show()
    return area
#IsoscelesTriangleArea(2, 5,"หน่วย")

# พื้นที่สามเหลี่ยมด้านไม่เท่า (ใช้สูตรเฮรอน)
def ScaleneTriangleArea(sideA, sideB, sideC, unit):
    unit_thai = unit
    english_unit, value = convert_unit_to_english(unit_thai, array_units)
   
    if not (sideA + sideB > sideC and sideA + sideC > sideB and sideB + sideC > sideA):
        return print("ไสร้างสามเหลี่ยมจากด้านที่ป้อนมาไม่ได้")
    
    s = (sideA + sideB + sideC) / 2
    area = math.sqrt(s * (s - sideA) * (s - sideB) * (s - sideC))
    
    #จุดยอด
    x2 = sideC
    x3 = (sideA**2 - sideB**2 + sideC**2) / (2 * sideC)
    y3 = math.sqrt(sideA**2 - x3**2)
    points = [(0, 0), (x2, 0), (x3, y3)]
    
    fig, ax = plt.subplots()
    polygon = plt.Polygon(points, closed=True, fill=False, edgecolor='blue')
    ax.add_patch(polygon)
    
    plt.text(sideC/2, -0.5, f"Side C: {sideC} {english_unit}", ha='center')
    plt.gca().set_aspect('equal', adjustable='box')
    print(f"พท.สามเหลี่ยมด้านไม่เท่า = {area:.2f} ตาราง{unit}")
    plt.show()
    return area

# พื้นที่รูปสี่เหลี่ยมจัตุรัส
def SquareArea(side, unit):
    unit_thai = unit
    english_unit, value = convert_unit_to_english(unit_thai, array_units)
   
    area = side * side

    fig, ax = plt.subplots()
    rect = plt.Rectangle((0, 0), side, side, fill=False, edgecolor='blue')
    ax.add_patch(rect)
    plt.text(side/2, -0.5, f"Side: {side} {english_unit}", ha='center')

    plt.xlim(-1, side + 1)
    plt.ylim(-1, side + 1)
    plt.gca().set_aspect('equal', adjustable='box')
    print(f"พท.รูปสี่เหลี่ยมจตุรัส = {area:.2f} ตาราง{unit}")
    plt.show()
    return area

# พื้นที่สี่เหลี่ยมผืนผ้า
def RectangleArea(length, width, unit):
    unit_thai = unit
    english_unit, value = convert_unit_to_english(unit_thai, array_units)
   
    area = length * width
    
    fig, ax = plt.subplots()
    rect = plt.Rectangle((0, 0), length, width, fill=False, edgecolor='blue')
    ax.add_patch(rect)
    
    plt.text(length/2, -0.5, f"Length: {length} {english_unit}", ha='center')
    plt.text(-0.5, width/2, f"Width: {width} {english_unit}", va='center', rotation=90)
    
    plt.xlim(-1, length + 1)
    plt.ylim(-1, width + 1)
    plt.gca().set_aspect('equal', adjustable='box')
    print(f"พื้นที่สี่เหลี่ยมผืนผ้า = {area:.2f} ตาราง{unit}")
    plt.show()
    return area
#RectangleArea(2, 3, "เมตร")

# พื้นที่สี่เหลี่ยมคางหมู
def TrapezoidArea(base1, base2, height, unit):
    unit_thai = unit
    english_unit, value = convert_unit_to_english(unit_thai, array_units)
   
    area = (base1 + base2) / 2 * height
    
    #จุดยอด
    points = [(0, 0), (base1, 0), ((base1-base2)/2 + base2, height), ((base1-base2)/2, height)]
    fig, ax = plt.subplots()
    polygon = plt.Polygon(points, closed=True, fill=False, edgecolor='blue')
    ax.add_patch(polygon)
    
    plt.text(base1/2, -0.5, f"Base1: {base1} {english_unit}", ha='center')
    plt.text((base1-base2)/2 + base2/2, height + 0.5, f"Base2: {base2} {english_unit}", ha='center')
    plt.plot([0, 0], [0, height], 'r--')
    plt.text(-0.5, height/2, f"Height: {height} {english_unit}", va='center')
    
    plt.gca().set_aspect('equal', adjustable='box')
    print(f"พื้นที่สี่เหลี่ยมคางหมู = {area:.2f} ตาราง{unit}")
    plt.show()
    return area

# พื้นที่ห้าเหลี่ยม
def PentagonArea(side, unit):
    unit_thai = unit
    english_unit, value = convert_unit_to_english(unit_thai, array_units)
   
    #apothem
    apothem = side / (2 * math.tan(3.14 / 5))
    area = (2.5 * side * apothem)
    
    #จุดยอด
    points = []
    angle_offset = 3.14 / 2
    for i in range(5):
        angle = 2 * 3.14 * i / 5 + angle_offset
        x = apothem * math.tan(3.14 / 5) * math.cos(angle) + 0.5 * side
        y = apothem * math.tan(3.14 / 5) * math.sin(angle) + apothem
        points.append((x, y))
    
    fig, ax = plt.subplots()
    polygon = plt.Polygon(points, closed=True, fill=False, edgecolor='blue')
    ax.add_patch(polygon)

    for i in range(5):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % 5]
        xm, ym = (x1 + x2) / 2, (y1 + y2) / 2
        plt.text(xm, ym, f"Side: {side} {english_unit}", ha='center', rotation=math.degrees(math.atan2(y2 - y1, x2 - x1)))
    
    plt.gca().set_aspect('equal', adjustable='box')
    print(f"พท.ห้าเหลี่ยม = {area:.2f} ตาราง{unit}")
    plt.show()
    return area
# PentagonArea(5, "เมตร")

# พื้นที่หกเหลี่ยม
def HexagonArea(length, unit):
    unit_thai = unit
    english_unit, value = convert_unit_to_english(unit_thai, array_units)
   
    area = (3 * math.sqrt(3) * (length**2)) / 2
    
    #จุดยอด
    points = []
    for i in range(6):
        angle_rad = math.pi / 3 * i
        x = length * math.cos(angle_rad)
        y = length * math.sin(angle_rad)
        points.append((x, y))
        
    fig, ax = plt.subplots()
    polygon = plt.Polygon(points, closed=True, fill=False, edgecolor='blue')
    ax.add_patch(polygon)
    
    for i in range(6):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % 6]
        xm, ym = (x1 + x2) / 2, (y1 + y2) / 2
        plt.text(xm, ym, f"Side: {length} {english_unit}", ha='center', rotation=math.degrees(math.atan2(y2 - y1, x2 - x1)))
    
    plt.gca().set_aspect('equal', adjustable='box')
    print(f"พท.หกเหลี่ยม = {area:.2f} ตาราง{unit}")
    plt.show()
    return area
# HexagonArea(10, "หน่วย")
