import pandas as pd
import matplotlib.pyplot as plt 
from matplotlib.backends._backend_tkagg import FigurecanvasTkAgg
import tkinter as tk

paises = pd.Series(
    [28.52, 50.34, 32.51, 17.64, 19.12],
    index=["Venezuela","Colombia", "Peru", "Ecuador","Chile"],
)
fig=plt.figure()
plt.plot(paises)
root = tk.Tk()
canvas = FigurecanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack()
root.mainloop()

