import customtkinter as ctk
from tkinter import StringVar

# Configuração inicial do tema
cores_tema = {
    "dark": {"bg": "#2E2E2E", "fg": "#FFFFFF"},
    "light": {"bg": "#FFFFFF", "fg": "#000000"}
}
tema_atual = "dark"
ctk.set_appearance_mode(tema_atual)
ctk.set_default_color_theme("blue")

def aplicar_tema():
    tema = cores_tema[tema_atual]
    app.configure(bg=tema["bg"])
    frame_esquerdo.configure(fg_color=tema["bg"])
    frame_direito.configure(fg_color=tema["bg"])
    label_resultado.configure(text_color=tema["fg"])

def alternar_tema():
    global tema_atual
    tema_atual = "light" if tema_atual == "dark" else "dark"
    ctk.set_appearance_mode(tema_atual)
    aplicar_tema()

def converter_temperatura():
    try:
        valor = float(entrada_temp.get())
        opcao = menu_opcoes.get()
        if opcao == "Celsius para Fahrenheit":
            resultado.set(f"{valor * 9/5 + 32:.2f}°F")
        elif opcao == "Fahrenheit para Celsius":
            resultado.set(f"{(valor - 32) * 5/9:.2f}°C")
        else:
            resultado.set("Selecione uma opção")
    except ValueError:
        resultado.set("Entrada inválida")

# Criando a janela principal
app = ctk.CTk()
app.title("Conversor de Temperatura")
app.geometry("700x400")
app.resizable(False, False)

app.update_idletasks()

largura_janela = 700
altura_janela = 400
largura_tela = app.winfo_screenwidth()
altura_tela = app.winfo_screenheight()
x_pos = (largura_tela - largura_janela) // 2
y_pos = (altura_tela - altura_janela) // 2
app.geometry(f"{largura_janela}x{altura_janela}+{x_pos}+{y_pos}")

frame_esquerdo = ctk.CTkFrame(app, width=350, height=400)
frame_direito = ctk.CTkFrame(app, width=350, height=400)
frame_esquerdo.pack(side="left", fill="both", expand=True, padx=5, pady=5)
frame_direito.pack(side="right", fill="both", expand=True, padx=5, pady=5)

# Frame interno centralizador
frame_conteudo_esquerdo = ctk.CTkFrame(frame_esquerdo, fg_color="transparent")
frame_conteudo_esquerdo.place(relx=0.5, rely=0.0, anchor="n")


largura_input = 220
entrada_temp = ctk.CTkEntry(
    frame_conteudo_esquerdo,
    placeholder_text="Digite a temperatura",
    width=largura_input,
    justify="center"
)

resultado = StringVar(value="Resultado")

menu_opcoes = ctk.CTkComboBox(
    frame_conteudo_esquerdo,
    values=["Celsius para Fahrenheit", "Fahrenheit para Celsius"],
    state="readonly",
    width=largura_input,
    justify="center"
)
menu_opcoes.set("Celsius para Fahrenheit")

label_titulo = ctk.CTkLabel(frame_conteudo_esquerdo, text="Conversor de Temperatura", font=("Arial", 20))
label_titulo.pack(pady=10)
entrada_temp.pack(pady=10)
menu_opcoes.pack(pady=5)
ctk.CTkButton(frame_conteudo_esquerdo, text="Converter", command=converter_temperatura).pack(pady=20)

botao_tema = ctk.CTkButton(frame_esquerdo, text="⚙", command=alternar_tema, width=40, height=40, font=("Segoe UI Symbol", 20))
botao_tema.place(x=10, y=330)

label_resultado = ctk.CTkLabel(frame_direito, textvariable=resultado, font=("Arial", 45), anchor="center", width=350, height=200)
label_resultado.place(relx=0.5, rely=0.5, anchor="center")
label_resultado.pack(expand=True)

aplicar_tema()
entrada_temp.focus_set()
app.mainloop()
