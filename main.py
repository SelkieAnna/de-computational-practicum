import plotter
import math

def main():
    plot = plotter.Plotter(lambda x, c: math.exp(-2 * x) * (math.sin(x) - math.cos(x)) * 0.5 + c,
                            lambda x0, y0: math.exp(-2 * x0) * (math.cos(x0) - math.sin(x0)) * 0.5 + y0,
                            lambda x, y: math.cos(x - y))
    pass

if __name__ == '__main__':
    main()