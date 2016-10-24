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

# generating the grid matrix for calculating the value of r - r'
# r is the observation point
# r' is the source point

match_X, node0_X = np.meshgrid(node0_xyz[:,0], match_xyz[:,0])
match_Y, node0_Y = np.meshgrid(node0_xyz[:,1], match_xyz[:,1])
match_Z, node0_Z = np.meshgrid(node0_xyz[:,2], match_xyz[:,2])

# the distance from node0 to match
R_match_node0 = np.sqrt( (match_X - node0_X)**2 + (match_Y - node0_Y)**2 \
                        + (match_Z - node0_Z)**2 )

match_X, node0_X = np.meshgrid(match_xyz[:,0], node0_xyz[:,0])
match_Y, node0_Y = np.meshgrid(match_xyz[:,1], node0_xyz[:,1])
match_Z, node0_Z = np.meshgrid(match_xyz[:,2], node0_xyz[:,2])

print match_xyz
print segment_xyz
print match_Z
print R_match_node0
