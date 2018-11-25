import bpy
import math

bpy.data.objects['Sphere'].keyframe_insert(data_path='location', frame=1)

bpy.ops.transform.translate(value=(0, 0, 5))
bpy.data.objects['Sphere'].keyframe_insert(data_path='location', frame=50)

bpy.ops.transform.translate(value=(0, 0, -5))
bpy.data.objects['Sphere'].keyframe_insert(data_path='location', frame=100)