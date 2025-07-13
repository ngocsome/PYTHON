class Rectangle : 
    def __init__( self , chieu_dai , chieu_rong) : 
        self.chieu_dai = chieu_dai 
        self.chieu_rong = chieu_rong 

    def __str__(self):
        return ( f'Chiều dài : {self.chieu_dai} , Chiều rộng : {self.chieu_rong}')
    
    def tinh_dien_tich ( self ) : 
        return ( self.chieu_dai * self.chieu_rong) 
    
    def tinh_chu_vi ( self ) : 
        return ( ( self.chieu_dai + self.chieu_rong) * 2 )
    
    def save_file(self, filename="Rectangle_data.txt"):
        """
        Phương thức lưu chiều dài và chiều rộng của hình chữ nhật vào một file.
        Mỗi thuộc tính sẽ được ghi trên một dòng riêng biệt.
        """
        try:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(f'Chiều dài: {self.chieu_dai}\n')  # Ghi chiều dài và xuống dòng
                f.write(f'Chiều rộng: {self.chieu_rong}\n') # Ghi chiều rộng và xuống dòng
            print("Đã lưu dữ liệu vào", filename)
        except IOError:
            print("Không lưu được dữ liệu vào file.")
        except Exception as e:
            print(f"Đã xảy ra lỗi không mong muốn khi lưu file: {e}")


def nhap() : 
    while True : 
        try : 
            length = float (input(" Nhập chiều dai : ")) 
            width = float( input ("Nhập chiều rộng ")) 
            if length <= 0 or width <= 0 : 
                print ( " Nhập sai rồi đmm !!! ")
            else : 
                return Rectangle(length , width )
        except : 
            print ( " Nhập cho đúng dcm ")

                
    
def main() : 
   rectangle = None
   while True : 
        print ( " ====MENU==== ") 
        print ( " 1. Nhập hình chữ nhật ") 
        print ( " 2. Lưu chiều dài chiều rộng vào file  ")
        print ( " 3. Tính chu vi ") 
        print ( " 4. Tính diện tích ") 
        print ( " 5. Thoát ")
        choice = ( input(" Nhập lựa chọn : "))

        if choice == '1' : 
            rectangle = nhap() 
        elif choice =='2' : 
            filename = "rectangle_data.txt"
            rectangle.save_file() 
        elif choice == '3' : 
            if rectangle : 
                print ( f'Chu vi hình chữ nhật :{rectangle.tinh_chu_vi()}') 
            else : 
                print ( "Lỗi ")
        elif choice == '4' : 
            if rectangle : 
                print (f'Diện tích hình chữ nhật : {rectangle.tinh_dien_tich()}') 
            else : 
                print ("Lỗi ") 
        elif choice =='5' : 
            break 
        else : 
            print ( " Chọn cho đúng !!! ") 

if __name__ == "__main__" : 
    main()      

       
  

