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
order = 4
sample, weight = np.polynomial.legendre.leggauss(order)
h = np.linalg.norm(ph1 - pc)
g = np.linalg.norm(pg1_23 - ph1)
base = np.linalg.norm(p1 - pg1_23)


# then calculate the sample points
phi_max = np.arctan(base / h)


weight_vec = np.tile(weight, order)
weight_mat = np.reshape(weight_vec, (order, order))

phi = Quad.sample_points1D(0.0, phi_max, sample)

phi_vec = np.repeat(phi, order)
phi_mat = np.reshape(phi_vec, (order, order))
weight_phi_mat = weight_mat.T / phi_max



theta_max = np.arctan(g/h/np.cos(phi))
theta = np.zeros((order, order), float)
weight_theta_mat = np.zeros((order, order), float)

for n in range(order):
    theta[n] = Quad.sample_points1D(0, theta_max[n], sample)
    weight_theta_mat[n] = weight_mat[n] / theta_max[n]


print 'phi'
print phi
print 'theta_max'
print theta_max
print 'weight_phi_mat'
print weight_phi_mat
print 'weight_theta_mat'
print weight_theta_mat
print 'weight_mat.T'
print weight_mat.T
print 'phi_mat'
print phi_mat
print 'theta'
print theta
print 'weight[1]'


