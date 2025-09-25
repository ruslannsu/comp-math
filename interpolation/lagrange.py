from interpolation.base import Base
from interpolation.src.lagrange_solver import lagrange_solver

class LagrangePolynomial(Base):
    def __init__(self, data_size):
        super().__init__(data_size)

    def fit(self, x_values, y_values):
        self.coef_ = lagrange_solver.lagrange_solver(x_values, y_values)
        
        
        
        
    
