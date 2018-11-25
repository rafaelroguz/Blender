import bpy

#Define vertices y caras
verts = [(0,0,0), (0,5,0), (5,5,0), (5,0,0), (2.5, 2.5, 5)]
faces = [(0,1,2,3), (0,1,4), (1,2,4), (2,3,4), (3,0,4)]

#Define la malla y las variables del objeto
myMesh = bpy.data.meshes.new("Plane")
myObject = bpy.data.objects.new("Plane", myMesh)

#Establecer la locación y escena del objeto
myObject.location = bpy.context.scene.cursor_location
bpy.context.scene.objects.link(myObject)

#Crea la malla
myMesh.from_pydata(verts, [], faces)
myMesh.update(calc_edges=True)