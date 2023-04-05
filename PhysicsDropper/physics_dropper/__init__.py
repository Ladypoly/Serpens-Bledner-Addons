# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
# This addon was created with the Serpens - Visual Scripting Addon.
# This code is generated from nodes and is not intended for manual editing.
# You can find out more about Serpens at <https://blendermarket.com/products/serpens>.


bl_info = {
    "name": "Physics Dropper",
    "description": "",
    "author": "Elin",
    "version": (1, 1, 3),
    "blender": (2, 93, 5),
    "location": "Tool",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "3D View"
}


###############   IMPORTS
import bpy
from bpy.utils import previews
import os
import math
from bpy.app.handlers import persistent
import random


###############   INITALIZE VARIABLES
physics_dropper = {
    "active": [], 
    "passive": [], 
    "dropped": False, 
    "wordsettings": [], 
    "meshselected": True, 
    "new_variable": "", 
    }
rigidbody = {
    "wordsettings": [], 
    "active": [], 
    "passive": None, 
    "tojoin": [], 
    "hightpoly": None, 
    "lowpoly": None, 
    "highpolylist": [], 
    "lowpolylist": [], 
    }
cloth = {
    "active": [], 
    "passive": None, 
    "tojoin": [], 
    }
earthquake = {
    "fmodifier": [], 
    }


###############   SERPENS FUNCTIONS
def exec_line(line):
    exec(line)

def sn_print(tree_name, *args):
    if tree_name in bpy.data.node_groups:
        item = bpy.data.node_groups[tree_name].sn_graphs[0].prints.add()
        for arg in args:
            item.value += str(arg) + ";;;"
        if bpy.context and bpy.context.screen:
            for area in bpy.context.screen.areas:
                area.tag_redraw()
    print(*args)

def sn_cast_string(value):
    return str(value)

def sn_cast_boolean(value):
    if type(value) == tuple:
        for data in value:
            if bool(data):
                return True
        return False
    return bool(value)

def sn_cast_float(value):
    if type(value) == str:
        try:
            value = float(value)
            return value
        except:
            return float(bool(value))
    elif type(value) == tuple:
        return float(value[0])
    elif type(value) == list:
        return float(len(value))
    elif not type(value) in [float, int, bool]:
        try:
            value = len(value)
            return float(value)
        except:
            return float(bool(value))
    return float(value)

def sn_cast_int(value):
    return int(sn_cast_float(value))

def sn_cast_boolean_vector(value, size):
    if type(value) in [str, bool, int, float]:
        return_value = []
        for i in range(size):
            return_value.append(bool(value))
        return tuple(return_value)
    elif type(value) == tuple:
        return_value = []
        for i in range(size):
            return_value.append(bool(value[i]) if len(value) > i else bool(value[0]))
        return tuple(return_value)
    elif type(value) == list:
        return sn_cast_boolean_vector(tuple(value), size)
    else:
        try:
            value = tuple(value)
            return sn_cast_boolean_vector(value, size)
        except:
            return sn_cast_boolean_vector(bool(value), size)

def sn_cast_float_vector(value, size):
    if type(value) in [str, bool, int, float]:
        return_value = []
        for i in range(size):
            return_value.append(sn_cast_float(value))
        return tuple(return_value)
    elif type(value) == tuple:
        return_value = []
        for i in range(size):
            return_value.append(sn_cast_float(value[i]) if len(value) > i else sn_cast_float(value[0]))
        return tuple(return_value)
    elif type(value) == list:
        return sn_cast_float_vector(tuple(value), size)
    else:
        try:
            value = tuple(value)
            return sn_cast_float_vector(value, size)
        except:
            return sn_cast_float_vector(sn_cast_float(value), size)

def sn_cast_int_vector(value, size):
    return tuple(map(int, sn_cast_float_vector(value, size)))

def sn_cast_color(value, use_alpha):
    length = 4 if use_alpha else 3
    value = sn_cast_float_vector(value, length)
    tuple_list = []
    for data in range(length):
        data = value[data] if len(value) > data else value[0]
        tuple_list.append(sn_cast_float(min(1, max(0, data))))
    return tuple(tuple_list)

def sn_cast_list(value):
    if type(value) in [str, tuple, list]:
        return list(value)
    elif type(value) in [int, float, bool]:
        return [value]
    else:
        try:
            value = list(value)
            return value
        except:
            return [value]

def sn_cast_blend_data(value):
    if hasattr(value, "bl_rna"):
        return value
    elif type(value) in [tuple, bool, int, float, list]:
        return None
    elif type(value) == str:
        try:
            value = eval(value)
            return value
        except:
            return None
    else:
        return None

def sn_cast_enum(string, enum_values):
    for item in enum_values:
        if item[1] == string:
            return item[0]
        elif item[0] == string.upper():
            return item[0]
    return string


###############   IMPERATIVE CODE
#######   Physics Dropper
def update_earthquake(self, context):
    function_return_BFB76 = updateearthquake()

def update_earthquakex(self, context):
    function_return_E33E4 = updateearthquake()

def update_earthquakey(self, context):
    function_return_55C4A = updateearthquake()

def update_earthquakez(self, context):
    function_return_75ADC = updateearthquake()


@persistent
def undo_pre_handler_7C101(dummy):
    pass

def checkmeshselected():
    try:
        physics_dropper["meshselected"] = False
        for_node_1B804 = 0
        for_node_index_1B804 = 0
        for for_node_index_1B804, for_node_1B804 in enumerate(bpy.context.selected_objects):
            physics_dropper["meshselected"] = for_node_1B804.type=="MESH"
        return physics_dropper["meshselected"], 
    except Exception as exc:
        print(str(exc) + " | Error in function CheckMeshSelected")
addon_keymaps = {}


#######   Rigidbody
def duplicate(name, display_as, ):
    try:
        rigidbody["tojoin"] = []
        for_node_FC74E = 0
        for_node_index_FC74E = 0
        for for_node_index_FC74E, for_node_FC74E in enumerate(bpy.context.selected_objects):
            run_function_on_F0B29 = for_node_FC74E.copy()
            run_function_on_CAC85 = bpy.context.scene.collection.objects.link(object=run_function_on_F0B29, )
            rigidbody["tojoin"].append(run_function_on_F0B29)
            bpy.context.view_layer.objects.active=run_function_on_F0B29
        bpy.ops.object.select_all('INVOKE_DEFAULT' if True else 'EXEC_DEFAULT',action=sn_cast_enum(r"DESELECT", [("TOGGLE","Toggle","Toggle selection for all elements"),("SELECT","Select","Select all elements"),("DESELECT","Deselect","Deselect all elements"),("INVERT","Invert","Invert selection of all elements"),]),)
        for_node_1AB22 = 0
        for_node_index_1AB22 = 0
        for for_node_index_1AB22, for_node_1AB22 in enumerate(rigidbody["tojoin"]):
            run_function_on_717DF = sn_cast_blend_data(for_node_1AB22).select_set(state=True, view_layer=None, )
            bpy.context.view_layer.objects.active=sn_cast_blend_data(for_node_1AB22)
            bpy.ops.object.make_single_user('INVOKE_DEFAULT' if False else 'EXEC_DEFAULT',type=sn_cast_enum(r"SELECTED_OBJECTS", [("SELECTED_OBJECTS","Selected Objects",""),("ALL","All",""),]),object=True,obdata=True,)
        bpy.ops.object.join('INVOKE_DEFAULT' if True else 'EXEC_DEFAULT',)
        bpy.ops.object.transform_apply('INVOKE_DEFAULT' if True else 'EXEC_DEFAULT',location=True,rotation=True,scale=True,properties=False,)
        bpy.context.active_object.display_type = display_as
        bpy.context.active_object.name=name
        bpy.context.active_object.parent_bone=r""
        if bpy.context.scene.p_optimizehighpoly:
            if bpy.context.scene.p_voxelsize == 0.0:
                pass
            else:
                run_function_on_41F95 = bpy.context.active_object.modifiers.new(name=r"Remesh", type=sn_cast_enum(r"REMESH", [("DATA_TRANSFER","Data Transfer","Transfer several types of data (vertex groups, UV maps, vertex colors, custom normals) from one mesh to another"),("MESH_CACHE","Mesh Cache","Deform the mesh using an external frame-by-frame vertex transform cache"),("MESH_SEQUENCE_CACHE","Mesh Sequence Cache","Deform the mesh or curve using an external mesh cache in Alembic format"),("NORMAL_EDIT","Normal Edit","Modify the direction of the surface normals"),("WEIGHTED_NORMAL","Weighted Normal","Modify the direction of the surface normals using a weighting method"),("UV_PROJECT","UV Project","Project the UV map coordinates from the negative Z axis of another object"),("UV_WARP","UV Warp","Transform the UV map using the difference between two objects"),("VERTEX_WEIGHT_EDIT","Vertex Weight Edit","Modify of the weights of a vertex group"),("VERTEX_WEIGHT_MIX","Vertex Weight Mix","Mix the weights of two vertex groups"),("VERTEX_WEIGHT_PROXIMITY","Vertex Weight Proximity","Set the vertex group weights based on the distance to another target object"),("ARRAY","Array","Create copies of the shape with offsets"),("BEVEL","Bevel","Generate sloped corners by adding geometry to the mesh's edges or vertices"),("BOOLEAN","Boolean","Use another shape to cut, combine or perform a difference operation"),("BUILD","Build","Cause the faces of the mesh object to appear or disappear one after the other over time"),("DECIMATE","Decimate","Reduce the geometry density"),("EDGE_SPLIT","Edge Split","Split away joined faces at the edges"),("NODES","Geometry Nodes",""),("MASK","Mask","Dynamically hide vertices based on a vertex group or armature"),("MIRROR","Mirror","Mirror along the local X, Y and/or Z axes, over the object origin"),("MESH_TO_VOLUME","Mesh to Volume",""),("MULTIRES","Multiresolution","Subdivide the mesh in a way that allows editing the higher subdivision levels"),("REMESH","Remesh","Generate new mesh topology based on the current shape"),("SCREW","Screw","Lathe around an axis, treating the input mesh as a profile"),("SKIN","Skin","Create a solid shape from vertices and edges, using the vertex radius to define the thickness"),("SOLIDIFY","Solidify","Make the surface thick"),("SUBSURF","Subdivision Surface","Split the faces into smaller parts, giving it a smoother appearance"),("TRIANGULATE","Triangulate","Convert all polygons to triangles"),("VOLUME_TO_MESH","Volume to Mesh",""),("WELD","Weld","Find groups of vertices closer than dist and merge them together"),("WIREFRAME","Wireframe","Convert faces into thickened edges"),("ARMATURE","Armature","Deform the shape using an armature object"),("CAST","Cast","Shift the shape towards a predefined primitive"),("CURVE","Curve","Bend the mesh using a curve object"),("DISPLACE","Displace","Offset vertices based on a texture"),("HOOK","Hook","Deform specific points using another object"),("LAPLACIANDEFORM","Laplacian Deform","Deform based a series of anchor points"),("LATTICE","Lattice","Deform using the shape of a lattice object"),("MESH_DEFORM","Mesh Deform","Deform using a different mesh, which acts as a deformation cage"),("SHRINKWRAP","Shrinkwrap","Project the shape onto another object"),("SIMPLE_DEFORM","Simple Deform","Deform the shape by twisting, bending, tapering or stretching"),("SMOOTH","Smooth","Smooth the mesh by flattening the angles between adjacent faces"),("CORRECTIVE_SMOOTH","Smooth Corrective","Smooth the mesh while still preserving the volume"),("LAPLACIANSMOOTH","Smooth Laplacian","Reduce the noise on a mesh surface with minimal changes to its shape"),("SURFACE_DEFORM","Surface Deform","Transfer motion from another mesh"),("WARP","Warp","Warp parts of a mesh to a new location in a very flexible way thanks to 2 specified objects"),("WAVE","Wave","Adds a ripple-like motion to an object's geometry"),("VOLUME_DISPLACE","Volume Displace","Deform volume based on noise or other vector fields"),("CLOTH","Cloth",""),("COLLISION","Collision",""),("DYNAMIC_PAINT","Dynamic Paint",""),("EXPLODE","Explode","Break apart the mesh faces and let them follow particles"),("FLUID","Fluid",""),("OCEAN","Ocean","Generate a moving ocean surface"),("PARTICLE_INSTANCE","Particle Instance",""),("PARTICLE_SYSTEM","Particle System","Spawn particles from the shape"),("SOFT_BODY","Soft Body",""),("SURFACE","Surface",""),]), )
                run_function_on_41F95.voxel_size = bpy.context.scene.p_voxelsize
            run_function_on_6C189 = bpy.context.active_object.modifiers.new(name=r"Decimate", type=sn_cast_enum(r"DECIMATE", [("DATA_TRANSFER","Data Transfer","Transfer several types of data (vertex groups, UV maps, vertex colors, custom normals) from one mesh to another"),("MESH_CACHE","Mesh Cache","Deform the mesh using an external frame-by-frame vertex transform cache"),("MESH_SEQUENCE_CACHE","Mesh Sequence Cache","Deform the mesh or curve using an external mesh cache in Alembic format"),("NORMAL_EDIT","Normal Edit","Modify the direction of the surface normals"),("WEIGHTED_NORMAL","Weighted Normal","Modify the direction of the surface normals using a weighting method"),("UV_PROJECT","UV Project","Project the UV map coordinates from the negative Z axis of another object"),("UV_WARP","UV Warp","Transform the UV map using the difference between two objects"),("VERTEX_WEIGHT_EDIT","Vertex Weight Edit","Modify of the weights of a vertex group"),("VERTEX_WEIGHT_MIX","Vertex Weight Mix","Mix the weights of two vertex groups"),("VERTEX_WEIGHT_PROXIMITY","Vertex Weight Proximity","Set the vertex group weights based on the distance to another target object"),("ARRAY","Array","Create copies of the shape with offsets"),("BEVEL","Bevel","Generate sloped corners by adding geometry to the mesh's edges or vertices"),("BOOLEAN","Boolean","Use another shape to cut, combine or perform a difference operation"),("BUILD","Build","Cause the faces of the mesh object to appear or disappear one after the other over time"),("DECIMATE","Decimate","Reduce the geometry density"),("EDGE_SPLIT","Edge Split","Split away joined faces at the edges"),("NODES","Geometry Nodes",""),("MASK","Mask","Dynamically hide vertices based on a vertex group or armature"),("MIRROR","Mirror","Mirror along the local X, Y and/or Z axes, over the object origin"),("MESH_TO_VOLUME","Mesh to Volume",""),("MULTIRES","Multiresolution","Subdivide the mesh in a way that allows editing the higher subdivision levels"),("REMESH","Remesh","Generate new mesh topology based on the current shape"),("SCREW","Screw","Lathe around an axis, treating the input mesh as a profile"),("SKIN","Skin","Create a solid shape from vertices and edges, using the vertex radius to define the thickness"),("SOLIDIFY","Solidify","Make the surface thick"),("SUBSURF","Subdivision Surface","Split the faces into smaller parts, giving it a smoother appearance"),("TRIANGULATE","Triangulate","Convert all polygons to triangles"),("VOLUME_TO_MESH","Volume to Mesh",""),("WELD","Weld","Find groups of vertices closer than dist and merge them together"),("WIREFRAME","Wireframe","Convert faces into thickened edges"),("ARMATURE","Armature","Deform the shape using an armature object"),("CAST","Cast","Shift the shape towards a predefined primitive"),("CURVE","Curve","Bend the mesh using a curve object"),("DISPLACE","Displace","Offset vertices based on a texture"),("HOOK","Hook","Deform specific points using another object"),("LAPLACIANDEFORM","Laplacian Deform","Deform based a series of anchor points"),("LATTICE","Lattice","Deform using the shape of a lattice object"),("MESH_DEFORM","Mesh Deform","Deform using a different mesh, which acts as a deformation cage"),("SHRINKWRAP","Shrinkwrap","Project the shape onto another object"),("SIMPLE_DEFORM","Simple Deform","Deform the shape by twisting, bending, tapering or stretching"),("SMOOTH","Smooth","Smooth the mesh by flattening the angles between adjacent faces"),("CORRECTIVE_SMOOTH","Smooth Corrective","Smooth the mesh while still preserving the volume"),("LAPLACIANSMOOTH","Smooth Laplacian","Reduce the noise on a mesh surface with minimal changes to its shape"),("SURFACE_DEFORM","Surface Deform","Transfer motion from another mesh"),("WARP","Warp","Warp parts of a mesh to a new location in a very flexible way thanks to 2 specified objects"),("WAVE","Wave","Adds a ripple-like motion to an object's geometry"),("VOLUME_DISPLACE","Volume Displace","Deform volume based on noise or other vector fields"),("CLOTH","Cloth",""),("COLLISION","Collision",""),("DYNAMIC_PAINT","Dynamic Paint",""),("EXPLODE","Explode","Break apart the mesh faces and let them follow particles"),("FLUID","Fluid",""),("OCEAN","Ocean","Generate a moving ocean surface"),("PARTICLE_INSTANCE","Particle Instance",""),("PARTICLE_SYSTEM","Particle System","Spawn particles from the shape"),("SOFT_BODY","Soft Body",""),("SURFACE","Surface",""),]), )
            run_function_on_6C189.ratio = sn_cast_float(bpy.context.scene.p_decimaterate)
            bpy.ops.object.convert('INVOKE_DEFAULT' if False else 'EXEC_DEFAULT',target=sn_cast_enum(r"MESH", [("CURVE","Curve","Curve from Mesh or Text objects"),("MESH","Mesh","Mesh from Curve, Surface, Metaball, or Text objects"),("GPENCIL","Grease Pencil","Grease Pencil from Curve or Mesh objects"),]),)
        else:
            pass
    except Exception as exc:
        print(str(exc) + " | Error in function Duplicate")

def setrigidpassiv():
    try:
        function_return_9D307 = set_worldsettings()
        bpy.ops.rigidbody.objects_add('INVOKE_DEFAULT' if True else 'EXEC_DEFAULT',type=sn_cast_enum(r"PASSIVE", [("ACTIVE","Active","Object is directly controlled by simulation results"),("PASSIVE","Passive","Object is directly controlled by animation system"),]),)
        rigidbody["passive"].rigid_body.collision_shape = bpy.context.scene.p_shape
        rigidbody["passive"].rigid_body.friction = sn_cast_float(bpy.context.scene.p_friction)
        rigidbody["passive"].rigid_body.restitution = sn_cast_float(bpy.context.scene.p_bunciness)
        rigidbody["passive"].rigid_body.use_margin = True
        rigidbody["passive"].rigid_body.collision_margin = bpy.context.scene.p_margin
        rigidbody["passive"].rigid_body.mass = bpy.context.scene.a_mass
        rigidbody["passive"].rigid_body.kinematic = True
        rigidbody["passive"].rigid_body.mesh_source = sn_cast_enum(r"FINAL", [("BASE","Base","Base mesh"),("DEFORM","Deform","Deformations (shape keys, deform modifiers)"),("FINAL","Final","All modifiers"),])
        function_return_38B56 = earthquakefunction(rigidbody["passive"], 0, 0, )
        function_return_C23DA = earthquakefunction(rigidbody["passive"], 1, 1, )
        function_return_A57AB = earthquakefunction(rigidbody["passive"], 2, 2, )
    except Exception as exc:
        print(str(exc) + " | Error in function SetRigidPassiv")

