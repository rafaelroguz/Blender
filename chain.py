import bpy
import math
from math import pi

def run(origin):
    #Add a single chain link to the scene
    bpy.ops.mesh.primitive_torus_add(
        #major_radius = 1,
        #minor_radius = 0.25,
        major_segment = 12,
        minor_segment = 8,
        abso_major_rad = 1,
        abso_minor_rad = 0.6,
        location = (0, 0, 0),
        rotation = (0, 0, 0))        
        
    #Scale de torus along the x axis
    ob = bpy.context.object
    ob.scale = (0.7, 1, 1)
    bpy.ops.object.transform_apply(scale = True)
    
    #Create an empty
    bpy.ops.object.add(
        type = 'EMPTY',
        location = (0, 1.2, 0.2),
        rotation = (pi/2, pi/4, pi/2))
    empty = bpy.context.object
        
    #Make chain link active again
    scn = bpy.context.scene
    scn.objects.active = ob
    
    #Add modifier
    mod = ob.modifiers.new('Chain', 'ARRAY')
    mod.fit_type = 'FIXED_COUNT'
    mod.count = 10
    mod.use_relative_offset = 0
    mod.use_object_offset = True
    mod.offset_object = empty
    
    #Apply the modifier
    bpy.ops.object.visual_transform_apply()
    bpy.ops.object.modifier_apply(apply_as='DATA', modifier='Chain')
    
    #Move chain into place
    bpy.ops.transform.translate(value=origin)
    
    #Don't need empty anymore
    scn.objects.unlink(empty)
    del(empty)
    
    return

run(1)