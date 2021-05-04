bl_info = {
    "name": "QR Cube Generator v1",
    "author": "Kevin Yang <zcwakya@ucl.ac.uk>",
    "version": (1, 0),
    "description": "A blender addon to generate QR cube Sculptures",
    "blender" : (2, 92, 0)
    }


import bpy
import os
import sys
import subprocess
import qrcode #Do Check with pipchecker if Pillow and qrcode is installed
import qrcode.image.svg #same with this


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

# -------------------
#    Properties
# -------------------

class MyProperties(PropertyGroup):


    my_string1: StringProperty(
        name="",
        description=":",
        default="",
        maxlen=14, #Maxlength of string is dependend on the 21x21 size of module 1 type QR code (stores up to 14 binaries)
        )

    my_string2: StringProperty(
        name="",
        description=":",
        default="",
        maxlen=14,
        )

    my_string3: StringProperty(
        name="",
        description=":",
        default="",
        maxlen=14,
        )

    my_string4: StringProperty(
        name="",
        description=":",
        default="",
        maxlen=14,
        )

    my_string5: StringProperty(
        name="",
        description=":",
        default="",
        maxlen=14,
        )

    my_string6: StringProperty(
        name="",
        description=":",
        default="",
        maxlen=14,
        )
# ------------------
#    BPY Operators
# ------------------
class WM_OT_AddCube(Operator):
    bl_label = "(2) Add the Maincube"
    bl_idname = "wm.add_cube"
    bl_context = "object"

    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool

        cubetrue = bpy.data.collections.get('maincube') #bpy.data.collections is the data type path for collections

        if cubetrue:
            print("Main Cube Created already")

        else:
            print("Generating new Maincube")
            # create a new cube
            bpy.ops.mesh.primitive_cube_add(size=0.030)

            # newly created cube will be automatically selected
            maincube = bpy.context.selected_objects[0]
            #set new origin to center of obj mass
            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='BOUNDS')
            # change name
            maincube.name = "maincube"

            # change its location
            maincube.location = (0.0, 0.0, 0.0)

            print("Main Cube Created")

        return {'FINISHED'}

#class WM_OT_PipChecker(Operator):
#    bl_label = "(1) PipCheck"
#    bl_idname = "wm.pip_check"
#    bl_context = "object"
#
#    def execute(self, context):
#        scene = context.scene
#        mytool = scene.my_tool
#
        # path to python.exe
#        python_exe = os.path.join(sys.prefix, 'bin', 'python.exe')
#
#        # upgrade pip
#        subprocess.call([python_exe, "-m", "ensurepip"])
#        subprocess.call([python_exe, "-m", "pip", "install", "--upgrade", "pip"])
#
#        # install required packages
#        subprocess.call([python_exe, "-m", "pip", "install", "Pillow"])
#        subprocess.call([python_exe, "-m", "pip", "install", "qrcode"])
#        subprocess.call([python_exe, "-m", "pip", "install", "lxml"]) #used for output svg files


#        print("Pip Check Complete")

#        return {'FINISHED'}


class WM_OT_HelloWorld(Operator):
    bl_label = "(3) Generate QR Codes(.svg)"
    bl_idname = "wm.hello_world"
    bl_context = "object"

    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool

        # print the values to the console
        print("Ahoy o/")
        print("string1 value:", mytool.my_string1)
        print("string2 value:", mytool.my_string2)
        print("string3 value:", mytool.my_string3)
        print("string4 value:", mytool.my_string4)
        print("string5 value:", mytool.my_string5)
        print("string6 value:", mytool.my_string6)

        #The Magics svg qr code factry with lxml
        # -----------------------------------------------------------
        factory = qrcode.image.svg.SvgImage # Im using the basic factory method to get a connected svg

        imgsvg1 = qrcode.make(mytool.my_string1, image_factory=factory)
        imgsvg2 = qrcode.make(mytool.my_string2, image_factory=factory)
        imgsvg3 = qrcode.make(mytool.my_string3, image_factory=factory)
        imgsvg4 = qrcode.make(mytool.my_string4, image_factory=factory)
        imgsvg5 = qrcode.make(mytool.my_string5, image_factory=factory)
        imgsvg6 = qrcode.make(mytool.my_string6, image_factory=factory)

        imgsvg1.save('qrstorage/1.svg')
        print("1.svg Created")
        imgsvg2.save("qrstorage/2.svg")
        print("2.svg Created")
        imgsvg3.save("qrstorage/3.svg")
        print("3.svg Created")
        imgsvg4.save("qrstorage/4.svg")
        print("4.svg Created")
        imgsvg5.save("qrstorage/5.svg")
        print("5.svg Created")
        imgsvg6.save("qrstorage/6.svg")
        print("6.svg Created")

        # -----------------------------------------------------------



        return {'FINISHED'}

