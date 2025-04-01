# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

# PRIMEIRA FORMA DE FAZER / Nessa forma o sistema puxa o áudio, mas não finaliza quando termina.

import pygame
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()



# SEGUNDA FORMA DE FAZER / Nessa forma, ele puxa o áudio e identifica até quando ele tá rodando, finalizando assim que para de tocar.

import pygame as pg
pg.mixer.init()

pg.mixer.music.load('C:/Users/TaynanSS/Downloads/spongebob-fail.mp3')
pg.mixer.music.play()

while pg.mixer.music.get_busy():
    pg.time.Clock().tick(10)