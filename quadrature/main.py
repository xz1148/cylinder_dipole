import numpy as np

def centroid(p1, p2, p3, p4):
    # input:
    # pn: float, n*3 size of array of cartisian coordinates
    pc = (p1+p2+p3+p4) / 4.0
    return pc


def ph_single_facet(p1, p2, p3, pc):
    # the projection of pc to surface formed by p1, p2, p3
    # p1, p2, p3, pc are array of length 3
    # return
    # a length 3 array
    M = np.matrix([[p1[0], p1[1], p1[2], 1],
                      [p2[0], p2[1], p2[2], 1],
                      [p3[0], p3[1], p3[2], 1]])
    a = np.linalg.det(M[:,[1,2,3]])
    b = -np.linalg.det(M[:,[0,2,3]])
    c = np.linalg.det(M[:,[0,1,3]])
    d = -np.linalg.det(M[:,[0,1,2]])  # ax + by + cz + d = 0

    t = -(a*pc[0] + b*pc[1] + c*pc[2] + d) / \
        (a**2 + b**2 + c**2)
    p = np.zeros(3, float)
    p[0] = a*t + pc[0]
    p[1] = b*t + pc[1]
    p[2] = c*t + pc[2]
    return p

def ph(p1, p2, p3, p4, pc):
    # pn, n=1,2,3,4, pc are n*3 size array
    N_tri = p1.shape[0]
    ph1 = np.zeros((N_tri, 3), float)
    ph2 = np.zeros((N_tri, 3), float)
    ph3 = np.zeros((N_tri, 3), float)
    ph4 = np.zeros((N_tri, 3), float)
    for n in range(N_tri):
        ph1[n] = ph_single_facet(p2[n], p3[n], p4[n], pc[n])
        ph2[n] = ph_single_facet(p1[n], p3[n], p4[n], pc[n])
        ph3[n] = ph_single_facet(p1[n], p2[n], p4[n], pc[n])
        ph4[n] = ph_single_facet(p1[n], p2[n], p3[n], pc[n])
    return ph1, ph2, ph3, ph4

if __name__ == '__main__':
    p1 = np.array([[0,0,0],[0,0,0]])
    p2 = np.array([[1,0,0],[0.3,0,0]])
    p3 = np.array([[0,0.5,0],[0,0.3,0]])
    p4 = np.array([[0,0,1],[0,0,0.3]])
    pc =  centroid(p1, p2, p3, p4)

    ph1, ph2, ph3, ph4 = ph(p1, p2, p3, p4, pc)

    a = ph1-pc
    b = ph1-p2
    c = ph1-p3
    d = ph1-p4

    print ph1
    print np.dot(a[0], b[0])
    print np.dot(a[0], c[0])
    print np.dot(a[0], d[0])
