radius = input('Please input the radius')
lc = input('Please input the characteristic length')
geo_file = open('sphere.geo', 'w')
radius_line = 'radius = ' + str(radius) + ';\n'
lc_line = 'lc = ' + str(lc) + ';\n'
length_content = radius_line + lc_line
mesh_content = '\
Point(1) = {0,0,0,lc};                              \n\
Point(2) = {radius,0,0,lc};                         \n\
Point(3) = {-radius,0,0,lc};                        \n\
Point(4) = {0,radius,0,lc};                         \n\
Point(5) = {0,-radius,0,lc};                        \n\
Point(6) = {0,0,radius,lc};                         \n\
Point(7) = {0,0,-radius,lc};                        \n\
                                                    \n\
                                                    \n\
// circle in xy-plane                               \n\
Circle(8) = {2, 1, 4};                              \n\
Circle(9) = {4, 1, 3};                              \n\
Circle(10) = {3, 1, 5};                             \n\
Circle(11) = {5, 1, 2};                             \n\
                                                    \n\
// circle in xz-plane                               \n\
Circle(12) = {2, 1, 6};                             \n\
Circle(13) = {6, 1, 3};                             \n\
Circle(14) = {3, 1, 7};                             \n\
Circle(15) = {7, 1, 2};                             \n\
                                                    \n\
// circle in yz-plane                               \n\
Circle(16) = {4, 1, 6};                             \n\
Circle(17) = {6, 1, 5};                             \n\
Circle(18) = {5, 1, 7};                             \n\
Circle(19) = {7, 1, 4};                             \n\
                                                    \n\
                                                    \n\
Line Loop(20) = {8, 16, -12};                       \n\
Line Loop(21) = {9, -13, -16};                      \n\
Line Loop(22) = {10, -17, 13};                      \n\
Line Loop(23) = {11, 12, 17};                       \n\
                                                    \n\
Line Loop(24) = {8, -19, 15};                       \n\
Line Loop(25) = {9, 14, 19};                        \n\
Line Loop(26) = {10, 18, -14};                      \n\
Line Loop(27) = {11, -15, -18};                     \n\
                                                    \n\
Ruled Surface(28) = {20};                           \n\
Ruled Surface(29) = {21};                           \n\
Ruled Surface(30) = {22};                           \n\
Ruled Surface(31) = {23};                           \n\
Ruled Surface(32) = {24};                           \n\
Ruled Surface(33) = {25};                           \n\
Ruled Surface(34) = {26};                           \n\
Ruled Surface(35) = {27};                           \n\
                                                    \n\
Surface Loop(36) = {28, 29, 30, 31, 32, 33, 34, 35};\n\
Volume(37) = {36};'
content = length_content + mesh_content
geo_file.write(content)
geo_file.close()
