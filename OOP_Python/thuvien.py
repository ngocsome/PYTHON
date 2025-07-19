class Sach : 
    def __init__ ( self , masach , tensach , tacgia , nam ) : 
        self.masach = masach 
        self.tensach = tensach 
        self.tacgia = tacgia 
        self.nam = nam 
    def tim( self , ten ) : 
        return self.tacgia == ten.lower() 
    def __str__(self ) : 
        return  f" Mã sách : {self.masach} , Tên sách : {self.tensach} , Tác giả : {self.tacgia} , Năm XB : {self.nam}" 
    
def quan_ly() : 
    danhsach = [] 
    n = int ( input ( " Nhập số sách : ")) 
    for i in range ( 0  , n ) : 
        print ( " Nhập thông tin sách thứ : " , i + 1 )
        ma = input("Mã sách : ") 
        ten_sach = input("Tên sách : ") 
        tac_gia = input("Tác giả : ") 
        nam_XB = input("Năm xuất bản : ") 
        danhsach.append(Sach( ma , ten_sach, tac_gia , nam_XB)) 
    for s in danhsach : 
        print ( s )

def main() : 
    quan_ly() 
    

if __name__ == "__main__" : 
    main()