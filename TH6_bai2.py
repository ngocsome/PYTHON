'''• Tạo một lớp Python Person với các thuộc tính: tên và tuổi kiểu dữ liệu chuỗi.
• Tạo một phương thức display() hiển thị tên và tuổi của một đối tượng được tạo
thông qua lớp Person.
• Tạo một lớp con Student kế thừa từ lớp Person và có thêm thuộc tính section.
• Tạo một phương thức displayStudent() hiển thị tên, tuổi và phần của một đối
tượng được tạo thông qua lớp Student.
• Tạo một đối tượng student thông qua một khởi tạo trên class Student và sau đó
kiểm tra phương thức displayStudent. '''

class Person : 
    def __init__ ( self , name , age ) : 
        self.name = name 
        self.age = age 
    def display(self) : 
        return f"Tuổi : {self.name} , Tuổi : {self.age} " 
    
class Student ( Person ) : 
    def __init__(self, name, age , section ):
        super().__init__(name, age) 
        self.section = section 
    def displayStudent ( self ) : 
        return f"Tuổi : {self.name} , Tuổi : {self.age} , Section : {self.section}" 

stu1 = Student ( " Ngọc " , 20 , " HaUi ") 
print (stu1.displayStudent() ) 