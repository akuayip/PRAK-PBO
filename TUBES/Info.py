import pygame
from Game_loader import screen
from Halaman_abstrak import Halaman
from Tombol import Tombol

class Info(Halaman):
    def __init__(self) -> None:
        super().__init__()

        self.nama_halaman = "Info"
        self.Background("asset/bg.png")

        self.tombol_kembali = Tombol("asset/button_back.png",pilihan=  "topleft", posisi = (30, 30))

        self.info = pygame.image.load("asset/board.png")
        self.info_rect = self.info.get_rect(center = (500, 333))

    def input(self):
        if self.tombol_kembali.diklik():
            self.status_game_sekarang["halaman_sekarang"] = "Menu_utama"

    def tampil(self):
        self.tombol_kembali.tampil()
        screen.blit(self.info, self.info_rect)