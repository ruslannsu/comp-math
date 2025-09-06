from base import Base
from src.lagrange_solver import lagrange_solver

class LagrangePolynomial(Base):
    def __init__(self, data_size):
        super().__init__(data_size)

    def fit(self, x_values, y_values):
        if len(x_values) != self.data_size or len(y_values != self.data_size):
            return None
        self.coef_ = lagrange_solver(x_values, y_values)
        
        
        
        
    
