import matplotlib.pyplot as plt

# ขนาดของสี่เหลี่ยม
width = 6
height = 4

# จุดมุมทั้ง 4
A = (0, 0)
B = (width, 0)
C = (width, height)
D = (0, height)

# สร้างพิกัดสำหรับวาดเส้นปิดรูป
x = [A[0], B[0], C[0], D[0], A[0]]
y = [A[1], B[1], C[1], D[1], A[1]]

# วาดรูป
plt.plot(x, y, 'b-', linewidth=2)
plt.fill(x, y, 'skyblue', alpha=0.3)

# ใส่ข้อความแสดงความยาวด้าน
plt.text((A[0] + B[0])/2, A[1] - 0.3, f"{width} ", ha='center')  # ด้านล่าง
plt.text((D[0] + C[0])/2, D[1] + 0.2, f"{width} ", ha='center')  # ด้านบน
plt.text(A[0] - 0.5, (A[1] + D[1])/2, f"{height} ", va='center', rotation=90)  # ด้านซ้าย
plt.text(B[0] + 0.3, (B[1] + C[1])/2, f"{height} ", va='center', rotation=90)  # ด้านขวา

# ใส่ชื่อจุด A, B, C, D
plt.text(A[0] - 0.2, A[1] - 0.2, 'A')
plt.text(B[0] + 0.1, B[1] - 0.2, 'B')
plt.text(C[0] + 0.1, C[1] + 0.1, 'C')
plt.text(D[0] - 0.2, D[1] + 0.1, 'D')

# ตั้งค่ากราฟ
plt.title("Rectangle with Side Length Labels")
plt.axis('equal')
plt.grid(True)

# แสดงผล
plt.show()
