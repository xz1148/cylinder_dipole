
# this module generates the coordinate and the boundary conditions of a diple
# the dipole is vertically polarized, so the dipole is aligned along the
# direction of z-axis
# unit: in meters


import numpy as np

def dipole_meshing(x0, y0, z0, x1, y1, z1, n_seg):
# input:
# float x0, y0, z0
# x1, y1, z1: the coordinate of starting point and ending point of dipole
# int n_seg : number of segments

# returned value:
# xyz: the n * 3 matrix of coordinates

    # x, y, z are the coordiantes of points
    n_node = n_seg + 1 # the number of nodes is n + 1
    x = np.linspace(x0, x1, n_node)
    y = np.linspace(y0, y1, n_node)
    z = np.linspace(z0, z1, n_node)
    xyz = np.stack((x, y, z), axis=1)

    # index of segments
    idx_seg = np.arange(n_seg)
    idx_node = np.arange(n_node)
    idx_node0 = idx_node[0:-1]
    idx_node1 = idx_node[1:n_node]
    mesh = np.stack((idx_seg, idx_node0, idx_node1), axis=1)

    return xyz, mesh

if __name__=="__main__":
    a, b = dipole_meshing(0,0,0,3.0,2.0,1.0,6)
    print a
    print b