def sn_branch(v1,v2,condition):
    if condition:
        return v1
    return v2

def set_worldsettings():
    try:
        rigidbody["wordsettings"] = []
        rigidbody["wordsettings"].append(bpy.context.scene.rigidbody_world.point_cache.frame_start)
        rigidbody["wordsettings"].append(bpy.context.scene.rigidbody_world.point_cache.frame_end)
        rigidbody["wordsettings"].append(bpy.context.scene.rigidbody_world.substeps_per_frame)
        rigidbody["wordsettings"].append(bpy.context.scene.rigidbody_world.solver_iterations)
        rigidbody["wordsettings"].append(bpy.context.scene.rigidbody_world.enabled)
        rigidbody["wordsettings"].append(bpy.context.scene.rigidbody_world.use_split_impulse)
        rigidbody["wordsettings"].append(bpy.context.scene.frame_end)
        bpy.context.scene.rigidbody_world.substeps_per_frame=bpy.context.scene.w_subframes
        bpy.context.scene.rigidbody_world.solver_iterations=10
        bpy.context.scene.rigidbody_world.point_cache.frame_start=bpy.context.scene.w_startframe
        bpy.context.scene.rigidbody_world.point_cache.frame_end=bpy.context.scene.w_endframe
        bpy.context.scene.rigidbody_world.point_cache.frame_step=0
        bpy.context.scene.rigidbody_world.point_cache.index=0
        bpy.context.scene.rigidbody_world.enabled=True
        bpy.context.scene.rigidbody_world.use_split_impulse=bpy.context.scene.w_split_impulse
        bpy.context.scene.frame_current=1
        bpy.context.scene.frame_start=1
        bpy.context.scene.frame_end=bpy.context.scene.w_endframe
        bpy.context.scene.frame_step=1
        bpy.context.scene.frame_preview_start=0
        bpy.context.scene.frame_preview_end=0
        bpy.context.scene.vr_landmarks_selected=0
        bpy.context.scene.vr_landmarks_active=0
        bpy.context.scene.NWSourceSocket=0
        bpy.context.scene.measureit_font_size=14
        bpy.context.scene.measureit_gl_precision=2
        bpy.context.scene.measureit_scale_font=14
        bpy.context.scene.measureit_scale_pos_x=5
        bpy.context.scene.measureit_scale_pos_y=5
        bpy.context.scene.measureit_scale_precision=0
        bpy.context.scene.measureit_ovr_font=14
        bpy.context.scene.measureit_ovr_width=1
        bpy.context.scene.measureit_ovr_font_rotation=0
        bpy.context.scene.measureit_rf_border=10
        bpy.context.scene.measureit_rf_line=1
        bpy.context.scene.measureit_glarrow_s=15
        bpy.context.scene.measureit_debug_font=14
        bpy.context.scene.measureit_debug_width=2
        bpy.context.scene.measureit_debug_precision=1
        bpy.context.scene.measureit_font_rotation=0
        bpy.context.scene.sresolution=0
        bpy.context.scene.scsamples=0
        bpy.context.scene.margin=0
        bpy.context.scene.randomize_factor=100
        bpy.context.scene.fadein=25
        bpy.context.scene.fadeout=25
        bpy.context.scene.selectiterations=150
        bpy.context.scene.selectiterationsdone=0
        bpy.context.scene.w_endframe=250
        bpy.context.scene.w_subframes=10
        bpy.context.scene.w_solver_iterations=10
    except Exception as exc:
        print(str(exc) + " | Error in function Set_WorldSettings")

def revert_worldsettings():
    try:
        bpy.context.scene.rigidbody_world.substeps_per_frame=sn_cast_int(rigidbody["wordsettings"][2])
        bpy.context.scene.rigidbody_world.solver_iterations=sn_cast_int(rigidbody["wordsettings"][3])
        bpy.context.scene.rigidbody_world.point_cache.frame_start=sn_cast_int(rigidbody["wordsettings"][0])
        bpy.context.scene.rigidbody_world.point_cache.frame_end=sn_cast_int(rigidbody["wordsettings"][1])
        bpy.context.scene.rigidbody_world.point_cache.frame_step=0
        bpy.context.scene.rigidbody_world.point_cache.index=0
        bpy.context.scene.rigidbody_world.enabled=sn_cast_boolean(rigidbody["wordsettings"][4])
        bpy.context.scene.rigidbody_world.use_split_impulse=sn_cast_boolean(rigidbody["wordsettings"][5])
        bpy.context.scene.frame_current=1
        bpy.context.scene.frame_start=1
        bpy.context.scene.frame_end=sn_cast_int(rigidbody["wordsettings"][6])
        bpy.context.scene.frame_step=1
        bpy.context.scene.frame_preview_start=0
        bpy.context.scene.frame_preview_end=0
        bpy.context.scene.vr_landmarks_selected=0
        bpy.context.scene.vr_landmarks_active=0
        bpy.context.scene.NWSourceSocket=0
        bpy.context.scene.measureit_font_size=14
        bpy.context.scene.measureit_gl_precision=2
        bpy.context.scene.measureit_scale_font=14
        bpy.context.scene.measureit_scale_pos_x=5
        bpy.context.scene.measureit_scale_pos_y=5
        bpy.context.scene.measureit_scale_precision=0
        bpy.context.scene.measureit_ovr_font=14
        bpy.context.scene.measureit_ovr_width=1
        bpy.context.scene.measureit_ovr_font_rotation=0
        bpy.context.scene.measureit_rf_border=10
        bpy.context.scene.measureit_rf_line=1
        bpy.context.scene.measureit_glarrow_s=15
        bpy.context.scene.measureit_debug_font=14
        bpy.context.scene.measureit_debug_width=2
        bpy.context.scene.measureit_debug_precision=1
        bpy.context.scene.measureit_font_rotation=0
        bpy.context.scene.sresolution=0
        bpy.context.scene.scsamples=0
        bpy.context.scene.margin=0
        bpy.context.scene.randomize_factor=100
        bpy.context.scene.fadein=25
        bpy.context.scene.fadeout=25
        bpy.context.scene.selectiterations=150
        bpy.context.scene.selectiterationsdone=0
        bpy.context.scene.w_endframe=250
        bpy.context.scene.w_subframes=10
        bpy.context.scene.w_solver_iterations=10
    except Exception as exc:
        print(str(exc) + " | Error in function Revert_WorldSettings")

def sn_handle_script_line_exception(exc, line):
    print("# # # # # # # # SCRIPT LINE ERROR # # # # # # # #")
    print("Line:", line)
    raise exc

def setrigidactive():
    try:
        bpy.ops.object.select_all('INVOKE_DEFAULT' if True else 'EXEC_DEFAULT',action=sn_cast_enum(r"DESELECT", [("TOGGLE","Toggle","Toggle selection for all elements"),("SELECT","Select","Select all elements"),("DESELECT","Deselect","Deselect all elements"),("INVERT","Invert","Invert selection of all elements"),]),)
        for_node_F7067 = 0
        for_node_index_F7067 = 0
        for for_node_index_F7067, for_node_F7067 in enumerate(sn_cast_list(sn_branch(rigidbody["lowpolylist"],rigidbody["active"],bpy.context.scene.optimizehighpoly))):
            run_function_on_E05A1 = sn_cast_blend_data(for_node_F7067).select_set(state=True, view_layer=None, )
            bpy.context.view_layer.objects.active=sn_cast_blend_data(for_node_F7067)
        bpy.ops.object.origin_set('INVOKE_DEFAULT' if True else 'EXEC_DEFAULT',type=sn_cast_enum(r"ORIGIN_CENTER_OF_VOLUME", [("GEOMETRY_ORIGIN","Geometry to Origin","Move object geometry to object origin"),("ORIGIN_GEOMETRY","Origin to Geometry","Calculate the center of geometry based on the current pivot point (median, otherwise bounding box)"),("ORIGIN_CURSOR","Origin to 3D Cursor","Move object origin to position of the 3D cursor"),("ORIGIN_CENTER_OF_MASS","Origin to Center of Mass (Surface)","Calculate the center of mass from the surface area"),("ORIGIN_CENTER_OF_VOLUME","Origin to Center of Mass (Volume)","Calculate the center of mass from the volume (must be manifold geometry with consistent normals)"),]),center=sn_cast_enum(r"MEDIAN", [("MEDIAN","Median Center",""),("BOUNDS","Bounds Center",""),]),)
        bpy.ops.rigidbody.objects_add('INVOKE_DEFAULT' if True else 'EXEC_DEFAULT',type=sn_cast_enum(r"ACTIVE", [("ACTIVE","Active","Object is directly controlled by simulation results"),("PASSIVE","Passive","Object is directly controlled by animation system"),]),)
        for_node_D8E18 = 0
        for_node_index_D8E18 = 0
        for for_node_index_D8E18, for_node_D8E18 in enumerate(sn_cast_list(sn_branch(rigidbody["lowpolylist"],rigidbody["active"],bpy.context.scene.optimizehighpoly))):
            sn_cast_blend_data(for_node_D8E18).rigid_body.collision_shape = bpy.context.scene.a_shape
            sn_cast_blend_data(for_node_D8E18).rigid_body.friction = sn_cast_float(bpy.context.scene.a_friction)
            sn_cast_blend_data(for_node_D8E18).rigid_body.restitution = sn_cast_float(bpy.context.scene.a_bunciness)
            sn_cast_blend_data(for_node_D8E18).rigid_body.use_margin = True
            sn_cast_blend_data(for_node_D8E18).rigid_body.collision_margin = bpy.context.scene.a_margin
            sn_cast_blend_data(for_node_D8E18).rigid_body.linear_damping = sn_cast_float(bpy.context.scene.a_tra_damp)
            sn_cast_blend_data(for_node_D8E18).rigid_body.angular_damping = sn_cast_float(bpy.context.scene.a_rot_damp)
            sn_cast_blend_data(for_node_D8E18).rigid_body.mesh_source = sn_cast_enum(r"FINAL", [("BASE","Base","Base mesh"),("DEFORM","Deform","Deformations (shape keys, deform modifiers)"),("FINAL","Final","All modifiers"),])
        bpy.ops.screen.animation_play('INVOKE_DEFAULT' if True else 'EXEC_DEFAULT',reverse=False,sync=False,)
    except Exception as exc:
        print(str(exc) + " | Error in function SetRigidActive")

def applyduplicatelink():
    try:
        bpy.ops.object.select_all('INVOKE_DEFAULT' if True else 'EXEC_DEFAULT',action=sn_cast_enum(r"DESELECT", [("TOGGLE","Toggle","Toggle selection for all elements"),("SELECT","Select","Select all elements"),("DESELECT","Deselect","Deselect all elements"),("INVERT","Invert","Invert selection of all elements"),]),)
        for_node_E892A = 0
        for_node_index_E892A = 0
        for for_node_index_E892A, for_node_E892A in enumerate(rigidbody["highpolylist"]):
            sn_cast_blend_data(for_node_E892A).hide_viewport=False
            run_function_on_5AD08 = sn_cast_blend_data(for_node_E892A).select_set(state=True, view_layer=None, )
            bpy.context.view_layer.objects.active=sn_cast_blend_data(for_node_E892A)
            bpy.ops.object.parent_clear('INVOKE_DEFAULT' if True else 'EXEC_DEFAULT',type=sn_cast_enum(r"CLEAR_KEEP_TRANSFORM", [("CLEAR","Clear Parent","Completely clear the parenting relationship, including involved modifiers if any"),("CLEAR_KEEP_TRANSFORM","Clear and Keep Transformation","As 'Clear Parent', but keep the current visual transformations of the object"),("CLEAR_INVERSE","Clear Parent Inverse","Reset the transform corrections applied to the parenting relationship, does not remove parenting itself"),]),)
            bpy.ops.object.select_all('INVOKE_DEFAULT' if True else 'EXEC_DEFAULT',action=sn_cast_enum(r"DESELECT", [("TOGGLE","Toggle","Toggle selection for all elements"),("SELECT","Select","Select all elements"),("DESELECT","Deselect","Deselect all elements"),("INVERT","Invert","Invert selection of all elements"),]),)
        for_node_60BA6 = 0
        for_node_index_60BA6 = 0
        for for_node_index_60BA6, for_node_60BA6 in enumerate(rigidbody["lowpolylist"]):
            run_function_on_A5B05 = sn_cast_blend_data(for_node_60BA6).select_set(state=True, view_layer=None, )
        bpy.ops.object.delete('INVOKE_DEFAULT' if True else 'EXEC_DEFAULT',use_global=True,confirm=False,)
        rigidbody["highpolylist"] = []
        rigidbody["lowpolylist"] = []
    except Exception as exc:
        print(str(exc) + " | Error in function ApplyDuplicateLink")

