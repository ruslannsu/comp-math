import numpy as np

def linear_regression_solver(x_values, y_values):
    x_values = x_values
    y_values = y_values
    X = np.array([[1, xx] for xx in x_values])
    params = np.matmul(np.matmul(np.linalg.inv(np.matmul(np.transpose(X), X)), np.transpose(X)), np.transpose(y_values))
    params = params[::-1]
    return params
