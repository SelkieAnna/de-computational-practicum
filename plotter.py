import approximator
import error_calculator
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt

# 
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

    # 
    def plot_exact(self, x0, y0, xmax , n):
        c = self.const(x0, y0)
        h = (xmax - x0) / n
        x = [x0]
        y = [y0]
        for i in range(1, n + 1):
            x.append(x0 + (i * h))
            y.append(self.exact(x[i], c))
        plt.figure()
        plt.plot(x, y)
        plt.title('The Exact Solution Plot')
        plt.show()

    def plot_euler(self, x0, y0, xmax, n):
        appr = approximator.Approximator(self.function)
        graph = appr.euler(x0, y0, xmax, n)
        calc = error_calculator.Error_calculator()
        gl_err = calc.calculate_global(self.exact, self.const, graph[0], graph[1])
        plt.figure()
        plt.subplot(2, 2, 1)
        plt.plot(graph[0], graph[1])
        plt.title('Euler Method Plot')
        plt.subplot(2, 2, 2)
        plt.plot(gl_err[0], gl_err[1])
        plt.title('Global Error')
        plt.show()

    def plot_improved_euler(self, x0, y0, xmax, n):
        appr = approximator.Approximator(self.function)
        graph = appr.improved_euler(x0, y0, xmax, n)
        calc = error_calculator.Error_calculator()
        gl_err = calc.calculate_global(self.exact, self.const, graph[0], graph[1])
        plt.figure()
        plt.subplot(2, 2, 1)
        plt.plot(graph[0], graph[1])
        plt.title('Improved Euler Method Plot')
        plt.subplot(2, 2, 2)
        plt.plot(gl_err[0], gl_err[1])
        plt.title('Global Error')
        plt.show()

    def plot_runge_kutta(self, x0, y0, xmax, n):
        appr = approximator.Approximator(self.function)
        graph = appr.runge_kutta(x0, y0, xmax, n)
        calc = error_calculator.Error_calculator()
        gl_err = calc.calculate_global(self.exact, self.const, graph[0], graph[1])
        plt.figure()
        plt.subplot(2, 2, 1)
        plt.plot(graph[0], graph[1])
        plt.title('Runge-Kutta  Method Plot')
        plt.subplot(2, 2, 2)
        plt.plot(gl_err[0], gl_err[1])
        plt.title('Global Error')
        plt.show()

    def plot_euler_err(self, parameter_list):
        pass

    def plot_improved_euler_err(self, parameter_list):
        pass

    def plot_runge_kutta_err(self, parameter_list):
        pass