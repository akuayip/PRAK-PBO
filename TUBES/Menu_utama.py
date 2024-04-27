import pygame
from Halaman_abstrak import Halaman
from Tombol import Tombol
from Game_loader import screen

class Menu_utama(Halaman):
    def __init__(self) -> None:
        super().__init__()
        self.nama_halaman = "Menu_utama"
        self.Background("asset/bg.png")
        self.backgroundsound = pygame.mixer.Sound("asset/bg-sound.mp3")
        self.gambar = pygame.image.load("asset/bg-2.png")
        self.gambar_rect = self.gambar.get_rect(center=(500, 360))
        
        self.tombol_mulai = Tombol("asset/button_play.png", pilihan= "center", posisi= (500, 320))
        self.tombol_info = Tombol("asset/button_info.png", pilihan= "center", posisi= (500, 400))
        self.tombol_keluar = Tombol("asset/button_exit.png", pilihan= "center", posisi= (500, 480))
        self.tombol_tanya_tanya = Tombol("asset/button_question.png", pilihan= "topright", posisi=(970, 30))
        self.tombol_mute = Tombol("asset/button_unmute.png", pilihan="bottomleft", posisi=(30, 633))
        
        
        self.timer = True
        self.status_mute = False

    def update(self):
        if self.suara == False:
            self.backgroundsound.play(-1)
            self.suara = True

    def input(self):
        if self.tombol_mulai.diklik():
            self.status_game_sekarang["halaman_sekarang"] = "Tebakaku"
            
        if self.tombol_info.diklik():
            self.status_game_sekarang["halaman_sekarang"] = "Info"

        if self.tombol_keluar.diklik():
            pygame.quit()
            exit()

        if self.tombol_tanya_tanya.diklik():
            self.status_game_sekarang["halaman_sekarang"] = "Cara_Bermain"
        
        if self.tombol_mute.diklik():
            print("Tombol mute diklik")
            self.status_mute = not self.status_mute
            if self.status_mute :
                self.backgroundsound.stop()
            else :
                self.backgroundsound.play(-1)
   

        

    def tampil(self):
        screen.blit(self.gambar, (self.gambar_rect))
        self.tombol_mulai.tampil()
        self.tombol_info.tampil()
        self.tombol_keluar.tampil()
        self.tombol_tanya_tanya.tampil()
        self.tombol_mute.tampil()