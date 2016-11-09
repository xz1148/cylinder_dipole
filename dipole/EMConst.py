# this file stores the EM constants that are common in daily use
import math

eps0 = 8.85418782e-12 # the permittivity in free space
mu0 = 1.25663706e-6 # the permeability in free space
c0 = 1/math.sqrt(eps0 * mu0)  # the speed of light in free space
eta0 = math.sqrt(eps0 / mu0)  # the characteristic impedance in free space
