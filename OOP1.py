class Person : 
    def __init__( self , name , age , address ) : 
        self.name = name 
        self.age = age 
        self.address = address 
    def __str__(self ) : 
        return (f'Xin chào tôi là {self.name} , tôi {self.age} tuổi , địa chỉ của tôi là {self.address} ') 
    
    def birthday(self) : 
        self.age += 1 
        print ( " Chúc mừng sinh nhật ! Tôi hưởng thọ " , self.age , " tuổi !!! ")
    

# khởi tạo 1 đối tượng mới 
person1 = Person( " Ngọc " , 20 , " Phú thọ ") 
# gọi hàm introduce 
print ( person1 )
# gọi hàm để chúc sn với tuổi tăng 
person1.birthday() 

# khởi tạo đối tượng new 
person2 = Person("Thạch " , 21 , " Thanh hóa ") 

print(person2) 

person2.birthday() 
