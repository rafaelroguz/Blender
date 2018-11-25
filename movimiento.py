import bpy

#bpy.data.objects["Cube"].data.vertices[0].co.x += 1.0

def func():
    print("Runnin...")
    import bpy
    bpy.data.objects["Cube"].location.x += 0.05

func()

def faces():
    for f in bpy.data.objects["Cube"].data.polygons:
        if (f.select):
            print(f.index)
            
faces()