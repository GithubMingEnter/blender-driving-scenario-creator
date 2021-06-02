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

import bpy
from mathutils import Vector, Matrix

from math import pi

from .operator_snap_draw import DSC_OT_snap_draw
from . import helpers


class DSC_OT_object_car(DSC_OT_snap_draw, bpy.types.Operator):
    bl_idname = "dsc.object_car"
    bl_label = "Car"
    bl_description = "Place a car object"
    bl_options = {'REGISTER', 'UNDO'}

    object_type = 'car'

    def __init__(self):
        self.object_snapping = False

    @classmethod
    def poll(cls, context):
        return True

    def create_object_xodr(self, context):
        '''
            Create a car object
        '''
        valid, mesh, params = self.get_mesh_and_params(for_stencil=False)
        if not valid:
            return None
        else:
            obj_id = helpers.get_new_id_openscenario(context)
            mesh.name = self.object_type + '_' + str(obj_id)
            obj = bpy.data.objects.new(mesh.name, mesh)
            obj.location = self.point_start
            helpers.link_object_openscenario(context, obj)

            helpers.select_activate_object(context, obj)

        # Remember connecting points for snapping
        obj['cp_down'] = obj.location + obj.data.vertices[0].co
        obj['cp_left'] = obj.location + obj.data.vertices[2].co
        obj['cp_up'] = obj.location + obj.data.vertices[4].co
        obj['cp_right'] = obj.location + obj.data.vertices[6].co

        # Set OpenSCENARIO custom properties
        obj['id_xosc'] = obj_id
        obj['x'] = self.point_start.x
        obj['y'] = self.point_start.y
        obj['z'] = self.point_start.z
        obj['hdg'] = params['heading_start']

        return obj

    def get_mesh_and_params(self, for_stencil):
        '''
            Calculate and return the vertices, edges and faces to create a road mesh.
        '''
        if self.point_start == self.point_selected_end:
            self.report({"WARNING"}, "Start and end point can not be the same!")
            valid = False
            return valid, None, {}
        vector_start_end = self.point_selected_end - self.point_start
        heading = vector_start_end.to_2d().angle_signed(Vector((1.0, 0.0)))
        params = {'point_start': self.point_selected_end,
                  'heading_start': heading,
                  'point_end': self.point_selected_end}
        vertices = [(2.0, 1.0, 0.0),
                    (-2.0, 1.0, 0.0),
                    (-2.0, -1.0, 0.0),
                    (2.0, -1.0, 0.0),
                    (2.0, 1.0, 1.5),
                    (-2.0, 1.0, 1.5),
                    (-2.0, -1.0, 1.5),
                    (2.0, -1.0, 1.5),
                    ]
        edges = [[0, 1],[1, 2],[2, 3],[3, 0],[4, 5],[5, 6],[6, 7],[7, 4],[0, 4],[1, 5],[2, 6],[3, 7]]
        if for_stencil:
            faces = []
        else:
            faces = [[3, 2, 1, 0], [4, 5, 6, 7], [0, 1, 5, 4],[ 2, 3, 7, 6], [4, 7, 3, 0], [1, 2, 6, 5]]
        # Create blender mesh
        mesh = bpy.data.meshes.new('temp')
        mesh.from_pydata(vertices, edges, faces)
        # Rotate and translate mesh according to selected start point
        self.transform_mesh_wrt_start(mesh, self.point_start, heading, self.snapped_start)
        valid = True
        return valid, mesh, params
