import numpy as np

def centroid(p1, p2, p3, p4):
    # input:
    # pn: float, n*3 size of array of cartisian coordinates
    pc = (p1+p2+p3+p4) / 4.0
    return pc


def ph(p1, p2, p3, pc):
    # the projection of pc to surface formed by p1, p2, p3
    M = np.matrix([[p1[0], p1[1], p1[2], 1],
                      [p2[0], p2[1], p2[2], 1],
                      [p3[0], p3[1], p3[2], 1]])
    print M
    a = np.linalg.det(M[:,[1,2,3]])
    b = -np.linalg.det(M[:,[0,2,3]])
    c = np.linalg.det(M[:,[0,1,3]])
    d = -np.linalg.det(M[:,[0,1,2]])


    print a, b, c, d
if __name__ == '__main__':
    p1 = np.array([[0,0,0],[0,0,0]])
    p2 = np.array([[1,0,0],[0.3,0,0]])
    p3 = np.array([[0,1,0],[0,0.3,0]])
    p4 = np.array([[0,0,1],[0,0,0.3]])
    pc =  centroid(p1, p2, p3, p4)
    print p1[0], p2[0], p3[0], pc[0]
    print ph(p1[0], p2[0], p3[0], pc[0])

