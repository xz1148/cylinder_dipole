import numpy as np
def sample_points(x1, y1, x2, y2, n):
    # x1, y1, x2, y2, x3, y3 are the cartisian coordinates, float
    # n is the order, int

    sample, weight = np.polynomial.legendre.leggauss(n)
    l = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    a = (x2 + x1) / 2.0
    b = (x2 - x1) / 2.0
    x_samples = sample*b + a
    a = (y2 + y1) / 2.0
    b = (y2 - y1) / 2.0
    y_samples = sample*b + a

    weight_samples = weight * l * 0.5
    return x_samples, y_samples, weight_samples



order = 6
sample, weight = np.polynomial.legendre.leggauss(order)

x1 = 1.0
y1 = 1.0
x2 = 2.0
y2 = 2.0
x3 = 1.0
y3 = 3.0


x_sample12, y_sample12, weight_sample12 = sample_points(x1, y1, x2, y2, order)
x_sample23, y_sample23, weight_sample23 = sample_points(x2, y2, x3, y3, order)
x_sample01, y_sample01, weight_sample01 = sample_points(1, 0, 1, 1, order)

print np.sum(np.sum(weight_sample01) * y_sample01 * weight_sample01)
print y_sample01


