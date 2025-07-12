import math 
class Circle:
    def __init__(self , radius): # init là phương thức khởi tạo của class 
        self.radius = radius # đối số đầu tiên thường là self để tham chiếu đến đối tượng hiện tại của class 
    def caculator(self) : 
        return round(math.pi * self.radius**2,2) 

# khởi tạo đối tượng : 
circle_1 = Circle(42) 
print(circle_1) 

# truy cập đối tượng , phương thức : sử dụng dấu chấm 
circle_1.radius
circle_1.caculator() 

# có thể gán giá trị 
circle_1.radius = 100 
print(circle_1.radius) 
print(circle_1.caculator())
