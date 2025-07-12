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



def main() : 
    a = float ( input("Nhập hệ số a : ")) 
    b = float ( input("Nhập hệ số b : ")) 
    c = float ( input ("Nhập hệ số c : ")) 
    pt1 = PT( a , b , c ) 
    delta=pt1.tinh_delta() 
    print ( " Delta : " , delta) 
    pt1.tinh_nghiem(delta) 

main()
