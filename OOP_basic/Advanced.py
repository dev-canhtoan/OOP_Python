class BankAccount:
    def __init__(self,account_number, balance=0):
        if balance < 0:
            raise ValueError("Không được âm")
        self.account_number = account_number
        self._balance = balance
    def deposit(self,amount):
        if amount > 0:
            self._balance += amount
            print(f"Đã nạp thành công {amount} vào tài khoản {self.account_number}")
        else:
            print("Số tiền nạp vào phải lớn hơn 0")
    def withdraw(self,amount):
        if amount > 0:
            if amount <= self._balance:
               self._balance -= amount
               print(f"Rút thành công {amount}")
            else:
                print("Số dư hông đủ")
        else:
            print("Số tiền rút phải lớn hơn 0")
    def display(self):
        return print(f"Tài khoản: {self.account_number}, số dư: {self._balance}")
account = BankAccount("666668899789", 5000000)
account.deposit(100000)
account.withdraw(100000)
account.display()