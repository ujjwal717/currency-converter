from forex_python.converter import CurrencyRates
import tkinter as tk

window = tk.Tk()
window.title("Currency Converter ")

def conversions():
    input_from = from1.get()
    input_to = to.get()
    rate = c.get_rate(input_from, input_to)
    result_label.config(text=f"Conversion Rate : {rate:.2f}")

label = tk.Label(window, text="Get Conversion Rate ")
label.pack()

instruction_label1 = tk.Label(window, text="From:")
instruction_label1.pack()

from1 = tk.Entry(window)
from1.pack()

instruction_label2 = tk.Label(window, text="To:")
instruction_label2.pack()
to = tk.Entry(window)
to.pack()

button = tk.Button(window, text="Get Conversions", command=conversions)
button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

c = CurrencyRates()

window.mainloop()