class WM_OT_Importer(Operator):
    bl_label = "(4) Import and Transform 3d Meshes"
    bl_idname = "wm.importer"
    bl_context = "object"

    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool

        # print the values to the console
        print("IMPORTTTTdaze!")

        #locate file path + checking if file exist
        fp1 = 'qrstorage/1.svg' #the file path !sanatized!
        fp2 = 'qrstorage/2.svg'
        fp3 = 'qrstorage/3.svg'
        fp4 = 'qrstorage/4.svg'
        fp5 = 'qrstorage/5.svg'
        fp6 = 'qrstorage/6.svg'

        #FP1
        if os.path.exists(fp1):
            #import file
            bpy.ops.import_curve.svg(filepath = fp1)
            print("FP1 Import Success")

            svgt1 = bpy.data.collections.get('1.svg') #bpy.data.collections is the data type path for collections

            #----------------------------------------------------------------------------------------------
            if svgt1:
                print("svgcollection1 found in scene")

                #To Clean up selections
                for obj in bpy.data.objects:
                    obj.select_set(False)

                bpy.context.view_layer.objects.active = bpy.data.objects['Curve']# **this label is only for testing, should change la **

                for obj in bpy.data.collections['1.svg'].all_objects:
                    obj.select_set(True)

                #Operator Functions (Convert to mesh + Join)
                bpy.ops.object.convert(target='MESH')
                bpy.ops.object.join()

                print("SVG1 Imported, Transformed to mesh and Joined!")

                #--------------------Extrued mesh----------------------
                bpy.ops.object.mode_set(mode='EDIT')# Go to edit mode, face selection mode and select all faces
                bpy.ops.mesh.select_mode(type='FACE')
                bpy.ops.mesh.select_all(action='SELECT')

                bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value":(0, 0, 0.0045)})

                bpy.ops.object.mode_set( mode = 'OBJECT' )

                print("SVG1 Curve Extruded!")
                #------------------------------------------------------

                bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='BOUNDS')#set origin to middle of mesh
                #bpy.ops.transform.transform(value=(0,0,0,0), orient_type='GLOBAL')#move mesh to GLOBAL 0,0,0 not working so far
                #bpy.ops.object.align(align_mode='OPT_1'),#align to scene 000 not working aswell

                #ffs the dumbest way works UwU im ded figuring this out for 2hrs
                bpy.context.object.location[0] = 0.0
                bpy.context.object.location[1] = -0.013
                bpy.context.object.location[2] = 0.0

                #Rotate
                bpy.context.object.rotation_euler[0] = 1.5708 #this number == 90 degrees



            else:
                print("svgcollection1 NOT found in scene")
            #----------------------------------------------------------------------------------------------

        else:
            print("FP1 file does not exist")

        #FP2
        if os.path.exists(fp2):
            #import file
            bpy.ops.import_curve.svg(filepath = fp2)
            print("FP2 Import Success")

            svgt2 = bpy.data.collections.get('2.svg') #bpy.data.collections is the data type path for collections

            #----------------------------------------------------------------------------------------------
            if svgt2:
                print("svgcollection2 found in scene")

                #To Clean up selections
                for obj in bpy.data.objects:
                    obj.select_set(False)

                bpy.context.view_layer.objects.active = bpy.data.objects['Curve.001']

                for obj in bpy.data.collections['2.svg'].all_objects:
                    obj.select_set(True)

                #Operator Functions (Convert to mesh + Join)
                bpy.ops.object.convert(target='MESH')
                bpy.ops.object.join()

                print("SVG2 Imported, Transformed to mesh and Joined!")

                #--------------------Extrued mesh----------------------
                bpy.ops.object.mode_set(mode='EDIT')# Go to edit mode, face selection mode and select all faces
                bpy.ops.mesh.select_mode(type='FACE')
                bpy.ops.mesh.select_all(action='SELECT')

                bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value":(0, 0, 0.0045)})

                bpy.ops.object.mode_set( mode = 'OBJECT' )

                print("SVG2 Curve Extruded!")
                #------------------------------------------------------

                bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='BOUNDS')

                bpy.context.object.location[0] = 0.013
                bpy.context.object.location[1] = 0.0
                bpy.context.object.location[2] = 0.0

                #Rotate
                bpy.context.object.rotation_euler[1] = 1.5708

            else:
                print("svgcollection2 NOT found in scene")
            #----------------------------------------------------------------------------------------------

        else:
            print("FP2 file does not exist")

        #FP3
        if os.path.exists(fp3):
            #import file
            bpy.ops.import_curve.svg(filepath = fp3)
            print("FP3 Import Success")

            svgt3 = bpy.data.collections.get('3.svg') #bpy.data.collections is the data type path for collections

            #----------------------------------------------------------------------------------------------
            if svgt3:
                print("svgcollection3 found in scene")

                #To Clean up selections
                for obj in bpy.data.objects:
                    obj.select_set(False)

                bpy.context.view_layer.objects.active = bpy.data.objects['Curve.002']

                for obj in bpy.data.collections['3.svg'].all_objects:
                    obj.select_set(True)

                #Operator Functions (Convert to mesh + Join)
                bpy.ops.object.convert(target='MESH')
                bpy.ops.object.join()

                print("SVG3 Imported, Transformed to mesh and Joined!")

                #--------------------Extrued mesh----------------------
                bpy.ops.object.mode_set(mode='EDIT')# Go to edit mode, face selection mode and select all faces
                bpy.ops.mesh.select_mode(type='FACE')
                bpy.ops.mesh.select_all(action='SELECT')

                bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value":(0, 0, 0.0045)})

                bpy.ops.object.mode_set( mode = 'OBJECT' )

                print("SVG3 Curve Extruded!")
                #------------------------------------------------------

                bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='BOUNDS')
                bpy.context.object.location[0] = 0.0
                bpy.context.object.location[1] = 0.0
                bpy.context.object.location[2] = 0.013

                #Rotate not needed for face 3 and 5
                #bpy.context.object.rotation_euler[0] = 1.5708


            else:
                print("svgcollection3 NOT found in scene")
            #----------------------------------------------------------------------------------------------

        else:
            print("FP3 file does not exist")

        #FP4
        if os.path.exists(fp4):
            #import file
            bpy.ops.import_curve.svg(filepath = fp4)
            print("FP4 Import Success")

            svgt4 = bpy.data.collections.get('4.svg') #bpy.data.collections is the data type path for collections

            #----------------------------------------------------------------------------------------------
            if svgt4:
                print("svgcollection4 found in scene")

                #To Clean up selections
                for obj in bpy.data.objects:
                    obj.select_set(False)

                bpy.context.view_layer.objects.active = bpy.data.objects['Curve.003']

                for obj in bpy.data.collections['4.svg'].all_objects:
                    obj.select_set(True)

                #Operator Functions (Convert to mesh + Join)
                bpy.ops.object.convert(target='MESH')
                bpy.ops.object.join()

                print("SVG4 Imported, Transformed to mesh and Joined!")

                #--------------------Extrued mesh----------------------
                bpy.ops.object.mode_set(mode='EDIT')# Go to edit mode, face selection mode and select all faces
                bpy.ops.mesh.select_mode(type='FACE')
                bpy.ops.mesh.select_all(action='SELECT')

                bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value":(0, 0, 0.0045)})

                bpy.ops.object.mode_set( mode = 'OBJECT' )

                print("SVG4 Curve Extruded!")
                #------------------------------------------------------

                bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='BOUNDS')
                bpy.context.object.location[0] = -0.013
                bpy.context.object.location[1] = 0.0
                bpy.context.object.location[2] = 0.0

                #Rotate
                bpy.context.object.rotation_euler[1] = -1.5708

            else:
                print("svgcollection4 NOT found in scene")
            #----------------------------------------------------------------------------------------------

        else:
            print("FP4 file does not exist")

        #FP5
        if os.path.exists(fp5):
            #import file
            bpy.ops.import_curve.svg(filepath = fp5)
            print("FP5 Import Success")

            svgt5 = bpy.data.collections.get('5.svg') #bpy.data.collections is the data type path for collections

            #----------------------------------------------------------------------------------------------
            if svgt5:
                print("svgcollection2 found in scene")

                #To Clean up selections
                for obj in bpy.data.objects:
                    obj.select_set(False)

                bpy.context.view_layer.objects.active = bpy.data.objects['Curve.004']

                for obj in bpy.data.collections['5.svg'].all_objects:
                    obj.select_set(True)

                #Operator Functions (Convert to mesh + Join)
                bpy.ops.object.convert(target='MESH')
                bpy.ops.object.join()

                print("SVG5 Imported, Transformed to mesh and Joined!")

                #--------------------Extrued mesh----------------------
                bpy.ops.object.mode_set(mode='EDIT')# Go to edit mode, face selection mode and select all faces
                bpy.ops.mesh.select_mode(type='FACE')
                bpy.ops.mesh.select_all(action='SELECT')

                bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value":(0, 0, 0.0045)})

                bpy.ops.object.mode_set( mode = 'OBJECT' )

                print("SVG5 Curve Extruded!")
                #------------------------------------------------------

                bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='BOUNDS')
                bpy.context.object.location[0] = 0.0
                bpy.context.object.location[1] = 0.0
                bpy.context.object.location[2] = -0.013

                #Rotate not needed for face 3 and 5
                #bpy.context.object.rotation_euler[0] = 1.5708

            else:
                print("svgcollection5 NOT found in scene")
            #----------------------------------------------------------------------------------------------

        else:
            print("FP5 file does not exist")

         #FP6
        if os.path.exists(fp6):
            #import file
            bpy.ops.import_curve.svg(filepath = fp6)
            print("FP6 Import Success")

            svgt6 = bpy.data.collections.get('6.svg') #bpy.data.collections is the data type path for collections

            #----------------------------------------------------------------------------------------------
            if svgt6:
                print("svgcollection6 found in scene")

                #To Clean up selections
                for obj in bpy.data.objects:
                    obj.select_set(False)

                bpy.context.view_layer.objects.active = bpy.data.objects['Curve.005']

                for obj in bpy.data.collections['6.svg'].all_objects:
                    obj.select_set(True)

                #Operator Functions (Convert to mesh + Join)
                bpy.ops.object.convert(target='MESH')
                bpy.ops.object.join()

                print("SVG6 Imported, Transformed to mesh and Joined!")

                #--------------------Extrued mesh----------------------
                bpy.ops.object.mode_set(mode='EDIT')# Go to edit mode, face selection mode and select all faces
                bpy.ops.mesh.select_mode(type='FACE')
                bpy.ops.mesh.select_all(action='SELECT')

                bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value":(0, 0, 0.0045)})

                bpy.ops.object.mode_set( mode = 'OBJECT' )

                print("SVG6 Curve Extruded!")
                #------------------------------------------------------

                bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='BOUNDS')
                bpy.context.object.location[0] = 0.0
                bpy.context.object.location[1] = 0.013
                bpy.context.object.location[2] = 0.0

                #Rotate not needed for face 3 and 5
                bpy.context.object.rotation_euler[0] = -1.5708

            else:
                print("svgcollection6 NOT found in scene")
            #----------------------------------------------------------------------------------------------

        else:
            print("FP6 file does not exist")

        return {'FINISHED'}


