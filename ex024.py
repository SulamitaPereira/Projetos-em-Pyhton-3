### Para criar um programa que reproduza áudio MP3:
### Faça o download do arquivo no computador;
### Salve com um nome simples, sem acento e letras maiúsculas;
### Copie o arquivo e cole no seu ambiente de projetos do PyCharm;
### Digite o código abaixo:

import pygame
pygame.init()
pygame.mixer.music.load('###nome do arquivo MP3')
pygame.mixer.music.play()
pygame.event.wait()
