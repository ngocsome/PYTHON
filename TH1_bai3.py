import math 
a = int ( input ( " Nhập hệ số a : ")) 
b = int ( input ( " Nhập hệ số b : ")) 
c = int ( input ( " Nhập hệ số c : "))

if a == 0 : 
    if b == 0 : 
        if c == 0 : 
            print ( " Phương trình có vô số nghiệm ! ")
        else : 
            print ( " Phương trình vô nghiệm ! ")

    else : 
        x = -c / b 
        print ( " Phương trình có nghiệm duy nhất : " , x ) 
else : 
    delta = b * b - 4 * a * c 
    if delta > 0 : 
        x1 = ( -b + math.sqrt(delta)) / ( 2 * a )
        x2 = ( -b - math.sqrt(delta)) / ( 2 * a )
        print ( " Phương trình có 2 nghiệm : " , x1 , " , " , x2 )
    elif  delta == 0 : 
        x3 = -b / ( 2 * a ) 
        print ( " Phương trình có nghiệm kép : " , x3 ) 
    else : 
        print ( " Phương trình đéo có nghiệm ")
       
