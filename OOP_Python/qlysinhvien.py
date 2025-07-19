class sinhVien : 
    def __init__( self , ma_sv , ten_sv , diem ) : 
        self.ma_sv = ma_sv 
        self.ten_sv = ten_sv 
        self.diem = diem 
    def xep_loai ( self ) : 
        if self.diem > 8 : 
            return " Giỏi " 
        elif 6 < self.diem < 8 : 
            return " Khá " 
        else : 
            return " Trung bình " 

    def __str__(self ) : 
        return f" Mã sinh viên : {self.ma_sv} - Tên sinh viên : {self.ten_sv} - Điểm : {self.diem} - Xếp loại : {self.xep_loai()}" 

class Lop : 
    def __init__ ( self ) : 
        self.danhsach = [] 
    
    def them (self , sv ) : 
        self.danhsach.append(sv) 

    
def quan_ly() : 
    lop = Lop() 
    n = int ( input ( " Nhập số sinh viên : ")) 
    for i in range ( n ) : 
        print ( " Nhập thông tin sinh viên thứ " , i + 1 , " : ") 
        ma = input("Nhập mã sinh viên : ") 
        ten = input ( " Nhập tên sinh viên : ") 
        diem = float ( input ( " Nhập điểm : ")) 
        lop.them( sinhVien ( ma , ten , diem )) 

    print ( " Danh sách sinh viên : ") 
    for sv in lop.danhsach : 
        print ( sv)
    
    
        
quan_ly()