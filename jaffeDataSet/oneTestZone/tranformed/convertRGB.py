import os, sys, re
from PIL import Image

for _root,_dir,files in os.walk("."):
	for f in files:
		if "jp" in f:
			Image.open(f).convert('RGB').save(f)
