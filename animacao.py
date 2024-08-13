import bpy

bpy.ops.wm.read_factory_settings(use_empty=True)

bpy.ops.mesh.primitive_plane_add(size=10, location=(0, 0, 0))
ground = bpy.context.object
ground.name = 'Ground'

bpy.ops.mesh.primitive_cube_add(size=0.5, location=(0, 0, 0.25))
body = bpy.context.object
body.name = 'DogBody'

def add_leg(x, y):
    bpy.ops.mesh.primitive_cylinder_add(radius=0.05, depth=0.5, location=(x, y, 0.25))
    leg = bpy.context.object
    leg.name = f'DogLeg_{x}_{y}'
    bpy.ops.object.shade_smooth()
    return leg

legs = [add_leg(x, y) for x in (-0.15, 0.15) for y in (-0.2, 0.2)]

bpy.ops.object.armature_add(enter_editmode=True, location=(0, 0, 0.25))
armature = bpy.context.object
armature.name = 'DogArmature'
bpy.ops.object.mode_set(mode='EDIT')


bpy.ops.armature.bone_primitive_add(name='Bone_Front_Left')
bpy.ops.armature.bone_primitive_add(name='Bone_Front_Right')
bpy.ops.armature.bone_primitive_add(name='Bone_Back_Left')
bpy.ops.armature.bone_primitive_add(name='Bone_Back_Right')

bones = armature.data.edit_bones
bones['Bone_Front_Left'].head = (0.15, -0.2, 0.25)
bones['Bone_Front_Left'].tail = (0.15, -0.2, 0)
bones['Bone_Front_Right'].head = (0.15, 0.2, 0.25)
bones['Bone_Front_Right'].tail = (0.15, 0.2, 0)
bones['Bone_Back_Left'].head = (-0.15, -0.2, 0.25)
bones['Bone_Back_Left'].tail = (-0.15, -0.2, 0)
bones['Bone_Back_Right'].head = (-0.15, 0.2, 0.25)
bones['Bone_Back_Right'].tail = (-0.15, 0.2, 0)

bpy.ops.object.mode_set(mode='OBJECT')

body.modifiers.new(type='ARMATURE', name='Armature')
body.modifiers['Armature'].object = armature

for leg in legs:
    leg.modifiers.new(type='ARMATURE', name='Armature')
    leg.modifiers['Armature'].object = armature

def create_running_animation():
    bpy.context.scene.frame_start = 1
    bpy.context.scene.frame_end = 40
    
    armature.animation_data_create()
    action = bpy.data.actions.new(name='RunAction')
    armature.animation_data.action = action

    fcurves = []
    bones = ['Bone_Front_Left', 'Bone_Front_Right', 'Bone_Back_Left', 'Bone_Back_Right']
    for bone in bones:
        data_path = f'pose.bones["{bone}"].rotation_quaternion'
        fcurve = action.fcurves.new(data_path=data_path, index=0)
        fcurves.append(fcurve)
    
    keyframes = [1, 10, 20, 30, 40]
    values = [1, 0, -1, 0, 1]
    
    for fcurve, value in zip(fcurves, values):
        for frame in keyframes:
            fcurve.keyframe_points.add(1)
            fcurve.keyframe_points[-1].co = (frame, value)
    
    for fcurve in fcurves:
        for keyframe in fcurve.keyframe_points:
            keyframe.interpolation = 'LINEAR'

create_running_animation()

bpy.ops.object.camera_add(location=(5, -5, 5), rotation=(1.1, 0, 0.9))
camera = bpy.context.object
bpy.context.scene.camera = camera

bpy.ops.object.light_add(type='SUN', location=(5, 5, 5))
light = bpy.context.object
light.data.energy = 5

bpy.ops.wm.save_as_mainfile(filepath='dog_running_animation.blend')
