import numpy as np
import Quad
import View
#p0 = np.array([0.0,0.0,0.0])
#p1 = np.array([1.0,5.0,2.0])
#p2 = np.array([1.0,3.0,3.0])
#p3 = np.array([2.0,2.0,3.0])

p0 = np.random.rand(3)
p1 = np.random.rand(3)
p2 = np.random.rand(3)
p3 = np.random.rand(3)
#
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

order = 20
sample, weight = np.polynomial.legendre.leggauss(order)

p1_new = np.squeeze(np.asarray(new_axis * v1_mat.T))
p2_new = np.squeeze(np.asarray(new_axis * v2_mat.T))
p3_new = np.squeeze(np.asarray(new_axis * v3_mat.T))
# change phi_max into a array
phi_max = np.squeeze(np.asarray(np.arctan2(p3_new[1], p3_new[0])))
phi = Quad.sample_points1D(0, phi_max, sample)
# the weight of phi should always be positive number, because the quadrature of
# solid angle cannot be negtive number
weight_phi = weight / 2.0 * np.abs(phi_max)
tan_phi = np.tan(phi)

#p1_new is one the z-axis
#p2_new is on the xz-plane
#p3_new is anywhere
v23_new = p3_new - p2_new # a vector p2 -> p3

t = (tan_phi*p2_new[0] - p2_new[1]) / (v23_new[1] - tan_phi*v23_new[0])
xyz_theta_max = np.zeros((order, 3), float)
for n in range(order):
    xyz_theta_max[n] = p2_new + t[n] * v23_new
theta_max = np.arccos(xyz_theta_max[:,2] / np.linalg.norm(xyz_theta_max, 2, 1))
theta = np.zeros((order, order), float)
weight_theta = np.zeros((order, order), float)
for n in range(order):
    theta[n] = Quad.sample_points1D(0, theta_max[n], sample)
    weight_theta[n] = weight / 2.0 * theta_max[n]
# this vector point form point1_new to those points define the theta max
v1_theta_max = xyz_theta_max - p1_new
theta2 = np.arccos(-v1_theta_max[:,2] / np.linalg.norm(v1_theta_max, 2, 1))
theta2_vec = np.repeat(theta2, order)
theta2_mat = np.reshape(theta2_vec, (order, order))
# this value is used for determine maximum r
theta3 = np.pi - (theta + theta2_mat)
sin_theta3 = np.sin(theta3)
sin_theta2_mat = np.sin(theta2_mat)
r_max = np.linalg.norm(p1_new) / sin_theta3 * sin_theta2_mat
r = np.zeros((order, order, order), float)
weight_r = np.zeros((order, order, order), float)
for m in range(order):
    for n in range(order):
        r[m,n] = Quad.sample_points1D(0, r_max[m,n], sample)
        weight_r[m,n] =  weight / 2.0 * r_max[m,n]

# this gives the new cartisian coordinate of all sample points
xyz_new = np.zeros((order, order, order, 3), float)
for l in range(order):
    for m in range(order):
        for n in range(order):
            xyz_new[l,m,n,0] = r[l,m,n] * np.sin(theta[l,m]) * np.cos(phi[l])
            xyz_new[l,m,n,1] = r[l,m,n] * np.sin(theta[l,m]) * np.sin(phi[l])
            xyz_new[l,m,n,2] = r[l,m,n] * np.cos(theta[l,m])
# transform it back to the global coordinate
new2global = np.linalg.inv(new_axis)
xyz_global = np.zeros((order, order, order, 3), float)
for l in range(order):
    for m in range(order):
        for n in range(order):
            # the column vector of xyz_new
            xyz_new_temp = np.asmatrix(xyz_new[l,m,n]).T
            # it turns to an array which can be stored
            xyz_global_temp = np.squeeze(np.asarray(new2global*xyz_new_temp))
            xyz_global[l,m,n] = xyz_global_temp






int_r = np.sum((r**2.0)*weight_r, 2)      # the integal over r
int_theta_r = np.sum(np.sin(theta)*int_r*weight_theta, 1)
int_phi_theta_r = np.sum(int_theta_r*weight_phi)


volume_ref = Quad.Volume_Tetra(np.array([0.0, 0.0, 0.0]), p1_new, p2_new, p3_new)
volume_ref2 = Quad.Volume_Tetra(p0, p1, p2, p3)

print volume_ref2
print volume_ref
print int_phi_theta_r
print xyz_global
View.ViewPoints(np.reshape(xyz_global, (order*order*order, 3)), 10)

#

#
#
#
