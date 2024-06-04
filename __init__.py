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

bl_info = {
    "name": "Mixamo Rig for Blender 4.0",
    "author": "Mixamo - Xin/obhi-d",
    "version": (1, 0, 6),
    "blender": (4, 0, 0),
    "location": "3D View > Mixamo> Control Rig",
    "description": "Generate a control rig from the selected Mixamo Fbx skeleton",
    "category": "Animation",
    "doc_url": "https://github.com/obhi-d/mixamo_ctrl_rig_ex.git",
    "tracker_url": "https://github.com/obhi-d/mixamo_ctrl_rig_ex.git"
}

from . import auto_load

auto_load.init()

def register():
    auto_load.register()

def unregister():
    auto_load.unregister()
