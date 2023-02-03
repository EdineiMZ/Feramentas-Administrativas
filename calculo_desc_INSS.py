import tkinter as tk

def inss_discount(salary):
  discount = 0
  if salary <= 1302:
    discount = salary * 0.075
  elif salary <= 2571.29:
    discount = 1302 * 0.075 + (salary - 1302) * 0.09
  elif salary <= 3856.94:
    discount = 1302 * 0.075 + (2571.29 - 1302) * 0.09 + (salary - 2571.29) * 0.12
  elif salary <= 7507.49:
    discount = 1302 * 0.075 + (2571.29 - 1302) * 0.09 + (3856.94 - 2571.29) * 0.12 + (salary - 3856.94) * 0.14
  else:
    discount = 1302 * 0.075 + (2571.29 - 1302) * 0.09 + (3856.94 - 2571.29) * 0.12 + (7507.49 - 3856.94) * 0.14 + (salary - 7507.49) * 0.14
  return discount

def show_discount():
  salary = float(salary_entry.get())
  discount = inss_discount(salary)
  discount_label.config(text=f"Desconto: {discount:.2f}")

root = tk.Tk()
root.title("Cálculo de Desconto INSS")
root.geometry('400x200')
root.iconbitmap("./icone.ico")
root['bg'] = "#0d76af"

salary_label = tk.Label(root, text="Salário:",
                        bg="#063970",
                        fg="#aaaaaa",
                        width=20) 
salary_entry = tk.Entry(root)

discount_label = tk.Label(root, text="Desconto:",
                        bg="#063970",
                        fg="#aaaaaa",
                        width=20)
calculate_button = tk.Button(root, text="Calcular", command=show_discount,
                        bg="#063970",
                        fg="#aaaaaa",
                        width=20)


salary_label.grid(row=0, column=0)
salary_entry.grid(row=0, column=1)
discount_label.grid(row=1, column=0)
calculate_button.grid(row=1, column=1)

root.mainloop()