def duplicatelink():
    try:
        for_node_92E19 = 0
        for_node_index_92E19 = 0
        for for_node_index_92E19, for_node_92E19 in enumerate(rigidbody["active"]):
            bpy.ops.object.select_all('INVOKE_DEFAULT' if True else 'EXEC_DEFAULT',action=sn_cast_enum(r"DESELECT", [("TOGGLE","Toggle","Toggle selection for all elements"),("SELECT","Select","Select all elements"),("DESELECT","Deselect","Deselect all elements"),("INVERT","Invert","Invert selection of all elements"),]),)
            rigidbody["highpolylist"].append(for_node_92E19)
            rigidbody["hightpoly"] = sn_cast_blend_data(for_node_92E19)
            run_function_on_C603C = sn_cast_blend_data(for_node_92E19).copy()
            rigidbody["lowpolylist"].append(run_function_on_C603C)
            rigidbody["lowpoly"] = run_function_on_C603C
            run_function_on_E57A2 = bpy.context.scene.collection.objects.link(object=run_function_on_C603C, )
            rigidbody["lowpoly"].name=(rigidbody["hightpoly"].name + r"_PhysProxy")
            rigidbody["lowpoly"].parent_bone=r""
            run_function_on_B6D76 = rigidbody["hightpoly"].select_set(state=True, view_layer=None, )
            run_function_on_328BC = rigidbody["lowpoly"].select_set(state=True, view_layer=None, )
            bpy.context.view_layer.objects.active=rigidbody["lowpoly"]
            bpy.ops.object.make_single_user('INVOKE_DEFAULT' if False else 'EXEC_DEFAULT',type=sn_cast_enum(r"SELECTED_OBJECTS", [("SELECTED_OBJECTS","Selected Objects",""),("ALL","All",""),]),object=True,obdata=True,)
            bpy.ops.object.parent_set('INVOKE_DEFAULT' if True else 'EXEC_DEFAULT',type=sn_cast_enum(r"OBJECT", [("OBJECT","Object",""),("ARMATURE","Armature Deform",""),("ARMATURE_NAME","   With Empty Groups",""),("ARMATURE_AUTO","   With Automatic Weights",""),("ARMATURE_ENVELOPE","   With Envelope Weights",""),("BONE","Bone",""),("BONE_RELATIVE","Bone Relative",""),("CURVE","Curve Deform",""),("FOLLOW","Follow Path",""),("PATH_CONST","Path Constraint",""),("LATTICE","Lattice Deform",""),("VERTEX","Vertex",""),("VERTEX_TRI","Vertex (Triangle)",""),]),xmirror=False,keep_transform=True,)
            rigidbody["hightpoly"].hide_viewport=True
            bpy.ops.object.select_all('INVOKE_DEFAULT' if True else 'EXEC_DEFAULT',action=sn_cast_enum(r"DESELECT", [("TOGGLE","Toggle","Toggle selection for all elements"),("SELECT","Select","Select all elements"),("DESELECT","Deselect","Deselect all elements"),("INVERT","Invert","Invert selection of all elements"),]),)
            run_function_on_4D649 = rigidbody["lowpoly"].select_set(state=True, view_layer=None, )
            bpy.context.view_layer.objects.active=rigidbody["lowpoly"]
            if bpy.context.scene.a_voxelsize == 0.0:
                pass
            else:
                run_function_on_84908 = rigidbody["lowpoly"].modifiers.new(name=r"Remesh", type=sn_cast_enum(r"REMESH", [("DATA_TRANSFER","Data Transfer","Transfer several types of data (vertex groups, UV maps, vertex colors, custom normals) from one mesh to another"),("MESH_CACHE","Mesh Cache","Deform the mesh using an external frame-by-frame vertex transform cache"),("MESH_SEQUENCE_CACHE","Mesh Sequence Cache","Deform the mesh or curve using an external mesh cache in Alembic format"),("NORMAL_EDIT","Normal Edit","Modify the direction of the surface normals"),("WEIGHTED_NORMAL","Weighted Normal","Modify the direction of the surface normals using a weighting method"),("UV_PROJECT","UV Project","Project the UV map coordinates from the negative Z axis of another object"),("UV_WARP","UV Warp","Transform the UV map using the difference between two objects"),("VERTEX_WEIGHT_EDIT","Vertex Weight Edit","Modify of the weights of a vertex group"),("VERTEX_WEIGHT_MIX","Vertex Weight Mix","Mix the weights of two vertex groups"),("VERTEX_WEIGHT_PROXIMITY","Vertex Weight Proximity","Set the vertex group weights based on the distance to another target object"),("ARRAY","Array","Create copies of the shape with offsets"),("BEVEL","Bevel","Generate sloped corners by adding geometry to the mesh's edges or vertices"),("BOOLEAN","Boolean","Use another shape to cut, combine or perform a difference operation"),("BUILD","Build","Cause the faces of the mesh object to appear or disappear one after the other over time"),("DECIMATE","Decimate","Reduce the geometry density"),("EDGE_SPLIT","Edge Split","Split away joined faces at the edges"),("NODES","Geometry Nodes",""),("MASK","Mask","Dynamically hide vertices based on a vertex group or armature"),("MIRROR","Mirror","Mirror along the local X, Y and/or Z axes, over the object origin"),("MESH_TO_VOLUME","Mesh to Volume",""),("MULTIRES","Multiresolution","Subdivide the mesh in a way that allows editing the higher subdivision levels"),("REMESH","Remesh","Generate new mesh topology based on the current shape"),("SCREW","Screw","Lathe around an axis, treating the input mesh as a profile"),("SKIN","Skin","Create a solid shape from vertices and edges, using the vertex radius to define the thickness"),("SOLIDIFY","Solidify","Make the surface thick"),("SUBSURF","Subdivision Surface","Split the faces into smaller parts, giving it a smoother appearance"),("TRIANGULATE","Triangulate","Convert all polygons to triangles"),("VOLUME_TO_MESH","Volume to Mesh",""),("WELD","Weld","Find groups of vertices closer than dist and merge them together"),("WIREFRAME","Wireframe","Convert faces into thickened edges"),("ARMATURE","Armature","Deform the shape using an armature object"),("CAST","Cast","Shift the shape towards a predefined primitive"),("CURVE","Curve","Bend the mesh using a curve object"),("DISPLACE","Displace","Offset vertices based on a texture"),("HOOK","Hook","Deform specific points using another object"),("LAPLACIANDEFORM","Laplacian Deform","Deform based a series of anchor points"),("LATTICE","Lattice","Deform using the shape of a lattice object"),("MESH_DEFORM","Mesh Deform","Deform using a different mesh, which acts as a deformation cage"),("SHRINKWRAP","Shrinkwrap","Project the shape onto another object"),("SIMPLE_DEFORM","Simple Deform","Deform the shape by twisting, bending, tapering or stretching"),("SMOOTH","Smooth","Smooth the mesh by flattening the angles between adjacent faces"),("CORRECTIVE_SMOOTH","Smooth Corrective","Smooth the mesh while still preserving the volume"),("LAPLACIANSMOOTH","Smooth Laplacian","Reduce the noise on a mesh surface with minimal changes to its shape"),("SURFACE_DEFORM","Surface Deform","Transfer motion from another mesh"),("WARP","Warp","Warp parts of a mesh to a new location in a very flexible way thanks to 2 specified objects"),("WAVE","Wave","Adds a ripple-like motion to an object's geometry"),("VOLUME_DISPLACE","Volume Displace","Deform volume based on noise or other vector fields"),("CLOTH","Cloth",""),("COLLISION","Collision",""),("DYNAMIC_PAINT","Dynamic Paint",""),("EXPLODE","Explode","Break apart the mesh faces and let them follow particles"),("FLUID","Fluid",""),("OCEAN","Ocean","Generate a moving ocean surface"),("PARTICLE_INSTANCE","Particle Instance",""),("PARTICLE_SYSTEM","Particle System","Spawn particles from the shape"),("SOFT_BODY","Soft Body",""),("SURFACE","Surface",""),]), )
                run_function_on_84908.voxel_size = bpy.context.scene.a_voxelsize
            run_function_on_111F0 = rigidbody["lowpoly"].modifiers.new(name=r"Decimate", type=sn_cast_enum(r"DECIMATE", [("DATA_TRANSFER","Data Transfer","Transfer several types of data (vertex groups, UV maps, vertex colors, custom normals) from one mesh to another"),("MESH_CACHE","Mesh Cache","Deform the mesh using an external frame-by-frame vertex transform cache"),("MESH_SEQUENCE_CACHE","Mesh Sequence Cache","Deform the mesh or curve using an external mesh cache in Alembic format"),("NORMAL_EDIT","Normal Edit","Modify the direction of the surface normals"),("WEIGHTED_NORMAL","Weighted Normal","Modify the direction of the surface normals using a weighting method"),("UV_PROJECT","UV Project","Project the UV map coordinates from the negative Z axis of another object"),("UV_WARP","UV Warp","Transform the UV map using the difference between two objects"),("VERTEX_WEIGHT_EDIT","Vertex Weight Edit","Modify of the weights of a vertex group"),("VERTEX_WEIGHT_MIX","Vertex Weight Mix","Mix the weights of two vertex groups"),("VERTEX_WEIGHT_PROXIMITY","Vertex Weight Proximity","Set the vertex group weights based on the distance to another target object"),("ARRAY","Array","Create copies of the shape with offsets"),("BEVEL","Bevel","Generate sloped corners by adding geometry to the mesh's edges or vertices"),("BOOLEAN","Boolean","Use another shape to cut, combine or perform a difference operation"),("BUILD","Build","Cause the faces of the mesh object to appear or disappear one after the other over time"),("DECIMATE","Decimate","Reduce the geometry density"),("EDGE_SPLIT","Edge Split","Split away joined faces at the edges"),("NODES","Geometry Nodes",""),("MASK","Mask","Dynamically hide vertices based on a vertex group or armature"),("MIRROR","Mirror","Mirror along the local X, Y and/or Z axes, over the object origin"),("MESH_TO_VOLUME","Mesh to Volume",""),("MULTIRES","Multiresolution","Subdivide the mesh in a way that allows editing the higher subdivision levels"),("REMESH","Remesh","Generate new mesh topology based on the current shape"),("SCREW","Screw","Lathe around an axis, treating the input mesh as a profile"),("SKIN","Skin","Create a solid shape from vertices and edges, using the vertex radius to define the thickness"),("SOLIDIFY","Solidify","Make the surface thick"),("SUBSURF","Subdivision Surface","Split the faces into smaller parts, giving it a smoother appearance"),("TRIANGULATE","Triangulate","Convert all polygons to triangles"),("VOLUME_TO_MESH","Volume to Mesh",""),("WELD","Weld","Find groups of vertices closer than dist and merge them together"),("WIREFRAME","Wireframe","Convert faces into thickened edges"),("ARMATURE","Armature","Deform the shape using an armature object"),("CAST","Cast","Shift the shape towards a predefined primitive"),("CURVE","Curve","Bend the mesh using a curve object"),("DISPLACE","Displace","Offset vertices based on a texture"),("HOOK","Hook","Deform specific points using another object"),("LAPLACIANDEFORM","Laplacian Deform","Deform based a series of anchor points"),("LATTICE","Lattice","Deform using the shape of a lattice object"),("MESH_DEFORM","Mesh Deform","Deform using a different mesh, which acts as a deformation cage"),("SHRINKWRAP","Shrinkwrap","Project the shape onto another object"),("SIMPLE_DEFORM","Simple Deform","Deform the shape by twisting, bending, tapering or stretching"),("SMOOTH","Smooth","Smooth the mesh by flattening the angles between adjacent faces"),("CORRECTIVE_SMOOTH","Smooth Corrective","Smooth the mesh while still preserving the volume"),("LAPLACIANSMOOTH","Smooth Laplacian","Reduce the noise on a mesh surface with minimal changes to its shape"),("SURFACE_DEFORM","Surface Deform","Transfer motion from another mesh"),("WARP","Warp","Warp parts of a mesh to a new location in a very flexible way thanks to 2 specified objects"),("WAVE","Wave","Adds a ripple-like motion to an object's geometry"),("VOLUME_DISPLACE","Volume Displace","Deform volume based on noise or other vector fields"),("CLOTH","Cloth",""),("COLLISION","Collision",""),("DYNAMIC_PAINT","Dynamic Paint",""),("EXPLODE","Explode","Break apart the mesh faces and let them follow particles"),("FLUID","Fluid",""),("OCEAN","Ocean","Generate a moving ocean surface"),("PARTICLE_INSTANCE","Particle Instance",""),("PARTICLE_SYSTEM","Particle System","Spawn particles from the shape"),("SOFT_BODY","Soft Body",""),("SURFACE","Surface",""),]), )
            run_function_on_111F0.ratio = sn_cast_float(bpy.context.scene.a_decimaterate)
        for_node_6D935 = 0
        for_node_index_6D935 = 0
        for for_node_index_6D935, for_node_6D935 in enumerate(rigidbody["lowpolylist"]):
            run_function_on_BC107 = sn_cast_blend_data(for_node_6D935).select_set(state=True, view_layer=None, )
        bpy.ops.object.convert('INVOKE_DEFAULT' if False else 'EXEC_DEFAULT',target=sn_cast_enum(r"MESH", [("CURVE","Curve","Curve from Mesh or Text objects"),("MESH","Mesh","Mesh from Curve, Surface, Metaball, or Text objects"),("GPENCIL","Grease Pencil","Grease Pencil from Curve or Mesh objects"),]),)
    except Exception as exc:
        print(str(exc) + " | Error in function DuplicateLink")

def applyrigid():
    try:
        bpy.context.scene.dropped = False
        if bpy.context.scene.optimizehighpoly:
            function_return_1BFA9 = applyduplicatelink()
        else:
            pass
        bpy.ops.object.select_all('INVOKE_DEFAULT' if True else 'EXEC_DEFAULT',action=sn_cast_enum(r"DESELECT", [("TOGGLE","Toggle","Toggle selection for all elements"),("SELECT","Select","Select all elements"),("DESELECT","Deselect","Deselect all elements"),("INVERT","Invert","Invert selection of all elements"),]),)
        for_node_24584 = 0
        for_node_index_24584 = 0
        for for_node_index_24584, for_node_24584 in enumerate(rigidbody["active"]):
            run_function_on_9E68B = sn_cast_blend_data(for_node_24584).select_set(state=True, view_layer=None, )
            bpy.context.view_layer.objects.active=sn_cast_blend_data(for_node_24584)
        bpy.ops.object.visual_transform_apply('INVOKE_DEFAULT' if True else 'EXEC_DEFAULT',)
        if bpy.context.scene.optimizehighpoly:
            pass
        else:
            bpy.ops.rigidbody.objects_remove('INVOKE_DEFAULT' if True else 'EXEC_DEFAULT',)
        bpy.ops.object.select_all('INVOKE_DEFAULT' if True else 'EXEC_DEFAULT',action=sn_cast_enum(r"DESELECT", [("TOGGLE","Toggle","Toggle selection for all elements"),("SELECT","Select","Select all elements"),("DESELECT","Deselect","Deselect all elements"),("INVERT","Invert","Invert selection of all elements"),]),)
        run_function_on_794C1 = rigidbody["passive"].select_set(state=True, view_layer=None, )
        bpy.context.view_layer.objects.active=rigidbody["passive"]
        bpy.ops.object.delete('INVOKE_DEFAULT' if True else 'EXEC_DEFAULT',use_global=True,confirm=False,)
        bpy.ops.object.select_all('INVOKE_DEFAULT' if True else 'EXEC_DEFAULT',action=sn_cast_enum(r"DESELECT", [("TOGGLE","Toggle","Toggle selection for all elements"),("SELECT","Select","Select all elements"),("DESELECT","Deselect","Deselect all elements"),("INVERT","Invert","Invert selection of all elements"),]),)
        rigidbody["passive"] = None
        for_node_32361 = 0
        for_node_index_32361 = 0
        for for_node_index_32361, for_node_32361 in enumerate(rigidbody["active"]):
            run_function_on_C2031 = sn_cast_blend_data(for_node_32361).select_set(state=True, view_layer=None, )
            bpy.context.view_layer.objects.active=sn_cast_blend_data(for_node_32361)
        rigidbody["active"] = []
        try: exec(r"bpy.context.scene.frame_current = 1")
        except Exception as exc: sn_handle_script_line_exception(exc, r"bpy.context.scene.frame_current = 1")
        function_return_E2131 = revert_worldsettings()
        print(r"DONE")
    except Exception as exc:
        print(str(exc) + " | Error in function ApplyRigid")

def sn_000_versiontest():
    try:
        pass # GetVersion Script Start
        import bpy
        #VersionString = bpy.app.version_string
        #CompactVersionString = VersionString.replace(".", "")
        #bpy.context.scene.versionnumber = int(CompactVersionString)
        #print(bpy.context.scene.versionnumber)
        if (2, 93, 0) > bpy.app.version:
            below293 = True
        else:
            below293 = False
        print(below293)
        #bpy.context.scene.Bool_Below293 = below293
        pass # GetVersion Script End
    except Exception as exc:
        print(str(exc) + " | Error in function 000_VersionTest")

def droprigid():
    try:
        rigidbody["active"] = []
        rigidbody["passive"] = None
        rigidbody["tojoin"] = []
        rigidbody["hightpoly"] = None
        rigidbody["lowpoly"] = None
        rigidbody["highpolylist"] = []
        bpy.context.scene.dropped = True
        for_node_4E5C1 = 0
        for_node_index_4E5C1 = 0
        for for_node_index_4E5C1, for_node_4E5C1 in enumerate(bpy.context.selected_objects):
            if for_node_4E5C1.type=="MESH":
                rigidbody["active"].append(for_node_4E5C1)
                bpy.context.view_layer.objects.active=for_node_4E5C1
            else:
                pass
        bpy.ops.object.select_all('INVOKE_DEFAULT' if True else 'EXEC_DEFAULT',action=sn_cast_enum(r"INVERT", [("TOGGLE","Toggle","Toggle selection for all elements"),("SELECT","Select","Select all elements"),("DESELECT","Deselect","Deselect all elements"),("INVERT","Invert","Invert selection of all elements"),]),)
        for_node_0D36D = 0
        for_node_index_0D36D = 0
        for for_node_index_0D36D, for_node_0D36D in enumerate(bpy.context.selected_objects):
            if for_node_0D36D.type=="MESH":
                bpy.context.view_layer.objects.active=None
            else:
                run_function_on_BF62E = for_node_0D36D.select_set(state=False, view_layer=None, )
        rigidbody["passive"] = None
        function_return_2E2A7 = duplicate(r"COLLIDER", sn_cast_enum(r"WIRE", [("BOUNDS","Bounds","Display the bounds of the object"),("WIRE","Wire","Display the object as a wireframe"),("SOLID","Solid","Display the object as a solid (if solid drawing is enabled in the viewport)"),("TEXTURED","Textured","Display the object with textures (if textures are enabled in the viewport)"),]), )
        rigidbody["passive"] = bpy.context.active_object
        function_return_9C12B = setrigidpassiv()
        if bpy.context.scene.optimizehighpoly:
            function_return_12D63 = duplicatelink()
            function_return_4F334 = setrigidactive()
        else:
            function_return_F618A = setrigidactive()
    except Exception as exc:
        print(str(exc) + " | Error in function DropRigid")


#######   Cloth
def setclothparameter(ca_qualitysteps, ca_mass, ca_air_viscosity, ca_stiff_tension, ca_stiff_compression, ca_stiff_shear, ca_stiff_bending, ca_damp_tension, ca_damp_compression, ca_damp_shear, ca_damp_bending, ca_internalsprings, ca_internalspringmaxlength, ca_internalspringmaxdevision, ca_internalspringtension, ca_internalspringcompression, ca_internalspringmaxtension, ca_internalspringmaxcompression, ca_usepressure, ca_pressure, ca_pressurescale, ca_pressurefluiddensity, ca_quality, ca_minimumdistance, ca_impulseclamping, ca_selfcollision, ca_selfcollisionfriction, ca_selfcollisiondistance, ca_selfcollisionimpulseclamping, ):
    try:
        bpy.context.scene.ca_qualitysteps = ca_qualitysteps
        bpy.context.scene.ca_mass = ca_mass
        bpy.context.scene.ca_air_viscosity = ca_air_viscosity
        bpy.context.scene.ca_stiff_tension = ca_stiff_tension
        bpy.context.scene.ca_stiff_compression = ca_stiff_compression
        bpy.context.scene.ca_stiff_shear = ca_stiff_shear
        bpy.context.scene.ca_stiff_bending = ca_stiff_bending
        bpy.context.scene.ca_damp_tension = ca_damp_tension
        bpy.context.scene.ca_damp_compression = ca_damp_compression
        bpy.context.scene.ca_damp_shear = ca_damp_shear
        bpy.context.scene.ca_damp_bending = ca_damp_bending
        bpy.context.scene.ca_internalsprings = ca_internalsprings
        bpy.context.scene.ca_internalspringmaxlength = ca_internalspringmaxlength
        bpy.context.scene.ca_internalspringmaxdevision = ca_internalspringmaxdevision
        bpy.context.scene.ca_internalspringtension = ca_internalspringtension
        bpy.context.scene.ca_internalspringcompression = ca_internalspringcompression
        bpy.context.scene.ca_internalspringmaxtension = ca_internalspringmaxtension
        bpy.context.scene.ca_internalspringmaxcompression = ca_internalspringmaxcompression
        bpy.context.scene.ca_usepressure = ca_usepressure
        bpy.context.scene.ca_pressure = ca_pressure
        bpy.context.scene.ca_pressurescale = ca_pressurescale
        bpy.context.scene.ca_pressurefluiddensity = ca_pressurefluiddensity
        bpy.context.scene.ca_quality = ca_quality
        bpy.context.scene.ca_minimumdistance = ca_minimumdistance
        bpy.context.scene.ca_impulseclamping = ca_impulseclamping
        bpy.context.scene.ca_selfcollision = ca_selfcollision
        bpy.context.scene.ca_selfcollisionfriction = ca_selfcollisionfriction
        bpy.context.scene.ca_selfcollisiondistance = ca_selfcollisiondistance
        bpy.context.scene.ca_selfcollisionimpulseclamping = ca_selfcollisionimpulseclamping
    except Exception as exc:
        print(str(exc) + " | Error in function SetClothParameter")

def setclothactive():
    try:
        bpy.ops.object.select_all('INVOKE_DEFAULT' if True else 'EXEC_DEFAULT',action=sn_cast_enum(r"DESELECT", [("TOGGLE","Toggle","Toggle selection for all elements"),("SELECT","Select","Select all elements"),("DESELECT","Deselect","Deselect all elements"),("INVERT","Invert","Invert selection of all elements"),]),)
        for_node_271E3 = 0
        for_node_index_271E3 = 0
        for for_node_index_271E3, for_node_271E3 in enumerate(cloth["active"]):
            run_function_on_FB76A = sn_cast_blend_data(for_node_271E3).select_set(state=True, view_layer=None, )
            bpy.context.view_layer.objects.active=sn_cast_blend_data(for_node_271E3)
            bpy.ops.object.modifier_add('INVOKE_DEFAULT' if True else 'EXEC_DEFAULT',type=sn_cast_enum(r"CLOTH", [("DATA_TRANSFER","Data Transfer","Transfer several types of data (vertex groups, UV maps, vertex colors, custom normals) from one mesh to another"),("MESH_CACHE","Mesh Cache","Deform the mesh using an external frame-by-frame vertex transform cache"),("MESH_SEQUENCE_CACHE","Mesh Sequence Cache","Deform the mesh or curve using an external mesh cache in Alembic format"),("NORMAL_EDIT","Normal Edit","Modify the direction of the surface normals"),("WEIGHTED_NORMAL","Weighted Normal","Modify the direction of the surface normals using a weighting method"),("UV_PROJECT","UV Project","Project the UV map coordinates from the negative Z axis of another object"),("UV_WARP","UV Warp","Transform the UV map using the difference between two objects"),("VERTEX_WEIGHT_EDIT","Vertex Weight Edit","Modify of the weights of a vertex group"),("VERTEX_WEIGHT_MIX","Vertex Weight Mix","Mix the weights of two vertex groups"),("VERTEX_WEIGHT_PROXIMITY","Vertex Weight Proximity","Set the vertex group weights based on the distance to another target object"),("ARRAY","Array","Create copies of the shape with offsets"),("BEVEL","Bevel","Generate sloped corners by adding geometry to the mesh's edges or vertices"),("BOOLEAN","Boolean","Use another shape to cut, combine or perform a difference operation"),("BUILD","Build","Cause the faces of the mesh object to appear or disappear one after the other over time"),("DECIMATE","Decimate","Reduce the geometry density"),("EDGE_SPLIT","Edge Split","Split away joined faces at the edges"),("NODES","Geometry Nodes",""),("MASK","Mask","Dynamically hide vertices based on a vertex group or armature"),("MIRROR","Mirror","Mirror along the local X, Y and/or Z axes, over the object origin"),("MESH_TO_VOLUME","Mesh to Volume",""),("MULTIRES","Multiresolution","Subdivide the mesh in a way that allows editing the higher subdivision levels"),("REMESH","Remesh","Generate new mesh topology based on the current shape"),("SCREW","Screw","Lathe around an axis, treating the input mesh as a profile"),("SKIN","Skin","Create a solid shape from vertices and edges, using the vertex radius to define the thickness"),("SOLIDIFY","Solidify","Make the surface thick"),("SUBSURF","Subdivision Surface","Split the faces into smaller parts, giving it a smoother appearance"),("TRIANGULATE","Triangulate","Convert all polygons to triangles"),("VOLUME_TO_MESH","Volume to Mesh",""),("WELD","Weld","Find groups of vertices closer than dist and merge them together"),("WIREFRAME","Wireframe","Convert faces into thickened edges"),("ARMATURE","Armature","Deform the shape using an armature object"),("CAST","Cast","Shift the shape towards a predefined primitive"),("CURVE","Curve","Bend the mesh using a curve object"),("DISPLACE","Displace","Offset vertices based on a texture"),("HOOK","Hook","Deform specific points using another object"),("LAPLACIANDEFORM","Laplacian Deform","Deform based a series of anchor points"),("LATTICE","Lattice","Deform using the shape of a lattice object"),("MESH_DEFORM","Mesh Deform","Deform using a different mesh, which acts as a deformation cage"),("SHRINKWRAP","Shrinkwrap","Project the shape onto another object"),("SIMPLE_DEFORM","Simple Deform","Deform the shape by twisting, bending, tapering or stretching"),("SMOOTH","Smooth","Smooth the mesh by flattening the angles between adjacent faces"),("CORRECTIVE_SMOOTH","Smooth Corrective","Smooth the mesh while still preserving the volume"),("LAPLACIANSMOOTH","Smooth Laplacian","Reduce the noise on a mesh surface with minimal changes to its shape"),("SURFACE_DEFORM","Surface Deform","Transfer motion from another mesh"),("WARP","Warp","Warp parts of a mesh to a new location in a very flexible way thanks to 2 specified objects"),("WAVE","Wave","Adds a ripple-like motion to an object's geometry"),("VOLUME_DISPLACE","Volume Displace","Deform volume based on noise or other vector fields"),("CLOTH","Cloth",""),("COLLISION","Collision",""),("DYNAMIC_PAINT","Dynamic Paint",""),("EXPLODE","Explode","Break apart the mesh faces and let them follow particles"),("FLUID","Fluid",""),("OCEAN","Ocean","Generate a moving ocean surface"),("PARTICLE_INSTANCE","Particle Instance",""),("PARTICLE_SYSTEM","Particle System","Spawn particles from the shape"),("SOFT_BODY","Soft Body",""),("SURFACE","Surface",""),]),)
            setattr(bpy.context.active_object.modifiers.active.point_cache,r"frame_end",bpy.context.scene.w_endframe)
            function_return_B641F = setclothsettings(bpy.context.active_object.modifiers.active, )
            function_return_6DE53 = addcollisionmodifier(sn_cast_blend_data(for_node_271E3), )
        bpy.ops.screen.animation_play('INVOKE_DEFAULT' if True else 'EXEC_DEFAULT',reverse=False,sync=False,)
    except Exception as exc:
        print(str(exc) + " | Error in function SetClothActive")

