import necpp
import EMConst     # this file contains basic EM constants
import dipole as dp
import numpy as np
import matplotlib.pyplot as plt
import func

print '==========program start running==========\n'
freq = 300.0e6   # frequency, the float number
print 'The frequency is %7.2f MHz' % (freq / 1e6)
lambda0 = EMConst.c0 / freq # the wave length in free space
print 'The wave length in free space is %2.1f meters' % (lambda0)
omega = 2.0 * np.pi * freq # the angular frequency
k0 = np.sqrt(omega ** 2.0 * EMConst.eps0 * EMConst.mu0) # the wave number in free space



# the position of the dipole
r_dipole = 1.0  #the locations of the dipole
theta_dipole = 0.0  # the cylindral coordinate of dipole
x_dipole = r_dipole * np.cos(theta_dipole) # the x coordiante of dipole
y_dipole = r_dipole * np.sin(theta_dipole) # the y coordinate of dipole
z_dipole = 0.0  # the z coordiante of the dipole

# length of the dipole
length_dipole = lambda0 / 2 * 0.95 # dipole antennas length is half wave length
# the segment length of dipole is fixed
# the maximum segment length of the dipole, this number could be different from
# the real segment length
dl_dipole = lambda0 / 30
rho_dipole = 0.015   # the radius of the dipole




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

# the distance from node0 to match
R_match_node0, v_match_node0_x, v_match_node0_y, v_match_node0_z \
    = func.R(match_xyz, node0_xyz)
R_match_segment, _, _, _ = func.R(match_xyz, segment_xyz)
R_match_node1, v_match_node1_x, v_match_node1_y, v_match_node1_z \
    = func.R(match_xyz, node1_xyz)

# normalize all the vectors, u means unit vector
u_match_node0_x = v_match_node0_x / R_match_node0
u_match_node0_y = v_match_node0_y / R_match_node0
u_match_node0_z = v_match_node0_z / R_match_node0
u_match_node1_x = v_match_node1_x / R_match_node1
u_match_node1_y = v_match_node1_y / R_match_node1
u_match_node1_z = v_match_node1_z / R_match_node1


# the vector of I * dl
dI_x, dI_y, dI_z = func.dI(node0_xyz, node1_xyz)
G_A = func.G_A(k0, R_match_segment)

# the E field contributed by G_A
E_A_x = -1j * omega * dI_x * G_A
E_A_y = -1j * omega * dI_y * G_A
E_A_z = -1j * omega * dI_z * G_A

# the charges at node0 and node1, current flow from node0 to node1
Q0 = 1 / (-1j * omega)
Q1 = -1 / (-1j * omega)
G_Q0 = func.G_Q(k0, R_match_node0)
G_Q1 = func.G_Q(k0, R_match_node1)
E_phi_x = Q0*G_Q0*u_match_node0_x + Q1*G_Q1*u_match_node1_x
E_phi_y = Q0*G_Q0*u_match_node0_y + Q1*G_Q1*u_match_node1_y
E_phi_z = Q0*G_Q0*u_match_node0_z + Q1*G_Q1*u_match_node1_z

print node0_xyz
print node1_xyz
E_z = E_A_z - E_phi_z
# set up the Excitations
V_in =  np.zeros(N_match, float)
n_source = (N_match + 1)/2 - 1

V_in[n_source] = 1.0
I = np.linalg.solve(E_z, V_in)
Z_in =  1.0 * np.abs(dI_z[0]) / I[n_source]
Z_in_2 = func.dipole_impedance(freq / 1.0e6, length_dipole, N_match, n_source,
                               rho_dipole)
print Z_in
print Z_in_2
#plt.plot(segment_xyz[:,2], np.abs(I))
#plt.show()

