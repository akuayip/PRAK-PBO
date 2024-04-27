import pygame
from Game_loader import screen
from Halaman_abstrak import Halaman
from Tombol import Tombol

class Cara_Bermain(Halaman):
    def __init__(self) -> None:
        super().__init__()

        self.nama_halaman = "Cara_Bermain"
        self.Background("asset/bg.png")

        self.tombol_kembali = Tombol("asset/button_back.png",pilihan=  "topleft", posisi = (10, 10))

        self.cara_bermain = pygame.image.load("asset/board_aturan.png")
        self.cara_bermain_rect = self.cara_bermain.get_rect(center = (500, 333))

    def input(self):
        if self.tombol_kembali.diklik():
            self.status_game_sekarang["halaman_sekarang"] = "Menu_utama"

    def tampil(self):
        self.tombol_kembali.tampil()
        screen.blit(self.cara_bermain, self.cara_bermain_rect)