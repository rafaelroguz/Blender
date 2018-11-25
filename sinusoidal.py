import bpy
import math

verts = []
faces = []
numX = 10
numY = 10
freq = 1
amp = 1
scale = 1

for i in range (0, numX):
    for j in range (0, numY):
        x = scale * i
        y = scale * j
        z = scale * ( (amp * math.cos(i * freq)) + (amp * math.sin(j * freq)) ) 
        vert = (x, y ,z)
        verts.append(vert)

for i in range (0, numX - 1):
    for j in range (0, numY - 1):
        poly = ( (10*i)+j, (10*i)+j+1, (10*i)+10+j+1, (10*i)+10+j )
        faces.append(poly)

myMesh = bpy.data.meshes.new("sinusoide")
myObject = bpy.data.objects.new("sinusoide", myMesh)
myObject.location = bpy.context.scene.cursor_location
bpy.context.scene.objects.link(myObject)

myMesh.from_pydata(verts, [], faces)
myMesh.update(calc_edges=True)