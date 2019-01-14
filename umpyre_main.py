"""
UMPYRE
Main file: Run this file
"""

from umpyre_functions import *
import pygame
from pygame.locals import *
import os
import sys


""" --------------------- INITIALIZE ------------------------ """
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.mixer.init()
pygame.init() # Initialize pygame
clock = pygame.time.Clock()

""" ------------------------- LABELS ------------------------------ """
font = pygame.font.SysFont(None, 48)
label_quit = font.render("ESC: Quit", 1, (255, 0, 0))
label_pitch = font.render("Press F to pitch!", 1, (0, 0, 255))
label_bat = font.render("Press SPACE to bat!", 1, (0, 0, 255))
label_playball = font.render("Press J to Play Ball!!!", 1, (0, 0, 255))
label_musictoggle = font.render("Press M to toggle music On/Off!", 1, (0, 0, 255))


""" ----------------------- BACKGROUND ---------------------------- """
bg = pygame.image.load(os.path.join("image", "umpyre_baseball_field.png"))
bg_width = bg.get_width()
bg_height = bg.get_height()
screen = pygame.display.set_mode((bg_width, bg_height))
bg = pygame.image.load(os.path.join("image", "umpyre_baseball_field.png")).convert()
pygame.display.set_caption("UMPYRE")


""" -------------------------- IMAGES ------------------------------ """
img_volume = pygame.image.load(os.path.join("icons", "volume_32.png")).convert_alpha()
img_volume_rect = screen.blit(img_volume, (bg_width - 45, 10))
img_mute = pygame.image.load(os.path.join("icons", "mute_32.png"))
img_batter = pygame.image.load(os.path.join("icons", "baseball-player-with-bat_128.png"))
img_pitcher = pygame.image.load(os.path.join("icons", "pitcher_64.png"))
img_ball = pygame.image.load(os.path.join("icons", "ball_16.png")).convert_alpha()
img_ball_rect = img_ball.get_rect()
img_glove = pygame.image.load(os.path.join("icons", "baseball-glove_64.png"))

""" ------------------------ SOUND FX ------------------------------ """
sound_playball = pygame.mixer.Sound(os.path.join("audio", "playball.wav"))
sound_playball.set_volume(0.2)
sound_strike = pygame.mixer.Sound(os.path.join("audio", "pitch_strike.wav"))
sound_strike.set_volume(0.2)
sound_homerun = pygame.mixer.Sound(os.path.join("audio", "batter_homerun.wav"))

""" -------------------------- MUSIC --------------------------------- """
music_rocksong_1 = pygame.mixer.music.load(os.path.join("audio", "rocksong_2.ogg"))
music_rocksong_2 = pygame.mixer.music.load(os.path.join("audio", "rocksong_1.ogg"))


# def pitch_ball(img_ball):
#
#     img_ball_rect = img_ball.get_rect()
#
#     for i in range(100):
#         screen.blit(bg, img_ball_rect)
#         img_ball_rect = img_ball_rect.move(2, 0)
#         screen.blit(img_ball, img_volume_rect)
#         pygame.display.update()
#         pygame.time.delay(50)


if __name__ == '__main__':


    key_index = 0

    # pygame.mixer.music.play(-1)
    # pygame.mixer.music.set_volume(0.05)

    # Create a total of nine Inning() instances

    inning_list = [Inning(inning_num=i) for i in range(1, 10)]

    print(inning_list, '\n')

    for inning in inning_list:
        visitor_runs = 0
        hometeam_runs = 0
        print("=" * 100)
        print(f"{inning.inning_num} " * 50)
        print("=" * 100)
        print(f"Visitor runs for inning {inning.inning_num}: {visitor_runs}")
        print(f"Home Team runs for inning {inning.inning_num}: {hometeam_runs}")
        print('\n')
        print(f"Inning {inning.inning_num}")
        visitor_runs = inning.visitors_atbat.team_at_bat()
        hometeam_runs = inning.home_atbat.team_at_bat()
        print(f"Visitor runs for inning {inning.inning_num}: {visitor_runs}")
        print(f"Home Team runs for inning {inning.inning_num}: {hometeam_runs}")


    while True:  # Event Loop
        clock.tick(60)
        screen.blit(bg, (0, 0))
        screen.blit(label_pitch, (600, 50))
        screen.blit(label_bat, (600, 100))
        screen.blit(label_playball, (600, 150))
        screen.blit(label_musictoggle, (600, 200))
        screen.blit(img_volume, (bg_width - 45, 10))
        screen.blit(label_quit, (20, bg_height - 50))
        screen.blit(img_pitcher, (820, 450))
        screen.blit(img_ball, (820, 450))
        screen.blit(img_glove, (833, bg_height - 75))
        screen.blit(img_batter, (735, bg_height - 225))




        mouse_x, mouse_y = pygame.mouse.get_pos()
        mouse_pos = font.render(f"( x: {mouse_x} , y: {mouse_y} )", 1, (0, 0, 0))
        screen.blit(mouse_pos, ([250, 20]))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                print(f"Mousebutton Down: x= {mouse_x}, y= {mouse_y}")
                if img_volume_rect.collidepoint(mouse_x, mouse_y):
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.fadeout(500)
                        # screen.blit(img_mute, (bg_width - 45, 10))
                    else:
                        print(f"You clicked the volume icon")
                        pygame.mixer.music.load(os.path.join("audio", "rocksong_2.ogg"))
                        pygame.mixer.music.set_volume(0.20)
                        pygame.mixer.music.play(-1)
                        # screen.blit(img_volume, (bg_width - 45, 10))
            elif event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[K_ESCAPE]:
                    sys.exit()
                if keys[K_j]:
                    print(f"{key_index}: You pressed {event.key:c}")
                    sound_playball.play()
                    pygame.mixer.music.set_volume(0.05)
                if keys[K_f]:
                    print(f"{key_index}: You pressed {event.key:c}")
                    # pitch_ball(img_ball)
                    sound_strike.play()
                    pygame.mixer.music.set_volume(0.05)
                if keys[K_SPACE]:
                    print(f"{key_index}: You pressed {event.key:c}")
                    sound_homerun.play()
                    pygame.mixer.music.set_volume(0.05)
                if keys[K_m]:
                    if pygame.mixer.music.get_busy():
                        print(f"{key_index}: You pressed {event.key:c}, music OFF")
                        pygame.mixer.music.fadeout(500)
                    else:
                        print(f"{key_index}: You pressed {event.key:c}, music ON")
                        pygame.mixer.music.load(os.path.join("audio", "rocksong_1.ogg"))
                        pygame.mixer.music.set_volume(0.20)
                        pygame.mixer.music.play(loops=-1)
            elif event.type == pygame.KEYUP:
                pygame.mixer.fadeout(500)
        pygame.display.update()



