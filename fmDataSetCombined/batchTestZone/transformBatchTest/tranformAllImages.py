import numpy
import os, sys, re

def find_coeffs(pa, pb):
    matrix = []
    for p1, p2 in zip(pa, pb):
        matrix.append([p1[0], p1[1], 1, 0, 0, 0, -p2[0]*p1[0], -p2[0]*p1[1]])
        matrix.append([0, 0, 0, p1[0], p1[1], 1, -p2[1]*p1[0], -p2[1]*p1[1]])

    A = numpy.matrix(matrix, dtype=numpy.float)
    B = numpy.array(pb).reshape(8)

    res = numpy.dot(numpy.linalg.inv(A.T * A) * A.T, B)
    return numpy.array(res).reshape(8)

import sys
from PIL import Image


coeffs = find_coeffs(
        [(0, 0), (256, 0), (256, 256), (0, 256)],
        [(0, 0), (256, 0), (296, 256), (-40, 256)])


for root,dirs,files in os.walk("."):
	for f in files:
		if "original" not in f:
			continue
		imgName = f
		img = Image.open(imgName)
		dest = f.replace("original","transform")
		
		width, height = img.size
		img.transform((width, height), Image.PERSPECTIVE, coeffs,Image.BICUBIC).save("all/"+dest)




#img = Image.open(sys.argv[1])
#img.transform((width, height), Image.PERSPECTIVE, coeffs,Image.BICUBIC).save(sys.argv[2])
