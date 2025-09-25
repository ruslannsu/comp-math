from interpolation.base import Base
from interpolation.src.linear_regression_solver.linear_regression_solver import linear_regression_solver


class LinearRegression(Base):
    def __init__(self, data_size) -> None:
        super().__init__(data_size)

    def fit(self, x_values, y_values) -> None:
        self.coef_ = linear_regression_solver(x_values, y_values)
        