def applycloth():
    try:
        bpy.context.scene.dropped = False
        bpy.ops.object.select_all('INVOKE_DEFAULT' if True else 'EXEC_DEFAULT',action=sn_cast_enum(r"DESELECT", [("TOGGLE","Toggle","Toggle selection for all elements"),("SELECT","Select","Select all elements"),("DESELECT","Deselect","Deselect all elements"),("INVERT","Invert","Invert selection of all elements"),]),)
        for_node_2A292 = 0
        for_node_index_2A292 = 0
        for for_node_index_2A292, for_node_2A292 in enumerate(cloth["active"]):
            run_function_on_B832A = sn_cast_blend_data(for_node_2A292).select_set(state=True, view_layer=None, )
            bpy.context.view_layer.objects.active=sn_cast_blend_data(for_node_2A292)
        bpy.ops.object.convert('INVOKE_DEFAULT' if True else 'EXEC_DEFAULT',target=sn_cast_enum(r"MESH", [("CURVE","Curve","Curve from Mesh or Text objects"),("MESH","Mesh","Mesh from Curve, Surface, Metaball, or Text objects"),("GPENCIL","Grease Pencil","Grease Pencil from Curve or Mesh objects"),]),)
        bpy.ops.object.origin_set('INVOKE_DEFAULT' if True else 'EXEC_DEFAULT',type=sn_cast_enum(r"ORIGIN_GEOMETRY", [("GEOMETRY_ORIGIN","Geometry to Origin","Move object geometry to object origin"),("ORIGIN_GEOMETRY","Origin to Geometry","Calculate the center of geometry based on the current pivot point (median, otherwise bounding box)"),("ORIGIN_CURSOR","Origin to 3D Cursor","Move object origin to position of the 3D cursor"),("ORIGIN_CENTER_OF_MASS","Origin to Center of Mass (Surface)","Calculate the center of mass from the surface area"),("ORIGIN_CENTER_OF_VOLUME","Origin to Center of Mass (Volume)","Calculate the center of mass from the volume (must be manifold geometry with consistent normals)"),]),center=sn_cast_enum(r"MEDIAN", [("MEDIAN","Median Center",""),("BOUNDS","Bounds Center",""),]),)
        bpy.ops.object.select_all('INVOKE_DEFAULT' if True else 'EXEC_DEFAULT',action=sn_cast_enum(r"DESELECT", [("TOGGLE","Toggle","Toggle selection for all elements"),("SELECT","Select","Select all elements"),("DESELECT","Deselect","Deselect all elements"),("INVERT","Invert","Invert selection of all elements"),]),)
        run_function_on_F88BF = cloth["passive"].select_set(state=True, view_layer=None, )
        bpy.context.view_layer.objects.active=cloth["passive"]
        bpy.ops.object.delete('INVOKE_DEFAULT' if True else 'EXEC_DEFAULT',use_global=True,confirm=False,)
        bpy.ops.object.select_all('INVOKE_DEFAULT' if True else 'EXEC_DEFAULT',action=sn_cast_enum(r"DESELECT", [("TOGGLE","Toggle","Toggle selection for all elements"),("SELECT","Select","Select all elements"),("DESELECT","Deselect","Deselect all elements"),("INVERT","Invert","Invert selection of all elements"),]),)
        for_node_4DEAB = 0
        for_node_index_4DEAB = 0
        for for_node_index_4DEAB, for_node_4DEAB in enumerate(cloth["active"]):
            run_function_on_E90E5 = sn_cast_blend_data(for_node_4DEAB).select_set(state=True, view_layer=None, )
            bpy.context.view_layer.objects.active=sn_cast_blend_data(for_node_4DEAB)
        cloth["active"] = []
        try: exec(r"bpy.context.scene.frame_current = 1")
        except Exception as exc: sn_handle_script_line_exception(exc, r"bpy.context.scene.frame_current = 1")
        print(r"DONE")
    except Exception as exc:
        print(str(exc) + " | Error in function ApplyCloth")

def setclothpassiv():
    try:
        bpy.context.view_layer.objects.active=cloth["passive"]
        function_return_D974A = addcollisionmodifier(cloth["passive"], )
        function_return_05FFD = earthquakefunction(cloth["passive"], 0, 0, )
        function_return_9FDDD = earthquakefunction(cloth["passive"], 1, 1, )
        function_return_B329D = earthquakefunction(cloth["passive"], 2, 2, )
    except Exception as exc:
        print(str(exc) + " | Error in function SetClothPassiv")

def setclothsettings(cloth, ):
    try:
        cloth.settings.quality = bpy.context.scene.ca_qualitysteps
        cloth.settings.mass = bpy.context.scene.ca_mass
        cloth.settings.air_damping = bpy.context.scene.ca_air_viscosity
        cloth.settings.tension_stiffness = bpy.context.scene.ca_stiff_tension
        cloth.settings.compression_stiffness = bpy.context.scene.ca_stiff_compression
        cloth.settings.shear_stiffness = bpy.context.scene.ca_stiff_shear
        cloth.settings.bending_stiffness = bpy.context.scene.ca_stiff_bending
        cloth.settings.tension_damping = bpy.context.scene.ca_damp_tension
        cloth.settings.compression_damping = bpy.context.scene.ca_damp_compression
        cloth.settings.shear_damping = bpy.context.scene.ca_damp_shear
        cloth.settings.bending_damping = bpy.context.scene.ca_damp_bending
        cloth.settings.use_internal_springs = bpy.context.scene.ca_internalsprings
        cloth.settings.internal_spring_max_length = bpy.context.scene.ca_internalspringmaxlength
        cloth.settings.internal_spring_max_diversion = bpy.context.scene.ca_internalspringmaxdevision
        cloth.settings.internal_tension_stiffness = bpy.context.scene.ca_internalspringtension
        cloth.settings.internal_compression_stiffness = bpy.context.scene.ca_internalspringcompression
        cloth.settings.internal_tension_stiffness_max = bpy.context.scene.ca_internalspringmaxtension
        cloth.settings.internal_compression_stiffness_max = bpy.context.scene.ca_internalspringmaxcompression
        cloth.settings.use_pressure = bpy.context.scene.ca_usepressure
        cloth.settings.uniform_pressure_force = bpy.context.scene.ca_pressure
        cloth.settings.pressure_factor = bpy.context.scene.ca_pressurescale
        cloth.settings.fluid_density = bpy.context.scene.ca_pressurefluiddensity
        cloth.collision_settings.collision_quality = bpy.context.scene.ca_quality
        cloth.collision_settings.distance_min = bpy.context.scene.ca_minimumdistance
        cloth.collision_settings.impulse_clamp = bpy.context.scene.ca_impulseclamping
        cloth.collision_settings.use_self_collision = bpy.context.scene.ca_selfcollision
        cloth.collision_settings.self_friction = bpy.context.scene.ca_selfcollisionfriction
        cloth.collision_settings.self_distance_min = bpy.context.scene.ca_selfcollisiondistance
        cloth.collision_settings.self_impulse_clamp = bpy.context.scene.ca_selfcollisionimpulseclamping
        print(r"SetClothSettingsDONE")
    except Exception as exc:
        print(str(exc) + " | Error in function SetClothSettings")

def update_c_a_presets(self, context):
    if self.c_a_presets == r"Cotton":
        function_return_DEA36 = setclothparameter(5, 0.30000001192092896, 1.0, 15.0, 15.0, 15.0, 0.5, 5.0, 5.0, 5.0, 0.5, False, 0.0, 45.0, 15.0, 15.0, 15.0, 15.0, False, 0.0, 1.0, 0.0, 2, 0.014999999664723873, 0.0, True, 5.0, 0.014999999664723873, 0.0, )
    else:
        if self.c_a_presets == r"Denim":
            function_return_92C93 = setclothparameter(12, 1.0, 1.0, 40.0, 40.0, 40.0, 10.0, 25.0, 25.0, 25.0, 0.5, False, 0.0, 45.0, 15.0, 15.0, 15.0, 15.0, False, 0.0, 1.0, 0.0, 2, 0.014999999664723873, 0.0, True, 5.0, 0.014999999664723873, 0.0, )
        else:
            if self.c_a_presets == r"Leather":
                function_return_45C71 = setclothparameter(15, 0.4000000059604645, 1.0, 80.0, 80.0, 80.0, 150.0, 25.0, 25.0, 25.0, 0.5, False, 0.0, 45.0, 15.0, 15.0, 15.0, 15.0, False, 0.0, 1.0, 0.0, 2, 0.014999999664723873, 0.0, True, 5.0, 0.014999999664723873, 0.0, )
            else:
                if self.c_a_presets == r"Rubber":
                    function_return_3D308 = setclothparameter(7, 3.0, 1.0, 15.0, 15.0, 15.0, 25.0, 25.0, 25.0, 25.0, 0.5, False, 0.0, 45.0, 15.0, 15.0, 15.0, 15.0, False, 0.0, 1.0, 0.0, 2, 0.014999999664723873, 0.0, True, 5.0, 0.014999999664723873, 0.0, )
                else:
                    if self.c_a_presets == r"Silk":
                        function_return_708D0 = setclothparameter(5, 0.15000000596046448, 1.0, 5.0, 5.0, 5.0, 0.05000000074505806, 0.0, 0.0, 0.0, 0.5, False, 0.0, 45.0, 15.0, 15.0, 15.0, 15.0, False, 0.0, 1.0, 0.0, 2, 0.014999999664723873, 0.0, True, 5.0, 0.014999999664723873, 0.0, )
                    else:
                        pass
    if bpy.context.scene.dropped:
        for_node_96267 = 0
        for_node_index_96267 = 0
        for for_node_index_96267, for_node_96267 in enumerate(cloth["active"]):
            function_return_9266F = setclothsettings(sn_cast_blend_data(for_node_96267).modifiers.active, )
    else:
        pass

def addcollisionmodifier(object, ):
    try:
        bpy.ops.object.modifier_add('INVOKE_DEFAULT' if True else 'EXEC_DEFAULT',type=sn_cast_enum(r"COLLISION", [("DATA_TRANSFER","Data Transfer","Transfer several types of data (vertex groups, UV maps, vertex colors, custom normals) from one mesh to another"),("MESH_CACHE","Mesh Cache","Deform the mesh using an external frame-by-frame vertex transform cache"),("MESH_SEQUENCE_CACHE","Mesh Sequence Cache","Deform the mesh or curve using an external mesh cache in Alembic format"),("NORMAL_EDIT","Normal Edit","Modify the direction of the surface normals"),("WEIGHTED_NORMAL","Weighted Normal","Modify the direction of the surface normals using a weighting method"),("UV_PROJECT","UV Project","Project the UV map coordinates from the negative Z axis of another object"),("UV_WARP","UV Warp","Transform the UV map using the difference between two objects"),("VERTEX_WEIGHT_EDIT","Vertex Weight Edit","Modify of the weights of a vertex group"),("VERTEX_WEIGHT_MIX","Vertex Weight Mix","Mix the weights of two vertex groups"),("VERTEX_WEIGHT_PROXIMITY","Vertex Weight Proximity","Set the vertex group weights based on the distance to another target object"),("ARRAY","Array","Create copies of the shape with offsets"),("BEVEL","Bevel","Generate sloped corners by adding geometry to the mesh's edges or vertices"),("BOOLEAN","Boolean","Use another shape to cut, combine or perform a difference operation"),("BUILD","Build","Cause the faces of the mesh object to appear or disappear one after the other over time"),("DECIMATE","Decimate","Reduce the geometry density"),("EDGE_SPLIT","Edge Split","Split away joined faces at the edges"),("NODES","Geometry Nodes",""),("MASK","Mask","Dynamically hide vertices based on a vertex group or armature"),("MIRROR","Mirror","Mirror along the local X, Y and/or Z axes, over the object origin"),("MESH_TO_VOLUME","Mesh to Volume",""),("MULTIRES","Multiresolution","Subdivide the mesh in a way that allows editing the higher subdivision levels"),("REMESH","Remesh","Generate new mesh topology based on the current shape"),("SCREW","Screw","Lathe around an axis, treating the input mesh as a profile"),("SKIN","Skin","Create a solid shape from vertices and edges, using the vertex radius to define the thickness"),("SOLIDIFY","Solidify","Make the surface thick"),("SUBSURF","Subdivision Surface","Split the faces into smaller parts, giving it a smoother appearance"),("TRIANGULATE","Triangulate","Convert all polygons to triangles"),("VOLUME_TO_MESH","Volume to Mesh",""),("WELD","Weld","Find groups of vertices closer than dist and merge them together"),("WIREFRAME","Wireframe","Convert faces into thickened edges"),("ARMATURE","Armature","Deform the shape using an armature object"),("CAST","Cast","Shift the shape towards a predefined primitive"),("CURVE","Curve","Bend the mesh using a curve object"),("DISPLACE","Displace","Offset vertices based on a texture"),("HOOK","Hook","Deform specific points using another object"),("LAPLACIANDEFORM","Laplacian Deform","Deform based a series of anchor points"),("LATTICE","Lattice","Deform using the shape of a lattice object"),("MESH_DEFORM","Mesh Deform","Deform using a different mesh, which acts as a deformation cage"),("SHRINKWRAP","Shrinkwrap","Project the shape onto another object"),("SIMPLE_DEFORM","Simple Deform","Deform the shape by twisting, bending, tapering or stretching"),("SMOOTH","Smooth","Smooth the mesh by flattening the angles between adjacent faces"),("CORRECTIVE_SMOOTH","Smooth Corrective","Smooth the mesh while still preserving the volume"),("LAPLACIANSMOOTH","Smooth Laplacian","Reduce the noise on a mesh surface with minimal changes to its shape"),("SURFACE_DEFORM","Surface Deform","Transfer motion from another mesh"),("WARP","Warp","Warp parts of a mesh to a new location in a very flexible way thanks to 2 specified objects"),("WAVE","Wave","Adds a ripple-like motion to an object's geometry"),("VOLUME_DISPLACE","Volume Displace","Deform volume based on noise or other vector fields"),("CLOTH","Cloth",""),("COLLISION","Collision",""),("DYNAMIC_PAINT","Dynamic Paint",""),("EXPLODE","Explode","Break apart the mesh faces and let them follow particles"),("FLUID","Fluid",""),("OCEAN","Ocean","Generate a moving ocean surface"),("PARTICLE_INSTANCE","Particle Instance",""),("PARTICLE_SYSTEM","Particle System","Spawn particles from the shape"),("SOFT_BODY","Soft Body",""),("SURFACE","Surface",""),]),)
        object.collision.damping = sn_cast_float(bpy.context.scene.c_p_damping)
        object.collision.thickness_outer = bpy.context.scene.c_p_thick_outer
        object.collision.thickness_inner = bpy.context.scene.c_p_thick_inner
        object.collision.cloth_friction = bpy.context.scene.c_p_friction
    except Exception as exc:
        print(str(exc) + " | Error in function AddCollisionModifier")