class WM_OT_BooleanMod(Operator):
    bl_label = "(5) Boolean Mod Apply"
    bl_idname = "wm.boolean_mod"
    bl_context = "object"

    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        context = bpy.context

        #For deselecting cleanup action
        cexist = scene.objects.get("maincube")

        if cexist:
            bpy.data.objects['Curve'].select_set(True)

        bpy.context.view_layer.objects.active = bpy.data.objects['maincube']

        #Boolean Function 1---------------------------------------------------
        boolcube = scene.objects.get("maincube")
        boolqrmesh = scene.objects.get("Curve")#Only Var

        if boolcube and boolqrmesh:
            bool = boolcube.modifiers.new(name='booltheqr', type='BOOLEAN')
            bool.object = boolqrmesh
            bool.operation = 'DIFFERENCE'
            bpy.context.object.modifiers["booltheqr"].use_self = True
            bpy.ops.object.modifier_apply(modifier='booltheqr', report=False)

            print("Boolean Modifier 1 Applyed")
        else:
            print("Maincube & Curve1 not found")
        #---------------------------------------------------------------------

        #Boolean Function 2---------------------------------------------------
        boolcube = scene.objects.get("maincube")
        boolqrmesh = scene.objects.get("Curve.001")#Only Var

        if boolcube and boolqrmesh:
            bool = boolcube.modifiers.new(name='booltheqr', type='BOOLEAN')
            bool.object = boolqrmesh
            bool.operation = 'DIFFERENCE'
            bpy.context.object.modifiers['booltheqr'].use_self = True
            bpy.ops.object.modifier_apply(modifier='booltheqr', report=False)

            print("Boolean Modifier 2 Applyed")
        else:
            print("Maincube & Curve2 not found")
        #---------------------------------------------------------------------

        #Boolean Function 3---------------------------------------------------
        boolcube = scene.objects.get("maincube")
        boolqrmesh = scene.objects.get("Curve.002")#Only Var

        if boolcube and boolqrmesh:
            bool = boolcube.modifiers.new(name='booltheqr', type='BOOLEAN')
            bool.object = boolqrmesh
            bool.operation = 'DIFFERENCE'
            bpy.context.object.modifiers['booltheqr'].use_self = True
            bpy.ops.object.modifier_apply(modifier='booltheqr', report=False)

            print("Boolean Modifier 3 Applyed")
        else:
            print("Maincube & Curve3 not found")
        #---------------------------------------------------------------------

        #Boolean Function 4---------------------------------------------------
        boolcube = scene.objects.get("maincube")
        boolqrmesh = scene.objects.get("Curve.003")#Only Var

        if boolcube and boolqrmesh:
            bool = boolcube.modifiers.new(name='booltheqr', type='BOOLEAN')
            bool.object = boolqrmesh
            bool.operation = 'DIFFERENCE'
            bpy.context.object.modifiers['booltheqr'].use_self = True
            bpy.ops.object.modifier_apply(modifier='booltheqr', report=False)

            print("Boolean Modifier 4 Applyed")
        else:
            print("Maincube & Curve4 not found")
        #---------------------------------------------------------------------

        #Boolean Function 5---------------------------------------------------
        boolcube = scene.objects.get("maincube")
        boolqrmesh = scene.objects.get("Curve.004")#Only Var

        if boolcube and boolqrmesh:
            bool = boolcube.modifiers.new(name='booltheqr', type='BOOLEAN')
            bool.object = boolqrmesh
            bool.operation = 'DIFFERENCE'
            bpy.context.object.modifiers['booltheqr'].use_self = True
            bpy.ops.object.modifier_apply(modifier='booltheqr', report=False)

            print("Boolean Modifier 5 Applyed")
        else:
            print("Maincube & Curve5 not found")
        #---------------------------------------------------------------------

        #Boolean Function 6---------------------------------------------------
        boolcube = scene.objects.get("maincube")
        boolqrmesh = scene.objects.get("Curve.005")#Only Var

        if boolcube and boolqrmesh:
            bool = boolcube.modifiers.new(name='booltheqr', type='BOOLEAN')
            bool.object = boolqrmesh
            bool.operation = 'DIFFERENCE'
            bpy.context.object.modifiers['booltheqr'].use_self = True
            bpy.ops.object.modifier_apply(modifier='booltheqr', report=False)

            print("Boolean Modifier 6 Applyed")
        else:
            print("Maincube & Curve6 not found")
        #---------------------------------------------------------------------


        # print the values to the console
        print("BooleanModApplydaze!")

        return {'FINISHED'}


