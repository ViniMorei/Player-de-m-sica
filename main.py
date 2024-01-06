from tkinter import *
from tkinter import filedialog
import pygame

# Janela principal
root = Tk()
root.title("Player de música 1.1")
root.geometry("500x300")

# Listbox com as músicas da playlist
songbox = Listbox(root, bg='black', fg='blue', width=60)
songbox.pack(pady=20)


# Funções
def add():
    song = filedialog.askopenfilename(initialdir='assets/songs/',
                                      title='Escolha 1 música',
                                      filetypes=(("Arquivos mp3", "*.mp3"),)
                                      )
    songbox.insert(END, song)

def add_multiple():
    songs = filedialog.askopenfilenames(initialdir='assets/songs/',
                                      title='Escolha 1 música',
                                      filetypes=(("Arquivos mp3", "*.mp3"),)
                                      )
    for song in songs:
        songbox.insert(END, song)

def play():
    song = songbox.get(ACTIVE)
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)


def stop():
    pygame.mixer.music.stop()
    songbox.selection_clear(ACTIVE)

# Variável global para saber se a música está pausada ou não
global paused
paused = False


def pause(is_paused):
    global paused
    paused = is_paused

    if paused:
        pygame.mixer.music.unpause()
        paused = False
    else:
        pygame.mixer.music.pause()
        paused = True

def next():
    next_song = songbox.curselection()
    next_song = next_song[0] + 1
    song = songbox.get(next_song)
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    songbox.selection_clear(0, END)
    songbox.activate(next_song)
    songbox.selection_set(next_song)

def back():
    last_song = songbox.curselection()
    last_song = last_song[0] - 1
    song = songbox.get(last_song)
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    songbox.selection_clear(0, END)
    songbox.activate(last_song)
    songbox.selection_set(last_song)


# Definição dos botões de ação principais
back_btn_img = PhotoImage(file="assets/imgs/back.png")
pause_btn_img = PhotoImage(file="assets/imgs/pause.png")
play_btn_img = PhotoImage(file="assets/imgs/play.png")
stop_btn_img = PhotoImage(file="assets/imgs/stop.png")
next_btn_img = PhotoImage(file="assets/imgs/next.png")

controls_frame = Frame(root)
controls_frame.pack()

back_button = Button(controls_frame, image=back_btn_img, borderwidth=0, command=back)
pause_button = Button(controls_frame, image=pause_btn_img, borderwidth=0, command=lambda: pause(paused))
play_button = Button(controls_frame, image=play_btn_img, borderwidth=0, command=play)
stop_button = Button(controls_frame, image=stop_btn_img, borderwidth=0, command=stop)
next_button = Button(controls_frame, image=next_btn_img, borderwidth=0, command=next)

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
add_song_menu.add_command(label="Adicionar múltiplas músicas à Playlist", command=add_multiple)

# Iniciar o programa
pygame.mixer.init()
root.mainloop()
