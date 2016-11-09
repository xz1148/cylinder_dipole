python sphere_mesh.py
gmsh -3 sphere.geo
gmsh sphere.msh
./result/find_neighbor sphere
python main.py
