from Menu_utama import Menu_utama
from Cara_bermain import Cara_Bermain
from Info import Info
from Tebakaku import Tebakaku
from Game_loader import *
from Mouse import Mouse


class Game:
    def __init__(self,framerate:int = 60) -> None:
        self.framerate = framerate
        self.clock = pygame.time.Clock()

        # list_halaman berisi halaman apa saja
        # yang terdapat dalam game
        # seperti suatu game terdiri dari menu utama, info, dan lain-lain.
        # halaman bisa diartikan juga sebagai menu

        self.list_halaman = {"Menu_utama":Menu_utama(),
                             "Info":Info(),
                             "Cara_Bermain":Cara_Bermain(),
                             "Tebakaku":Tebakaku(),
                            }
        self.list_halaman_key = self.list_halaman.keys()
        self.status_game_sekarang = {"halaman_sekarang":"Menu_utama"}
        
    def mulai(self):
        while True :
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    Mouse.set_mouse_keklik()

                if event.type == pygame.MOUSEMOTION:
                    Mouse.set_mouse_pos(event.pos)

            for key in self.list_halaman_key:
                if self.status_game_sekarang["halaman_sekarang"] == key:
                    self.list_halaman[key].Update(self.status_game_sekarang)
                    self.status_game_sekarang = self.list_halaman[key].kembalikan_status_game()
        
            pygame.display.update()
            self.clock.tick(self.framerate)