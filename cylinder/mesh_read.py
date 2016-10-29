# this file reads tetrahedron from gmsh .msh file
import numpy as np
def mesh_read(file_name):
    # this function reads the tetrahedron data from a file
    print 'reading from file ' + file_name
    f = open(file_name, 'r')
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

def neighbor_read(file_name):
    print 'reading neighbor from file ' + file_name
    f = open(file_name, 'r')
    line_temp = np.empty(4, int)
    #read the first line
    line_temp_txt = f.readline()
    line_temp_split = line_temp_txt.split()
    neighbor = np.empty(4, int)
    for n in range(4):
        neighbor[n] = int(line_temp_split[n])
    line_temp_txt = f.readline()
    #read the following lines
    while line_temp_txt != '':
        line_temp_split = line_temp_txt.split()
        for n in range(4):
            line_temp[n] = int(line_temp_split[n])
        neighbor = np.vstack((neighbor, line_temp))
        line_temp_txt = f.readline()
    # this combination will give the tetrahedron pairs
    file_length = neighbor.shape[0]
    combination = [0,1,0,2,0,3,1,2,1,3,2,3]
    raw_tri_pair = neighbor[:, combination]
    tri_pair  = raw_tri_pair.reshape(6*file_length, 2)
    tri_pair_contains_empty_1 = tri_pair[:, 0] == -1
    tri_pair_contains_empty_2 = tri_pair[:, 1] == -1
    tri_pair_contains_empty = np.logical_or(
        tri_pair_contains_empty_1,
        tri_pair_contains_empty_2)
    tri_pair_empty_filtered = \
        tri_pair[np.logical_not(tri_pair_contains_empty), :]
    return tri_pair_empty_filtered

