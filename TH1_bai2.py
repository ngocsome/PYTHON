from math import*
x1 = int ( input("Nhập x1 : ")) 
y1 = int ( input("Nhập x2 : ")) 

x2 = int ( input("Nhập x2 : ")) 
y2 = int ( input("Nhập y2 : ")) 

print ( " A(" , x1 , ",", y1 , ") ")
print ( " B(" , x2 ,"," , y2 , ") ")

D = sqrt ( ( x2 - x1 )* ( x2 - x1 ) + ( y2 - y1 ) * ( y2 - y1 )) 
print ( " Khoảng cách Euclidean : " , D ) 

M = abs ( x2 - x1 ) + abs ( y2 - y1 )
print ( " Khoảng cách Manhattan :  " , M ) 

C = 1 - ( (x1*x2 + y1 * y2 ) / ( sqrt ( x1*x1 + y1*y1) * sqrt ( x2*x2 + y2*y2)))
print ( " Khoảng cách Cosin : " , C )