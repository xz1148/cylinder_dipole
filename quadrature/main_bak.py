import numpy as np


def sample_points(x1, y1, x2, y2, sample):
    # x1, y1, x2, y2, x3, y3 are the cartisian coordinates, float
    # n is the order, int
    # sample: the sample of abscicass given by Gaussian quadrature
    # length of vector p2 - p1
    # area of triangle formed by the vector
    # height of the triangle
    a = (x2 + x1) / 2.0
    b = (x2 - x1) / 2.0
    x_samples = sample*b + a
    a = (y2 + y1) / 2.0
    b = (y2 - y1) / 2.0
    y_samples = sample*b + a
    return x_samples, y_samples


def Quad_Tri_Sample(x1, y1, x2, y2, x3, y3, sample):
    # pass the function to another function
    # quadrature of function f over the area defined by (xn, yn) : n = 1 to 3
    # returns:
    # the final quadrature results
    x_samples12, y_samples12 = sample_points(x1, y1, x2, y2, sample);
    x_samples13, y_samples13 = sample_points(x1, y1, x3, y3, sample);
    n = sample.shape[0]
    tri_x_samples =  np.zeros((n, n), float)
    tri_y_samples =  np.zeros((n, n), float)
    for m in range(n):
        tri_x_samples[m][:], tri_y_samples[m][:] = sample_points(x_samples12[m], y_samples12[m],
                                         x_samples13[m], y_samples13[m],
                                         sample)
    return tri_x_samples, tri_y_samples


def Quad_Tri_Weight(x1, y1, x2, y2, x3, y3, sample, weight):
    # this calculates the weight at each point
    v12_x = x2 - x1
    v12_y = y2 - y1
    v13_x = x3 - x1
    v13_y = y3 - y1
    area = np.abs(v12_x*v13_y - v12_y*v13_x)
    l = np.sqrt((x3-x2)**2.0 + (y3-y2)**2.0)
    h = area/l
    weight1 = l * 0.5 * weight
    x, _ = sample_points(0,0,1,1, sample)

    print h
    weight2 = x * h * weight * 0.5
    print weight2
    return weight1, weight2


def Kernel(x):
    # the quadrature kernel
    # input: array of X, array of Y
    # output: array of f(x,y)
    return x+1




#x1 = 0.0
#y1 = 0.0
#x2 = 1.0
#y2 = 1.0
#x3 = 1.0
#y3 = 5.0
order = 5
sample, weight = np.polynomial.legendre.leggauss(order)
#a, b = Quad_Tri_Sample(x1, y1, x2, y2, x3, y3, sample)
#c, d = Quad_Tri_Weight(x1, y1, x2, y2, x3, y3, sample, weight)
#z = np.ones((order, order), float)
#Z = np.asmatrix(z)
#C = np.asmatrix(c)
#D = np.asmatrix(d)
x, _ = sample_points(0,0,2,2,sample)

print np.sum(np.sin(x) * weight)
print  -np.cos(2.0) + 1

