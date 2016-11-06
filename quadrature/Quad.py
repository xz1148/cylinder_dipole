import numpy as np
import TriPoints as TP
import Quad
def Quad_SubTetra(pc, ph, p1, p2, order):
    # the function calculates the quadrature over a tetrahedron
    # ph: the projection of centroid on each faces
    # p1, p2: the segment to which ph will project to
    # the final tetrahedon is formed by 4 points
    # ph, pg, pg_12, and p1
    # for another tetrahedron(ph, pg, pg_12, p2) can be calculated in the same
    # way
    pg_12 = TP.pg_single_segment(ph, p1, p2)

    # the tetrahedron is formed by pc, ph1, pg1_23, p1
    sample, weight = np.polynomial.legendre.leggauss(order)
    h = np.linalg.norm(ph - pc) # ph1 is the point projected on face (p2, p3, p4)
    g = np.linalg.norm(pg_12 - ph)
    base = np.linalg.norm(p1 - pg_12)


    # then calculate the sample points
    phi_max = np.arctan(base / g)  # this is a single valu
    phi = Quad.sample_points1D(0.0, phi_max, sample)
    weight_phi = weight / 2.0 *  phi_max

    theta_max = np.arctan(g/np.cos(phi)/h)   # an array
    theta = np.zeros((order, order), float)
    weight_theta = np.zeros((order, order), float)
    for n in range(order):
        theta[n] = Quad.sample_points1D(0, theta_max[n], sample)
        weight_theta[n] = weight / 2.0 * theta_max[n]

    r_max = h / np.cos(theta)
    r = np.zeros((order, order, order), float)
    weight_r = np.zeros((order, order, order), float)
    for m in range(order):
        for n in range(order):
            r[m,n] = Quad.sample_points1D(0, r_max[m,n], sample)
            weight_r[m,n] =  weight / 2.0 * r_max[m,n]

    int_r = np.sum((r**2.0)*weight_r, 2)      # the integal over r
    int_theta_r = np.sum(np.sin(theta)*int_r*weight_theta, 1)
    int_phi_theta_r = np.sum(int_theta_r*weight_phi)
    volume = base*h*g*0.5 / 3.0
    return int_phi_theta_r, volume



def sample_points1D(x1, x2, sample):
    a = (x2 + x1) / 2.0
    b = (x2 - x1) / 2.0
    samples = sample*b + a
    return samples

def sample_points(x1, y1, x2, y2, sample):
    # x1, y1, x2, y2, x3, y3 are the cartisian coordinates, float
    # n is the order, int
    # sample: the sample of abscicass given by Gaussian quadrature
    # length of vector p2 - p1
    # area of triangle formed by the vector
    # height of the triangle
    # a = (x2 + x1) / 2.0
    # b = (x2 - x1) / 2.0
    # x_samples = sample*b + a
    # a = (y2 + y1) / 2.0
    # b = (y2 - y1) / 2.0
    # y_samples = sample*b + a
    x_samples = sample_points1D(x1, x2, sample)
    y_samples = sample_points1D(y1, y2, sample)
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

