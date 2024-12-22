#bai2
# Nhập hai số thực từ người dùng
a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))

# Cộng, trừ, nhân, chia
tong = a + b
hieu = a - b
tich = a * b

# Kiểm tra điều kiện chia cho 0
if b != 0:
    thuong = a / b
else:
    thuong = "Không thể chia cho 0"

# In kết quả
print(f"Tổng: {tong}")
print(f"Hiệu: {hieu}")
print(f"Tích: {tich}")
print(f"Thương: {thuong}")
