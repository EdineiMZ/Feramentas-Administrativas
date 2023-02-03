import tkinter as tk
from tkinter import messagebox

def calcular_inss():
    try:
        salario = float(entry_salario.get())
        if salario <= 1302:
            desconto = salario * 0.075
        elif salario <= 2571.29:
            desconto = (1302 * 0.075) + ((salario - 1302) * 0.09)
        elif salario <= 3856.94:
            desconto = (1302 * 0.075) + (1269.29 * 0.09) + ((salario - 2571.29) * 0.12)
        elif salario <= 7507.49:
            desconto = (1302 * 0.075) + (1269.29 * 0.09) + (1185.65 * 0.12) + ((salario - 3856.94) * 0.14)
        else:
            desconto = (1302 * 0.075) + (1269.29 * 0.09) + (1185.65 * 0.12) + (3650.55 * 0.14)
        label_resultado_inss["text"] = f"Desconto do INSS: R$ {desconto:.2f}"
    except:
        messagebox.showerror("Erro", "Digite um número válido")
        
def calcular_decimo_terceiro():
    try:
        salario = float(entry_salario_13.get())
        meses = float(entry_meses_13.get())
        parcela = entry_parcela_13.get().lower()
        decimo_terceiro = (salario / 12) * meses
        if parcela == "primeira":
            decimo_terceiro /= 2
        label_resultado_13["text"] = f"13º Salário: R$ {decimo_terceiro:.2f}"
    except:
        messagebox.showerror("Erro", "Digite números válidos")

root = tk.Tk()
root.geometry("700x300")
root.title("Calculador de Desconto do INSS e 13º Salário")

frame_inss = tk.Frame(root)
frame_inss.place(relx=0.5, rely=0.2, anchor="center")

label_salario = tk.Label(frame_inss, text="Salário:")
label_salario.pack(side="left")

entry_salario = tk.Entry(frame_inss)
entry_salario.pack(side="left")

button_calcular_inss = tk.Button(frame_inss, text="Calcular", command=calcular_inss)
button_calcular_inss.pack(side="left")

label_resultado_inss = tk.Label(frame_inss, text="")
label_resultado_inss.pack()

frame_13 = tk.Frame(root)
frame_13.place(relx=0.5, rely=0.5, anchor="center")

label_salario_13 = tk.Label(frame_13, text="Salário:")
label_salario_13.pack(side="left")

entry_salario_13 = tk.Entry(frame_13)
entry_salario_13.pack(side="left")

label_meses_13 = tk.Label(frame_13, text="Meses:")
label_meses_13.pack(side="left")

entry_meses_13 = tk.Entry(frame_13)
entry_meses_13.pack(side="left")

label_parcela_13 = tk.Label(frame_13, text="Parcela:")
label_parcela_13.pack(side="left")

entry_parcela_13 = tk.Entry(frame_13)
entry_parcela_13.pack(side="left")

button_calcular_13 = tk.Button(frame_13, text="Calcular", command=calcular_decimo_terceiro)
button_calcular_13.pack(side="left")

label_resultado_13 = tk.Label(frame_13, text="")
label_resultado_13.pack()

root.mainloop()
