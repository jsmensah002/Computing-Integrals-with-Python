## CALCULUS
from scipy.integrate import quad
from scipy.integrate import dblquad
from scipy.integrate import tplquad
import numpy as np

### Integration (Single Integrals)
# x³ * cos(x) dx  # integral from 0 to π
integrand = lambda x: x**3 * np.cos(x)
lower_x = 0
upper_x = np.pi
integral, integral_error = quad(integrand, lower_x, upper_x)   
# print(integral)
# print(integral_error)

# e^(-x²) * x  # integral from 0 to 2
integrand = lambda x: np.exp(-x**2) * x
lower_x = 0
upper_x = 2
integral, integral_error = quad(integrand, lower_x, upper_x)   
# print(integral)
# print(integral_error)

# x * ln(x)  # integral from 1 to 3
integrand = lambda x: x * np.log(x)
lower_x = 1
upper_x = 3
integral, integral_error = quad(integrand, lower_x, upper_x)    
# print(integral)
# print(integral_error)


### Integration (Double Integrals)
# x²y dx ; first integral bounds (0,2), second integral bounds (0, x)
integrand = lambda y, x: x**2 * y 
lower_x = 0
upper_x = 2
lower_y = lambda x: 0  # lower y bound
upper_y = lambda x: x   # upper y bound
integral, integral_error = dblquad(integrand, lower_x, upper_x, lower_y, upper_y) 
# print(integral)
# print(integral_error)

# e^(x+y) ; first integral bounds (0,1), second integral bounds (-x, x**2)
integrand = lambda y, x: np.exp(x+y) 
lower_x = 0
upper_x = 1
lower_y = lambda x: -x  # lower y bound
upper_y = lambda x: x**2   # upper y bound
integral, integral_error = dblquad(integrand, lower_x, upper_x, lower_y, upper_y) 
# print(integral)
# print(integral_error)

# cos(x) * sin(y) ; first integral bounds (0,pi), second integral bounds (0, x**2)
integrand = lambda y, x: np.cos(x) * np.sin(y)  
lower_x = 0
upper_x = np.pi
lower_y = lambda x: 0  # lower y bound
upper_y = lambda x: x**2   # upper y bound
integral, integral_error = dblquad(integrand, lower_x, upper_x, lower_y, upper_y) 
# print(integral)
# print(integral_error)


### Integration (Triple Integrals)
# cos(x) * sin(y) * z  ; x bounds (0,pi), y bounds (0, x**2), z bounds (x, x**3)
integrand = lambda z, y, x: np.cos(x) * np.sin(y) * z
lower_x = 0
upper_x = np.pi
lower_y = lambda x: 0
upper_y = lambda x: x**2
lower_z = lambda x, y: x
upper_z = lambda x, y: x**3 
integral, integral_error = tplquad(integrand, lower_x, upper_x, lower_y, upper_y, lower_z, upper_z)
# print(integral)
# print(integral_error)

