import EMConst
import dipole as dp
import numpy as np

r_dipole = 1.0  #the locations of the dipole
theta_dipole = 0  # the cylindral coordinate of dipole

x_dipole = r_dipole * np.cos(theta_dipole) # the x coordiante of dipole
y_dipole = r_dipole * np.sin(theta_dipole) # the y coordinate of dipole






x = 1
y = 1
z = 0
length = 1
dl = 0.1

xyz, segment = dp.dipole(x,y,z, length, dl)
print xyz
print segment