class WM_OT_CleanUp(Operator):
    bl_label = "(6) CleanUp Scene for Output"
    bl_idname = "wm.cleanup"
    bl_context = "object"

    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool

        #collection delete
        collection1 = bpy.data.collections.get('1.svg')
        if collection1:
            bpy.data.collections.remove(collection1)

        collection2 = bpy.data.collections.get('2.svg')
        if collection2:
            bpy.data.collections.remove(collection2)

        collection3 = bpy.data.collections.get('3.svg')
        if collection3:
            bpy.data.collections.remove(collection3)

        collection4 = bpy.data.collections.get('4.svg')
        if collection4:
            bpy.data.collections.remove(collection4)

        collection5 = bpy.data.collections.get('5.svg')
        if collection5:
            bpy.data.collections.remove(collection5)

        collection6 = bpy.data.collections.get('6.svg')
        if collection6:
            bpy.data.collections.remove(collection6)

        #obj delete
        bpy.ops.object.select_all()

        mce = bpy.data.objects.get('maincube')
        if mce:
            bpy.data.objects['maincube'].select_set(False)

        bpy.ops.object.delete()




        # print the values to the console
        print("CleanUPdaze! Unwanted Mesh and Collections deleted!")

        return {'FINISHED'}


# -----------------
#    UI Panels
# -----------------
class OBJECT_PT_PIP(Panel):
    bl_label = "Spawn Maincube"
    bl_idname = "OBJECT_PT_pip_check"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "QRC Generator"
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
        row.label(text = "Do PipChecker before Anything Else!", icon = 'ERROR' )
        row = layout.row()



