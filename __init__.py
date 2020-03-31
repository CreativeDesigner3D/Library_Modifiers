import bpy
import os
from .bp_lib import bp_utils
from . import modifier_library
from . import modifier_ops
from . import modifier_ui

bl_info = {
    "name": "Modifier Library",
    "author": "Andrew Peel",
    "version": (0, 0, 1),
    "blender": (2, 80, 0),
    "location": "Asset Library",
    "description": "Library that adds the ability to drop modifiers",
    "warning": "",
    "wiki_url": "",
    "category": "Asset Library",
}

LIBRARY_PATH = os.path.join(os.path.dirname(__file__),"library")
PANEL_ID = "MODIFIER_PT_library_settings"

def register():
    lib = bpy.context.window_manager.bp_lib.script_libraries.add()
    lib.name = "Modifiers"
    lib.library_path = LIBRARY_PATH
    lib.panel_id = PANEL_ID

    bp_utils.load_library_items_from_module(lib,modifier_library)

def unregister():
    for i, lib in enumerate(bpy.context.window_manager.bp_lib.script_libraries):
        if lib.name == "Modifiers":
            bpy.context.window_manager.bp_lib.script_libraries.remove(i)