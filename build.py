import os
import FreeCAD
import Part

def ConvertToStepAndStl(path,name):
	input = path + "/src/" + name + ".FCStd"
	stl = path + "/stl/" + name + ".stl"
	step = path + "/step/" + name + ".step"
	doc = FreeCAD.openDocument(input);
	doc.ActiveObject.Shape.exportStl(stl)
	doc.ActiveObject.Shape.exportStep(step)
	FreeCAD.closeDocument(doc.Name)


def MirrorPart(path, name):
	
	input = path + "/step/" + name + ".step"
	step = path + "/step/" + name + "-mirrored.step"
	stl = path + "/stl/" + name + "-mirrored.stl"

	print "Reading: " + input	
	s1 = Part.read(input)
	s2 = s1.mirror(FreeCAD.Base.Vector(0,0,0),FreeCAD.Base.Vector(0,0,1))
	s2.rotate(FreeCAD.Base.Vector(0,0,0),FreeCAD.Base.Vector(0,1,0),180)
	s2.exportStep(step)
	s2.exportStl(stl)


path=os.path.realpath(__file__)
path=os.path.dirname(path)

#
# find all FreeCAD source files
#
files = []
for f in os.listdir(path + "/src"):
	if f.lower().endswith(".fcstd"):
		if not f.startswith("core-XY"):
			files.append(f[:-6])
	
#
# Convert all FreeCAD files to STEP and STL files
#
for f in files:
	print "ConvertToStepAndStl(" + path + "," + f + ")"	
	ConvertToStepAndStl(path,f)

#
# A few parts needs a mirrored variant
# These files are not drawn in FreeCAD but generated here
# STEP files and STL files are generated
#
PartNames = [ "belt-clamp",
			 "idler-block", "idler-block-top",
			 "motor-block", "motor-block-top",
			 "Z-motor-mount", "Z-block"  ]
for name in PartNames:
	print "MirrorPart(" + path + "," + name + ")"	
	MirrorPart(path,name)
