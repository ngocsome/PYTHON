def list_to_matrix ( a , n , m ) : 
    if len(a ) < n * m : 
        print ( " Không thể xây dựng ma trận ") 
        return None 

    matrix= [] 
    index = 0 
    for i in range ( n ) : 
        row = [] 
        for i in range ( m ) : 
            row.append([a[index]]) 
            index += 1 
        matrix.append(row) 
    return matrix 


n = int ( input("Nhập n : ")) 
m = int ( input("Nhập m : ")) 
a = list(map(int, input("Nhập các phần tử list cách nhau bởi dấu cách: ").split()))

result = list_to_matrix( a , n , m ) 
if result : 
    for row in result : 
        print ( row )