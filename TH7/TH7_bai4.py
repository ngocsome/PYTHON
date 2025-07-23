''' Sử dụng cách viết static duck typing, xây dựng chương trình để thông báo các thành
viên được khen thưởng trong năm học của một trường đại học. Tiêu chuẩn xét khen
thưởng:
• Sinh viên: điểm trung bình tích lũy (GPA) phải lớn hơn 3.2
• Giảng viên: có ít nhất hai công trình nghiên cứu khoa học.
• Người quản lý: hoàn thành tốt công việc được giao.
Xuất danh sách các người được khen thưởng gồm họ tên và bộ phận trực thuộc'''
class Sinhvien : 
    def __init__ ( self ,name ,  gpa ) : 
        self.name = name 
        self.gpa = gpa 
        self.department = " Sinh viên "
    def khen_thuong ( self ) : 
        return self.gpa > 3.2 

class Giangvien : 
    def __init__ ( self , name , nckh ) : 
        self.name = name 
        self.nckh = nckh 
        self.department = " Giảng viên " 
    def khen_thuong( self ) : 
        return self.nckh > 2 

class Quanly : 
    def __init__ ( self , name , hoan_thanh ) : 
        self.name = name 
        self.hoan_thanh = hoan_thanh 
        self.department = " Người quản lý "
    def khen_thuong ( self ) : 
        return self.hoan_thanh 

members = [
    Sinhvien("Nguyễn Văn A", 3.5),
    Sinhvien("Trần Thị B", 2.9),
    Giangvien("TS. Lê Văn C", 3),
    Giangvien("ThS. Phạm Thị D", 1),
    Quanly("Ngô Minh E", True),
    Quanly("Đỗ Thị F", False)
]

# Lọc danh sách những người được khen thưởng
print("Danh sách các thành viên được khen thưởng:")
for person in members:
    # Static duck typing: chỉ cần có phương thức is_awarded và thuộc tính name, department
    if person.khen_thuong() : 
        print(f"- {person.name} ({person.department})")

    
