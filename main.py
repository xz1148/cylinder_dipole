import EMConst     # this file contains basic EM constants
import dipole as dp
import numpy as np
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
rho_dipole = 0.001   # the radius of the dipole




# node_xyz is the coordinate in meters
# segment is a 2 * N tuple, the indexes of two nodes who connected together
node_xyz, segment, N_nodes, N_segments = dp.dipole( x_dipole,
                              y_dipole,
                              z_dipole,
                              length_dipole,
                              dl_dipole )

# first calculate the coordinate of segments center point
# then give the y coordinate a little offset
# make the matching point located on the surface of dipole
segment_xyz = (node_xyz[segment[:,0]] + node_xyz[segment[:,1]]) / 2.0
match_xyz = (node_xyz[segment[:,0]] + node_xyz[segment[:,1]]) / 2.0
match_xyz[:, 1] += rho_dipole

##dl_segment is the length of each segments
#dl_segment_square = ( node_xyz[segment[:,1]] - node_xyz[segment[:,0]] ) ** 2
#dl_segment = np.sqrt( np.sum(dl_segment_square, axis = 1) )
## dl_segment is now a 1D array of floats
#dl_segment = dl_segment * np.ones((3,1), float)

# "I" is the current filament frow from node0 to node1
dI =  node_xyz[segment[:,1]] - node_xyz[segment[:,0] ]
v_seg_to_match = np.reshape(np.tile(match_xyz, N_segments), (N_segments, N_segments, 3)) \
    - np.tile(segment_xyz, (N_segments, 1, 1))
r_seg_to_match = np.linalg.norm(v_seg_to_match, axis = 2)

print v_seg_to_match
print np.tile(segment_xyz, (N_segments, 1, 1))
print r_seg_to_match


#for x in match_xyz:
#    # this is the vector point from the segment center to the match point
#    v_seg_to_match = x - segment_xyz
#    r_seg_to_match = np.linalg.norm(v_seg_to_match, axis = 1)
#    print v_seg_to_match
#    print r_seg_to_match

