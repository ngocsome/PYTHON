# khởi tạo 1 tuple 
t = ( " 123 " , " 234 " , "456") 

convert = tuple ( int ( x ) for x in t ) # chuyển đổi từ string sag int 

tb = sum(convert) / len( convert ) 

print ( " Tuple được khởi tạo " , convert ) 
print ( " Trung bình cộng : " , tb)

# Khởi tạo tập hợp mã sinh viên
A = {"SV001", "SV002", "SV003", "SV005"}
B = {"SV003", "SV004", "SV005", "SV006"}

# In hai tập hợp
print("Sinh viên đăng ký tại bàn 1:", A)
print("Sinh viên đăng ký tại bàn 2:", B)

# Sinh viên đăng ký tại cả hai bàn
both = A & B
if both:
    print("Sinh viên đăng ký tại cả hai bàn:", both)
else:
    print("Không có sinh viên nào đăng ký tại cả hai bàn.")

# Danh sách tổng hợp (hợp của A và B)
all_students = A | B
print("Danh sách tổng hợp sinh viên đã đăng ký:", all_students)

# Sinh viên đăng ký tại bàn 1 mà không đăng ký tại bàn 2
only_A = A - B
print("Sinh viên chỉ đăng ký tại bàn 1:", only_A)
