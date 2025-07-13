n = int ( input ("Nhập số nguyên : ")) 

ngan = n //  1000 
tram = ( n % 1000  ) // 100 
chuc = ( n % 100 ) // 10 
donvi = n % 10 

print ( " Cách đọc số đã nhập : ") 
print ( f"{ngan} Ngàn {tram} trăm {chuc} chục {donvi} đơn vị ")