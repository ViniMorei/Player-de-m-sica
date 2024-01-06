from tkinter import *
from tkinter import filedialog
from functions import *
import pygame

# Janela principal
root = Tk()
root.title("Player de música 1.1")
root.geometry("500x300")

# Inicialização do player
pygame.mixer.init()

# Listbox com as músicas da playlist
songbox = Listbox(root, bg='black', fg='blue',width=60)
songbox.pack(pady=20)

def add():
    song = filedialog.askopenfilename(initialdir='assets/songs/',
                                      title='Escolha 1 música',
                                      filetypes=(("Arquivos mp3", "*.mp3"), )
                                      )
    songbox.insert(END, song)

def play():
    song = songbox.get(ACTIVE)
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

def stop():
    pygame.mixer.music.stop()
    songbox.selection_clear(ACTIVE)

# Definição dos botões de ação principais
back_btn_img = PhotoImage(file="assets/imgs/back.png")
pause_btn_img = PhotoImage(file="assets/imgs/pause.png")
play_btn_img = PhotoImage(file="assets/imgs/play.png")
stop_btn_img = PhotoImage(file="assets/imgs/stop.png")
next_btn_img = PhotoImage(file="assets/imgs/next.png")

controls_frame = Frame(root)
controls_frame.pack()

back_button = Button(controls_frame,image=back_btn_img, borderwidth=0)
pause_button = Button(controls_frame,image=pause_btn_img, borderwidth=0)
play_button = Button(controls_frame,image=play_btn_img, borderwidth=0, command=play)
stop_button = Button(controls_frame,image=stop_btn_img, borderwidth=0, command=stop)
next_button = Button(controls_frame,image=next_btn_img, borderwidth=0)

back_button.grid(row=0, column=0, padx=10)
pause_button.grid(row=0, column=1, padx=10)
play_button.grid(row=0, column=2, padx=10)
stop_button.grid(row=0, column=3, padx=10)
next_button.grid(row=0, column=4, padx=10)

# Menu
menu_opcoes = Menu(root)
root.config(menu=menu_opcoes)

add_song_menu = Menu(menu_opcoes)
menu_opcoes.add_cascade(label="Adicionar músicas", menu=add_song_menu)
add_song_menu.add_command(label="Adicionar 1 música à Playlist", command=add)

# Iniciar o programa
root.mainloop()
