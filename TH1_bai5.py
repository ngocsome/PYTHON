from math import*
def is_prime(n) : 
    if n < 2 : 
        return False 
    elif n == 2 : 
        return True 
    elif n % 2 == 0 : 
        return False 
    for i in range ( 2 , int ( sqrt ( n )) , 1 ) : 
        if n % i == 0 : 
            return False 
        else : 
            return True 

def check(n) : 
    return str(n ) == str(n) [ :: -1 ] 


n = int ( input("Nhập số : ")) 
if is_prime(n) and check( n ) : 
    print ( " Số hợp lệ ! ")
else :
    print ( " Số không hợp lệ ! ")

