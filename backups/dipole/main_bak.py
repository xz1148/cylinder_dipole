import EMConst     # this file contains basic EM constants
import numpy as np
import impedance
import matplotlib.pyplot as plt
freq = np.arange(300e6, 1000e6, 10e6)
n_freq = freq.shape[0]

# the position of the dipole
r_dipole = 1.0  #the locations of the dipole
theta_dipole = 0.0  # the cylindral coordinate of dipole
x_dipole = r_dipole * np.cos(theta_dipole) # the x coordiante of dipole
y_dipole = r_dipole * np.sin(theta_dipole) # the y coordinate of dipole
z_dipole = 0.0  # the z coordiante of the dipole

# length of the dipole
# the segment length of dipole is fixed
# the maximum segment length of the dipole, this number could be different from
# the real segment length
rho_dipole = 0.008   # the radius of the dipole

Z0 = np.zeros(n_freq, complex)
Z1 = np.zeros(n_freq, complex)

for x in range(n_freq):
    lambda0 = EMConst.c0 / freq[x] # the wave length in free space
    length_dipole = lambda0 / 2 * 0.95 # dipole antennas length is half wave length
    dl_dipole = lambda0 / 30
    Z0[x], Z1[x] = impedance.dipole_impedance_calculation(freq[x], length_dipole, rho_dipole, dl_dipole,
        x_dipole, y_dipole, z_dipole)
print freq.shape[0]

plt.plot(freq, np.real(Z0), freq, np.real(Z1))
plt.show()


