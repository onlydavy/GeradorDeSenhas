import tkinter as tk
from tkinter import ttk
import random
import string

def gera_senha(tamanho):
    caracteres = string.ascii_letters + string.digits
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

def gerar_senhas():
    quantidade_senhas = int(quantidade_combobox.get())
    tamanho_senhas = int(tamanho_senha_entry.get())

    with open("senha.txt", "w") as arquivo:
        for _ in range(quantidade_senhas):  # Corrigido o nome da variável
            senha = gera_senha(tamanho_senhas)  # Corrigido o nome da variável
            arquivo.write(senha + "\n")
            resultado_text.insert(tk.END, senha + "\n")

    resultado_text.insert(tk.END, "As senhas foram salvas em 'senha.txt'.\n")

def escolher_quantidade(event):
    quantidade = int(quantidade_combobox.get())
    quantidade_senhas_entry.delete(0, tk.END)  # Corrigido o nome da variável
    quantidade_senhas_entry.insert(tk.END, quantidade)   # Corrigido o nome da variável

# Cria uma janela
janela = tk.Tk()
janela.title("Gerador de Senhas")

# Cria um rótulo e uma entrada para o tamanho das senhas
tamanho_senha_label = tk.Label(janela, text="Tamanho das Senhas:")
tamanho_senha_label.pack()
tamanho_senha_entry = tk.Entry(janela)
tamanho_senha_entry.pack()

# Cria um rótulo e uma combobox para escolher a quantidade de senhas
quantidade_label = tk.Label(janela, text="Quantidade de Senhas:")
quantidade_label.pack()
quantidade_combobox = ttk.Combobox(janela, values=[1, 5, 10, 15, 20 , 25])
quantidade_combobox.current(0)
quantidade_combobox.bind("<<ComboboxSelected>>", escolher_quantidade)
quantidade_combobox.pack()

# Cria um botão para gerar as senhas
gerar_senhas_button = tk.Button(janela, text="Gerar Senhas", command=gerar_senhas)
gerar_senhas_button.pack()

# Cria uma área de texto para exibir as senhas geradas
resultado_text = tk.Text(janela)
resultado_text.pack()

# Inicia o loop principal da janela
janela.mainloop()
