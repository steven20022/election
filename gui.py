import data
import matplotlib
import numpy
import sys

matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

if sys.version_info[0] < 3:
    import Tkinter as Tk
else:
    import tkinter as Tk

root = Tk.Tk()

f = Figure(figsize=(5, 4), dpi=100)
ax = f.add_subplot(111)
ax.set_xlabel("Parties")
ax.set_ylabel("Votes")
ax.set_xticks([0, 1, 2])
ax.set_xticklabels(['Democrats', 'Republicans', 'Swing'])

_data = (data.blue, data.red, data.swing)

ind = numpy.arange(3)
width = .5
ax.bar(ind, _data, width)

canvas = FigureCanvasTkAgg(f, master=root)
canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

v = Tk.IntVar()
v.set(3)

party = [
    ("Republican",1),
    ("Democratic",2),
    ("Swing",3)]


def move():
    print(v.get())
    if v.get() == 0:
        data.Move_States("data.txt", "Pennsylvania", "swing", "red")
    if v.get() == 1:
        data.Move_States("data.txt", "Pennsylvania", "swing", "blue")
    if v.get() == 2:
        data.Move_States("data.txt", "Pennsylvania", "swing", "swing")
    Tk.Frame.update(root)


Tk.Label(root,
         text="""Pennsylvania""",
         justify=Tk.LEFT,
         padx=20).pack()
for val, language in enumerate(party):
    Tk.Radiobutton(root,
                   text=language,
                   padx=20,
                   variable=v,
                   command=move(),
                   value=val).pack(anchor=Tk.W)



Tk.mainloop()
