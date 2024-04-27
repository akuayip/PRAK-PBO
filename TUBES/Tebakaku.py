import pygame
import random
from Game_loader import screen
from Halaman_abstrak import Halaman
from Tombol import Tombol

class Tebakaku(Halaman):
    def __init__(self) -> None:
        super().__init__()
        self.nama_halaman = "Tebakaku"
        self.Background("asset/bg.png")
        self.tombol_kembali = Tombol("asset/button_back.png", pilihan="topleft", posisi=(30, 30))
        self.board = pygame.image.load("asset/board.png")
        self.board_rect = self.board.get_rect(center=(500, 333))
        self.win = pygame.image.load("asset/win.png")
        self.win_rect = self.win.get_rect(center=(500,275))
        self.status_win = False

        # Font
        self.font = pygame.font.SysFont(None, 34)

        # Angka rahasia
        self.angka_rahasia = random.randint(1, 100)
        self.tebakan = None
        self.jumlah_tebakan = 0

        # Teks
        self.teks = "Silahkan tebak Angka 1-100"
        self.teks_rendered = self.font.render(self.teks, True, (255, 255, 255))
        self.teks_rect = self.teks_rendered.get_rect(center=(500, 225))
        self.status_teks = True

        # Kotak input
        self.input_rect = pygame.Rect(405, 300, 200, 40)
        self.input_text = ''
        self.status_kotak = True

        # Pesan tebakan
        self.pesan_tebakan = ""
        self.pesan_tebakan_rendered = None
        self.pesan_tebakan_rect = None

    def input(self):
        if self.tombol_kembali.diklik():
            self.status_game_sekarang["halaman_sekarang"] = "Menu_utama"

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    self.input_text = self.input_text[:-1]
                elif event.key == pygame.K_RETURN:
                    self.tebak()
                else:
                    self.input_text += event.unicode

    def tebak(self):
        if self.input_text and self.input_text.isdigit():
            self.tebakan = int(self.input_text)
            self.jumlah_tebakan += 1

            if self.tebakan < self.angka_rahasia:
                self.pesan_tebakan = "Tebakan Anda terlalu rendah. Coba lagi."
            elif self.tebakan > self.angka_rahasia:
                self.pesan_tebakan = "Tebakan Anda terlalu tinggi. Coba lagi."
            else:
                self.pesan_tebakan = f"Selamat! Anda menebak dengan benar! \nAngka rahasia adalah {self.angka_rahasia}. \nAnda menebak dalam \n{self.jumlah_tebakan} kali tebakan."
                self.tebakan = None
                self.angka_rahasia = random.randint(1, 100)
                self.jumlah_tebakan = 0
                self.status_teks = False
                self.status_kotak = False
                self.status_win = True
            self.input_text = ''  # Reset input

            # Render pesan tebakan
            self.pesan_tebakan_rendered = self.font.render(self.pesan_tebakan, True, (255, 255, 255))
            self.pesan_tebakan_rect = self.pesan_tebakan_rendered.get_rect(center=(500, 400))

    def tampil(self):
        self.tombol_kembali.tampil()
        screen.blit(self.board, self.board_rect)

        # Icon Win
        if self.status_win:
            screen.blit(self.win, self.win_rect)
    
        # Tampilkan teks
        if self.status_teks:
            screen.blit(self.teks_rendered, self.teks_rect)
            # Tampilkan teks jumlah tebakan di bawah teks utama
            teks_tebakan = f"({self.jumlah_tebakan} tebakan)"
            teks_tebakan_rendered = self.font.render(teks_tebakan, True, (255, 255, 255))
            teks_tebakan_rect = teks_tebakan_rendered.get_rect(center=(500, 255))
            screen.blit(teks_tebakan_rendered, teks_tebakan_rect)

        # Kotak input
        if self.status_kotak:
            pygame.draw.rect(screen, (255, 255, 255), self.input_rect, 2)
            input_surface = self.font.render(self.input_text, True, (255, 255, 255))
            input_rect_center = self.input_rect.center
            input_rect_surface = input_surface.get_rect(center=input_rect_center)
            screen.blit(input_surface, input_rect_surface.topleft)

        # Tampilkan pesan tebakan
        if self.pesan_tebakan_rendered:
            screen.blit(self.pesan_tebakan_rendered, self.pesan_tebakan_rect)
