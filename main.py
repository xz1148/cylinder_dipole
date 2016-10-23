import EMConst     # this file contains basic EM constants
import dipole as dp
import numpy as np
print '==========program start running=========='
freq = 300.0e6   # frequency, the float number
print 'The frequency is %7.2f MHz' % (freq / 1e6)
lambda0 = EMConst.c0 / freq # the wave length in free space
print 'The wave length in free space is %2.1f meters' % (lambda0)




# the position of the dipole
r_dipole = 1.0  #the locations of the dipole
theta_dipole = 0.0  # the cylindral coordinate of dipole
x_dipole = r_dipole * np.cos(theta_dipole) # the x coordiante of dipole
y_dipole = r_dipole * np.sin(theta_dipole) # the y coordinate of dipole
z_dipole = 0.0  # the z coordiante of the dipole

# length of the dipole
length_dipole = lambda0 / 2 # dipole antennas length is half wave length
dl_dipole = lambda0 / 10   # the maximum segment length of the dipole





# node_xyz is the coordinate in meters
# segment is a 2 * N tuple, the indexes of two nodes who connected together
node_xyz, segment, N_nodes, N_segments = dp.dipole( x_dipole,
                              y_dipole,
                              z_dipole,
                              length_dipole,
                              dl_dipole )

# first calculate the coordinate of segments center point
segment_center_xyz = (node_xyz[segment[:,0]] + node_xyz[segment[:,1]]) / 2.0


print "this is the result"
print segment_center_xyz
print node_xyz

