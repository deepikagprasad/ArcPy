import arcpy, os
from arcpy import env
from arcpy.sa import *

arcpy.env.workspace = r"C:/Users/12147/Documents/Resample/20190313PEP"

for files in arcpy.ListFiles("*.jp2"):
	arcpy.Resample_management(files, files + "_re.jp2", "10", "NEAREST")
