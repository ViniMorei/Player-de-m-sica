from tkinter import *
import pygame

# Janela principal
root = Tk()
root.title("Player de música 1.0")
root.geometry("500x400")

# Inicialização do player
pygame.mixer.init()


def play():  # Função que irá tocar a música
    pygame.mixer.music.load("C:/Users/vinic/Downloads/SPARKS_FLY_SAMPLE.mp3")
    pygame.mixer.music.play(loops=0)


def stop():  # Função que para a música
    pygame.mixer.music.stop()


# Definição dos botões principais
play_button = Button(root, text="Tocar música", font=("Helvetica", 32), command=play)
play_button.pack(pady=20)

stop_button = Button(root, text="Parar música", font=("Helvetica", 32), command=stop)
stop_button.pack(pady=20)


# Iniciar o programa
root.mainloop()
