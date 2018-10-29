import plotter
import math
from tkinter import *

def main():
    window = Tk()

    head = Label(window, text = "This application is designed to plot the equation y' = cos(x) - y.")
    note = Label(window, text = "All graph tabs must be closed in order for the main window to work correctly.")
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
    buttn = Frame(window)
    bttn_ex = Button(buttn, text = "Plot the exact solution graph")
    bttn_eu = Button(buttn, text = "Plot using Euler method")
    bttn_ie = Button(buttn, text = "Plot using Improved Euler method")
    bttn_rk = Button(buttn, text = "Plot using Runge-Kutta method")

    head.pack()
    note.pack()
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
    inp.pack(side = LEFT)
    bttn_ex.pack()
    bttn_eu.pack()
    bttn_ie.pack()
    bttn_rk.pack()
    buttn.pack(side = RIGHT)

    plot = plotter.Plotter(lambda x, c: math.exp(-2 * x) * (math.sin(x) - math.cos(x)) * 0.5 + c,
                            lambda x0, y0: math.exp(-2 * x0) * (math.cos(x0) - math.sin(x0)) * 0.5 + y0,
                            lambda x, y: math.cos(x) - y)

    bttn_ex.configure(command = lambda: execute_ex(plot, xzi, yzi, xmi, nui))
    bttn_eu.configure(command = lambda: execute_eu(plot, xzi, yzi, xmi, nui))
    bttn_ie.configure(command = lambda: execute_ie(plot, xzi, yzi, xmi, nui))
    bttn_rk.configure(command = lambda: execute_rk(plot, xzi, yzi, xmi, nui))

    window.mainloop()

def execute_ex(plot, xzi, yzi, xmi, nui):
    try:
        x0 = float(xzi.get())
        y0 = float(yzi.get())
        xmax = float(xmi.get())
        n = int(nui.get())
    except ValueError:
        print("Wrong input")
        pass
    else:
        plot.plot_exact(x0, y0, xmax, n)

def execute_eu(plot, xzi, yzi, xmi, nui):
    try:
        x0 = float(xzi.get())
        y0 = float(yzi.get())
        xmax = float(xmi.get())
        n = int(nui.get())
    except ValueError:
        print("Wrong input")
        pass
    else:
        plot.plot_euler(x0, y0, xmax, n)

def execute_ie(plot, xzi, yzi, xmi, nui):
    try:
        x0 = float(xzi.get())
        y0 = float(yzi.get())
        xmax = float(xmi.get())
        n = int(nui.get())
    except ValueError:
        print("Wrong input")
        pass
    else:
        plot.plot_improved_euler(x0, y0, xmax, n)

def execute_rk(plot, xzi, yzi, xmi, nui):
    try:
        x0 = float(xzi.get())
        y0 = float(yzi.get())
        xmax = float(xmi.get())
        n = int(nui.get())
    except ValueError:
        print("Wrong input")
        pass
    else:
        plot.plot_runge_kutta(x0, y0, xmax, n)


if __name__ == '__main__':
    main()