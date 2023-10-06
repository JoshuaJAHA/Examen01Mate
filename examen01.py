import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt

# Establecer los puntos dados
x = np.array([0.2, 0.21, 0.4, 0.66, 0.9, 1.3, 1.8, 2.1, 2.47, 2.8, 3.2, 3.6, 4, 4.3, 4.7, 5.1, 5.4, 5.5, 5.7, 6, 6.16])
y = np.array([0.84, 0.4, 0.66, 0.9, 1.3, 1.8, 2.1, 2.47, 2.8, 3.2, 3.6, 4, 4.3, 4.7, 5.1, 5.4, 5.5, 5.7, 6, 6.16, 6.29])

# Formar el spline cúbico
cs = CubicSpline(x, y, bc_type='natural')

# Evaluar el spline cúbico
x_new = np.linspace(0.2, 7.3, 1000)
y_new = cs(x_new)

# Graficar el spline cúbico
plt.plot(x, y, 'bo', label='Puntos Dados')
plt.plot(x_new, y_new, 'r-', label='Spline Cúbico')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='best')
plt.title('Interpolación Spline Cúbica')
plt.show()
