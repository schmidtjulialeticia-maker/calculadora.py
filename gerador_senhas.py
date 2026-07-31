import tkinter as tk
import random
import string

janela = tk.Tk()

janela.title("Gerador de Senhas")
janela.geometry("400x300")

titulo = tk.Label(
    janela,
    text="Gerador de Senhas",
    font=("Arial", 18, "bold")
)
titulo.pack(pady=20)

label_tamanho = tk.Label(
    janela,
    text="Tamanho da senha:"
)

label_tamanho.pack()

entrada_tamanho = tk.Entry(
    janela
)

entrada_tamanho.pack(pady=10)

def gerar_senha():
    tamanho = int(entrada_tamanho.get())
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ""

    for i in range(tamanho):
        senha += random.choice(caracteres)

    resultado.config(text=senha)

resultado = tk.Label(
    janela,
    text="Sua senha aparecerá aqui",
    font=("Arial", 12)
)
resultado.pack(pady=20)

botao_gerar = tk.Button(
    janela,
    text="Gerar Senha",
    command=gerar_senha
)

botao_gerar.pack(pady=10)

janela.mainloop()