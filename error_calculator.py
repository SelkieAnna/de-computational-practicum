import math

class Error_calculator:
    '''
        The class is used to calculate the errors in approximated graph, 
        given the exact graph function and the set of points of approximated graph.
    '''

    def calculate_local(self, exact, const, x_appr, y_appr):
        x = []
        err = []
        for i in range(len(x_appr)):
            x.append(x_appr[i])
            err.append(math.fabs(exact(x_appr[i], const(x_appr[0], y_appr[0])) - y_appr[i]))
        return x, err

    def calculate_total(self, exact, const, approx_function, x0, y0, xmax, n0, nmax):
        x = []
        err = []
        for n in range(n0, nmax):
            x.append(n)
            approx = approx_function(x0, y0, xmax, n)
            loc = self.calculate_local(exact, const, *approx)
            m = max(loc[1])
            err.append(m)
        return x, err