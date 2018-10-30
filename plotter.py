import approximator
import error_calculator
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
import math

class Plotter:
    '''
        This class plots exact and approximated graphs of a solution of FODE IVP depending on x0, y0, maximum x and n, 
        given IVP's exact solution, a function to compute the constant in the exact solution and a function (y' = f(x, y)).
    '''

    def __init__(self, exact_solution, constant, fun):
        self.exact = exact_solution
        self.const = constant
        self.function = fun

    def exact_graph(self, x0, y0, xmax , n):
        c = self.const(x0, y0)
        h = (xmax - x0) / n
        x = [x0]
        y = [y0]
        for i in range(1, n + 1):
            x.append(x0 + (i * h))
            y.append(self.exact(x[i], c))
        return x, y

    def plot(self, x0, y0, xmax, n, n0, nmax):
        appr = approximator.Approximator(self.function)
        calc = error_calculator.Error_calculator()

        graph_exact = self.exact_graph(x0, y0, xmax, n)
        graph_euler = appr.euler(x0, y0, xmax, n)
        graph_improvedeuler = appr.improved_euler(x0, y0, xmax, n)
        graph_rungekutta = appr.runge_kutta(x0, y0, xmax, n)

        localerror_euler = calc.calculate_local(self.exact, self.const, *graph_euler)
        localerror_improvedeuler = calc.calculate_local(self.exact, self.const, *graph_improvedeuler)
        localerror_rungekutta = calc.calculate_local(self.exact, self.const, *graph_rungekutta)

        if (n0 and nmax and n):
            globalerror_euler = calc.calculate_total(self.exact, self.const, appr.euler, x0, y0, xmax, n0, nmax)
            globalerror_improvedeuler = calc.calculate_total(self.exact, self.const, appr.improved_euler, x0, y0, xmax, n0, nmax)
            globalerror_rungecutta = calc.calculate_total(self.exact, self.const, appr.runge_kutta, x0, y0, xmax, n0, nmax)

        plt.figure()

        plt.subplot(2, 2, 1)
        plt.plot(*graph_euler, label = "Euler")
        plt.plot(*graph_improvedeuler, label = "Improved Euler")
        plt.plot(*graph_rungekutta, label = "Runge-Kutta")
        plt.plot(*graph_exact, label = "Exact")
        plt.title('Function & its approximations')
        plt.legend(loc=9, bbox_to_anchor=(0.5, -0.1))

        plt.subplot(2, 2, 2)
        plt.plot(*localerror_euler, label = "Euler")
        plt.plot(*localerror_improvedeuler, label = "Improved Euler")
        plt.plot(*localerror_rungekutta, label = "Runge-Kutta")
        plt.title('Local Errors')

        if (n0 and nmax):
            plt.subplot(2, 2, 4)
            plt.plot(*globalerror_euler, label = "Euler")
            plt.plot(*globalerror_improvedeuler, label = "Improved Euler")
            plt.plot(*globalerror_rungecutta, label = "Runge-Kutta")
            plt.ylabel('max error for a number of glid cells n')
            plt.title('Total Errors')

        plt.show()