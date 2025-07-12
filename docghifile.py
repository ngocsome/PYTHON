n = int (input("Nhập n : ")) 
m = int(input("Nhập m : "))

with open ('text.txt',"w" , encoding="utf-8") as f : 
    f.write(f'{n}{m}')
    for i in range(n) : 
        for j in range(m) : 
            f.write(input(f"Nhập a[{i}{j}] :  "))
            f.write(" ")
        f.write("\n ")

with open("text.txt","r",encoding="utf-8") as f : 
    n , m = ( int ( x ) for x in f.readline().split()) 
    b = [] 
    for line in f.readline() : 
        list_str = line.split() 
        b.append([float(num) for num in list_str]) 

print(n , m )
print (b)