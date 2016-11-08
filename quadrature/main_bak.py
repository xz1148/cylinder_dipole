import numpy as np
import Quad


p0 = np.array([0.0,0.0,0.0])
p1 = np.array([1.0,1.0,0.0])
p2 = np.array([1.0,0.0,3.0])
p3 = np.array([0.0,2.0,3.0])


v1 = p1 - p0
v2 = p2 - p0
v3 = p3 - p0

axis3_norm = v1 / np.linalg.norm(v1)
axis2 = np.cross(v1, v2)
axis2_norm = axis2 / np.linalg.norm(axis2)
axis1_norm = np.cross(axis2_norm, axis3_norm)

new_axis = np.matrix([axis1_norm, axis2_norm, axis3_norm])

v1_mat =  np.asmatrix(v1)
v2_mat =  np.asmatrix(v2)
v3_mat =  np.asmatrix(v3)

order = 5
sample, weight = np.polynomial.legendre.leggauss(order)

p1_new = np.squeeze(np.asarray(new_axis * v1_mat.T))
p2_new = np.squeeze(np.asarray(new_axis * v2_mat.T))
p3_new = np.squeeze(np.asarray(new_axis * v3_mat.T))
# change phi_max into a array
phi_max = np.squeeze(np.asarray(np.arctan2(p3_new[1], p3_new[0])))
phi = Quad.sample_points1D(0, phi_max, sample)
tan_phi = np.tan(phi)

#p1_new is one the z-axis
#p2_new is on the xz-plane
#p3_new is anywhere
v23_new = p3_new - p2_new # a vector p2 -> p3

print p1_new
print p2_new
print p3_new
print tan_phi
