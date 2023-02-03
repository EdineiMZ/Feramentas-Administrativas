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
root.geometry('800x100')
root.iconbitmap("./icone.ico")
root['bg'] = "#0d76af"

frame = tk.Frame(root)
frame.pack(pady=10)

salario_label = tk.Label(frame, text='Salário bruto: R$ ')
salario_label.pack(side=tk.LEFT)

salario_entry = tk.Entry(frame)
salario_entry.pack(side=tk.LEFT)

meses_label = tk.Label(frame, text='Meses trabalhados: ')
meses_label.pack(side=tk.LEFT)

meses_entry = tk.Entry(frame)
meses_entry.pack(side=tk.LEFT)

var = tk.StringVar(value='segunda')
primeira_radio = tk.Radiobutton(frame, text='Primeira parcela', variable=var, value='primeira')
primeira_radio.pack(side=tk.LEFT)

segunda_radio = tk.Radiobutton(frame, text='Segunda parcela', variable=var, value='segunda')
segunda_radio.pack(side=tk.LEFT)

calcular_button = tk.Button(root, text='Calcular', command=calcular)
calcular_button.pack(pady=10)

root.mainloop()
