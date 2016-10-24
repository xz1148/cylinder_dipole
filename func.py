# common functions in the program
import numpy as np

def xs2xsm (xs, N_match):
# this function will turn a (N_segments, 3) matrix into a (N_match, N_segments,
# 3) matrix.
# input:
# x: is a (N_segments, 3) matrix
# N_match: is an integer
    N_segments = xs.shape[0]  #first check the number of N_segments
    xs_tile = np.tile( xs, (N_match, 1) )
    xsm = np.reshape( xs_tile, (N_match, N_segments, 3) )
    return xsm


def xo2xom (xo, N_segments):
# this function will make a matrix of xo (N_match, 3) matrix into a (N_match,
# N_segment, 3) matrix
    N_match = xo.shape[0]  #first check the number of N_segments
    xo_tile = np.tile( xo, N_segments )
    xom = np.reshape( xo_tile, (N_match, N_segments, 3) )
    return xom


