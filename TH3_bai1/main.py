import myvector 

print ( " Nhập mảng thứ nhất : ") 
v1 = myvector.vecinput() 
print()

print ( " Nhập mảng thứ hai : ") 
v2=myvector.vecinput()
print()

print ( " Tổng phần tử mảng thứ nhất  :" , myvector.vecsum(v1) ) 
print()
print ( " Tổng phần tử mảng thứ hai : " , myvector.vecsum(v2)) 
print()

print ( " Giờ đến phần chèn này ! ") 
pos = int ( input(" Vị trí chèn : ")) 
val = int ( input("Giá trị chèn : ")) 
myvector.vecinsert(v1 , pos , val ) 
print ( " List sau khi chèn : " , v1) 
print ()

print ( " Chèn xong đến xóa nhé ! ") 
pos = int ( input(" Vị trí muốn delete : ") ) 
myvector.vecdel( v1 , pos ) 
print ( " Mảng sau khi xóa : " , v1 )
print() 

print ( " Cộng 2 List ") 
result = myvector.vecadd( v1 , v2 ) 
if result : 
    print ( " Mảng sau khi cộng : " , result )
