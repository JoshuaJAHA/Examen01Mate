import numpy as np

def cubic_spline_coefficients(x, y):
    n = len(x) - 1
    h = [x[i+1] - x[i] for i in range(n)]
    alpha = [3/h[i] * (y[i+1] - y[i]) - 3/h[i-1] * (y[i] - y[i-1]) for i in range(1, n)]

    l = [1] * (n+1)
    mu = [0] * (n+1)
    z = [0] * (n+1)

    for i in range(1, n):
        l[i] = 2*(x[i+1] - x[i-1]) - h[i-1]*mu[i-1]
        mu[i] = h[i]/l[i]
        z[i] = (alpha[i-1] - h[i-1]*z[i-1])/l[i]

    b = [0] * (n+1)
    c = [0] * (n+1)
    d = [0] * (n+1)
    a = [y[i] for i in range(n+1)]

    for i in range(n-1, -1, -1):
        c[i] = z[i] - mu[i]*c[i+1]
        b[i] = (y[i+1] - y[i])/h[i] - h[i]*(c[i+1] + 2*c[i])/3
        d[i] = (c[i+1] - c[i])/(3*h[i])

    return a[:-1], b[:-1], c[:-1], d[:-1]

def cubic_spline_polynomials(x, y):
    a, b, c, d = cubic_spline_coefficients(x, y)
    polynomials = []
    for i in range(len(x)-1):
        poly = f'{a[i]} + {b[i]}(x - {x[i]}) + {c[i]}(x - {x[i]})^2 + {d[i]}(x - {x[i]})^3'
        polynomials.append(poly)
    return polynomials

# Generar puntos para las funciones dadas en sus respectivos intervalos.
intervals = [(0.2, 0.4), (0.4, 0.66), (0.66, 0.9), (0.9, 1.3), (1.3, 1.8), (1.8, 2.1), (2.1, 2.47), (2.47, 2.8)]
functions = [lambda x: 2.17*x + 0.3, lambda x: 0.42*x + 1, lambda x: -0.07*x + 1.36, lambda x: -0.42*x + 1.7, lambda x: -0.41*x + 1.69, lambda x: -0.42*x + 1.7, lambda x: -0.45*x + 1.78, lambda x: -0.38*x + 1.6]

x_points = []
y_points = []
for i, (interval, func) in enumerate(zip(intervals, functions)):
    if i == len(intervals) - 1:
        x = np.linspace(interval[0], interval[1], 10)
    else:
        x = np.linspace(interval[0], interval[1], 10)[:-1]
    y = func(x)
    x_points.extend(x)
    y_points.extend(y)

polynomials = cubic_spline_polynomials(x_points, y_points)
for i, poly in enumerate(polynomials):
    print(f'Spline segment {i}: {poly}')