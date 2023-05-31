import tkinter as tk
import math

calculo = str()

def inserir_texto(x):
    global calculo
    calculo = calculo + x
    texto.delete(1.0, "end")
    texto.insert(1.0, calculo)

def avaliar():
    global calculo
    a = str(eval(texto.get(1.0, "end")))
    calculo = str()
    inserir_texto(a)

def apagar():
    global calculo
    calculo = str()
    texto.delete(1.0, "end")

def potencia():
    global calculo
    a = str(eval(texto.get(1.0, "end")))
    resultado = float(a) ** 2
    calculo = str()
    inserir_texto(str(resultado))

def raiz_quadrada():
    global calculo
    a = str(eval(texto.get(1.0, "end")))
    resultado = math.sqrt(float(a))
    calculo = str()
    inserir_texto(str(resultado))

def um_sobre_x():
    global calculo
    a = str(eval(texto.get(1.0, "end")))
    resultado = 1 / float(a)
    calculo = str()
    inserir_texto(str(resultado))

janela = tk.Tk()

texto = tk.Text(janela, height=4, width=26, font=("Arial", 24))
texto.grid(columnspan=5)

botao1 = tk.Button(janela, text="1", command=lambda: inserir_texto("1"), width=13, height=4, font=("Arial", 12))
botao1.grid(column=1, row=2)
# Adicione os demais botões de 2 a 9, 0 e botões adicionais conforme necessário

botao_potencia = tk.Button(janela, text="^2", command=potencia, width=13, height=4, font=("Arial", 12))
botao_potencia.grid(column=4, row=2)
botao_raiz = tk.Button(janela, text="√", command=raiz_quadrada, width=13, height=4, font=("Arial", 12))
botao_raiz.grid(column=4, row=3)
botao_um_sobre_x = tk.Button(janela, text="1/x", command=um_sobre_x, width=13, height=4, font=("Arial", 12))
botao_um_sobre_x.grid(column=4, row=4)
# Adicione outros botões adicionais conforme necessário

janela.mainloop()