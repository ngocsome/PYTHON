def vecinput() : 
    arr = input("Nhập các phần tử mảng cách nhau bởi dấu cách : ").split() 
    return [ int ( x ) for x in arr ] # trả về kết quả list 

def vecsum( v ) : 
    return sum(v) 

def vecinsert( v , pos , val ) : 
    if 0 <= pos <= len(v) : # kiểm tra vị trí chèn nếu nhỏ hơn độ dài list 
        v.insert( pos , val )
    else : 
        print ( " Vị trí chèn không hợp lệ ")

def vecdel( v , pos ) : 
    if 0 <= pos <= len(v) : 
       v.pop(pos )
    else : 
        print ( " Vị trí xóa không hợp lí ! ")

def vecadd ( v1 , v2 ) : 
    if len(v1 ) != len(v2) : 
        print ( " Không cùng kích thước không cộng được đâu ! ") 
        return [] 
    else : 
        return [ v1[i] + v2[i] for i in range ( len(v1))] 
    
    
