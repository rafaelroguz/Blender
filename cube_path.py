import bpy
import math

#Crea un cubo sino existe, pero podría ser cualquier objeto
if not 'Cube' in bpy.data.objects:
    bpy.ops.mesh.primitive_cube_add()

frames_per_revolution = 120.0
step_size = 2*math.pi / frames_per_revolution

def set_object_location(n):
    x = math.sin(n) * 5
    y = math.cos(n) * 5
    z = 0.0
    ob = bpy.data.objects.get("Cube")
    ob.location = (x, y, z)

#Cada cambio de frame se llama esta función
def my_handler(scene):
    frame = scene.frame_current
    n = frame % frames_per_revolution

    if n == 0:
        set_object_location(n)
    else:
        set_object_location(n*step_size)

bpy.app.handlers.frame_change_pre.append(my_handler)