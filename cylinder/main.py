import numpy as np
import mesh_read
from sys import getsizeof
# node_idx is a list of node index
# node_xyz the N * 3 matrix of coordinate
# tetra_node records the index of nodes that forms a tetrahedron
node_idx, node_xyz, tetra_node= mesh_read.mesh_read('sphere.msh')
N_node = np.max(node_idx)
tetra_node_sorted = np.sort(tetra_node)

def write_table_file(file_name, var):
    f = open(file_name, 'w')
    print 'Writing to file ' + file_name
    for line in var:
        for entry in line:
            f.write('{:<25} '.format(entry))  # left aligned
        f.write('\n')
    f.close()




node_file_name = 'sphere_nodes.txt'
element_file_name = 'sphere_elements.txt'
neighbor_file_name = 'cube_element_neighbors.txt'


write_table_file(node_file_name, node_xyz)
write_table_file(element_file_name, tetra_node)
neighbor = mesh_read.neighbor_read(neighbor_file_name)

print neighbor



