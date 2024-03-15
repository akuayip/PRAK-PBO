class Mobil:
    def __init__(self):
        # atribt
        self.__bensin = 0  
        self.__odometer = 0  

    def isi_bensin(self):
        self.__bensin = min(60, self.__bensin + 60)  # Isi bensin maksimal 60 liter

    def mengendarai(self, kilometer):
        bensin_dibutuhkan = kilometer
        if self.__bensin >= bensin_dibutuhkan:
            self.__odometer += kilometer
            self.__bensin -= bensin_dibutuhkan
        else:
            # Jika bensin tidak cukup, mobil hanya akan menempuh sejauh bensin yang tersedia
            self.__odometer += self.__bensin
            self.__bensin = 0

    def lihat_info(self):
        print(f"Odometer berada pada angka {self.__odometer} km, bensin yang tersisa {self.__bensin} liter")


mobil = Mobil()
mobil.lihat_info()
mobil.isi_bensin()
mobil.lihat_info()
mobil.mengendarai(20)
mobil.lihat_info()
mobil.mengendarai(50)
mobil.lihat_info()
mobil.mengendarai(10)
mobil.lihat_info()
mobil.isi_bensin()
mobil.isi_bensin()
mobil.lihat_info()