def duplicatecloth(name, display_as, ):
    try:
        cloth["tojoin"] = []
        for_node_E7714 = 0
        for_node_index_E7714 = 0
        for for_node_index_E7714, for_node_E7714 in enumerate(bpy.context.selected_objects):
            run_function_on_EBA21 = for_node_E7714.copy()
            run_function_on_209C7 = bpy.context.scene.collection.objects.link(object=run_function_on_EBA21, )
            cloth["tojoin"].append("")
            bpy.context.view_layer.objects.active=run_function_on_EBA21
        bpy.ops.object.select_all('INVOKE_DEFAULT' if True else 'EXEC_DEFAULT',action=sn_cast_enum(r"DESELECT", [("TOGGLE","Toggle","Toggle selection for all elements"),("SELECT","Select","Select all elements"),("DESELECT","Deselect","Deselect all elements"),("INVERT","Invert","Invert selection of all elements"),]),)
        for_node_27AE0 = 0
        for_node_index_27AE0 = 0
        for for_node_index_27AE0, for_node_27AE0 in enumerate(cloth["tojoin"]):
            run_function_on_B180E = sn_cast_blend_data(for_node_27AE0).select_set(state=True, view_layer=None, )
            bpy.context.view_layer.objects.active=sn_cast_blend_data(for_node_27AE0)
            bpy.ops.object.make_single_user('INVOKE_DEFAULT' if False else 'EXEC_DEFAULT',type=sn_cast_enum(r"SELECTED_OBJECTS", [("SELECTED_OBJECTS","Selected Objects",""),("ALL","All",""),]),object=True,obdata=True,)
        bpy.ops.object.join('INVOKE_DEFAULT' if True else 'EXEC_DEFAULT',)
        bpy.ops.object.transform_apply('INVOKE_DEFAULT' if True else 'EXEC_DEFAULT',location=True,rotation=True,scale=True,properties=False,)
        bpy.context.active_object.display_type = display_as
        bpy.context.active_object.name=name
        bpy.context.active_object.parent_bone=r""
        if bpy.context.scene.p_voxelsize == 0.0:
            pass
        else:
            run_function_on_BF6B8 = bpy.context.active_object.modifiers.new(name=r"Remesh", type=sn_cast_enum(r"REMESH", [("DATA_TRANSFER","Data Transfer","Transfer several types of data (vertex groups, UV maps, vertex colors, custom normals) from one mesh to another"),("MESH_CACHE","Mesh Cache","Deform the mesh using an external frame-by-frame vertex transform cache"),("MESH_SEQUENCE_CACHE","Mesh Sequence Cache","Deform the mesh or curve using an external mesh cache in Alembic format"),("NORMAL_EDIT","Normal Edit","Modify the direction of the surface normals"),("WEIGHTED_NORMAL","Weighted Normal","Modify the direction of the surface normals using a weighting method"),("UV_PROJECT","UV Project","Project the UV map coordinates from the negative Z axis of another object"),("UV_WARP","UV Warp","Transform the UV map using the difference between two objects"),("VERTEX_WEIGHT_EDIT","Vertex Weight Edit","Modify of the weights of a vertex group"),("VERTEX_WEIGHT_MIX","Vertex Weight Mix","Mix the weights of two vertex groups"),("VERTEX_WEIGHT_PROXIMITY","Vertex Weight Proximity","Set the vertex group weights based on the distance to another target object"),("ARRAY","Array","Create copies of the shape with offsets"),("BEVEL","Bevel","Generate sloped corners by adding geometry to the mesh's edges or vertices"),("BOOLEAN","Boolean","Use another shape to cut, combine or perform a difference operation"),("BUILD","Build","Cause the faces of the mesh object to appear or disappear one after the other over time"),("DECIMATE","Decimate","Reduce the geometry density"),("EDGE_SPLIT","Edge Split","Split away joined faces at the edges"),("NODES","Geometry Nodes",""),("MASK","Mask","Dynamically hide vertices based on a vertex group or armature"),("MIRROR","Mirror","Mirror along the local X, Y and/or Z axes, over the object origin"),("MESH_TO_VOLUME","Mesh to Volume",""),("MULTIRES","Multiresolution","Subdivide the mesh in a way that allows editing the higher subdivision levels"),("REMESH","Remesh","Generate new mesh topology based on the current shape"),("SCREW","Screw","Lathe around an axis, treating the input mesh as a profile"),("SKIN","Skin","Create a solid shape from vertices and edges, using the vertex radius to define the thickness"),("SOLIDIFY","Solidify","Make the surface thick"),("SUBSURF","Subdivision Surface","Split the faces into smaller parts, giving it a smoother appearance"),("TRIANGULATE","Triangulate","Convert all polygons to triangles"),("VOLUME_TO_MESH","Volume to Mesh",""),("WELD","Weld","Find groups of vertices closer than dist and merge them together"),("WIREFRAME","Wireframe","Convert faces into thickened edges"),("ARMATURE","Armature","Deform the shape using an armature object"),("CAST","Cast","Shift the shape towards a predefined primitive"),("CURVE","Curve","Bend the mesh using a curve object"),("DISPLACE","Displace","Offset vertices based on a texture"),("HOOK","Hook","Deform specific points using another object"),("LAPLACIANDEFORM","Laplacian Deform","Deform based a series of anchor points"),("LATTICE","Lattice","Deform using the shape of a lattice object"),("MESH_DEFORM","Mesh Deform","Deform using a different mesh, which acts as a deformation cage"),("SHRINKWRAP","Shrinkwrap","Project the shape onto another object"),("SIMPLE_DEFORM","Simple Deform","Deform the shape by twisting, bending, tapering or stretching"),("SMOOTH","Smooth","Smooth the mesh by flattening the angles between adjacent faces"),("CORRECTIVE_SMOOTH","Smooth Corrective","Smooth the mesh while still preserving the volume"),("LAPLACIANSMOOTH","Smooth Laplacian","Reduce the noise on a mesh surface with minimal changes to its shape"),("SURFACE_DEFORM","Surface Deform","Transfer motion from another mesh"),("WARP","Warp","Warp parts of a mesh to a new location in a very flexible way thanks to 2 specified objects"),("WAVE","Wave","Adds a ripple-like motion to an object's geometry"),("VOLUME_DISPLACE","Volume Displace","Deform volume based on noise or other vector fields"),("CLOTH","Cloth",""),("COLLISION","Collision",""),("DYNAMIC_PAINT","Dynamic Paint",""),("EXPLODE","Explode","Break apart the mesh faces and let them follow particles"),("FLUID","Fluid",""),("OCEAN","Ocean","Generate a moving ocean surface"),("PARTICLE_INSTANCE","Particle Instance",""),("PARTICLE_SYSTEM","Particle System","Spawn particles from the shape"),("SOFT_BODY","Soft Body",""),("SURFACE","Surface",""),]), )
            run_function_on_BF6B8.voxel_size = bpy.context.scene.p_voxelsize
        run_function_on_660CF = bpy.context.active_object.modifiers.new(name=r"Decimate", type=sn_cast_enum(r"DECIMATE", [("DATA_TRANSFER","Data Transfer","Transfer several types of data (vertex groups, UV maps, vertex colors, custom normals) from one mesh to another"),("MESH_CACHE","Mesh Cache","Deform the mesh using an external frame-by-frame vertex transform cache"),("MESH_SEQUENCE_CACHE","Mesh Sequence Cache","Deform the mesh or curve using an external mesh cache in Alembic format"),("NORMAL_EDIT","Normal Edit","Modify the direction of the surface normals"),("WEIGHTED_NORMAL","Weighted Normal","Modify the direction of the surface normals using a weighting method"),("UV_PROJECT","UV Project","Project the UV map coordinates from the negative Z axis of another object"),("UV_WARP","UV Warp","Transform the UV map using the difference between two objects"),("VERTEX_WEIGHT_EDIT","Vertex Weight Edit","Modify of the weights of a vertex group"),("VERTEX_WEIGHT_MIX","Vertex Weight Mix","Mix the weights of two vertex groups"),("VERTEX_WEIGHT_PROXIMITY","Vertex Weight Proximity","Set the vertex group weights based on the distance to another target object"),("ARRAY","Array","Create copies of the shape with offsets"),("BEVEL","Bevel","Generate sloped corners by adding geometry to the mesh's edges or vertices"),("BOOLEAN","Boolean","Use another shape to cut, combine or perform a difference operation"),("BUILD","Build","Cause the faces of the mesh object to appear or disappear one after the other over time"),("DECIMATE","Decimate","Reduce the geometry density"),("EDGE_SPLIT","Edge Split","Split away joined faces at the edges"),("NODES","Geometry Nodes",""),("MASK","Mask","Dynamically hide vertices based on a vertex group or armature"),("MIRROR","Mirror","Mirror along the local X, Y and/or Z axes, over the object origin"),("MESH_TO_VOLUME","Mesh to Volume",""),("MULTIRES","Multiresolution","Subdivide the mesh in a way that allows editing the higher subdivision levels"),("REMESH","Remesh","Generate new mesh topology based on the current shape"),("SCREW","Screw","Lathe around an axis, treating the input mesh as a profile"),("SKIN","Skin","Create a solid shape from vertices and edges, using the vertex radius to define the thickness"),("SOLIDIFY","Solidify","Make the surface thick"),("SUBSURF","Subdivision Surface","Split the faces into smaller parts, giving it a smoother appearance"),("TRIANGULATE","Triangulate","Convert all polygons to triangles"),("VOLUME_TO_MESH","Volume to Mesh",""),("WELD","Weld","Find groups of vertices closer than dist and merge them together"),("WIREFRAME","Wireframe","Convert faces into thickened edges"),("ARMATURE","Armature","Deform the shape using an armature object"),("CAST","Cast","Shift the shape towards a predefined primitive"),("CURVE","Curve","Bend the mesh using a curve object"),("DISPLACE","Displace","Offset vertices based on a texture"),("HOOK","Hook","Deform specific points using another object"),("LAPLACIANDEFORM","Laplacian Deform","Deform based a series of anchor points"),("LATTICE","Lattice","Deform using the shape of a lattice object"),("MESH_DEFORM","Mesh Deform","Deform using a different mesh, which acts as a deformation cage"),("SHRINKWRAP","Shrinkwrap","Project the shape onto another object"),("SIMPLE_DEFORM","Simple Deform","Deform the shape by twisting, bending, tapering or stretching"),("SMOOTH","Smooth","Smooth the mesh by flattening the angles between adjacent faces"),("CORRECTIVE_SMOOTH","Smooth Corrective","Smooth the mesh while still preserving the volume"),("LAPLACIANSMOOTH","Smooth Laplacian","Reduce the noise on a mesh surface with minimal changes to its shape"),("SURFACE_DEFORM","Surface Deform","Transfer motion from another mesh"),("WARP","Warp","Warp parts of a mesh to a new location in a very flexible way thanks to 2 specified objects"),("WAVE","Wave","Adds a ripple-like motion to an object's geometry"),("VOLUME_DISPLACE","Volume Displace","Deform volume based on noise or other vector fields"),("CLOTH","Cloth",""),("COLLISION","Collision",""),("DYNAMIC_PAINT","Dynamic Paint",""),("EXPLODE","Explode","Break apart the mesh faces and let them follow particles"),("FLUID","Fluid",""),("OCEAN","Ocean","Generate a moving ocean surface"),("PARTICLE_INSTANCE","Particle Instance",""),("PARTICLE_SYSTEM","Particle System","Spawn particles from the shape"),("SOFT_BODY","Soft Body",""),("SURFACE","Surface",""),]), )
        run_function_on_660CF.ratio = sn_cast_float(bpy.context.scene.p_decimaterate)
        bpy.ops.object.convert('INVOKE_DEFAULT' if False else 'EXEC_DEFAULT',target=sn_cast_enum(r"MESH", [("CURVE","Curve","Curve from Mesh or Text objects"),("MESH","Mesh","Mesh from Curve, Surface, Metaball, or Text objects"),("GPENCIL","Grease Pencil","Grease Pencil from Curve or Mesh objects"),]),)
    except Exception as exc:
        print(str(exc) + " | Error in function DuplicateCloth")

def sn_handle_script_line_exception(exc, line):
    print("# # # # # # # # SCRIPT LINE ERROR # # # # # # # #")
    print("Line:", line)
    raise exc

def dropcloth():
    try:
        cloth["active"] = []
        cloth["passive"] = None
        cloth["tojoin"] = []
        bpy.context.scene.dropped = True
        for_node_CD1FB = 0
        for_node_index_CD1FB = 0
        for for_node_index_CD1FB, for_node_CD1FB in enumerate(bpy.context.selected_objects):
            if for_node_CD1FB.type=="MESH":
                cloth["active"].append(for_node_CD1FB)
                bpy.context.view_layer.objects.active=for_node_CD1FB
            else:
                pass
        bpy.ops.object.select_all('INVOKE_DEFAULT' if True else 'EXEC_DEFAULT',action=sn_cast_enum(r"INVERT", [("TOGGLE","Toggle","Toggle selection for all elements"),("SELECT","Select","Select all elements"),("DESELECT","Deselect","Deselect all elements"),("INVERT","Invert","Invert selection of all elements"),]),)
        for_node_70768 = 0
        for_node_index_70768 = 0
        for for_node_index_70768, for_node_70768 in enumerate(bpy.context.selected_objects):
            if for_node_70768.type=="MESH":
                bpy.context.view_layer.objects.active=None
            else:
                run_function_on_6568A = for_node_70768.select_set(state=False, view_layer=None, )
        cloth["passive"] = None
        function_return_270CE = duplicate(r"COLLIDER", sn_cast_enum(r"WIRE", [("BOUNDS","Bounds","Display the bounds of the object"),("WIRE","Wire","Display the object as a wireframe"),("SOLID","Solid","Display the object as a solid (if solid drawing is enabled in the viewport)"),("TEXTURED","Textured","Display the object with textures (if textures are enabled in the viewport)"),]), )
        cloth["passive"] = bpy.context.active_object
        function_return_3DCF7 = setclothpassiv()
        function_return_3720B = setclothactive()
    except Exception as exc:
        print(str(exc) + " | Error in function DropCloth")


#######   Earthquake
def earthquakefunction(object, keyindex, curveindex, ):
    try:
        run_function_on_5AC49 = object.keyframe_insert(data_path=r"location", index=keyindex, frame=1.0, group=r"", )
        run_function_on_1FDE8 = object.animation_data.action.fcurves.find(data_path=r"location", index=curveindex, )
        new_return_83149 = run_function_on_1FDE8.modifiers.new(type=sn_cast_enum(r"NOISE", [("NULL","Invalid",""),("GENERATOR","Generator","Generate a curve using a factorized or expanded polynomial"),("FNGENERATOR","Built-In Function","Generate a curve using standard math functions such as sin and cos"),("ENVELOPE","Envelope","Reshape F-Curve values, e.g. change amplitude of movements"),("CYCLES","Cycles","Cyclic extend/repeat keyframe sequence"),("NOISE","Noise","Add pseudo-random noise on top of F-Curves"),("LIMITS","Limits","Restrict maximum and minimum values of F-Curve"),("STEPPED","Stepped Interpolation","Snap values to nearest grid step, e.g. for a stop-motion look"),]), )
        earthquake["fmodifier"].append(new_return_83149)
        setattr(new_return_83149,r"strength",0.0)
        setattr(new_return_83149,r"scale",0.20000000298023224)
    except Exception as exc:
        print(str(exc) + " | Error in function EarthquakeFunction")

def resetfmodifierlist():
    try:
        earthquake["fmodifier"] = []
    except Exception as exc:
        print(str(exc) + " | Error in function ResetFModifierList")

def updateearthquake():
    try:
        if bpy.context.scene.earthquakex:
            setattr(sn_cast_blend_data(earthquake["fmodifier"][0]),r"strength",(bpy.context.scene.earthquake / 400.0))
            setattr(sn_cast_blend_data(earthquake["fmodifier"][0]),r"phase",random.uniform(min(1.0, 10.0), max(1.0, 10.0)))
        else:
            setattr(sn_cast_blend_data(earthquake["fmodifier"][0]),r"strength",0.0)
        if bpy.context.scene.earthquakey:
            setattr(sn_cast_blend_data(earthquake["fmodifier"][1]),r"strength",(bpy.context.scene.earthquake / 400.0))
            setattr(sn_cast_blend_data(earthquake["fmodifier"][1]),r"phase",random.uniform(min(1.0, 10.0), max(1.0, 10.0)))
        else:
            setattr(sn_cast_blend_data(earthquake["fmodifier"][1]),r"strength",0.0)
        if bpy.context.scene.earthquakez:
            setattr(sn_cast_blend_data(earthquake["fmodifier"][2]),r"strength",(bpy.context.scene.earthquake / 400.0))
            setattr(sn_cast_blend_data(earthquake["fmodifier"][2]),r"phase",random.uniform(min(1.0, 10.0), max(1.0, 10.0)))
        else:
            setattr(sn_cast_blend_data(earthquake["fmodifier"][2]),r"strength",0.0)
    except Exception as exc:
        print(str(exc) + " | Error in function UpdateEarthquake")


###############   EVALUATED CODE
#######   Physics Dropper
class SNA_PT_Active_Settings_1C85D(bpy.types.Panel):
    bl_label = "Active Settings"
    bl_idname = "SNA_PT_Active_Settings_1C85D"
    bl_parent_id = "SNA_PT_Physics_Dropper_4B116"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_options = {"DEFAULT_CLOSED",}


    @classmethod
    def poll(cls, context):
        return not (sn_cast_boolean(bpy.context.scene.dropped) or not sn_cast_blend_data(bpy.context.scene).is_rigid)

    def draw_header(self, context):
        try:
            layout = self.layout
            layout.label(text=r"",icon_value=37)
        except Exception as exc:
            print(str(exc) + " | Error in Active Settings subpanel header")

    def draw(self, context):
        try:
            layout = self.layout
            col = layout.column(align=True)
            col.enabled = True
            col.alert = False
            col.scale_x = 1.0
            col.scale_y = 1.0
            box = col.box()
            box.enabled = True
            box.alert = False
            box.scale_x = 1.0
            box.scale_y = 1.0
            box.prop(sn_cast_blend_data(bpy.context.scene),'optimizehighpoly',icon_value=0,text=r"Use Proxy for Highpoly Objects",emboss=True,toggle=False,invert_checkbox=False,)
            if sn_cast_blend_data(bpy.context.scene).optimizehighpoly:
                row = box.row(align=True)
                row.enabled = True
                row.alert = False
                row.scale_x = 1.0
                row.scale_y = 1.0
                row.prop(sn_cast_blend_data(bpy.context.scene),'a_voxelsize',text=r"Voxel Size",emboss=True,slider=False,)
                row.prop(sn_cast_blend_data(bpy.context.scene),'a_decimaterate',text=r"Decimate Rate",emboss=True,slider=False,)
            else:
                pass
            col.prop(sn_cast_blend_data(bpy.context.scene),'a_shape',icon_value=0,text=r"Shape",emboss=True,expand=False,)
            col.prop(sn_cast_blend_data(bpy.context.scene),'a_mass',text=r"Mass",emboss=True,slider=False,)
            col.prop(sn_cast_blend_data(bpy.context.scene),'a_friction',text=r"Friction",emboss=True,slider=True,)
            col.prop(sn_cast_blend_data(bpy.context.scene),'a_bunciness',text=r"Bunciness",emboss=True,slider=True,)
            col.prop(sn_cast_blend_data(bpy.context.scene),'a_margin',text=r"Margin",emboss=True,slider=True,)
            col.prop(sn_cast_blend_data(bpy.context.scene),'a_tra_damp',text=r"Damping Translation",emboss=True,slider=True,)
            col.prop(sn_cast_blend_data(bpy.context.scene),'a_rot_damp',text=r"Damping  Rotation",emboss=True,slider=True,)
        except Exception as exc:
            print(str(exc) + " | Error in Active Settings subpanel")


