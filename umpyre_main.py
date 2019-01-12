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
label_pitch = font.render("Press F to pitch!", 1, (0, 0, 255))
label_bat = font.render("Press SPACE to bat!", 1, (0, 0, 255))
label_playball = font.render("Press J to Play Ball!!!", 1, (0, 0, 255))


""" ----------------------- BACKGROUND ---------------------------- """
bg = pygame.image.load(os.path.join("image", "umpyre_baseball_field.png"))
bg_width = bg.get_width()
bg_height = bg.get_height()
screen = pygame.display.set_mode((bg_width, bg_height))
pygame.display.set_caption("UMPYRE")


""" ------------------------ SOUNDS ------------------------------ """
sound_beep = pygame.mixer.Sound(os.path.join("audio", "beep.wav"))
sound_playball = pygame.mixer.Sound(os.path.join("audio", "playball.wav"))
sound_strike = pygame.mixer.Sound(os.path.join("audio", "pitch_strike.wav"))
sound_homerun = pygame.mixer.Sound(os.path.join("audio", "batter_homerun.wav"))


if __name__ == '__main__':

    key_index = 0

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
        screen.blit(label_pitch, (850, 400))
        screen.blit(label_bat, (850, 450))
        screen.blit(label_playball, (850, 500))

        mouse_x, mouse_y = pygame.mouse.get_pos()
        mouse_pos = font.render(f"( x: {mouse_x} , y: {mouse_y} )", 1, (0, 0, 0))
        screen.blit(mouse_pos, ([250, 20]))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                pass
            elif event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[K_j]:
                    print(f"{key_index}: You pressed {event.key:c}")
                    sound_playball.play()
                if keys[K_f]:
                    print(f"{key_index}: You pressed {event.key:c}")
                    sound_strike.play()
                if keys[K_SPACE]:
                    print(f"{key_index}: You pressed {event.key:c}")
                    sound_homerun.play()
            elif event.type == pygame.KEYUP:
                pygame.mixer.fadeout(500)
        pygame.display.update()



