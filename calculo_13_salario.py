import tkinter as tk

def decimo_terceiro(salario, meses, parcela):
    decimo = salario / 12 * meses
    if parcela == 'primeira':
        decimo = decimo / 2
    return decimo

def calcular():
    salario = float(salario_entry.get())
    meses = int(meses_entry.get())
    parcela = var.get()
    resultado = decimo_terceiro(salario, meses, parcela)
    resultado_label['text'] = f'O décimo terceiro salário é: R$ {resultado:.2f}'

root = tk.Tk()
root.title('Calculadora de Décimo Terceiro Salário')
root.geometry('400x200')
root.iconbitmap("./icone.ico")
root['bg'] = "#0d76af"

frame = tk.Frame(root)
frame.pack(pady=10)

salario_label = tk.Label(frame, text='Salário bruto: R$ ')
salario_label.place(x=0, y=0)

salario_entry = tk.Entry(frame)
salario_entry.place(x=100, y=0)

meses_label = tk.Label(frame, text='Meses trabalhados: ')
meses_label.place(x=0, y=50)

meses_entry = tk.Entry(frame)
meses_entry.place(x=100, y=50)

var = tk.StringVar(value='segunda')
primeira_radio = tk.Radiobutton(frame, text='Primeira parcela', variable=var, value='primeira')
primeira_radio.place(x=0, y=100)

segunda_radio = tk.Radiobutton(frame, text='Segunda parcela', variable=var, value='segunda')
segunda_radio.place(x=100, y=100)

calcular_button = tk.Button(frame, text='Calcular', command=calcular)
calcular_button.place(x=0, y=150, width=200)

resultado_label = tk.Label(frame, text='')
resultado_label.place(x=0, y=200, width=200)

root.mainloop()