class SNA_PT_Word_Settings_65161(bpy.types.Panel):
    bl_label = "Word Settings"
    bl_idname = "SNA_PT_Word_Settings_65161"
    bl_parent_id = "SNA_PT_Physics_Dropper_4B116"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_options = {"DEFAULT_CLOSED",}


    @classmethod
    def poll(cls, context):
        return not (sn_cast_boolean(bpy.context.scene.dropped) or not sn_cast_blend_data(bpy.context.scene).is_rigid)

    def draw_header(self, context):
        try:
            layout = self.layout
            layout.label(text=r"",icon_value=117)
        except Exception as exc:
            print(str(exc) + " | Error in Word Settings subpanel header")

    def draw(self, context):
        try:
            layout = self.layout
            col = layout.column(align=True)
            col.enabled = True
            col.alert = False
            col.scale_x = 1.0
            col.scale_y = 1.0
            row = col.row(align=True)
            row.enabled = True
            row.alert = False
            row.scale_x = 1.0
            row.scale_y = 1.0
            row.prop(sn_cast_blend_data(bpy.context.scene),'w_startframe',text=r"Start Frame",emboss=True,slider=False,)
            row.prop(sn_cast_blend_data(bpy.context.scene),'w_endframe',text=r"End Frame",emboss=True,slider=False,)
            col.prop(sn_cast_blend_data(bpy.context.scene),'w_subframes',text=r"Substeps Per Frame",emboss=True,slider=False,)
            col.prop(sn_cast_blend_data(bpy.context.scene),'w_solver_iterations',text=r"Solver Iterations",emboss=True,slider=False,)
            col.prop(sn_cast_blend_data(bpy.context.scene),'w_split_impulse',icon_value=0,text=r"Split Impulse",emboss=True,toggle=False,invert_checkbox=False,)
        except Exception as exc:
            print(str(exc) + " | Error in Word Settings subpanel")


class SNA_PT_Passive_Settings_76F70(bpy.types.Panel):
    bl_label = "Passive Settings"
    bl_idname = "SNA_PT_Passive_Settings_76F70"
    bl_parent_id = "SNA_PT_Physics_Dropper_4B116"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_options = {"DEFAULT_CLOSED",}


    @classmethod
    def poll(cls, context):
        return not (sn_cast_boolean(bpy.context.scene.dropped) or not sn_cast_blend_data(bpy.context.scene).is_rigid)

    def draw_header(self, context):
        try:
            layout = self.layout
            layout.label(text=r"",icon_value=66)
        except Exception as exc:
            print(str(exc) + " | Error in Passive Settings subpanel header")

    def draw(self, context):
        try:
            layout = self.layout
            col = layout.column(align=True)
            col.enabled = True
            col.alert = False
            col.scale_x = 1.0
            col.scale_y = 1.0
            box = col.box()
            box.enabled = True
            box.alert = False
            box.scale_x = 1.0
            box.scale_y = 1.0
            box.prop(sn_cast_blend_data(bpy.context.scene),'p_optimizehighpoly',icon_value=0,text=r"Use Proxy for Highpoly Objects",emboss=True,toggle=False,invert_checkbox=False,)
            if sn_cast_blend_data(bpy.context.scene).p_optimizehighpoly:
                row = box.row(align=True)
                row.enabled = True
                row.alert = False
                row.scale_x = 1.0
                row.scale_y = 1.0
                row.prop(sn_cast_blend_data(bpy.context.scene),'p_voxelsize',text=r"Voxel Size",emboss=True,slider=False,)
                row.prop(sn_cast_blend_data(bpy.context.scene),'p_decimaterate',text=r"Decimate Rate",emboss=True,slider=False,)
            else:
                pass
            col.prop(sn_cast_blend_data(bpy.context.scene),'p_shape',icon_value=0,text=r"Shape",emboss=True,expand=False,)
            col.prop(sn_cast_blend_data(bpy.context.scene),'p_friction',text=r"Friction",emboss=True,slider=True,)
            col.prop(sn_cast_blend_data(bpy.context.scene),'p_bunciness',text=r"Bunciness",emboss=True,slider=True,)
            col.prop(sn_cast_blend_data(bpy.context.scene),'p_margin',text=r"Margin",emboss=True,slider=True,)
        except Exception as exc:
            print(str(exc) + " | Error in Passive Settings subpanel")


class SNA_OT_Pausesim(bpy.types.Operator):
    bl_idname = "sna.pausesim"
    bl_label = "PauseSim"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}


    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        try:
            pass
        except Exception as exc:
            print(str(exc) + " | Error in execute function of PauseSim")
        return {"FINISHED"}

    def invoke(self, context, event):
        try:
            bpy.ops.screen.animation_play('INVOKE_DEFAULT' if True else 'EXEC_DEFAULT',reverse=False,sync=False,)
        except Exception as exc:
            print(str(exc) + " | Error in invoke function of PauseSim")
        return self.execute(context)


class SNA_OT_Setrigid(bpy.types.Operator):
    bl_idname = "sna.setrigid"
    bl_label = "SetRigid"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}


    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        try:
            pass
        except Exception as exc:
            print(str(exc) + " | Error in execute function of SetRigid")
        return {"FINISHED"}

    def invoke(self, context, event):
        try:
            sn_cast_blend_data(bpy.context.scene).is_rigid = True
        except Exception as exc:
            print(str(exc) + " | Error in invoke function of SetRigid")
        return self.execute(context)


class SNA_OT_Setcloth(bpy.types.Operator):
    bl_idname = "sna.setcloth"
    bl_label = "SetCloth"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}


    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        try:
            pass
        except Exception as exc:
            print(str(exc) + " | Error in execute function of SetCloth")
        return {"FINISHED"}

    def invoke(self, context, event):
        try:
            sn_cast_blend_data(bpy.context.scene).is_rigid = False
        except Exception as exc:
            print(str(exc) + " | Error in invoke function of SetCloth")
        return self.execute(context)


class SNA_PT_Damping_C3699(bpy.types.Panel):
    bl_label = "Damping"
    bl_idname = "SNA_PT_Damping_C3699"
    bl_parent_id = "SNA_PT_Physics_Dropper_4B116"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_options = {"DEFAULT_CLOSED",}


    @classmethod
    def poll(cls, context):
        return not (sn_cast_boolean(bpy.context.scene.dropped) or sn_cast_blend_data(bpy.context.scene).is_rigid)

    def draw_header(self, context):
        try:
            layout = self.layout
            layout.label(text=r"",icon_value=536)
        except Exception as exc:
            print(str(exc) + " | Error in Damping subpanel header")

    def draw(self, context):
        try:
            layout = self.layout
            col = layout.column(align=True)
            col.enabled = True
            col.alert = False
            col.scale_x = 1.0
            col.scale_y = 1.0
            col.prop(sn_cast_blend_data(bpy.context.scene),'ca_damp_tension',text=r"Tension",emboss=True,slider=False,)
            col.prop(sn_cast_blend_data(bpy.context.scene),'ca_damp_compression',text=r"Compression",emboss=True,slider=False,)
            col.prop(sn_cast_blend_data(bpy.context.scene),'ca_damp_shear',text=r"Shear",emboss=True,slider=False,)
            col.prop(sn_cast_blend_data(bpy.context.scene),'ca_damp_bending',text=r"Bending",emboss=True,slider=False,)
        except Exception as exc:
            print(str(exc) + " | Error in Damping subpanel")


class SNA_PT_Pressure_FF804(bpy.types.Panel):
    bl_label = "Pressure"
    bl_idname = "SNA_PT_Pressure_FF804"
    bl_parent_id = "SNA_PT_Physics_Dropper_4B116"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_options = {"DEFAULT_CLOSED",}


    @classmethod
    def poll(cls, context):
        return not (sn_cast_boolean(bpy.context.scene.dropped) or sn_cast_blend_data(bpy.context.scene).is_rigid)

    def draw_header(self, context):
        try:
            layout = self.layout
            layout.prop(sn_cast_blend_data(bpy.context.scene),'ca_usepressure',icon_value=0,text=r"",emboss=True,toggle=False,invert_checkbox=False,)
        except Exception as exc:
            print(str(exc) + " | Error in Pressure subpanel header")

    def draw(self, context):
        try:
            layout = self.layout
            col = layout.column(align=True)
            col.enabled = True
            col.alert = False
            col.scale_x = 1.0
            col.scale_y = 1.0
            col.prop(sn_cast_blend_data(bpy.context.scene),'ca_pressure',text=r"Pressure",emboss=True,slider=False,)
            col.prop(sn_cast_blend_data(bpy.context.scene),'ca_pressurescale',text=r"Pressure Scale",emboss=True,slider=False,)
            col.prop(sn_cast_blend_data(bpy.context.scene),'ca_pressurefluiddensity',text=r"Fluid Density",emboss=True,slider=False,)
        except Exception as exc:
            print(str(exc) + " | Error in Pressure subpanel")


class SNA_PT_Self_Collision_4C94E(bpy.types.Panel):
    bl_label = "Self Collision"
    bl_idname = "SNA_PT_Self_Collision_4C94E"
    bl_parent_id = "SNA_PT_Physics_Dropper_4B116"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_options = {"DEFAULT_CLOSED",}


    @classmethod
    def poll(cls, context):
        return not (sn_cast_boolean(bpy.context.scene.dropped) or sn_cast_blend_data(bpy.context.scene).is_rigid)

    def draw_header(self, context):
        try:
            layout = self.layout
            layout.prop(sn_cast_blend_data(bpy.context.scene),'ca_selfcollision',icon_value=0,text=r"",emboss=True,toggle=False,invert_checkbox=False,)
        except Exception as exc:
            print(str(exc) + " | Error in Self Collision subpanel header")

    def draw(self, context):
        try:
            layout = self.layout
            layout.prop(sn_cast_blend_data(bpy.context.scene),'ca_selfcollisionfriction',text=r"Friction",emboss=True,slider=False,)
            layout.prop(sn_cast_blend_data(bpy.context.scene),'ca_selfcollisiondistance',text=r"Distance",emboss=True,slider=False,)
            layout.prop(sn_cast_blend_data(bpy.context.scene),'ca_selfcollisionimpulseclamping',text=r"Impulse Clamping",emboss=True,slider=False,)
        except Exception as exc:
            print(str(exc) + " | Error in Self Collision subpanel")


class SNA_PT_Stiffness_C0453(bpy.types.Panel):
    bl_label = "Stiffness"
    bl_idname = "SNA_PT_Stiffness_C0453"
    bl_parent_id = "SNA_PT_Physics_Dropper_4B116"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_options = {"DEFAULT_CLOSED",}


    @classmethod
    def poll(cls, context):
        return not (sn_cast_boolean(bpy.context.scene.dropped) or sn_cast_blend_data(bpy.context.scene).is_rigid)

    def draw_header(self, context):
        try:
            layout = self.layout
            layout.label(text=r"",icon_value=650)
        except Exception as exc:
            print(str(exc) + " | Error in Stiffness subpanel header")

    def draw(self, context):
        try:
            layout = self.layout
            col = layout.column(align=True)
            col.enabled = True
            col.alert = False
            col.scale_x = 1.0
            col.scale_y = 1.0
            col.prop(sn_cast_blend_data(bpy.context.scene),'ca_stiff_tension',text=r"Tension",emboss=True,slider=False,)
            col.prop(sn_cast_blend_data(bpy.context.scene),'ca_stiff_compression',text=r"Compression",emboss=True,slider=False,)
            col.prop(sn_cast_blend_data(bpy.context.scene),'ca_stiff_shear',text=r"Shear",emboss=True,slider=False,)
            col.prop(sn_cast_blend_data(bpy.context.scene),'ca_stiff_bending',text=r"Bending",emboss=True,slider=False,)
        except Exception as exc:
            print(str(exc) + " | Error in Stiffness subpanel")


class SNA_PT_Advanced_Cloth_Settings_88CBB(bpy.types.Panel):
    bl_label = "Advanced Cloth Settings"
    bl_idname = "SNA_PT_Advanced_Cloth_Settings_88CBB"
    bl_parent_id = "SNA_PT_Physics_Dropper_4B116"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_options = {"DEFAULT_CLOSED",}


    @classmethod
    def poll(cls, context):
        return not (sn_cast_boolean(bpy.context.scene.dropped) or sn_cast_blend_data(bpy.context.scene).is_rigid)

    def draw_header(self, context):
        try:
            layout = self.layout
            layout.label(text=r"",icon_value=233)
        except Exception as exc:
            print(str(exc) + " | Error in Advanced Cloth Settings subpanel header")

    def draw(self, context):
        try:
            layout = self.layout
            col = layout.column(align=True)
            col.enabled = True
            col.alert = False
            col.scale_x = 1.0
            col.scale_y = 1.0
            col.prop(sn_cast_blend_data(bpy.context.scene),'ca_qualitysteps',text=r"Quality Steps",emboss=True,slider=False,)
            col.prop(sn_cast_blend_data(bpy.context.scene),'ca_quality',text=r"Collision Quality",emboss=True,slider=False,)
            col.prop(sn_cast_blend_data(bpy.context.scene),'ca_minimumdistance',text=r"Collision Distance",emboss=True,slider=False,)
            col.prop(sn_cast_blend_data(bpy.context.scene),'ca_impulseclamping',text=r"Collision Impulse Clamping",emboss=True,slider=False,)
            col.prop(sn_cast_blend_data(bpy.context.scene),'ca_mass',text=r"Mass",emboss=True,slider=False,)
            col.prop(sn_cast_blend_data(bpy.context.scene),'ca_air_viscosity',text=r"Air Viscosity",emboss=True,slider=False,)
        except Exception as exc:
            print(str(exc) + " | Error in Advanced Cloth Settings subpanel")


class SNA_OT_Dupliapply(bpy.types.Operator):
    bl_idname = "sna.dupliapply"
    bl_label = "DupliApply"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}


    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        try:
            pass
        except Exception as exc:
            print(str(exc) + " | Error in execute function of DupliApply")
        return {"FINISHED"}

    def invoke(self, context, event):
        try:
            function_return_14B15 = applyduplicatelink()
        except Exception as exc:
            print(str(exc) + " | Error in invoke function of DupliApply")
        return self.execute(context)


class SNA_PT_Internal_Spring_25135(bpy.types.Panel):
    bl_label = "Internal Spring"
    bl_idname = "SNA_PT_Internal_Spring_25135"
    bl_parent_id = "SNA_PT_Physics_Dropper_4B116"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_options = {"DEFAULT_CLOSED",}


    @classmethod
    def poll(cls, context):
        return not (sn_cast_boolean(bpy.context.scene.dropped) or sn_cast_blend_data(bpy.context.scene).is_rigid)

    def draw_header(self, context):
        try:
            layout = self.layout
            layout.prop(sn_cast_blend_data(bpy.context.scene),'ca_internalsprings',icon_value=0,text=r"",emboss=True,toggle=False,invert_checkbox=False,)
        except Exception as exc:
            print(str(exc) + " | Error in Internal Spring subpanel header")

    def draw(self, context):
        try:
            layout = self.layout
            col = layout.column(align=True)
            col.enabled = True
            col.alert = False
            col.scale_x = 1.0
            col.scale_y = 1.0
            col.prop(sn_cast_blend_data(bpy.context.scene),'ca_internalspringmaxlength',text=r"Max Spring Creation Length",emboss=True,slider=False,)
            col.prop(sn_cast_blend_data(bpy.context.scene),'ca_internalspringmaxdevision',text=r"Max Creation Diversion",emboss=True,slider=False,)
            col.prop(sn_cast_blend_data(bpy.context.scene),'ca_internalspringtension',text=r"Tension",emboss=True,slider=False,)
            col.prop(sn_cast_blend_data(bpy.context.scene),'ca_internalspringcompression',text=r"Compression",emboss=True,slider=False,)
            col.prop(sn_cast_blend_data(bpy.context.scene),'ca_internalspringmaxtension',text=r"Max Tension",emboss=True,slider=False,)
            col.prop(sn_cast_blend_data(bpy.context.scene),'ca_internalspringmaxcompression',text=r"Max Compression",emboss=True,slider=False,)
        except Exception as exc:
            print(str(exc) + " | Error in Internal Spring subpanel")


class SNA_PT_World_Collision_Settings_6B7B3(bpy.types.Panel):
    bl_label = "World Collision Settings"
    bl_idname = "SNA_PT_World_Collision_Settings_6B7B3"
    bl_parent_id = "SNA_PT_Physics_Dropper_4B116"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_options = {"DEFAULT_CLOSED",}


    @classmethod
    def poll(cls, context):
        return not (sn_cast_boolean(bpy.context.scene.dropped) or sn_cast_blend_data(bpy.context.scene).is_rigid)

    def draw_header(self, context):
        try:
            layout = self.layout
            layout.label(text=r"",icon_value=82)
        except Exception as exc:
            print(str(exc) + " | Error in World Collision Settings subpanel header")

    def draw(self, context):
        try:
            layout = self.layout
            col = layout.column(align=True)
            col.enabled = True
            col.alert = False
            col.scale_x = 1.0
            col.scale_y = 1.0
            box = col.box()
            box.enabled = True
            box.alert = False
            box.scale_x = 1.0
            box.scale_y = 1.0
            box.prop(sn_cast_blend_data(bpy.context.scene),'p_optimizehighpoly',icon_value=0,text=r"Use Proxy for Highpoly Objects",emboss=True,toggle=False,invert_checkbox=False,)
            if sn_cast_blend_data(bpy.context.scene).p_optimizehighpoly:
                row = box.row(align=True)
                row.enabled = True
                row.alert = False
                row.scale_x = 1.0
                row.scale_y = 1.0
                row.prop(sn_cast_blend_data(bpy.context.scene),'p_voxelsize',text=r"Voxel Size",emboss=True,slider=False,)
                row.prop(sn_cast_blend_data(bpy.context.scene),'p_decimaterate',text=r"Decimate Rate",emboss=True,slider=False,)
            else:
                pass
            col.prop(sn_cast_blend_data(bpy.context.scene),'w_endframe',text=r"Simulation Length",emboss=True,slider=False,)
            col.prop(sn_cast_blend_data(bpy.context.scene),'c_p_damping',text=r"Damping",emboss=True,slider=True,)
            col.prop(sn_cast_blend_data(bpy.context.scene),'c_p_thick_outer',text=r"Outer Thickness",emboss=True,slider=True,)
            col.prop(sn_cast_blend_data(bpy.context.scene),'c_p_thick_inner',text=r"Inner Thickness",emboss=True,slider=True,)
            col.prop(sn_cast_blend_data(bpy.context.scene),'c_p_friction',text=r"Friction",emboss=True,slider=True,)
        except Exception as exc:
            print(str(exc) + " | Error in World Collision Settings subpanel")


class SNA_OT_Test(bpy.types.Operator):
    bl_idname = "sna.test"
    bl_label = "TEST"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}


    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        try:
            pass
        except Exception as exc:
            print(str(exc) + " | Error in execute function of TEST")
        return {"FINISHED"}

    def invoke(self, context, event):
        try:
            function_return_9AD25 = sn_000_versiontest()
        except Exception as exc:
            print(str(exc) + " | Error in invoke function of TEST")
        return self.execute(context)


class SNA_OT_Drop(bpy.types.Operator):
    bl_idname = "sna.drop"
    bl_label = "Drop"
    bl_description = "Drop all selected Objects"
    bl_options = {"REGISTER", "UNDO"}


    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        try:
            pass
        except Exception as exc:
            print(str(exc) + " | Error in execute function of Drop")
        return {"FINISHED"}

    def invoke(self, context, event):
        try:
            if sn_cast_boolean(bpy.context.scene.dropped):
                pass
            else:
                function_return_D23D4 = checkmeshselected()
                if function_return_D23D4[0]:
                    function_return_1B44F = resetfmodifierlist()
                    if bpy.context.scene.is_rigid:
                        function_return_4D0DC = droprigid()
                    else:
                        function_return_8B125 = dropcloth()
                    function_return_C87F4 = updateearthquake()
                else:
                    pass
        except Exception as exc:
            print(str(exc) + " | Error in invoke function of Drop")
        return self.execute(context)


