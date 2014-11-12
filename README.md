This is the first release of a RepRap-XY 3D printer. It is based on the excellent design of Zelogik. See his github archive at:  https://github.com/zelogik/AluXY

His design and my variant are discussed in the RepRap forum at:: http://forums.reprap.org/read.php?4,297740

When I saw this printer I thought, this is the printer I want. It has all the features I want in a printer:

- Based on the Core-XY system. (see http://corexy.com/theory.html)
- Frame made from aluminium extrusions.
- No motors, belts and guides on the outside of the frame.

It only has one problem for me, it is made from CNC-ed aluminium and I do not have access to a CNC machine.
I decided to build a printer based on this design, but use printed parts instead of aluminium parts. That is what you will find here.

This is a work in progress, Use at your own risk.

I made one and it is working just fine.
I did not yet make something for the X and Y endstops.
A simple adjustable Z endstop exists and does the job for adjusting the first layer height.

The file src/RepRap-XY.FCStd is the complete assembly in FreeCAD format.
The file src/RepRap-XY.vc3 is the complete assembly in VIACAD format.

The file build.py will mirror a few parts and generate the STEP and STL files.
Just open the file in FreeCAD and run a a macro.

In the doc folder you will find a BOM. This BOM is not generated from the model but hand made, so be carefull
You will not (yet?) find build instructions there.  Have a look at the sourcefile RepRap-XY.FCStd (FreeCAD) and RepRap-XY.vc3 to see how everything fits together.

To see some videos of my printer have a look at my youtube channel: https://www.youtube.com/channel/UCOyTdQOCCLdy45FtSlam_3A/feed
and some images at my imgur album: http://jand1122.imgur.com/


Have fun. 
