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

frame = tk.Frame(root)
frame.pack(pady=10)

salario_label = tk.Label(frame, text='Salário bruto: R$ ')
salario_label.grid(row=0, column=0)

salario_entry = tk.Entry(frame)
salario_entry.grid(row=0, column=1)

meses_label = tk.Label(frame, text='Meses trabalhados: ')
meses_label.grid(row=1, column=0)

meses_entry = tk.Entry(frame)
meses_entry.grid(row=1, column=1)

var = tk.StringVar(value='segunda')
primeira_radio = tk.Radiobutton(frame, text='Primeira parcela', variable=var, value='primeira')
primeira_radio.grid(row=2, column=0)

segunda_radio = tk.Radiobutton(frame, text='Segunda parcela', variable=var, value='segunda')
segunda_radio.grid(row=2, column=1)

calcular_button = tk.Button(frame, text='Calcular', command=calcular)
calcular_button.grid(row=3, column=0, columnspan=2)

resultado_label = tk.Label(frame, text='')
resultado_label.grid(row=4, column=0, columnspan=2)

root.mainloop()
