import pygame
import os

pygame.init()
pygame.mixer.init()

caminho_absoluto = os.path.abspath('C:/Users/Usuário/Documents/aula08/interestelar.mp3')

pygame.mixer.music.load(caminho_absoluto)

pygame.mixer.music.play()

pygame.event.wait()

pygame.quit()
