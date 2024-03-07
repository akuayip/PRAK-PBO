def log_motor_sale(func):
    def wrapper(self):
        print(f"Sebelum menjalankan fungsi")
        func(self)
        print(f"Setelah menjalankan fungsi")
    return wrapper

class Garasi:
    def __init__(self, satu):
        self.motor = satu
        
    @log_motor_sale
    def motor_info(self):
        print(f"Motor : {self.motor}")

    def __del__(self):
        print(f"Motor {self.motor} sudah terjual")

contoh = Garasi("Beat")

contoh.motor_info()


