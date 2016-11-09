import vtk
import numpy as np
num_p = 20
points = vtk.vtkPoints()
p = np.random.rand(num_p,3)
vertices = vtk.vtkCellArray()

vertices.InsertNextCell(num_p)
for x in p:
    id = points.InsertNextPoint(x)
    vertices.InsertCellPoint(id)



point = vtk.vtkPolyData()
point.SetPoints(points)
point.SetVerts(vertices)
mapper = vtk.vtkPolyDataMapper()
if vtk.VTK_MAJOR_VERSION <=5:
    mapper.SetInput(point)
else:
    mapper.SetInputData(point)



actor = vtk.vtkActor()
actor.SetMapper(mapper)
actor.GetProperty().SetPointSize(20)



ren = vtk.vtkRenderer()
renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren)
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)
actor.GetProperty().SetColor(1,0,1)
ren.AddActor(actor)

iren.Initialize()
renWin.Render()
iren.Start()

