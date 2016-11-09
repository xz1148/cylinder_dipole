radius = 1;
lc = 0.5;
Point(1) = {0,0,0,lc};                              
Point(2) = {radius,0,0,lc};                         
Point(3) = {-radius,0,0,lc};                        
Point(4) = {0,radius,0,lc};                         
Point(5) = {0,-radius,0,lc};                        
Point(6) = {0,0,radius,lc};                         
Point(7) = {0,0,-radius,lc};                        
                                                    
                                                    
// circle in xy-plane                               
Circle(8) = {2, 1, 4};                              
Circle(9) = {4, 1, 3};                              
Circle(10) = {3, 1, 5};                             
Circle(11) = {5, 1, 2};                             
                                                    
// circle in xz-plane                               
Circle(12) = {2, 1, 6};                             
Circle(13) = {6, 1, 3};                             
Circle(14) = {3, 1, 7};                             
Circle(15) = {7, 1, 2};                             
                                                    
// circle in yz-plane                               
Circle(16) = {4, 1, 6};                             
Circle(17) = {6, 1, 5};                             
Circle(18) = {5, 1, 7};                             
Circle(19) = {7, 1, 4};                             
                                                    
                                                    
Line Loop(20) = {8, 16, -12};                       
Line Loop(21) = {9, -13, -16};                      
Line Loop(22) = {10, -17, 13};                      
Line Loop(23) = {11, 12, 17};                       
                                                    
Line Loop(24) = {8, -19, 15};                       
Line Loop(25) = {9, 14, 19};                        
Line Loop(26) = {10, 18, -14};                      
Line Loop(27) = {11, -15, -18};                     
                                                    
Ruled Surface(28) = {20};                           
Ruled Surface(29) = {21};                           
Ruled Surface(30) = {22};                           
Ruled Surface(31) = {23};                           
Ruled Surface(32) = {24};                           
Ruled Surface(33) = {25};                           
Ruled Surface(34) = {26};                           
Ruled Surface(35) = {27};                           
                                                    
Surface Loop(36) = {28, 29, 30, 31, 32, 33, 34, 35};
Volume(37) = {36};