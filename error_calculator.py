import math

class Error_calculator:
    '''
        The class is used to calculate the errors in approximated graph, 
        given the exact graph function and the set of points of approximated graph.
    '''

    def calculate_local(self, exact, x_appr, y_appr):
        x = []
        err = []
        for i in len(x_appr):
            x.append(x_appr[i])
            err.append(math.fabs(exact(x_appr[i]) - y_appr[i]))
        return x, err

    def calculate_total(self, parameter_list):
        pass