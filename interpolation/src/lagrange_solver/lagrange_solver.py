import numpy as np
from matplotlib import pyplot as pl



def lagrange_solver(x_values, y_values):
    inter_poly_coef = [0.0] * (len(x_values))
    inter_poly_coef = np.array(inter_poly_coef)
    for i in range(len(y_values)):
        func_val = y_values[i]
        poly = []
        for j in range(len(x_values)):
            if (i != j):
                sub_poly = np.array([1, -x_values[j]]) / (x_values[i] - x_values[j])  
                poly.append(sub_poly)
        for k in range(len(poly) - 1):
            poly[k + 1] = np.polymul(poly[k], poly[k + 1])
        poly_coef = poly[len(poly) - 1] * func_val
        inter_poly_coef += poly_coef
    return inter_poly_coef