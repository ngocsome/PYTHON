''' Thực hiện các yêu cầu sau:
• Xây dựng ba lớp Vehicle, Car, và ElectricCar. Car kế thừa từ Vehicle và
ElectricCar kế thừa từ Car. Mỗi lớp sẽ có phương thức description() ghi đè
phương thức của lớp cha.
• Lớp Vehicle có thuộc tính make (hãng sản xuất) và phương thức description()
in ra thông tin của phương tiện.
• Lớp Car kế thừa từ Vehicle, có thêm thuộc tính model (tên dòng xe), và có
phương thức description() in ra thông tin của ô tô.
• Lớp ElectricCar kế thừa từ Car, có thêm thuộc tính battery_size (dung lượng
pin), và phương thức description() in ra thông tin của xe điện.
• Tạo ra các đối tượng thuộc các lớp đã xây dựng và in thông tin của các đối
tượng đó ra màn hình.'''
class Vehicle :
    def __init__(self , make ) : 
        self.make = make 

    def descripton ( self ) : 
        print ( f"Hãng : {self.make}") 
        print ( " ")
class Car ( Vehicle ) : 
    def __init__(self, make , model ):
        super().__init__(make)
        self.model = model 
    def descripton ( self ) : 
        print ( f" Hãng : {self.make}")
        print ( f'Model : {self.model}')
        print ( " ")
        

class ElectricCar ( Car ) : 
    def __init__(self, make, model , size ):
        super().__init__(make, model)
        self.size = size 
    def descripton ( self ) : 
        print ( f" Hãng : {self.make}")
        print ( f'Model : {self.model}')
        print ( f' Size : {self.size}')
        print ( " ")

vehicle = Vehicle ( " Vinfast ")
vehicle.descripton() 

car = Car ( " Honda " , " Wave ") 
car.descripton()

electric = ElectricCar ( " Vinfast " , " VF9 " , 1000 )
electric.descripton()