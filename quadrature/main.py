import numpy as np
import Quad
import View
#p0 = np.array([0.0,0.0,0.0])
#p1 = np.array([1.0,5.0,2.0])
#p2 = np.array([1.0,3.0,3.0])
#p3 = np.array([2.0,2.0,3.0])
def fun(p):
    return 2

p0 = np.random.rand(3) * np.random.rand(1)
p1 = np.random.rand(3) * np.random.rand(1)
p2 = np.random.rand(3) * np.random.rand(1)
p3 = np.random.rand(3) * np.random.rand(1)
order = 10
sample, weight = np.polynomial.legendre.leggauss(order)

volume, xyz_new, xyz_global = \
    Quad.Quad_Tetra(fun, p0, p1, p2, p3, sample, weight)
volume2 = Quad.Volume_Tetra(p0, p1, p2, p3)



xyz_new_array = np.reshape(xyz_new, (order*order*order, 3))
xyz_global_array = np.reshape(xyz_global, (order*order*order, 3))
xyz_all = np.concatenate((xyz_new_array, xyz_global_array))


print volume
print volume2 * 2

