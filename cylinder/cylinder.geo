radius = 0.1;
height = 0.2;

lc = 0.05;
// the bottom circle
Point(1) = {0, 0, 0, lc};
Point(2) = {radius, 0, 0, lc};
Point(3) = {-radius, 0, 0, lc};
// the top circle
Point(4) = {0, 0, height, lc};
Point(5) = {radius, 0, height, lc};
Point(6) = {-radius, 0, height, lc};


// the top circle and bottom circle
Circle(7) = {2, 1, 3};
Circle(8) = {3, 1, 2};

Circle(9) = {5, 4, 6};
Circle(10) = {6, 4, 5};


// the top circle and bottom circle
Line Loop(11) = {7, 8};
Line Loop(12) = {9, 10};

Line(13) = {5, 2};
Line(14) = {6, 3};

Line Loop(15) = {13, 7, -14, -9};
Line Loop(16) = {14, 8, -13, -10};


Plane Surface(17) = {11};
Plane Surface(18) = {12};
Ruled Surface(19) = {15};
Ruled Surface(20) = {16};

Surface Loop(21) = {17, 18, 19, 20};
Volume(22) = {21};



