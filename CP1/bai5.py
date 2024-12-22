#bai5
# Nhập tuổi từ người dùng
tuoi = int(input("Nhập tuổi của bạn: "))

# Kiểm tra độ tuổi và tính giá vé
if tuoi < 12:
    gia_ve = 50000
elif 12 <= tuoi <= 60:
    gia_ve = 100000
else:
    gia_ve = 70000

# In kết quả giá vé
print(f"Giá vé: {gia_ve} VNĐ")
