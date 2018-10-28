import approximator
import error_calculator

class Plotter:
    '''
        This class plots exact and approximated graphs of a solution of FODE IVP depending on x0, y0, maximum x and n, 
        given IVP's exact solution, a function to compute the constant in the exact solution and a function (y' = f(x, y)).
    '''

    def __init__(self, exact_solution, constant, fun):
        self.exact = exact_solution
        self.const = constant
        self.function = fun
        pass

    def plot_exact(self, x0, y0, xmax, n, exact, const):
        c = const(x0, y0)
        h = (xmax - x0) / n
        x = [x0]
        y = [y0]
        for i in range(1, n+1):
            x.append(x0 + (i * h))
            y.append(exact(x[i], c))
        # plot graph
        pass

    def plot_euler(self, x0, y0, xmax, n, function):
        appr = approximator.Approximator(function)
        graph = appr.euler(x0, y0, xmax, n)
        calc = error_calculator.Error_calculator()
        err = calc.calculate_local(exact, graph[0], graph[1])
        # plot graph
        # plot error
        pass

    def plot_improved_euler(self, x0, y0, xmax, n, function):
        appr = approximator.Approximator(function)
        graph = appr.improved_euler(x0, y0, xmax, n)
        calc = error_calculator.Error_calculator()
        err = calc.calculate_local(exact, graph[0], graph[1])
        # plot graph
        # plot error
        pass

    def plot_runge_kutta(self, x0, y0, xmax, n, function):
        appr = approximator.Approximator(function)
        graph = appr.runge_kutta(x0, y0, xmax, n)
        calc = error_calculator.Error_calculator()
        err = calc.calculate_local(exact, graph[0], graph[1])
        # plot graph
        # plot error
        pass

    def plot_euler_err(self, parameter_list):
        pass

    def plot_improved_euler_err(self, parameter_list):
        pass

    def plot_runge_kutta_err(self, parameter_list):
        pass