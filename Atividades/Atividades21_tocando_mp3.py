#ATIVIDADE 21 CURSO EM VIDEO

# Exercício Python 021: Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

import pygame
pygame.init()
pygame.mixer.music.load('../cadastrar.mp3')
pygame.mixer.music.play()
input(pygame.event.wait())