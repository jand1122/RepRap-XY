import os
import FreeCAD
import Part
import Mesh

def ConvertToStepAndStl(path,name,tess=0.0):
	input = path + "/src/" + name + ".FCStd"
	stl = path + "/stl/" + name + ".stl"
	step = path + "/step/" + name + ".step"
	print("Input = " + input)	
	doc = FreeCAD.openDocument(input);
	s = doc.ActiveObject.Shape
	s.exportStep(step)
	print("tess = " + str(tess))
	if tess == 0.0:
		s.exportStl(stl)
	else:
		m=Mesh.Mesh()
		m.addFacets(s.tessellate(tess))
		m.write(stl)
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
		if not f.startswith("RepRap-XY"):
			files.append(f[:-6])

	
#
# Convert all FreeCAD files to STEP and STL files
#
for f in files:
	print "ConvertToStepAndStl(" + path + "," + f + ")"	
	if not f.startswith("washer-M4"):
		ConvertToStepAndStl(path,f)

#
# A few parts needs a mirrored variant
# These files are not drawn in FreeCAD but generated here
# STEP files and STL files are generated
#
PartNames = [ "belt-clamp",
			 "idler-block",
			 "idler-block-top",
			 "motor-block",
			 "motor-block-top",
			 "Z-motor-mount", 
			 "Z-block-1"  ]
for name in PartNames:
	print "MirrorPart(" + path + "," + name + ")"	
	MirrorPart(path,name)
