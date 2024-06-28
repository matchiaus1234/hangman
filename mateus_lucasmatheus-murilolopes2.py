import tkinter as tk
from tkinter import messagebox, PhotoImage
import random as rnd

# Lista de palavras por categoria
categorias = {
    'animais': ['gato', 'cachorro', 'elefante', 'girafa', 'leao', 'tigre', 'macaco', 'zebra', 'coelho', 'cavalo'],
    'fruta': ['maça', 'banana', 'laranja', 'morango', 'abacaxi', 'melancia', 'uva', 'pessego', 'manga', 'kiwi'],
    'objeto': ['caneta', 'caderno', 'computador', 'telefone', 'mesa', 'cadeira', 'carro', 'bola', 'relógio', 'óculos']
}

# Inicialização da aplicação
window = tk.Tk()
window.title("Jogo da Forca")

# Variáveis globais
palavra = ''
tentativas = 10
palavra_forca = []
ja_chutadas = []

# Funções do jogo
def start_game():
    global palavra, tentativas, palavra_forca, ja_chutadas
    categoria = rnd.choice(list(categorias.keys()))
    palavra = rnd.choice(categorias[categoria])
    tentativas = 10
    palavra_forca = ['_' for _ in palavra]
    ja_chutadas = []
    

    

    
def handle_guess():
    global tentativas, ja_chutadas, palavra

    guess = guess_entry.get().lower()
    guess_entry.delete(0, tk.END)

    if len(guess) != 1 or not guess.isalpha():
        messagebox.showinfo("Entrada inválida", "Entre com uma única letra válida.")
        return

    if guess in ja_chutadas:
        messagebox.showinfo("Letra repetida", "Você já tentou esta letra.")
        return

    ja_chutadas.append(guess)

    if guess in palavra:
        for i in range(len(palavra)):
            if palavra[i] == guess:
                palavra_forca[i] = guess
        update_display()

        if ''.join(palavra_forca) == palavra:
            messagebox.showinfo("Parabéns!", f"Você acertou! A palavra era {palavra.upper()}.")
            reset_game()
    else:
        
        tentativas -=1
        if tentativas == 9:
            img["file"] = "IMGERRO3.png"
            update_display()

        if tentativas == 8:
            img["file"] = "IMGERRO4.png"
            update_display()

        if tentativas == 7:
            img["file"] = "IMGERRO5.png"
            update_display()

        if tentativas == 6:
            img["file"] = "IMGERRO6.png"
            update_display()

        if tentativas == 5:
            img["file"] = "IMGERRO7.png"
        update_display()

        if tentativas == 4:
            img["file"] = "IMGERRO8.png"
            update_display()

        if tentativas == 3:
            img["file"] = "IMGERRO9.png"
            update_display()

        if tentativas == 2:
            img["file"] = "IMGERRO10.png"
            update_display()
      
        if tentativas == 0:
            messagebox.showinfo("Fim de jogo", f"Suas tentativas acabaram. A palavra era {palavra.upper()}.")
            reset_game()

def update_display():
    word_label.config(text=" ".join(palavra_forca))
    guessed_label.config(text=f"Tentativas restantes: {tentativas}")
    guessed_letters_label.config(text=f"Letras já tentadas: {' '.join(ja_chutadas)}")

def reset_game():
    start_game()

# Widgets da interface
category_label = tk.Label(window, text="Categoria: ", font=("Arial", 14))
category_label.grid(row=0, column=0, pady=5)

word_label = tk.Label(window, text="", font=("Arial", 24))
word_label.grid(row=1, column=0, pady=10)

guessed_label = tk.Label(window, text="Tentativas restantes: ", font=("Arial", 14))
guessed_label.grid(row=2, column=0, pady=5)

guessed_letters_label = tk.Label(window, text="Letras já tentadas: ", font=("Arial", 14))
guessed_letters_label.grid(row=3, column=0, pady=5)

guess_entry = tk.Entry(window, font=("Arial", 14), width=2)
guess_entry.grid(row=4, column=0, pady=10)

submit_button = tk.Button(window, text="Enviar", font=("Arial", 14), command=handle_guess)
submit_button.grid(row=5, column=0)

img = PhotoImage(file='IMGERRO1.png')
label_img = tk.Label(window, image=img)
label_img.grid(row=6, column=0, pady=10)

# Iniciar o jogo pela primeira vez
start_game()
window.mainloop()
