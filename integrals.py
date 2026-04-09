## CALCULUS
# Integration (Single Integrals)
# x**2 * np.sin(2*x) * np.exp(-x)  # integral from 0 to 1

from scipy.integrate import quad
import numpy as np
integrand = lambda x: x**2 * np.sin(x) * np.exp(-x)
integral, integral_error = quad(integrand, 0, 1)   # 0 and 1 are the bounds
# print(integral)
# print(integral_error)

# Integration (Double Integrals)
# np.sin(x+y)**2 ; first integral bounds (0,1), second integral bounds ( -x, x**2)
from scipy.integrate import dblquad
integrand = lambda x,y: np.sin(x+y**2)  
lower_y = lambda x: -x  # lower y bound
upper_y = lambda x: x**2   # upper y bound
integral, integral_error = dblquad(integrand, 0, 1, lower_y, upper_y) 
# print(integral)
# print(integral_error)