from tkinter import *
from tkinter import ttk

# importando Pillow
from PIL import Image, ImageTk

#cores
co0 = "#444466"  # Preta
co1 = "#feffff"  # branca
co2 = "#6f9fbd"  # azul
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#ef5350"   # vermelha

#criando janela
janela = Tk()
janela.title('')
janela.geometry('550x510')
janela.configure(bg=co1)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=272)

style = ttk.Style(janela)
style.theme_use("clam")

# criando frame
frame_pokemon = Frame(janela, width=550, height=290, relief='flat')
frame_pokemon.grid(row=1, column=0)

# nome
pok_nome = Label(frame_pokemon, text='Pikachu', relief='flat', anchor=CENTER, font=('Fixedsys 20'), bg=co1, fg=co0)
pok_nome.place(x=12, y=15)

# categoria
pok_tipo = Label(frame_pokemon, text='Eletrico', relief='flat', anchor=CENTER, font=('ivy 10 bold'), bg=co1, fg=co0)
pok_tipo.place(x=12, y=50)


# tipo
pok_tipo = Label(frame_pokemon, text='#025', relief='flat', anchor=CENTER, font=('ivy 10 bold'), bg=co1, fg=co0)
pok_tipo.place(x=12, y=65)










janela.mainloop()