import os, sys

for _root,_dir,files in os.walk("."):
	for f in files:
		if "jpeg" in f:
			os.rename(f,f.replace("jpeg","jpg"))