#        layout.operator("wm.pip_check")
        layout.operator("wm.add_cube")
        layout.separator()

class OBJECT_PT_QRMT(Panel):
    bl_label = "QRMessageTranslator"
    bl_idname = "OBJECT_PT_custom_panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "QRC Generator"
    bl_context = "objectmode"


    @classmethod
    def poll(self,context):
        return context.object is not None

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool
        row = layout.row()

        layout.prop(mytool, "my_string1")
        layout.prop(mytool, "my_string2")
        layout.prop(mytool, "my_string3")
        layout.prop(mytool, "my_string4")
        layout.prop(mytool, "my_string5")
        layout.prop(mytool, "my_string6")
        row = layout.row()
        row.label(text = "Be sure the file location are created", icon = 'FILEBROWSER' )
        row = layout.row()
        layout.operator("wm.hello_world")
        #layout.operator("wm.transformer")
        #layout.menu(OBJECT_MT_CustomMenu.bl_idname, text="Presets", icon="SCENE")
        layout.separator()

#class OBJECT_PT_FileImport(Panel):
#    bl_label = "QRFileImport"
#    bl_idname = "OBJECT_PT_file_import"
#    bl_space_type = "VIEW_3D"
#    bl_region_type = "UI"
#    bl_category = "Ahoy.V5"
#     bl_context = "objectmode"
#
#
#   @classmethod
#    def poll(self,context):
#        return context.object is not None

#    def draw(self, context):
#        layout = self.layout
#        scene = context.scene
#        mytool = scene.my_tool

#        layout.operator("wm.importer")
        #layout.menu(OBJECT_MT_CustomMenu.bl_idname, text="Presets", icon="SCENE")
 #       layout.separator()

class OBJECT_PT_QRCCreate(Panel):
    bl_label = "QRCCreate"
    bl_idname = "OBJECT_PT_qrc_create"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "QRC Generator"
    bl_context = "objectmode"


    @classmethod
    def poll(self,context):
        return context.object is not None

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        mytool = scene.my_tool

        layout.operator("wm.importer")
        layout.operator("wm.boolean_mod")
        layout.operator("wm.cleanup")

        #layout.menu(OBJECT_MT_CustomMenu.bl_idname, text="Presets", icon="SCENE")
        layout.separator()

# ----------------
#    Registration
# ----------------

classes = (
    MyProperties,
    WM_OT_AddCube,
    OBJECT_PT_PIP,
    WM_OT_HelloWorld,
    WM_OT_Importer,
    WM_OT_CleanUp,
    OBJECT_PT_QRMT,
    WM_OT_BooleanMod,
    OBJECT_PT_QRCCreate
)

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
