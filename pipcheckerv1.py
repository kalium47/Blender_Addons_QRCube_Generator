bl_info = {
    "name": "PipChecker",
    "author": "Kevin Yang <zcwakya@ucl.ac.uk>",
    "version": (1, 0),
    "description": "A auto pip checker / Library installer",
    "blender" : (2, 92, 0)
    }


import bpy
import os
import sys
import subprocess

from bpy.props import (StringProperty,
                       BoolProperty,
                       IntProperty,
                       FloatProperty,
                       FloatVectorProperty,
                       EnumProperty,
                       PointerProperty,
                       )

from bpy.types import (Panel,
                       Menu,
                       Operator,
                       PropertyGroup,
                       )
from pathlib import (Path)


class MyProperties(PropertyGroup):


    my_string1: StringProperty(
        name="",
        description=":",
        default="",
        maxlen=14, #Maxlength of string is dependend on the 21x21 size of module 1 type QR code (stores up to 14 binaries)
        )



class WM_OT_PipChecker(Operator):
    bl_label = "(1) PipCheck"
    bl_idname = "wm.pip_check"
    bl_context = "object"

    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool

        # path to python.exe
        python_exe = os.path.join(sys.prefix, 'bin', 'python.exe')

        # upgrade pip
        subprocess.call([python_exe, "-m", "ensurepip"])
        subprocess.call([python_exe, "-m", "pip", "install", "--upgrade", "pip"])

        # install required packages
        subprocess.call([python_exe, "-m", "pip", "install", "Pillow"])
        subprocess.call([python_exe, "-m", "pip", "install", "qrcode"])
        subprocess.call([python_exe, "-m", "pip", "install", "lxml"]) #used for output svg files


        print("Pip Check Complete")

        return {'FINISHED'}

class OBJECT_PT_PIPC(Panel):
        bl_label = "PipCheck"
        bl_idname = "OBJECT_PT_pip_checkc"
        bl_space_type = "VIEW_3D"
        bl_region_type = "UI"
        bl_category = "PipChecker"
        bl_context = "objectmode"


        @classmethod
        def poll(self,context):
          return context.object is not None

        def draw(self, context):
          layout = self.layout
          scene = context.scene
          mytool = scene.my_tool
          row = layout.row()


          row.label(text = "Follow the Operation Checklist", icon = 'HELP' )
          row = layout.row()
          row.label(text = "Toggle Console to see the progress", icon = 'EVENT_OS' )
          row = layout.row()
          row.label(text = "Window > Toggle System Console" )
          row = layout.row()
          row.label(text = "--------------------------------------" )
          row = layout.row()
          row.label(text = "Do PipCheck before Anything Else!", icon = 'ERROR' )
          row = layout.row()

          layout.operator("wm.pip_check")
          layout.separator()

classes = (MyProperties, OBJECT_PT_PIPC, WM_OT_PipChecker)

def register():
      from bpy.utils import register_class
      for cls in classes:
        register_class(cls)

        bpy.types.Scene.my_tool = PointerProperty(type=MyProperties)

def unregister():
      from bpy.utils import unregister_class
      for cls in reversed(classes):
        unregister_class(cls)
        del bpy.types.Scene.my_tool
