import TriPoints as TP
import numpy as np
import Quad

p1 = np.array([0.0, 0.0, 0.0])
p2 = np.array([1.0, 0.0, 0.0])
p3 = np.array([0.0, 1.0, 0.0])
p4 = np.array([0.0, 0.0, 1.0])

pc = TP.centroid(p1, p2, p3, p4)
ph1, ph2, ph3, ph4 = TP.ph(p1, p2, p3, p4, pc)
pg1_23 = TP.pg_single_segment(ph1, p2, p3)

# the tetrahedron is formed by pc, ph1, pg1_23, p1
order = 20
sample, weight = np.polynomial.legendre.leggauss(order)
h = np.linalg.norm(ph1 - pc) # ph1 is the point projected on face (p2, p3, p4)
g = np.linalg.norm(pg1_23 - ph1)
base = np.linalg.norm(p2 - pg1_23)
tang = np.linalg.norm(p2 - ph1)

# then calculate the sample points
phi_max = np.arctan(base / g)  # this is a single valu
phi = Quad.sample_points1D(0.0, phi_max, sample)
weight_phi = weight / 2.0 / phi_max


theta_max = np.arctan(g/np.cos(phi)/h)   # an array
theta = np.zeros((order, order), float)
for n in range(order):
    theta[n] = Quad.sample_points1D(0, theta_max[n], sample)
weight_theta_vec = np.tile(weight, order)
weight_theta_mat = np.reshape(weight_theta_vec, (order, order))
for n in range(order):
    weight_theta_mat[n] /= theta_max[n]


r_max = h / np.cos(theta)



print 'phi'
print phi
print 'theta_max'
print theta_max
# print 'weight_phi'
# print weight_phi
# print 'weight_theta_mat'
# print weight_theta_mat
print 'theta'
print theta
print 'r_max'
print r_max
print 'h, g, base, tang'
print h, g, base, tang
print np.sqrt(g**2 + base**2)
print np.sqrt(h**2 + g**2)
