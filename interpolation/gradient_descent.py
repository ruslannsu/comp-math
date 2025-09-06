from base import Base


class GradientDescent(Base):
    def __init__(self, data_size, rate=0.1, iterations=10):
        super().__init__(data_size)
        self.rate = rate
        self.iterations = iterations
   # def fit(self, x_values, y_values):
        
         