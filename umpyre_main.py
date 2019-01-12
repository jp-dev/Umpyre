"""
UMPYRE
Main file: Run this file
"""

from umpyre_functions import *
import pygame
from pygame.locals import *
import os
import sys


pygame.init() # Initialize pygame
clock = pygame.time.Clock()
font = pygame.font.SysFont("monospace", 15)
# render text
label = font.render("Some text!", 1, (255,255,0))


""" ----------------------- BACKGROUND ---------------------------- """
bg = pygame.image.load(os.path.join("image", "umpyre_baseball_field.png"))
bg_width = bg.get_width()
bg_height = bg.get_height()

screen = pygame.display.set_mode((bg_width, bg_height))
screen.blit(label, (bg_width/2, 100))

pygame.display.set_caption("UMPYRE")


""" -------------------------- AUDIO --------------------------------- """
pygame.mixer.init()
sound_beep = pygame.mixer.Sound(os.path.join("audio", "beep.wav"))
sound_playball = pygame.mixer.Sound(os.path.join("audio", "playball.wav"))
sound_strike = pygame.mixer.Sound(os.path.join("audio", "pitch_strike.wav"))


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

    while True:
        clock.tick(60)
        screen.blit(bg, (0, 0))
        x, y = pygame.mouse.get_pos()



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                pass
            elif event.type == pygame.KEYDOWN:
                print(f"{key_index}: You pressed {event.key:c}")
                sound_playball.play()
            elif event.type == pygame.KEYUP:
                print(f"{key_index}: You released {event.key:c}")
                sound_playball.stop()
                sound_strike.play()

        pygame.display.update()



