import math

class Approximator:
    '''
        This class implements three numerical methods for computing FODE IVP.
    '''

    def __init__(self, fun):
        self.function = fun

    def euler(self, x0, y0, xmax, n, function):
        h = (xmax - x) / n
        x = [x0]
        y = [y0]
        for i in range(1, n + 1):
            x.append(x0 + (i * h))
            y.append(y[i - 1] + (h * function(x[i - 1], y[i - 1])))
        return x, y

    def improved_euler(self, x0, y0, xmax, n, function):
        h = (xmax - x) / n
        x = [x0]
        y = [y0]
        for i in range(1, n + 1):
            x.append(x0 + (i * h))
            dy = h * function(x[i - 1] + h/2, y[i - 1] + h/2 * function(x[i - 1], y[i - 1]))
            y.append(y[i - 1] + dy)
        return x, y

    def runge_kutta(self, x0, y0, xmax, n, function):
        h = (xmax - x) / n
        x = [x0]
        y = [y0]
        for i in range(1, n + 1):
            x.append(x0 + (i * h))
            k1 = function(x[i - 1], y[i - 1])
            k2 = function(x[i - 1] + h/2, y[i - 1] + k1 * h/2)
            k3 = function(x[i - 1] + h/2, y[i - 1] + k2 * h/2)
            k4 = function(x[i - 1] + h, y[i - 1] + h * k3)
            dy = h/6 * (k1 + 2*k2 + 2*k3 + k4)
            y.append(y[i - 1] + dy)
        return x, y