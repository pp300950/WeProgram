import matplotlib.pyplot as plt #ใช้วาดกราฟ
import math
import sys

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


# รับค่าเเเบบพิกัดจุด
def input_vertices(): # สำหรับอินพุตค่าพิกัดจุด
    vertices = []
    num_points = int(input("--> ป้อนจำนวนจุดของรูปหลายเหลี่ยม: "))
    
    for i in range(num_points):
        while True:
            try:
                user_input = input(f"--> ป้อนพิกัดจุดที่ {i+1} (รูปแบบ: x y): ")
                x_str, y_str = user_input.strip().split()
                x, y = float(x_str), float(y_str)
                vertices.append((x, y))
                break
            except ValueError:
                print("## รูปแบบไม่ถูกต้อง กรุณาป้อนใหม่ เช่น: 3 4")
    
    return vertices


#ฟังก์ชันสำหรับแสดงหน่วยวัดที่มีให้เลือก ยกเว้นหน่วยปัจจุบัน
def show_available_units(current_unit):
    for i, unit_info in enumerate(array_units):
        unit_name = unit_info[0]
        if unit_name != current_unit:
            print(f"{i+1}. {unit_name}")

area = 0 #ตัวเเปรพื้นที่ที่ผู้ใช้ต้องการเเปลง

#ฟังก์ชันสำหรับจัดการหลังจากคำนวณพื้นที่เสร็จ
def after_stare():
    print("คุณยังต้องการอะไรอีกไหม?\n1. กลับไปหน้าเริ่มต้น\n2. ต้องการเเปลงหน่วย\n3. หาปริมาตร\n4. ออกจากโปรเเกรม")
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
            elif choice == 4:
                print(">>> คุณเลือก: ออกจากโปรเเกรม")
                print("#### ไปไหนก็ไป ชิ้วๆ ###\n  \n████████╗██╗  ██╗ █████╗ ███╗   ██╗██╗  ██╗\n╚══██╔══╝██║  ██║██╔══██╗████╗  ██║██║ ██╔╝\n   ██║   ███████║███████║██╔██╗ ██║█████╔╝\n   ██║   ██╔══██║██╔══██║██║╚██╗██║██╔═██╗\n   ██║   ██║  ██║██║  ██║██║ ╚████║██║  ██╗\n   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝  \n                thank you for use!")
                sys.exit()
            
            else:
                print("กรุณาป้อนหมายเลข 1-4 เท่านั้น")
        except ValueError:
            print("กรุณาป้อนตัวเลขจำนวนเต็มเท่านั้น")
            

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

def Unit_finder():
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
        return start_program()
    
    print(f'>>> คุณเลือกหน่วย ตาราง{unit_input}')
    return name_unit

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

# ใช้หาพื้นที่เเบบทั่วไป
def basic_area():
    global area, name_unit
    name_unit = ''
    
    Unit_finder() #เรียกใช้ฟังก์ชันเพื่อเลือกหน่วย

    area = what_shape(0, name_unit) 
    after_stare() 

#วิธีการใช้งาน + เปิดโปรเเกรม
def start_program():
    print("ยินดีต้อนรับสู่โปรเเกรมหาพื้นที่\nหาพื้นที่เเบบไหนดี?\n1. พิกัดจุด/2. ปกติ")
    while True:
        try:
            type_calculator = int(input("--> ป้อนเลขตัวเลือก: "))
            if type_calculator == 1:
                global area, name_unit
                name_unit = ''
                
                print(">>> คุณเลือกการคำนวณแบบ พิกัดจุด")
                vertices_quad = input_vertices()
                print(">>> พิกัดที่ได้:", vertices_quad)
                name_unit = Unit_finder() #เรียกใช้ฟังก์ชันเพื่อเลือกหน่วย
                plot_polygon_simple(vertices_quad,name_unit)
                
                after_stare()
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
