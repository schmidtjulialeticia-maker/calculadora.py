import tkinter as tk

janela = tk.Tk()

janela.title("Calculadora")
janela.geometry("400x300")


titulo = tk.Label(
    janela,
    text="Calculadora",
    font=("Arial", 18, "bold")
)

titulo.pack(pady=15)


# Primeiro número
label_numero1 = tk.Label(
    janela,
    text="Primeiro número:"
)

label_numero1.pack()


entrada_numero1 = tk.Entry(
    janela,
    width=20
)

entrada_numero1.pack(pady=5)


# Segundo número
label_numero2 = tk.Label(
    janela,
    text="Segundo número:"
)

label_numero2.pack()


entrada_numero2 = tk.Entry(
    janela,
    width=20
)

entrada_numero2.pack(pady=5)



# Função da calculadora
def calcular(operacao):

    try:
        numero1 = float(entrada_numero1.get())
        numero2 = float(entrada_numero2.get())


        if operacao == "+":
            resultado = numero1 + numero2

        elif operacao == "-":
            resultado = numero1 - numero2

        elif operacao == "*":
            resultado = numero1 * numero2

        elif operacao == "/":

            if numero2 == 0:
                resultado = "Erro: divisão por zero!"

            else:
                resultado = numero1 / numero2


        label_resultado.config(
            text=f"Resultado: {resultado}"
        )


    except ValueError:
        label_resultado.config(
            text="Digite apenas números!"
        )



# Resultado
label_resultado = tk.Label(
    janela,
    text="Resultado:",
    font=("Arial", 12, "bold")
)

label_resultado.pack(pady=15)



# Botões
frame_botoes = tk.Frame(janela)

frame_botoes.pack(pady=10)


botao_somar = tk.Button(
    frame_botoes,
    text="+",
    width=5,
    command=lambda: calcular("+")
)

botao_somar.grid(row=0, column=0, padx=5)



botao_subtrair = tk.Button(
    frame_botoes,
    text="-",
    width=5,
    command=lambda: calcular("-")
)

botao_subtrair.grid(row=0, column=1, padx=5)



botao_multiplicar = tk.Button(
    frame_botoes,
    text="×",
    width=5,
    command=lambda: calcular("*")
)

botao_multiplicar.grid(row=0, column=2, padx=5)



botao_dividir = tk.Button(
    frame_botoes,
    text="÷",
    width=5,
    command=lambda: calcular("/")
)

botao_dividir.grid(row=0, column=3, padx=5)



janela.mainloop()