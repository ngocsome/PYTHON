from math import*
def is_prime(n) : 
    if n < 2 : 
        return False 
    for i in range ( 2 , int ( sqrt(n)) ) : 
        if n % i == 0 : 
            return False 
    return True 

def is_palindrome(n) : 
    return str(n) == str ( n )[ :: - 1 ] 

def nhap() : 
    while True : 
        try : 
            s = int ( input(" Nhập số s : "))
            e = int ( input( " Nhập số e : ")) 
            if s < e and e <= 99999 : 
                return s , e 
            else : 
                print ( " Lỗi rồi dmmm ! ") 
        except ValueError : 
            print (" Nhập lại cho đúng đmm !!! ") 

def tinh_tong( s , e ) : 
    tong = 0 
    for i in range ( s , e + 1 ) : 
        if is_prime(i) and is_palindrome(i) : 
            tong += i 
    return tong 

s,e = nhap() 
tong = tinh_tong(s, e ) 
print(f"Tổng các số đối xứng và nguyên tố :{tong} "  )
