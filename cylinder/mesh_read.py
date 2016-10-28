# this file reads tetrahedron from gmsh .msh file
import numpy as np
def mesh_read(file_name):
    # this function reads the tetrahedron data from a file
    print 'reading from file ' + file_name
    f = open('sphere.msh', 'r')
    for n in range(4):
        f.readline()
    N_nodes = int(f.readline()) # reads the number of nodes

    idx_nodes = np.empty(N_nodes, int)
    xyz_nodes = np.empty((N_nodes, 3), float)

    for n in range(N_nodes):
        line_read_tmp = f.readline()
        line_read_split = line_read_tmp.split()
        idx_nodes[n] = int(line_read_split[0])
        xyz_nodes[n][0] = float(line_read_split[1])
        xyz_nodes[n][1] = float(line_read_split[2])
        xyz_nodes[n][2] = float(line_read_split[3])

    for n in range(2):
        f.readline() # skip another two lines

    N_elements = int(f.readline()) # reads the number of elements

    first_tetra = True
    tetra_nodes_temp = np.empty(4, int)
    tetra_nodes = np.empty(4, int)
    for n in range(N_elements):
        line_read_tmp = f.readline()
        line_read_split = line_read_tmp.split()
        if line_read_split[1] == '4':
            tetra_nodes_temp[0] = int(line_read_split[5])
            tetra_nodes_temp[1] = int(line_read_split[6])
            tetra_nodes_temp[2] = int(line_read_split[7])
            tetra_nodes_temp[3] = int(line_read_split[8])
            if first_tetra == True:
                for m in range(4):
                    tetra_nodes[m] = tetra_nodes_temp[m]
                first_tetra = False
            else:
                tetra_nodes = np.vstack((tetra_nodes, tetra_nodes_temp))
    return idx_nodes, xyz_nodes, tetra_nodes
