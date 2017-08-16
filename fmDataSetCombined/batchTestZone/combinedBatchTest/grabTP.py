import os, sys, re

fname = sys.argv[1]
F = open(fname,"r")

fp = []
tp =[]
fn = []
tn = []

for line in F.readlines():
	if "Tol" in line:
		#print(line.split(" ")) 
		l = line.split(":")[2:]
		d = []
		index = 0
		for i in l:
			i = re.sub('[^0-9]', '', i)
			d.append(int(i))
		#print(lineData)
		fp.append(d[0])
		tp.append(d[1])
		fn.append(d[2])
		tn.append(d[3])

print(tp)	
