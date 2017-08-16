import os, sys, re, random
import subprocess
from shutil import copyfile

inFile = sys.argv[1]

file = open(inFile,"r")
rand = file.readlines()


#l = sys.argv[1]
#lowTolerance = float(l)
#h = sys.argv[2]
#highTolerance = float(h) 

def getSubject(fileName):
        return fileName.split("-")[1]

def analyzeRun(enrolledImg, res):
	trueSubject = getSubject(enrolledImg)

	runStats = {'enrolled': enrolledImg, 'fP': 0, 'tP': 0, 'fN': 0, 'tN':0}

	for r in res.splitlines():
		if "unknown" in r:
			#print(r)
			#this image was not detected
			
			testSubject = getSubject(r)
			if testSubject==trueSubject:
				runStats['fN'] = runStats['fN']+1
			else:
				runStats['tN'] = runStats['tN']+1

		if "enrolled" in r:
			testSubject = getSubject(r)
			if testSubject==trueSubject:
				runStats['tP'] = runStats['tP']+1
			else:
				runStats['fP'] = runStats['fP']+1
				#print("Found: " + trueSubject + " in "+ r.split(",")[0] +  ". Actual subject was: " + testSubject + ". Tuple|" + trueSubject +"|" + testSubject  )
	
	#print(runStats)
	return runStats



def runDetection(enrolledImg,t):
	tString = "-- " + str(t)
	print("RUNNING AGAINST: " + enrolledImg + tString)
	#print(tString)
	proc = subprocess.Popen(['face_recognition', 'known/',  'all/', '--tolerance', str(t)], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

	res = proc.communicate()[0].decode("utf-8")
	return analyzeRun(enrolledImg,res)

def updateGlobalStats(g,r):
	g['tP'] = g['tP'] + r['tP']
	g['tN'] = g['tN'] + r['tN']
	g['fP'] = g['fP'] + r['fP']
	g['fN'] = g['fN'] + r['fN']


# Begin my running all against empty. Look for WARNING
# Split lines, identify the file name and move the image to noID folder
proc = subprocess.Popen(['face_recognition', 'all/',  'empty/'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
res = proc.communicate()[0].decode("utf-8")
for line in res.splitlines():
	if "WARNING" in line:
		msg = line.split(" ")
		noIdFile = msg[-3][:-1]
		print("Moving: " + noIdFile)
		os.rename(noIdFile,"noFaceDetected/"+noIdFile)

globalStats = {'fP': 0, 'tP': 0, 'fN': 0, 'tN':0}


def clearStats(d):
	for key in d:
		d[key] = 0

#for root,dirs,files in os.walk("all/"):
#for tol in range(0,100):
for tol in range(45,46):
	t = tol/100
	t = str(t)
	#f = str(int(rand[tol]))
	f = rand[tol].rstrip()
	for _root,_dirs,files in os.walk("mod/"):
		for file in files:
			if "jp" in file:
				s= file.split("-")
				if f == s[1]:
					f = "-".join(s)
					break
	print(f)	
	enrolledImg = f 
	copyfile(os.path.join("mod/",f),"known/enrolled.jpg")
	runRes = runDetection(f,t)
	updateGlobalStats(globalStats,runRes)
	print("Tol: " + t + " | " + str(globalStats))
	clearStats(globalStats)
