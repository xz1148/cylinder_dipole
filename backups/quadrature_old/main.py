import TriPoints as TP
import numpy as np
import Quad

p1 = np.array([0.0, 0.0, 0.0])
p2 = np.array([3.0, 1.9, 0.0])
p3 = np.array([2.9, 2.0, 0.0])
p4 = np.array([0.0, 0.0, 2.0])
order = 20

pc = TP.centroid(p1, p2, p3, p4)
ph1, ph2, ph3, ph4 = TP.ph(p1, p2, p3, p4, pc)

a = Quad.Quad_SubTetra_Face(pc, ph1, p2, p3, p4, order)
b = Quad.Volume_Tetra(pc, p2, p3, p4)

c = Quad.Quad_SubTetra_Segment(pc, ph1, p2, p3, order)
pg1_23 = TP.pg_single_segment(ph1, p2, p3)
d = Quad.Volume_Tetra(pc, ph1, pg1_23, p2)

v1 = pg1_23 - ph1
v2 = p3 - p4
pen = np.dot(v1, v2)


#pg1_23 = TP.pg_single_segment(ph1, p2, p3)
#
## the tetrahedron is formed by pc, ph1, pg1_23, p1
#order = input("please input the order of quadrature")
#sample, weight = np.polynomial.legendre.leggauss(order)
#h = np.linalg.norm(ph1 - pc) # ph1 is the point projected on face (p2, p3, p4)
#g = np.linalg.norm(pg1_23 - ph1)
#base = np.linalg.norm(p2 - pg1_23)
#tang = np.linalg.norm(p2 - ph1)
#
#
## then calculate the sample points
#phi_max = np.arctan(base / g)  # this is a single valu
#phi = Quad.sample_points1D(0.0, phi_max, sample)
#weight_phi = weight / 2.0 *  phi_max
#
#theta_max = np.arctan(g/np.cos(phi)/h)   # an array
#theta = np.zeros((order, order), float)
#weight_theta = np.zeros((order, order), float)
#for n in range(order):
#    theta[n] = Quad.sample_points1D(0, theta_max[n], sample)
#    weight_theta[n] = weight / 2.0 * theta_max[n]
#
#r_max = h / np.cos(theta)
#r = np.zeros((order, order, order), float)
#weight_r = np.zeros((order, order, order), float)
#for m in range(order):
#    for n in range(order):
#        r[m,n] = Quad.sample_points1D(0, r_max[m,n], sample)
#        weight_r[m,n] =  weight / 2.0 * r_max[m,n]
#
#int_r = np.sum((r**2.0)*weight_r, 2)      # the integal over r
#int_theta_r = np.sum(np.sin(theta)*int_r*weight_theta, 1)
#int_phi_theta_r = np.sum(int_theta_r*weight_phi)
#
#volume = base*h*g*0.5 / 3.0
#rl_diff = (int_phi_theta_r - volume) / volume
#
#print np.dot(ph1 - pc, p2 - p3)
#print np.dot(ph1 - pc, p4 - p3)
#print np.dot(ph1 - pc, p2 - p4)
#print np.dot(pg1_23 - ph1, p2 - p3)
#print np.max(r_max[n])
#print np.linalg.norm(p2 - pg1_23)
#print 'rl_diff, volume, int_phi_theta_r'
#print rl_diff, volume, int_phi_theta_r
##sample_result = Quad.sample_points1D(0, r_max[0,0], sample)
##weight_result = weight / 2.0 * r_max[0,0]
##print sample_result
#print np.linalg.norm(int_r - r_max **3.0 / 3.0)
print 'a,b'
print a, b

print 'c,d'
print c, d
print 'p3'
print p3

print 'p4'
print p4
print 'pg1_23'
print pg1_23
print 'ph1'
print ph1
print 'pen'
print pen
