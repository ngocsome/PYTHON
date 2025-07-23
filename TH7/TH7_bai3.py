''' Viết chương trình Python thực hiện các yêu cầu sau:
• Tạo một lớp cơ sở trừu tượng tài khoản Account với phương thức trừu tượng
deposit() để gửi tiền, withdraw() để rút tiền, và get_balance() để xem số dư.
• Sau đó, tạo hai lớp con SavingsAccount và CheckingAccount kế thừa từ
Account.
• Lớp SavingsAccount có thuộc tính balance và phương thức withdraw() chỉ cho
phép rút tiền nếu số tiền rút nhỏ hơn hoặc bằng số dư.
• Lớp CheckingAccount có thuộc tính balance và limit, phương thức withdraw()
cho phép số dư âm tới một mức limit.

• Tạo ra các đối tượng thuộc các lớp con và sử dụng các phương thức đã có để
nạp, rút tiền trong tài khoản.
'''

from abc import ABC , abstractmethod 
class Account ( ABC) : 
    @abstractmethod 
    def deposit ( self , amount) : 
        pass 
    
    @abstractmethod 
    def withdreaw ( self , amount ) : 
        pass 
    
    def get_balance( self ) : 
        pass 

class SavingAccount ( Account ) : 
    def __init__( self , int_balance = 0 ) : 
        self.balance = int_balance 
    
    def deposit ( self , amount ) : 
        if amount > 0 : 
            self.balance += amount 
            print ( f' Đã nạp thành công {amount} VND . Số dư : {self.balance} VND ')
        else : 
            print ( " Số tiền nạp phải lớn hơn 0 ") 
    def withdreaw ( self , amount ) : 
        if amount < self.balance : 
            if amount > 0 : 
                self.balance -= amount 
                print ( f'Đã rút {amount } VND . Số dư : {self.balance}VND ')
            else : 
                print ( " số tiền phải lớn hơn 0 ")
        else : 
            print ( " Số tiền rút phải nhỏ hơn số dư !!! ") 
    
    def get_balance(self):
        return self.balance

class CheckingAccount(Account):
    def __init__(self, initial_balance=0, limit=0):
        self.balance = initial_balance
        self.limit = limit

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Nạp {amount} vào tài khoản thanh toán. Số dư: {self.balance}")
        else:
            print("Số tiền nạp phải lớn hơn 0.")

    def withdraw(self, amount):
        if self.balance - amount >= -self.limit:
            self.balance -= amount
            print(f"Rút {amount} từ tài khoản thanh toán. Số dư: {self.balance}")
        else:
            print("Vượt quá hạn mức cho phép!")

    def get_balance(self):
        return self.balance 
    
from abc import ABC, abstractmethod

# Lớp trừu tượng Account
class Account(ABC):
    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def get_balance(self):
        pass


# Lớp con SavingsAccount
class SavingsAccount(Account):
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Nạp {amount} vào tài khoản tiết kiệm. Số dư: {self.balance}")
        else:
            print("Số tiền nạp phải lớn hơn 0.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Rút {amount} từ tài khoản tiết kiệm. Số dư: {self.balance}")
        else:
            print("Không đủ số dư để rút.")

    def get_balance(self):
        return self.balance


# Lớp con CheckingAccount
class CheckingAccount(Account):
    def __init__(self, initial_balance=0, limit=0):
        self.balance = initial_balance
        self.limit = limit

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Nạp {amount} vào tài khoản thanh toán. Số dư: {self.balance}")
        else:
            print("Số tiền nạp phải lớn hơn 0.")

    def withdraw(self, amount):
        if self.balance - amount >= -self.limit:
            self.balance -= amount
            print(f"Rút {amount} từ tài khoản thanh toán. Số dư: {self.balance}")
        else:
            print("Vượt quá hạn mức cho phép!")

    def get_balance(self):
        return self.balance


# =======================
# Thử nghiệm chương trình
# =======================
# Tạo tài khoản tiết kiệm
savings = SavingsAccount(initial_balance=1000)
savings.deposit(500)
savings.withdraw(300)
savings.withdraw(1500)  # vượt quá số dư
print(f"Số dư tài khoản tiết kiệm: {savings.get_balance()}")

print("--------")

# Tạo tài khoản thanh toán
checking = CheckingAccount(initial_balance=500, limit=1000)
checking.deposit(200)
checking.withdraw(1000)  # được phép rút vượt quá số dư đến giới hạn
checking.withdraw(1000)  # vượt quá hạn mức
print(f"Số dư tài khoản thanh toán: {checking.get_balance()}")
