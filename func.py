# common functions in the program
import numpy as np
import EMConst


def xs2xsm(xs, N_match):
    # this function will turn a (N_segments, 3) matrix into a (N_match, N_segmen
    # ts,
    # 3) matrix.
    # input:
    # x: is a (N_segments, 3) matrix
    # N_match: is an integer
    N_segments = xs.shape[0]  # first check the number of N_segments
    xs_tile = np.tile(xs, (N_match, 1))
    xsm = np.reshape(xs_tile, (N_match, N_segments, 3))
    return xsm


def xo2xom(xo, N_segments):
    # this function will make a matrix of xo (N_match, 3) matrix into a (N_match
    # ,N_segment, 3) matrix
    N_match = xo.shape[0]  # first check the number of N_segments
    xo_tile = np.tile(xo, N_segments)
    xom = np.reshape(xo_tile, (N_match, N_segments, 3))
    return xom


def G_A(k, R):
    # this is the Green's function for A vector
    # input:
    # R: the matrix |r - r'|, r is the observation point, r' is the source point
    G = -EMConst.mu0 * (-1.0 / (4.0*np.pi*R)) * np.exp(-1j*k*R)
    return G


def G_Q(k, R):
    # the greens function calculates the contribution of chareges
    # input:
    # R: distance
    # k: wavenumber
    G = (-1/EMConst.eps0) * (1/(4*np.pi*R)) * (1j*k + 1/R) * np.exp(-1j*k*R)
    return G


def dI(node0_xyz, node1_xyz):
    # this function gives I*dl.
    # input:
    # node0_xyz: (N_segment, 3) scale vector, the xyz cartisian coordinate of no
    # de0
    # node1_xyz: (N_segment, 3) scale vector, the xyz cartisian coordinate of no
    # de1
    dI_x = node1_xyz[:, 0] - node0_xyz[:, 0]
    dI_y = node1_xyz[:, 1] - node0_xyz[:, 1]
    dI_z = node1_xyz[:, 2] - node0_xyz[:, 2]
    return dI_x, dI_y, dI_z


def R(field_xyz, source_xyz):
    # this function returns a matrix of |r-r'| value, where r is the field point
    # and
    # r' is the source point
    field_X, source_X = np.meshgrid(source_xyz[:, 0], field_xyz[:, 0])
    field_Y, source_Y = np.meshgrid(source_xyz[:, 1], field_xyz[:, 1])
    field_Z, source_Z = np.meshgrid(source_xyz[:, 2], field_xyz[:, 2])

    v_field_source_x = field_X - source_X
    v_field_source_y = field_Y - source_Y
    v_field_source_z = field_Z - source_Z
    R_source_to_field = np.sqrt(v_field_source_x ** 2 +
                                v_field_source_y ** 2 +
                                v_field_source_z ** 2)

    return R_source_to_field, v_field_source_x, v_field_source_y, \
        v_field_source_z
