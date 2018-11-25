import bpy
import mathutils
import math

r = 10

for i in range (0, 9):
    for j in range (0, 9):
        
        x = sqrt(r-j^2)
        y = sqrt(r-i^2)
        z = 0
    
        bpy.ops.mesh.primitive_cube_add(location=(x, y, z))