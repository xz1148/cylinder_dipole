import numpy as np
import mesh_read
from sys import getsizeof
# node_idx is a list of node index
# node_xyz the N * 3 matrix of coordinate
# tetra_node records the index of nodes that forms a tetrahedron
def listgen3d(x, y, z):
    print 'Generating a 3d list: %i, %i, %i' % (x, y, z)
    list = []
    for i in range(x):
        list.append([])
    for i in range(x):
        for j in range(y):
            list[i].append([])
    for i in range(x):
        for j in range(y):
            for k in range(z):
                list[i][j].append([])
    list_size = getsizeof(list)
    print 'the size of list is %i' % list_size
    return list

node_idx, node_xyz, tetra_node= mesh_read.mesh_read('sphere.msh')
N_node = np.max(node_idx)
tetra_node_sorted = np.sort(tetra_node)
list_gen = listgen3d(N_node,N_node-1,N_node-2)

list_gen[4][3][2].append(11)
list_gen[4][3][2].append(11)
list_gen[4][3][2].append(11)
list_gen[4][3][2].append(11)
list_gen[4][3][2].append(11)

print list_gen
print type(node_idx)
print type(node_xyz)
print type(tetra_node)





