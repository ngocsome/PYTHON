''' Thực hiện các yêu cầu sau:
• Xây dựng lớp PERSON gồm các thông tin: Họ và tên, Ngày sinh, Quê quán.
• Sau đó, xây dựng lớp dẫn xuất KYSU ngoài các thông tin của lớp Person, lớp
KYSU còn có các thông tin về: Ngành học, Năm tốt nghiệp và các phương thức
thực hiện:
o Khởi tạo thông tin của kỹ sư.
o In các thông tin lên màn hình.
• Nhập vào một danh sách n kỹ sư. In danh sách của các kỹ sư lên màn hình và
thông tin của các kỹ sư tốt nghiệp gần đây nhất (năm tốt nghiệp lớn nhất).''' 

class Person : 
    def __init__ ( self , hoten , ngaysinh , quequan ) : 
        self.hoten = hoten 
        self.ngaysinh = ngaysinh 
        self.quequan = quequan 

    def hienthi( self ) : 
        pass 

class Kisu ( Person ) : 
    def __init__(self, hoten, ngaysinh, quequan , nganh , nam ):
        super().__init__(hoten, ngaysinh, quequan)
        self.nganh = nganh 
        self.nam = nam 
    def hienthi( self ) : 
        print (f'Tên : {self.hoten}') 
        print ( f'Ngày sinh : {self.ngaysinh} , Quê quán : {self.quequan}') 
        print ( f'Ngành học : {self.nganh} , Năm tốt nghiệp : {self.nam}') 
    
def main() : 
    n = int ( input ( " Nhập số kĩ sư muốn thêm vào danh sách : ")) 
    danhsach = []
    for i in range ( n ) : 
        print ( " Nhập thông tin của kĩ sư thứ " , i + 1 ) 
        ten = input ( " Nhập tên : ") 
        sinh = input ( " Nhập ngày sinh : ") 
        que = input ( " Nhập quê quán : ") 
        nganh = input ( " Nhập ngành học : ") 
        namtn = input ( " Nhập năm tốt nghiệp : ") 
        new = Kisu ( ten , sinh , que , nganh , namtn )
        danhsach.append ( new )
        
    print ( " Thông tin kĩ sư : ") 
    for i in danhsach : 
        i.hienthi() 

if __name__ == "__main__" : 
    main()



    
    