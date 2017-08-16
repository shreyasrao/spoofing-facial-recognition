import os, sys, re, random, subprocess
from random import randint
#inFile = sys.argv[1]

#file = open("../../randomSubjects.txt","r")
#rand = file.readlines()


#def randomNeutral():
#    swapImg = ""
#    swap = rand[randint(0, 99)].rstrip()
#    for root,_dirs,files in os.walk("neutralFaces/"):
#            for file in files:
#                if "jp" in file:
#                    s = file.split("-")
#                    if swap == s[1]:
#                        swapImg = "-".join(s)
#                        swapImg = os.path.join(root,swapImg)
#                        break
#    print(swapImg)
#    return swapImg   

def randomNeutral():
    f = random.choice(os.listdir("neutralFaces/"))
    while "jpg" not in f:
        f = random.choice(os.listdir("neutralFaces/"))
    return "neutralFaces/" + f    

#print(randomNeutral())
#n1 = randomNeutral()
#n2 = randomNeutral()
#n3 = randomNeutral()


for root,dirs,files in os.walk("smileFaces/"):
    for file in files:
        if "jp" in file:
            f = os.path.join(root,file)
            swapImg = randomNeutral()
            print(" for: " + f)
            sp = subprocess.Popen(['python3', 'mouthswap.py', f,  swapImg], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            sp.wait()
        print("Done with " + str(file))
#    subprocess.Popen(['python3', 'mouthswap.py', enrolledImg,  swapImg], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    
    #produce output.jpg file