Point(1) = {0, 0, 0, 0.2};
Point(2) = {1, 0, 0, 0.2};
Point(3) = {0, 1, 0, 0.2};
Point(4) = {0, 0, 1, 0.2};


Line(5) = {1, 2};
Line(6) = {1, 3};
Line(7) = {1, 4};
Line(8) = {2, 3};
Line(9) = {3, 4};
Line(10) = {4, 2};

Line Loop(11) = {5, 8, -6};
Line Loop(12) = {6, 9, -7};
Line Loop(13) = {7, 10, -5};
Line Loop(14) = {-8, -9, -10};

Plane Surface(15) = {11};
Plane Surface(16) = {12};
Plane Surface(17) = {13};
Plane Surface(18) = {14};

Surface Loop(19) = {15, 16, 17, 18};
Volume(20) = {19};


