import math 
class PT : 
    def __init__(self , a , b , c ) : 
        self.a = a 
        self.b = b 
        self.c = c 
    
    def tinh_delta ( self ) : 
        delta = ( self.b * self.b )- (4 * self.a * self.c ) 
        return delta 

    def tinh_nghiem(self , delta) : 
        if delta < 0 : 
            print ("Phương trình vô nghiệm !!! ") 
        elif delta == 0 : 
            x = - self.b / ( 2 *  self.a) 
            print ( " Phương tình có nghiệm kép : " , x )
        else : 
            x1 = ( - self.b + math.sqrt(delta)) / ( 2 * self.a)
            x2 = ( - self.b  - math.sqrt(delta)) / ( 2 * self.a)
            print ( " Phương trình có 2 nghiệm : " , x1 , x2 )

def nhapPT() : 
    a = float ( input("Nhập hệ số a : ")) 
    b = float ( input("Nhập hệ số b : ")) 
    c = float ( input ("Nhập hệ số c : "))  
    pt1=PT( a , b , c )
    return pt1 
def luu_file(pt1) : 
    with open("pt2.text" , "w" , encoding = "utf_8") as file  : 
        file.write(str(pt1.a) + "\n") 
        file.write(str(pt1.b) + "\n")
        file.write(str(pt1.c) + "\n ")
        print ("Đã ghi dữ liệu vào file ")
def doc_file(pt1) : 
     with open("pt2.text" , "r" , encoding = "utf_8") as file  : 
         a = float ( file.readline())
         b = float ( file .readline()) 
         c = float ( file .readline()) 
         pt1 = PT ( a , b , c ) 
         print (pt1)
       
def main() : 
   while True : 
       print ("-----Menu-----")
       print (" 1.Nhập hệ số  ") 
       print("2.Tính nghiệm ") 
       print("3.Lưu vào file ")
       print("4.Đọc từ file ")
       choice = int (input("Nhập lựa chọn : ") )
       if choice == 1 : 
           pt1=nhapPT() 
       elif choice == 2 : 
           delta=pt1.tinh_delta() 
           pt1.tinh_nghiem(delta)
       elif choice == 3 : 
           luu_file(pt1) 
           
       elif choice == 4 : 
           doc_file(pt1) 

           

main()
