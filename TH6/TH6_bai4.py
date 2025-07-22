''' 
Bài 6.4.
Viết chương trình Python thực hiện các yêu cầu sau:
• Định nghĩa một lớp Point gồm các thuộc tính và phương thức xác định một
điểm trong mặt phẳng tọa độ.
• Định nghĩa một lớp Circle cho phép tạo một đường tròn C(O, r) với tâm O(a, b)
và bán kính r bằng cách sử dụng hàm tạo:
• Định nghĩa một phương thức Area() của lớp để tính diện tích của đường tròn.
• Định nghĩa một phương thức Perimeter() của lớp cho phép bạn tính chu vi của
đường tròn.
• Định nghĩa một phương thức testBelongs() của lớp cho phép kiểm tra xem một
điểm A(x, y) có thuộc đường tròn C(O, r) hay không.'''
import math 
class Point : 
    def __init__ ( self , x , y ) : 
        self.x = x 
        self.y = y 

    def distance ( self , others ) : 
        return math.sqrt  ( ( self.x - others.x ) ** 2 + ( self.y - others.y ) ** 2 ) 
    
    def display ( self ) : 
        print ( f" X : {self.x}") 
        print ( f'Y : {self.y}')

class Circle : 
    def __init__ ( self , center , radius ) : 
        self.center = center 
        self.radius = radius 
    
    def Area( self ) : 
        return math.pi * ( self.radius ** 2 ) 
    def Perimeter ( self ) : 
        return math.pi * self.radius * 2 
    
    def testBelongs(self, point):
        d = self.center.distance(point)
        if math.isclose(d, self.radius, abs_tol=1e-6):  # kiểm tra gần đúng (trên đường tròn)
            return "✅ Điểm nằm trên đường tròn"
        elif d < self.radius:
            return "🟢 Điểm nằm bên trong đường tròn"
        else:
            return "🔴 Điểm nằm ngoài đường tròn"

# Tạo tâm O(3, 4) và bán kính r = 5
O = Point(3, 4)
C = Circle(O, 5)

# In diện tích và chu vi
print(f"Diện tích: {C.Area():.2f}")
print(f"Chu vi: {C.Perimeter():.2f}")

# Kiểm tra điểm A có thuộc đường tròn không
A = Point(6, 8)
print(f"Điểm A {A.x},{A.y}: {C.testBelongs(A)}")




    