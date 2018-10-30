import plotter
import math
from tkinter import *

def main():
    window = Tk()

    head = Label(window, text = "This application is designed to plot the equation y' = cos(x) - y.")
    note = Label(window, text = "All graph tabs must be closed in order for the main window to work correctly.")
    lbl_inp_gr = Label(window, text = "Input for the graphs:")
    inp = Frame(window)
    xz = Frame(inp)
    xzl = Label(xz, text = "x0")
    xzi = Entry(xz)
    yz = Frame(inp)
    yzl = Label(yz, text = "y0")
    yzi = Entry(yz)
    xm = Frame(inp)
    xml = Label(xm, text = "x max")
    xmi = Entry(xm)
    nu = Frame(inp)
    nul = Label(nu, text = "n")
    nui = Entry(nu)
    lbl_inp_err = Label(window, text = "Input for the total error:")
    inp_err = Frame(window)
    nz = Frame(inp_err)
    nzl = Label(nz, text = "n0")
    nzi = Entry(nz)
    nm = Frame(inp_err)
    nml = Label(nm, text = "n max")
    nmi = Entry(nm)
    bttn = Button(window, text = "Plot")

    head.pack()
    note.pack()
    lbl_inp_gr.pack()
    xzl.pack(side = LEFT)
    xzi.pack(side = RIGHT)
    xz.pack()
    yzl.pack(side = LEFT)
    yzi.pack(side = RIGHT)
    yz.pack()
    xml.pack(side = LEFT)
    xmi.pack(side = RIGHT)
    xm.pack()
    nul.pack(side = LEFT)
    nui.pack(side = RIGHT)
    nu.pack()
    inp.pack()
    lbl_inp_err.pack()
    nzl.pack(side = LEFT)
    nzi.pack(side = RIGHT)
    nz.pack()
    nml.pack(side = LEFT)
    nmi.pack(side = RIGHT)
    nm.pack()
    inp_err.pack()
    bttn.pack()

    plot = plotter.Plotter(lambda x, c: (math.sin(x) + math.cos(x)) * 0.5 + c * math.exp(-x),
                            lambda x0, y0: math.exp(x0) * ((math.cos(x0) + math.sin(x0)) * 0.5),
                            lambda x, y: math.cos(x) - y)

    bttn.configure(command = lambda: execute(plot, xzi, yzi, xmi, nui, nzi, nmi))

    window.mainloop()

def execute(plot, xzi, yzi, xmi, nui, nzi, nmi):
    try:
        x0 = float(xzi.get())
        y0 = float(yzi.get())
        xmax = float(xmi.get())
        n = int(nui.get())
    except ValueError:
        print("Wrong input")
    else:
        try:
            n0 = int(nzi.get())
            nmax = int(nmi.get())
        except ValueError:
            n0 = None
            nmax = None
        finally:
            plot.plot(x0, y0, xmax, n, n0, nmax)


if __name__ == '__main__':
    main()