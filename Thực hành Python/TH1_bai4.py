n = int ( input( " Nhập số n : ")) 
x = int ( input(" Nhập số x : "))
def tinh_S( x , n ) : 
    if n % 2 != 0 : 
        return 0 
    else : 
        S = 2016 * x 
        for i in range ( 2  , n , 1  ) : 
            S  += x ** i / 3 ** ( i - 1 )
        return S 

s = tinh_S ( x , n ) 
print ( " Kết quả : " , s )