
# this module generates the coordinate and the boundary conditions of a diple
# the dipole is vertically polarized, so the dipole is aligned along the
# direction of z-axis
# unit: in meters


import numpy as np

def dipole(x, y, z, length, dl):
# input:
# x, y, z: float, the coordinate of the central point of a dipole
# length: float, the total length of the dipole
# dl: the filament size of the dipole
# returned value:

# Nodes_xyz: the coordinate of all nodes, N_nodes * 3 array
# Segments:the tuple of node's indexes, which forms a segment, N_segments * 2
# array
# N_nodes: number of the nodes
# N_segments: number of the segments


    N_nodes = int(np.rint(length / dl)) # round the value, the number of nodes
    if N_nodes%2 == 0:       # if the number of nodes is even
        N_nodes += 1         # change it into a odd value
        print 'The number of segments is even number, changed to odd'
    N_segments = N_nodes - 1 # this is the number of segments

    Tip1_z = z + length / 2.0  # the z coordinate of one tip of dipole
    Tip2_z = z - length / 2.0  # the z coordinate of another tip of the dipole
    Nodes_z = np.linspace(Tip1_z, Tip2_z, N_nodes) # the nodes z coordinate

    xy = np.array([x,y])  # a single row of x, y
    Nodes_xy = np.tile(xy, (N_nodes, 1)); # now the xy coordinates is constructed N_nodes times

    # now concatenate the Nodes_xy and Nodes_z
    # Nodes_xyz is an array of xyz coordinates
    Nodes_xyz =  np.concatenate((Nodes_xy, np.reshape(Nodes_z,(N_nodes,1))), axis = 1)
    # Now define the segments

    Segments_node1 = np.reshape(np.arange(N_segments), (N_segments, 1)) # the index of the nodes of one end of segment
    Segments_node2 = np.reshape(np.arange(N_segments)+1, (N_segments, 1))  # the index of the nodes of one end of segment
    Segments = np.concatenate((Segments_node1, Segments_node2), axis = 1)
    return Nodes_xyz, Segments, N_nodes, N_segments