class SNA_AddonPreferences_E5569(bpy.types.AddonPreferences):
    bl_idname = 'physics_dropper'

    def draw(self, context):
        try:
            layout = self.layout
            col = layout.column(align=False)
            col.enabled = True
            col.alert = False
            col.scale_x = 1.25
            col.scale_y = 1.0
            if "4814A" in addon_keymaps:
                _, kmi = addon_keymaps["4814A"]
                col.prop(kmi, "type", text=r"Drop Shortcut", full_event=True, toggle=False)
            else:
                col.label(text="Couldn't find keymap item!", icon="ERROR")
            if "4A4D6" in addon_keymaps:
                _, kmi = addon_keymaps["4A4D6"]
                col.prop(kmi, "type", text=r"Apply Shortcut", full_event=True, toggle=False)
            else:
                col.label(text="Couldn't find keymap item!", icon="ERROR")
        except Exception as exc:
            print(str(exc) + " | Error in addon preferences")

def register_key_4814A():
    kc = bpy.context.window_manager.keyconfigs.addon
    if kc:
        km = kc.keymaps.new(name="Window", space_type="EMPTY")
        kmi = km.keymap_items.new("sna.drop",
                                    type= "V",
                                    value= "PRESS",
                                    repeat= False,
                                    ctrl=False,
                                    alt=False,
                                    shift=False)
        addon_keymaps['4814A'] = (km, kmi)

def register_key_4A4D6():
    kc = bpy.context.window_manager.keyconfigs.addon
    if kc:
        km = kc.keymaps.new(name="Window", space_type="EMPTY")
        kmi = km.keymap_items.new("sna.apply",
                                    type= "V",
                                    value= "PRESS",
                                    repeat= False,
                                    ctrl=False,
                                    alt=False,
                                    shift=True)
        addon_keymaps['4A4D6'] = (km, kmi)


class SNA_OT_Simpleforce(bpy.types.Operator):
    bl_idname = "sna.simpleforce"
    bl_label = "SimpleForce"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}


    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        try:
            pass
        except Exception as exc:
            print(str(exc) + " | Error in execute function of SimpleForce")
        return {"FINISHED"}

    def invoke(self, context, event):
        try:
            bpy.ops.object.effector_add('INVOKE_DEFAULT' if True else 'EXEC_DEFAULT',type=sn_cast_enum(r"FORCE", [("FORCE","Force",""),("WIND","Wind",""),("VORTEX","Vortex",""),("MAGNET","Magnetic",""),("HARMONIC","Harmonic",""),("CHARGE","Charge",""),("LENNARDJ","Lennard-Jones",""),("TEXTURE","Texture",""),("GUIDE","Curve Guide",""),("BOID","Boid",""),("TURBULENCE","Turbulence",""),("DRAG","Drag",""),("FLUID","Fluid Flow",""),]),radius=0.0,enter_editmode=False,align=sn_cast_enum(r"WORLD", [("WORLD","World","Align the new object to the world"),("VIEW","View","Align the new object to the view"),("CURSOR","3D Cursor","Use the 3D cursor orientation for the new object"),]),location=bpy.context.active_object.location,rotation=(0.0, 0.0, 0.0),scale=(0.0, 0.0, 0.0),)
            bpy.context.active_object.field.strength = 10000.0
            bpy.context.active_object.field.use_min_distance = True
            bpy.context.active_object.field.use_max_distance = True
            bpy.context.active_object.field.distance_max = 1.0
            bpy.ops.transform.translate('INVOKE_DEFAULT' if True else 'EXEC_DEFAULT',)
        except Exception as exc:
            print(str(exc) + " | Error in invoke function of SimpleForce")
        return self.execute(context)


class SNA_OT_Apply(bpy.types.Operator):
    bl_idname = "sna.apply"
    bl_label = "Apply"
    bl_description = "Apply the current state of the dropped objects"
    bl_options = {"REGISTER", "UNDO"}


    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        try:
            pass
        except Exception as exc:
            print(str(exc) + " | Error in execute function of Apply")
        return {"FINISHED"}

    def invoke(self, context, event):
        try:
            if sn_cast_boolean(bpy.context.scene.dropped):
                if bpy.context.scene.is_rigid:
                    function_return_0CF1C = applyrigid()
                else:
                    function_return_B4B0A = applycloth()
            else:
                pass
        except Exception as exc:
            print(str(exc) + " | Error in invoke function of Apply")
        return self.execute(context)


class SNA_OT_Reset(bpy.types.Operator):
    bl_idname = "sna.reset"
    bl_label = "RESET"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}


    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        try:
            pass
        except Exception as exc:
            print(str(exc) + " | Error in execute function of RESET")
        return {"FINISHED"}

    def invoke(self, context, event):
        try:
            if bpy.context.screen.is_animation_playing:
                bpy.ops.screen.animation_play('INVOKE_DEFAULT' if True else 'EXEC_DEFAULT',reverse=False,sync=False,)
            else:
                pass
            bpy.context.scene.frame_current=1
            if bpy.context.scene.is_rigid:
                function_return_BFF8A = applyrigid()
            else:
                function_return_AA778 = applycloth()
        except Exception as exc:
            print(str(exc) + " | Error in invoke function of RESET")
        return self.execute(context)


class SNA_PT_Physics_Dropper_4B116(bpy.types.Panel):
    bl_label = "Physics Dropper"
    bl_idname = "SNA_PT_Physics_Dropper_4B116"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = 'PhyDrop'
    bl_order = 0


    @classmethod
    def poll(cls, context):
        return True

    def draw_header(self, context):
        try:
            layout = self.layout
            layout.label(text=r"",icon_value=bpy.context.scene.physics_dropper_icons['DROPBOX'].icon_id)
        except Exception as exc:
            print(str(exc) + " | Error in Physics Dropper panel header")

    def draw(self, context):
        try:
            layout = self.layout
            if sn_cast_boolean(bpy.context.scene.dropped):
                row = layout.row(align=False)
                row.enabled = True
                row.alert = False
                row.scale_x = 1.0
                row.scale_y = 1.0
                op = row.operator("sna.reset",text=r"RESET",emboss=True,depress=False,icon_value=2)
            else:
                pass
            if sn_cast_boolean(bpy.context.scene.dropped):
                pass
            else:
                row = layout.row(align=True)
                row.enabled = True
                row.alert = False
                row.scale_x = 1.0
                row.scale_y = 1.5
                op = row.operator("sna.setrigid",text=r"Rigidbody",emboss=True,depress=sn_cast_blend_data(bpy.context.scene).is_rigid,icon_value=353)
                op = row.operator("sna.setcloth",text=r"Cloth",emboss=True,depress=not sn_cast_blend_data(bpy.context.scene).is_rigid,icon_value=468)
            if sn_cast_boolean(bpy.context.scene.dropped):
                col = layout.column(align=True)
                col.enabled = True
                col.alert = True
                col.scale_x = 1.0
                col.scale_y = 2.0
                op = col.operator("sna.apply",text=r"Apply",emboss=True,depress=False,icon_value=43)
            else:
                row = layout.row(align=True)
                row.enabled = sn_cast_boolean(bpy.context.selected_objects)
                row.alert = False
                row.scale_x = 1.0
                row.scale_y = 2.0
                op = row.operator("sna.drop",text=r"Drop",emboss=True,depress=False,icon_value=bpy.context.scene.physics_dropper_icons['DROPBOX'].icon_id if sn_cast_blend_data(bpy.context.scene).is_rigid else bpy.context.scene.physics_dropper_icons['DROPCLOTH'].icon_id)
                if sn_cast_boolean(bpy.context.selected_objects):
                    pass
                else:
                    layout.label(text=r"Please select a mesh object",icon_value=0)
            if sn_cast_boolean(bpy.context.scene.dropped):
                col = layout.column(align=False)
                col.enabled = True
                col.alert = False
                col.scale_x = 1.0
                col.scale_y = 2.0
                op = col.operator("sna.pausesim",text=r"Pause/Play Simulation",emboss=True,depress=False,icon_value=498 if bpy.context.screen.is_animation_playing else 495)
                col.separator(factor=1.0)
                row = col.row(align=True)
                row.enabled = True
                row.alert = False
                row.scale_x = 1.0
                row.scale_y = 0.5
                row.prop(sn_cast_blend_data(bpy.context.scene),'earthquake',text=r"Earthquake",emboss=True,slider=True,)
                row.prop(sn_cast_blend_data(bpy.context.scene),'earthquakex',icon_value=bpy.context.scene.physics_dropper_icons['X'].icon_id,text=r"",emboss=True,toggle=True,invert_checkbox=False,)
                row.prop(sn_cast_blend_data(bpy.context.scene),'earthquakey',icon_value=bpy.context.scene.physics_dropper_icons['Y'].icon_id,text=r"",emboss=True,toggle=True,invert_checkbox=False,)
                row.prop(sn_cast_blend_data(bpy.context.scene),'earthquakez',icon_value=bpy.context.scene.physics_dropper_icons['Z'].icon_id,text=r"",emboss=True,toggle=True,invert_checkbox=False,)
            else:
                pass
            if not (sn_cast_boolean(bpy.context.scene.dropped) or bpy.context.scene.is_rigid):
                col = layout.column(align=True)
                col.enabled = True
                col.alert = False
                col.scale_x = 1.0
                col.scale_y = 1.0
                col.label(text=r"Presets:",icon_value=0)
                col.separator(factor=1.0)
                row = col.row(align=True)
                row.enabled = True
                row.alert = False
                row.scale_x = 1.0
                row.scale_y = 1.0
                row.prop(sn_cast_blend_data(bpy.context.scene),'c_a_presets',icon_value=0,text=r"Presets",emboss=True,expand=True,)
            else:
                pass
        except Exception as exc:
            print(str(exc) + " | Error in Physics Dropper panel")


class SNA_OT_Paypal(bpy.types.Operator):
    bl_idname = "sna.paypal"
    bl_label = "Paypal"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}


    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        try:
            pass
        except Exception as exc:
            print(str(exc) + " | Error in execute function of Paypal")
        return {"FINISHED"}

    def invoke(self, context, event):
        try:
            pass
        except Exception as exc:
            print(str(exc) + " | Error in invoke function of Paypal")
        return context.window_manager.invoke_props_dialog(self, width=300)

    def draw(self, context):
        layout = self.layout
        try:
            pass
        except Exception as exc:
            print(str(exc) + " | Error in draw function of Paypal")


class SNA_OT_Bymecoffee(bpy.types.Operator):
    bl_idname = "sna.bymecoffee"
    bl_label = "ByMeCoffee"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}


    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        try:
            pass
        except Exception as exc:
            print(str(exc) + " | Error in execute function of ByMeCoffee")
        return {"FINISHED"}

    def invoke(self, context, event):
        try:
            pass
        except Exception as exc:
            print(str(exc) + " | Error in invoke function of ByMeCoffee")
        return context.window_manager.invoke_props_dialog(self, width=300)

    def draw(self, context):
        layout = self.layout
        try:
            pass
        except Exception as exc:
            print(str(exc) + " | Error in draw function of ByMeCoffee")


class SNA_OT_Donate(bpy.types.Operator):
    bl_idname = "sna.donate"
    bl_label = "Donate"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}


    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        try:
            pass
        except Exception as exc:
            print(str(exc) + " | Error in execute function of Donate")
        return {"FINISHED"}

    def invoke(self, context, event):
        try:
            pass
        except Exception as exc:
            print(str(exc) + " | Error in invoke function of Donate")
        return context.window_manager.invoke_props_dialog(self, width=300)

    def draw(self, context):
        layout = self.layout
        try:
            split = layout.split(align=True,factor=0.5)
            split.enabled = True
            split.alert = False
            split.scale_x = 1.0
            split.scale_y = 1.5
            op = split.operator("wm.url_open",text=r"By me a Tea",emboss=True,depress=False,icon_value=bpy.context.scene.physics_dropper_icons['BMAC'].icon_id)
            op.url = r"https://buymeacoffee.com/FunAddons"
            op = split.operator("wm.url_open",text=r"Paypal",emboss=True,depress=False,icon_value=bpy.context.scene.physics_dropper_icons['PAYPAL'].icon_id)
            op.url = r"https://www.paypal.com/donate/?hosted_button_id=JYSV3UW4TJR64"
        except Exception as exc:
            print(str(exc) + " | Error in draw function of Donate")


###############   REGISTER ICONS
def sn_register_icons():
    icons = ["DROPBOX","X","Y","Z","DROPCLOTH","BMAC","PAYPAL",]
    bpy.types.Scene.physics_dropper_icons = bpy.utils.previews.new()
    icons_dir = os.path.join( os.path.dirname( __file__ ), "icons" )
    for icon in icons:
        bpy.types.Scene.physics_dropper_icons.load( icon, os.path.join( icons_dir, icon + ".png" ), 'IMAGE' )

def sn_unregister_icons():
    bpy.utils.previews.remove( bpy.types.Scene.physics_dropper_icons )


