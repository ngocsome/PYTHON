def tao_mang( a , b ) : 
    i = j = 0 
    c = [] 
    while ( i < len(a) and j < len(b)) : 
        if a[i] < b[ j ] : 
            c.append( a[i]) 
            i += 1 
        else : 
            c.append(b[ j ])
            j += 1 
    c.extend( a[i:]) 
    c.extend(b[i:])

    return c 


a = list ( map (int , input("Nhập các phần tử mảng a :  ").split() )) 
b = list ( map( int , input("Nhập các phần tử mảng b : ").split())) 

a.sort() 
b.sort() 
c = tao_mang ( a , b ) 

print ( " Mảng a sau sắp xếp : " , a ) 
print ( " Mảng b sau sắp xếp : " , b ) 
print ( " Mảng được gộp : " , c )

