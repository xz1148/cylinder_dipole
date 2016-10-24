import EMConst     # this file contains basic EM constants
import dipole as dp
import numpy as np
import func


print '==========program start running=========='
freq = 300.0e6   # frequency, the float number
print 'The frequency is %7.2f MHz' % (freq / 1e6)
lambda0 = EMConst.c0 / freq # the wave length in free space
print 'The wave length in free space is %2.1f meters' % (lambda0)
omega = 2.0 * np.pi * freq # the angular frequency
k0 = omega ** 2.0 * EMConst.eps0 * EMConst.mu0 # the wave number in free space



# the position of the dipole
r_dipole = 1.0  #the locations of the dipole
theta_dipole = 0.0  # the cylindral coordinate of dipole
x_dipole = r_dipole * np.cos(theta_dipole) # the x coordiante of dipole
y_dipole = r_dipole * np.sin(theta_dipole) # the y coordinate of dipole
z_dipole = 0.0  # the z coordiante of the dipole

# length of the dipole
length_dipole = lambda0 / 2 # dipole antennas length is half wave length
# the segment length of dipole is fixed
# the maximum segment length of the dipole, this number could be different from
# the real segment length
dl_dipole = lambda0 / 10
rho_dipole = 0.003   # the radius of the dipole




# node_xyz is the coordinate in meters
# segment is a 2 * N tuple, the indexes of two nodes who connected together
node_xyz, segment, N_nodes, N_segments = dp.dipole( x_dipole,
                              y_dipole,
                              z_dipole,
                              length_dipole,
                              dl_dipole )

# the cartisian coordinate of node1 and node2
node0_xyz = node_xyz[segment[:,0]]
node1_xyz = node_xyz[segment[:,1]]
segment_xyz = (node0_xyz + node1_xyz) / 2.0

# first calculate the coordinate of segments center point
# then give the y coordinate a little offset
# make the matching point located on the surface of dipole
match_xyz = (node0_xyz + node1_xyz) / 2.0
match_xyz[:, 1] += rho_dipole
N_match = match_xyz.shape[0]

# reshape the vector coordinate matrix
node0_xyz_m = func.xs2xsm(node0_xyz, N_match)
node1_xyz_m = func.xs2xsm(node1_xyz, N_match)
segment_xyz_m = func.xs2xsm(segment_xyz, N_match)
match_xyz_m = func.xo2xom(match_xyz, N_segments)

# the vector point from the center of segment to the matching points
v_seg_to_match =  match_xyz_m - segment_xyz_m
# length of all the segments
r_seg_to_match = np.linalg.norm(v_seg_to_match, axis = 2)


# dI is actually I * dl
dI = node1_xyz_m - node0_xyz_m
G_A = -EMConst.mu0 * (-1.0 / (4.0 * np.pi)) * np.exp( 1j * k0 * r_seg_to_match )
G_A_reshape = np.reshape( np.repeat(G_A, 3, axis = 1), (N_match, N_segments, 3))
A =  dI * G_A_reshape


# the charges at node0 and node1
Q0 = 1 / (-1j * omega)
Q1 = -1 / (-1j * omega)
# vector point from the nodes to the matching points
v_node0_to_match = match_xyz_m - node0_xyz_m;
v_node1_to_match = match_xyz_m - node1_xyz_m;


# the distance from the nodes to the matching point, also the magnitude of all
# those vectors

r_node0_to_match = np.linalg.norm(v_node0_to_match, axis = 2)
r_node1_to_match = np.linalg.norm(v_node1_to_match, axis = 2)
r_node0_to_match_reshape = np.reshape( np.repeat( r_node0_to_match, 3, axis = 1), \
                                      (N_match, N_segments, 3))
r_node1_to_match_reshape = np.reshape( np.repeat( r_node1_to_match, 3, axis = 1), \
                                      (N_match, N_segments, 3))


# unit vector point form the nodes to the matching point
u_node0_to_match = v_node0_to_match / r_node0_to_match_reshape
u_node1_to_match = v_node1_to_match / r_node1_to_match_reshape



G_Q0 = (-1.0/EMConst.eps0) * (1.0/(4.0*np.pi)) * (1/r_node0_to_match) * \
    (1/r_node0_to_match + 1j * k0) * np.exp(-1j * k0 * r_node0_to_match)
G_Q1 = (-1.0/EMConst.eps0) * (1.0/(4.0*np.pi)) * (1/r_node1_to_match) * \
    (1/r_node1_to_match + 1j * k0) * np.exp(-1j * k0 * r_node1_to_match)
G_Q0_reshape = np.reshape( np.repeat(G_Q0, 3, axis = 1), (N_match, N_segments, 3))
G_Q1_reshape = np.reshape( np.repeat(G_Q1, 3, axis = 1), (N_match, N_segments, 3))


# E = -1j * omega * A - laplace * phi
E = -1j * omega * A - Q0 * u_node0_to_match * G_Q0_reshape - \
    Q1 * u_node0_to_match * G_Q1_reshape




print E
## "I" is the current filament frow from node0 to node1
#dI =  node1_xyz - node0_xyz
#v_seg_to_match = np.reshape(np.tile(match_xyz, N_segments), (N_segments, N_segments, 3)) \
#    - np.tile(segment_xyz, (N_segments, 1, 1))
#r_seg_to_match = np.linalg.norm(v_seg_to_match, axis = 2)
#
## this is a matrix of vectors (N_segments, N_segments, 3)
## A is vector magnetic potential
#A = -mu0 * G_A_reshape * dI
#
#
## charges at node one
#Q_node0 = 1.0 / (-1j * omega) * node0_xyz
## charges at node two
#Q_node1 = -1.0 / (-1j * omega) * node1_xyz
#
#
#print dI
#print G_A_reshape
#print G_A
#print G_A_reshape * dI
#
#
