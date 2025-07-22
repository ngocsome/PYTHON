'''Thực hiện các yêu cầu sau:
• Xây dựng một lớp Hình chữ nhật bằng ngôn ngữ Python với các thuộc tính
chiều dài và chiều rộng.
• Tạo một phương thức Perimeter() để tính chu vi của hình chữ nhật và một
phương thức Area() để tính diện tích của hình chữ nhật.
• Tạo một phương thức display() hiển thị chiều dài, chiều rộng, chu vi và diện
tích của một đối tượng được tạo bằng cách sử dụng khởi tạo trên lớp hình chữ
nhật.'''

class Rectangle : 
    def __init__( self , length , width ) : 
        self.length = length 
        self.width = width 

    def Perimeter( self) : 
        return  ( self.length + self.width) * 2 
    
    def Area ( self ) : 
        return self.length * self .width 
    def Display( self ) : 
        print ( " Chiều dài : " , self.length) 
        print ( " Chiều rộng : " , self.width) 
        print( " Chu vi : " , self.Perimeter()) 
        print ( " Diện tích : " , self.Area()) 

hcn = Rectangle( 5 , 3 ) 
hcn.Display()