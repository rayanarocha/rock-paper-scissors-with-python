import tkinter
from tkinter import *
from tkinter import ttk

# cores --------------------------------
co0 = "#FFFFFF"  # white / branca
co1 = "#333333"  # black / preta
co2 = "#fcc058"  # orange / laranja
co3 = "#fff873"  # yellow / amarela
co4 = "#34eb3d"   # green / verde
co5 = "#e85151"   # red / vermelha

fundo = "#3b3b3b"

#configurando a janela
janela = Tk()
janela.title('')
janela.geometry('260x280')
janela.configure(bg=fundo)

#dividindo a janela

frame_cima = Frame(janela, width=260, height=100, bg=co1, relief='raised')
frame_cima.grid(row=0, column=0, sticky=NW)

frame_baixo = Frame(janela, width=260, height=300, bg=co0, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NW)

estilo = ttk.Style(janela)
estilo.theme_use('clam')

#configurando o frame_cima
app_1 = Label(frame_cima, text='Você', height=1, anchor='center', font=('Ivy 10 bold'), bg=co1, fg=co0)
app_1.place(x=0, y=70)

janela.mainloop()