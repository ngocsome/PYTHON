'''Bài 6.3.
Viết chương trình Python thực hiện các yêu cầu sau:
• Tạo một lớp Python có tên BankAccount đại diện cho tài khoản ngân hàng, có
các thuộc tính: accountNumber, tên chủ tài khoản, số dư.
• Tạo một hàm tạo với các tham số: accountNumber, name, balance.
• Tạo một phương thức Deposit() quản lý các hành động nạp tiền.
• Tạo một phương thức Withdrawal() quản lý các hành động rút tiền.
• Tạo một phương thức bankFees() để áp dụng phí ngân hàng với tỷ lệ phần trăm
là 5% của tài khoản số dư.
• Tạo một phương thức display() để hiển thị chi tiết tài khoản.
• Tạo một đối tượng thuộc lớp BankAccount, sử dụng các phương thức tương
ứng. '''

class BankAccount : 
    def __init__ ( self , accountNumber , ten , so_du ) : 
        self.accountNumber = accountNumber 
        self.ten = ten 
        self.so_du = so_du 
    
    def deposit ( self , nap ) : 
      if nap > 0 : 
        self.so_du += nap 
        print ( f"Đã nạp {nap} vào tài khoản ") 
      else : 
         print ( " Số tiền muốn nạp phải lớn hơn 0 !!! ")
    
    def Withdrawal ( self , rut ) : 
       if rut > 0 : 
          if rut < self.so_du : 
             self.so_du -= rut 
             print ( f'Đã rút {rut} từ tài khoản ! ')
            
          else : 
             print ( " Số dư không đủ ! ") 
       else : 
          print ( " Số tiền rút phải lớn hơn 0 ") 

    def bankFees( self )  : 
       fees = self.so_du * 0.05 
       self.so_du -= fees 
       print ( f'Đã trừ phí ngân hàng {fees}') 
    def display(self ) : 
       print ( f'Số tài khoản : {self.accountNumber}')
       print ( f'Tên chủ tài khoản :{self.ten}')
       print (f'Số dư : {self.so_du } VND ' ) 
def main ( ) : 
   n = int ( input ( " Nhập số Account muốn thêm : ")) 
   danhSach = []
   for i in range ( n ) : 
       acc = input ( " Nhập số tài khoản ") 
       ten_acc = input( " Nhập tên chủ tài khoản : ") 
       sodu = input ( " Nhập số dư : ")
       them = BankAccount ( acc , ten_acc , sodu ) 
       danhSach.append( them ) 
    
    
   print("\nDanh sách thông tin account:")
   for i in danhSach:
        i.display()

main()
   
     




