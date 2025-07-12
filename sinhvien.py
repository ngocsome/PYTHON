class Sinhvien : 
    def __init__(self , hoTen , queQuan , lop , diem_1 , diem_2  ) : # khởi taoj , self là bắt buộc 
        self.hoTen = hoTen 
        self.queQuan = queQuan 
        self.lop = lop 
        self.diem_1 = diem_1 
        self.diem_2 = diem_2 


    # phương thức của lớp 
    def tinhdiemTB(self ) : 
        dtb = ( self.diem_1 * 4 + self.diem_2 * 5 ) / 9 
        return round ( dtb , 2 ) # làm tròn chữ số sau phần thập phân 

    def xeploai(self , dtb ) : 
        if dtb  < 5 : 
            print ( " Xếp loại yếu ")
        elif 5 < dtb < 7 : 
            print ( " Xếp loại trung bình ")
        elif 7 < dtb < 8 : 
            print ( " Xếp loại khá ")
        else : 
            print ( " Xếp loại giỏi ")



sv1 = Sinhvien("Ngọc  " , " Phú Thọ  " , " KTPM-02 " , 8 , 9 )
print ( type(sv1))
sv2 = Sinhvien("Thạch ", "Thanh Hóa " , " KTPM-02" , 9 , 7 )

# truy cập vào và in ra 
print (sv1.hoTen , "," , sv1.queQuan , "," , sv1.lop ,"," , sv1.tinhdiemTB())
print(sv2.hoTen,"," , sv2.queQuan,"," , sv2.lop , "," , sv2.tinhdiemTB())

# gọi phương thức xếp loại 
print( " Xếp loại của : " , sv1.hoTen)
sv1.xeploai ( sv1.tinhdiemTB()) # vì xeploai cần truyền vào tham số \
print(" Xếp loại của : " , sv2.hoTen)
sv2.xeploai( sv2.tinhdiemTB())