###############   REGISTER PROPERTIES
def sn_register_properties():
    bpy.types.Scene.a_shape = bpy.props.EnumProperty(name='A_Shape',description='Determines the collision shape of the object; these can be broken into two categories: primitive shapes and mesh based shapes.',options=set(),items=[('CONVEX_HULL', 'CONVEX_HULL', 'This is my enum item'), ('MESH', 'MESH', 'This is my enum item'), ('BOX', 'BOX', 'This is my enum item'), ('SPHERE', 'SPHERE', 'This is my enum item'), ('CAPSULE', 'CAPSULE', 'This is my enum item'), ('CYLINDER', 'CYLINDER', 'This is my enum item'), ('CONE', 'CONE', 'This is my enum item'), ('COMPOUND', 'COMPOUND', 'This is my enum item')])
    bpy.types.Scene.a_friction = bpy.props.FloatProperty(name='A_Friction',description='Resistance of object to movement. Specifies how much velocity is lost when objects collide with each other.',subtype='NONE',unit='NONE',options=set(),precision=2, default=1.0,min=0.0,max=1.0)
    bpy.types.Scene.a_bunciness = bpy.props.FloatProperty(name='A_Bunciness',description='Tendency of object to bounce after colliding with another (0 to 1) (rigid to perfectly elastic). Specifies how much objects can bounce after collisions.',subtype='NONE',unit='NONE',options=set(),precision=2, default=0.0,min=0.0,max=1.0)
    bpy.types.Scene.a_margin = bpy.props.FloatProperty(name='A_Margin',description='Threshold of distance near the surface where collisions are still considered (best results when nonzero).',subtype='NONE',unit='NONE',options=set(),precision=3, default=0.0010000000474974513,min=0.0010000000474974513,max=0.10000000149011612)
    bpy.types.Scene.a_tra_damp = bpy.props.FloatProperty(name='A_Tra_Damp',description='Amount of linear velocity that is lost over time.',subtype='NONE',unit='NONE',options=set(),precision=3, default=0.03999999910593033,min=0.0010000000474974513,max=1.0)
    bpy.types.Scene.a_rot_damp = bpy.props.FloatProperty(name='A_Rot_Damp',description='Amount of angular velocity that is lost over time.',subtype='NONE',unit='NONE',options=set(),precision=3, default=0.10000000149011612,min=0.009999999776482582,max=1.0)
    bpy.types.Scene.p_shape = bpy.props.EnumProperty(name='P_Shape',description='Determines the collision shape of the object; these can be broken into two categories: primitive shapes and mesh based shapes.',options=set(),items=[('MESH', 'MESH', 'This is my enum item'), ('CONVEX_HULL', 'CONVEX_HULL', 'This is my enum item'), ('BOX', 'BOX', 'This is my enum item'), ('SPHERE', 'SPHERE', 'This is my enum item'), ('CAPSULE', 'CAPSULE', 'This is my enum item'), ('CYLINDER', 'CYLINDER', 'This is my enum item'), ('CONE', 'CONE', 'This is my enum item'), ('COMPOUND', 'COMPOUND', 'This is my enum item')])
    bpy.types.Scene.p_friction = bpy.props.FloatProperty(name='P_Friction',description='Resistance of object to movement. Specifies how much velocity is lost when objects collide with each other.',subtype='NONE',unit='NONE',options=set(),precision=2, default=1.0,min=0.0,max=1.0)
    bpy.types.Scene.p_bunciness = bpy.props.FloatProperty(name='P_Bunciness',description='Tendency of object to bounce after colliding with another (0 to 1) (rigid to perfectly elastic). Specifies how much objects can bounce after collisions.',subtype='NONE',unit='NONE',options=set(),precision=2, default=0.0,min=0.0,max=1.0)
    bpy.types.Scene.p_margin = bpy.props.FloatProperty(name='P_Margin',description='Threshold of distance near the surface where collisions are still considered (best results when nonzero).',subtype='NONE',unit='NONE',options=set(),precision=3, default=0.0010000000474974513,min=0.0010000000474974513,max=0.10000000149011612)
    bpy.types.Scene.w_endframe = bpy.props.IntProperty(name='W_EndFrame',description='The endframe of the simulation',subtype='NONE',options=set(),default=250)
    bpy.types.Scene.w_split_impulse = bpy.props.BoolProperty(name='W_Split_Impulse',description='Reducing extra velocity that can build up when objects collide (lowers the simulation stability a little so use only when necessary)',options=set(),default=False)
    bpy.types.Scene.w_subframes = bpy.props.IntProperty(name='W_Subframes',description='Number of simulation steps made per second (higher values are more accurate but slower). This only influences the accuracy and not the speed of the simulation.',subtype='NONE',options=set(),default=10)
    bpy.types.Scene.w_solver_iterations = bpy.props.IntProperty(name='W_Solver_Iterations',description='Amount of constraint solver iterations made per simulation step (higher values are more accurate but slower). Increasing this makes constraints and object stacking more stable.',subtype='NONE',options=set(),default=10)
    bpy.types.Scene.is_rigid = bpy.props.BoolProperty(name='Is_Rigid',description='',options=set(),default=True)
    bpy.types.Scene.a_mass = bpy.props.FloatProperty(name='A_Mass',description='Specifies how heavy the object is and “weights” irrespective of gravity.',subtype='NONE',unit='NONE',options=set(),precision=2, default=1.0)
    bpy.types.Scene.c_a_presets = bpy.props.EnumProperty(name='C_A_Presets',description='A selected preset will set the default properties below',options=set(),update=update_c_a_presets,items=[('Cotton', 'Cotton', 'This is my enum item'), ('Denim', 'Denim', 'This is my enum item'), ('Leather', 'Leather', 'This is my enum item'), ('Rubber', 'Rubber', 'This is my enum item'), ('Silk', 'Silk', 'This is my enum item')])
    bpy.types.Scene.c_p_damping = bpy.props.FloatProperty(name='C_P_Damping',description='Damping during a collision. The amount of bounce that the surfaces will have.',subtype='NONE',unit='NONE',options=set(),precision=3, default=0.10000000149011612,min=0.0,max=1.0)
    bpy.types.Scene.c_p_thick_outer = bpy.props.FloatProperty(name='C_P_Thick_Outer',description='Size of the outer collision zone.',subtype='NONE',unit='NONE',options=set(),precision=3, default=0.019999999552965164,min=0.0,max=1.0)
    bpy.types.Scene.c_p_thick_inner = bpy.props.FloatProperty(name='C_P_Thick_Inner',description='Size of the inner collision zone (padding distance).',subtype='NONE',unit='NONE',options=set(),precision=3, default=0.20000000298023224,min=0.0,max=1.0)
    bpy.types.Scene.c_p_friction = bpy.props.FloatProperty(name='C_P_Friction',description='Friction during movements along the surface.',subtype='NONE',unit='NONE',options=set(),precision=2, default=80.0,min=0.0,max=80.0)
    bpy.types.Scene.ca_qualitysteps = bpy.props.IntProperty(name='CA_QualitySteps',description='Set the number of simulation steps per frame. Higher values result in better quality, but will be slower.',subtype='NONE',options=set(),default=5)
    bpy.types.Scene.ca_mass = bpy.props.FloatProperty(name='CA_Mass',description='The mass of the cloth material.',subtype='NONE',unit='MASS',options=set(),precision=2, default=0.30000001192092896)
    bpy.types.Scene.ca_air_viscosity = bpy.props.FloatProperty(name='CA_Air_Viscosity',description='Air has some thickness which slows falling things down.',subtype='NONE',unit='NONE',options=set(),precision=2, default=1.0)
    bpy.types.Scene.ca_stiff_tension = bpy.props.FloatProperty(name='CA_Stiff_Tension',description='How much the material resists stretching.',subtype='NONE',unit='NONE',options=set(),precision=2, default=15.0)
    bpy.types.Scene.ca_stiff_compression = bpy.props.FloatProperty(name='CA_Stiff_Compression',description='How much the material resists compression.',subtype='NONE',unit='NONE',options=set(),precision=2, default=15.0)
    bpy.types.Scene.ca_stiff_shear = bpy.props.FloatProperty(name='CA_Stiff_Shear',description='How much the material resists shearing.',subtype='NONE',unit='NONE',options=set(),precision=2, default=15.0)
    bpy.types.Scene.ca_stiff_bending = bpy.props.FloatProperty(name='CA_Stiff_Bending',description='Wrinkle coefficient. Higher creates more large folds.',subtype='NONE',unit='NONE',options=set(),precision=2, default=0.5)
    bpy.types.Scene.ca_damp_tension = bpy.props.FloatProperty(name='CA_Damp_Tension',description='Amount of damping in stretching behavior.',subtype='NONE',unit='NONE',options=set(),precision=2, default=5.0)
    bpy.types.Scene.ca_damp_compression = bpy.props.FloatProperty(name='CA_Damp_Compression',description='Amount of damping in compression behavior.',subtype='NONE',unit='NONE',options=set(),precision=2, default=0.0)
    bpy.types.Scene.ca_damp_shear = bpy.props.FloatProperty(name='CA_Damp_Shear',description='Amount of damping in shearing behavior.',subtype='NONE',unit='NONE',options=set(),precision=2, default=5.0)
    bpy.types.Scene.ca_damp_bending = bpy.props.FloatProperty(name='CA_Damp_Bending',description='Amount of damping in bending behavior.',subtype='NONE',unit='NONE',options=set(),precision=2, default=0.5)
    bpy.types.Scene.ca_internalsprings = bpy.props.BoolProperty(name='CA_InternalSprings',description='3D or Internal Springs can be used to make a mesh behave similarly to a Soft Body. Internal springs can be enabled by toggling the checkbox in the Internal Springs panel header.',options=set(),default=False)
    bpy.types.Scene.ca_internalspringmaxlength = bpy.props.FloatProperty(name='CA_InternalSpringMaxLength',description='The maximum length an internal spring can have during creation. If the distance between internal points is greater than this, no internal spring will be created between these points. A length of zero means that there is no length limit.',subtype='NONE',unit='NONE',options=set(),precision=2, default=0.0)
    bpy.types.Scene.ca_internalspringmaxdevision = bpy.props.FloatProperty(name='CA_InternalSpringMaxDevision',description='The maximum angle that is allowed to use to connect the internal points can diverge from the vertex normal.',subtype='ANGLE',unit='NONE',options=set(),precision=2, default=45.0)
    bpy.types.Scene.ca_internalspringtension = bpy.props.FloatProperty(name='CA_InternalSpringTension',description='How much the material resists stretching.',subtype='NONE',unit='NONE',options=set(),precision=2, default=15.0)
    bpy.types.Scene.ca_internalspringcompression = bpy.props.FloatProperty(name='CA_InternalSpringCompression',description='How much the material resists compression.',subtype='NONE',unit='NONE',options=set(),precision=2, default=15.0)
    bpy.types.Scene.ca_internalspringmaxtension = bpy.props.FloatProperty(name='CA_InternalSpringMaxTension',description='Maximum tension stiffness value.',subtype='NONE',unit='NONE',options=set(),precision=2, default=15.0)
    bpy.types.Scene.ca_internalspringmaxcompression = bpy.props.FloatProperty(name='CA_InternalSpringMaxCompression',description='Maximum Compression stiffness value.',subtype='NONE',unit='NONE',options=set(),precision=2, default=15.0)
    bpy.types.Scene.ca_usepressure = bpy.props.BoolProperty(name='CA_usePressure',description='Cloth pressure allows the simulation of soft-shelled objects such as balloons or balls that are filled with a type of fluid. This fluid is modeled as a gas; to emulate an incompressible liquid set Pressure Scale as high as possible without breaking the simulation. Cloth pressure can be enabled by toggling the checkbox in the Pressure panel header.',options=set(),default=False)
    bpy.types.Scene.ca_pressure = bpy.props.FloatProperty(name='CA_Pressure',description='The uniform pressure that is constantly applied to the mesh. This value is specified in units of Pressure Scale, and can be negative to simulate implosions or any other case where an object has outside pressure pushing inwards.',subtype='NONE',unit='NONE',options=set(),precision=2, default=1.0)
    bpy.types.Scene.ca_pressurescale = bpy.props.FloatProperty(name='CA_PressureScale',description='Ambient pressure (in kPa) that exists both inside and outside the object, balancing out when the volume matches the target. Increase the value to make the object resist changes in volume more strongly.',subtype='NONE',unit='NONE',options=set(),precision=2, default=1.0)
    bpy.types.Scene.ca_pressurefluiddensity = bpy.props.FloatProperty(name='CA_PressureFluidDensity',description='Specifies the density of the fluid contained inside the object (in kg/liter = 1000 kg/m3, use 1 for water), used to generate a hydrostatic pressure gradient that simulates the weight of the fluid. If the value is negative, it instead models buoyancy from a surrounding fluid.',subtype='NONE',unit='NONE',options=set(),precision=3, default=0.0)
    bpy.types.Scene.ca_quality = bpy.props.IntProperty(name='CA_Quality',description='A general setting for how fine and good a simulation you wish. Higher numbers take more time but ensure less tears and penetrations through the cloth.',subtype='NONE',options=set(),default=2)
    bpy.types.Scene.ca_minimumdistance = bpy.props.FloatProperty(name='CA_MinimumDistance',description='The distance another object must get to the cloth for the simulation to repel the cloth out of the way. Smaller values might give errors but gives some speed-up while larger will give unrealistic results if too large and can be slow. It is best to find a good in between value.',subtype='DISTANCE',unit='NONE',options=set(),precision=4, default=0.014999999664723873)
    bpy.types.Scene.ca_impulseclamping = bpy.props.FloatProperty(name='CA_ImpulseClamping',description='Prevents explosions in tight and complicated collision situations by restricting the amount of movement after a collision.',subtype='NONE',unit='NONE',options=set(),precision=3, default=0.0)
    bpy.types.Scene.ca_selfcollision = bpy.props.BoolProperty(name='CA_SelfCollision',description='Real cloth cannot penetrate itself, so you normally want the cloth to self-collide. Enable this to tell the cloth object that it should not penetrate itself. This adds to the simulation’s compute time, but provides more realistic results.',options=set(),default=False)
    bpy.types.Scene.ca_selfcollisionfriction = bpy.props.FloatProperty(name='CA_SelfCollisionFriction',description='A coefficient for how slippery the cloth is when it collides with itself. For example, silk has a lower coefficient of friction than cotton.',subtype='NONE',unit='NONE',options=set(),precision=2, default=5.0)
    bpy.types.Scene.ca_selfcollisiondistance = bpy.props.FloatProperty(name='CA_SelfCollisionDistance',description='As cloth at this distance begins to repel away from itself. Smaller values might give errors but gives some speed-up while larger will give unrealistic results if too large and can be slow. It is best to find a good in between value.',subtype='DISTANCE',unit='NONE',options=set(),precision=4, default=0.014999999664723873)
    bpy.types.Scene.ca_selfcollisionimpulseclamping = bpy.props.FloatProperty(name='CA_SelfCollisionImpulseClamping',description='Prevents explosions in tight and complicated collision situations by restricting the amount of movement after a collision.',subtype='NONE',unit='NONE',options=set(),precision=2, default=0.0)
    bpy.types.Scene.dropped = bpy.props.BoolProperty(name='Dropped',description='',options=set(),default=False)
    bpy.types.Scene.earthquake = bpy.props.FloatProperty(name='Earthquake',description='Set the amount on world shake',subtype='PERCENTAGE',unit='NONE',options=set(),precision=2, update=update_earthquake,default=0.0,min=0.0,max=100.0)
    bpy.types.Scene.optimizehighpoly = bpy.props.BoolProperty(name='OptimizeHighPoly',description='A Lowpoly version will be generated and used for the simulation',options=set(),default=False)
    bpy.types.Scene.earthquakex = bpy.props.BoolProperty(name='EarthquakeX',description='Shake the world along the X axis',options=set(),update=update_earthquakex,default=True)
    bpy.types.Scene.earthquakey = bpy.props.BoolProperty(name='EarthquakeY',description='Shake the world along the Y axis',options=set(),update=update_earthquakey,default=True)
    bpy.types.Scene.earthquakez = bpy.props.BoolProperty(name='EarthquakeZ',description='Shake the world along the Z axis',options=set(),update=update_earthquakez,default=True)
    bpy.types.Scene.useproxy = bpy.props.BoolProperty(name='UseProxy',description='A Lowpoly version will be generated and used for the simulation',options=set(),default=False)
    bpy.types.Scene.w_startframe = bpy.props.IntProperty(name='W_StartFrame',description='Set the Start Frame of the Simulation',subtype='NONE',options=set(),default=1,min=1)
    bpy.types.Scene.a_voxelsize = bpy.props.FloatProperty(name='A_VoxelSize',description='Set the size of Voxels uns in remeshing, which will be used for optimization. A Voxel Size of 0 will disable the remeshing',subtype='NONE',unit='NONE',options=set(),precision=2, default=0.05000000074505806,min=0.0)
    bpy.types.Scene.a_decimaterate = bpy.props.FloatProperty(name='A_DecimateRate',description='Set the decimation rate which will be used for optimization',subtype='NONE',unit='NONE',options=set(),precision=2, default=0.10000000149011612,min=0.0,max=1.0)
    bpy.types.Scene.p_optimizehighpoly = bpy.props.BoolProperty(name='P_OptimizeHighPoly',description='A Lowpoly version will be generated and used for the simulation',options=set(),default=False)
    bpy.types.Scene.p_voxelsize = bpy.props.FloatProperty(name='P_VoxelSize',description='Set the size of Voxels uns in remeshing, which will be used for optimization. A Voxel Size of 0 will disable the remeshing',subtype='NONE',unit='NONE',options=set(),precision=2, default=0.0,min=0.0)
    bpy.types.Scene.p_decimaterate = bpy.props.FloatProperty(name='P_DecimateRate',description='Set the decimation rate which will be used for optimization',subtype='NONE',unit='NONE',options=set(),precision=2, default=0.10000000149011612,min=0.0,max=1.0)
    bpy.types.Scene.bool_below293 = bpy.props.BoolProperty(name='Bool_Below293',description='',options=set(),default=False)

def sn_unregister_properties():
    del bpy.types.Scene.a_shape
    del bpy.types.Scene.a_friction
    del bpy.types.Scene.a_bunciness
    del bpy.types.Scene.a_margin
    del bpy.types.Scene.a_tra_damp
    del bpy.types.Scene.a_rot_damp
    del bpy.types.Scene.p_shape
    del bpy.types.Scene.p_friction
    del bpy.types.Scene.p_bunciness
    del bpy.types.Scene.p_margin
    del bpy.types.Scene.w_endframe
    del bpy.types.Scene.w_split_impulse
    del bpy.types.Scene.w_subframes
    del bpy.types.Scene.w_solver_iterations
    del bpy.types.Scene.is_rigid
    del bpy.types.Scene.a_mass
    del bpy.types.Scene.c_a_presets
    del bpy.types.Scene.c_p_damping
    del bpy.types.Scene.c_p_thick_outer
    del bpy.types.Scene.c_p_thick_inner
    del bpy.types.Scene.c_p_friction
    del bpy.types.Scene.ca_qualitysteps
    del bpy.types.Scene.ca_mass
    del bpy.types.Scene.ca_air_viscosity
    del bpy.types.Scene.ca_stiff_tension
    del bpy.types.Scene.ca_stiff_compression
    del bpy.types.Scene.ca_stiff_shear
    del bpy.types.Scene.ca_stiff_bending
    del bpy.types.Scene.ca_damp_tension
    del bpy.types.Scene.ca_damp_compression
    del bpy.types.Scene.ca_damp_shear
    del bpy.types.Scene.ca_damp_bending
    del bpy.types.Scene.ca_internalsprings
    del bpy.types.Scene.ca_internalspringmaxlength
    del bpy.types.Scene.ca_internalspringmaxdevision
    del bpy.types.Scene.ca_internalspringtension
    del bpy.types.Scene.ca_internalspringcompression
    del bpy.types.Scene.ca_internalspringmaxtension
    del bpy.types.Scene.ca_internalspringmaxcompression
    del bpy.types.Scene.ca_usepressure
    del bpy.types.Scene.ca_pressure
    del bpy.types.Scene.ca_pressurescale
    del bpy.types.Scene.ca_pressurefluiddensity
    del bpy.types.Scene.ca_quality
    del bpy.types.Scene.ca_minimumdistance
    del bpy.types.Scene.ca_impulseclamping
    del bpy.types.Scene.ca_selfcollision
    del bpy.types.Scene.ca_selfcollisionfriction
    del bpy.types.Scene.ca_selfcollisiondistance
    del bpy.types.Scene.ca_selfcollisionimpulseclamping
    del bpy.types.Scene.dropped
    del bpy.types.Scene.earthquake
    del bpy.types.Scene.optimizehighpoly
    del bpy.types.Scene.earthquakex
    del bpy.types.Scene.earthquakey
    del bpy.types.Scene.earthquakez
    del bpy.types.Scene.useproxy
    del bpy.types.Scene.w_startframe
    del bpy.types.Scene.a_voxelsize
    del bpy.types.Scene.a_decimaterate
    del bpy.types.Scene.p_optimizehighpoly
    del bpy.types.Scene.p_voxelsize
    del bpy.types.Scene.p_decimaterate
    del bpy.types.Scene.bool_below293


###############   REGISTER ADDON
def register():
    sn_register_icons()
    sn_register_properties()
    bpy.utils.register_class(SNA_OT_Pausesim)
    bpy.utils.register_class(SNA_OT_Setrigid)
    bpy.utils.register_class(SNA_OT_Setcloth)
    bpy.utils.register_class(SNA_OT_Dupliapply)
    bpy.utils.register_class(SNA_OT_Test)
    bpy.app.handlers.undo_pre.append(undo_pre_handler_7C101)
    bpy.utils.register_class(SNA_OT_Drop)
    bpy.utils.register_class(SNA_AddonPreferences_E5569)
    register_key_4814A()
    register_key_4A4D6()
    bpy.utils.register_class(SNA_OT_Simpleforce)
    bpy.utils.register_class(SNA_OT_Apply)
    bpy.utils.register_class(SNA_OT_Reset)
    bpy.utils.register_class(SNA_PT_Physics_Dropper_4B116)
    bpy.utils.register_class(SNA_OT_Paypal)
    bpy.utils.register_class(SNA_OT_Bymecoffee)
    bpy.utils.register_class(SNA_OT_Donate)
    bpy.utils.register_class(SNA_PT_Active_Settings_1C85D)
    bpy.utils.register_class(SNA_PT_Word_Settings_65161)
    bpy.utils.register_class(SNA_PT_Passive_Settings_76F70)
    bpy.utils.register_class(SNA_PT_Damping_C3699)
    bpy.utils.register_class(SNA_PT_Pressure_FF804)
    bpy.utils.register_class(SNA_PT_Self_Collision_4C94E)
    bpy.utils.register_class(SNA_PT_Stiffness_C0453)
    bpy.utils.register_class(SNA_PT_Advanced_Cloth_Settings_88CBB)
    bpy.utils.register_class(SNA_PT_Internal_Spring_25135)
    bpy.utils.register_class(SNA_PT_World_Collision_Settings_6B7B3)


###############   UNREGISTER ADDON
def unregister():
    sn_unregister_icons()
    sn_unregister_properties()
    bpy.utils.unregister_class(SNA_PT_World_Collision_Settings_6B7B3)
    bpy.utils.unregister_class(SNA_PT_Internal_Spring_25135)
    bpy.utils.unregister_class(SNA_PT_Advanced_Cloth_Settings_88CBB)
    bpy.utils.unregister_class(SNA_PT_Stiffness_C0453)
    bpy.utils.unregister_class(SNA_PT_Self_Collision_4C94E)
    bpy.utils.unregister_class(SNA_PT_Pressure_FF804)
    bpy.utils.unregister_class(SNA_PT_Damping_C3699)
    bpy.utils.unregister_class(SNA_PT_Passive_Settings_76F70)
    bpy.utils.unregister_class(SNA_PT_Word_Settings_65161)
    bpy.utils.unregister_class(SNA_PT_Active_Settings_1C85D)
    bpy.utils.unregister_class(SNA_OT_Donate)
    bpy.utils.unregister_class(SNA_OT_Bymecoffee)
    bpy.utils.unregister_class(SNA_OT_Paypal)
    bpy.utils.unregister_class(SNA_PT_Physics_Dropper_4B116)
    bpy.utils.unregister_class(SNA_OT_Reset)
    bpy.utils.unregister_class(SNA_OT_Apply)
    bpy.utils.unregister_class(SNA_OT_Simpleforce)
    for key in addon_keymaps:
        km, kmi = addon_keymaps[key]
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()
    bpy.utils.unregister_class(SNA_AddonPreferences_E5569)
    bpy.utils.unregister_class(SNA_OT_Drop)
    bpy.app.handlers.undo_pre.remove(undo_pre_handler_7C101)
    bpy.utils.unregister_class(SNA_OT_Test)
    bpy.utils.unregister_class(SNA_OT_Dupliapply)
    bpy.utils.unregister_class(SNA_OT_Setcloth)
    bpy.utils.unregister_class(SNA_OT_Setrigid)
    bpy.utils.unregister_class(SNA_OT_Pausesim)