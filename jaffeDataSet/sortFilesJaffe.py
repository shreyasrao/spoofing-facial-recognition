import os, sys, re


neCount = 0
for root,dirs,files in os.walk("images"):
	for f in files:
		if "NE" in f:
			neCount += 1
			os.rename(os.path.join(root,f),"neutral/"+f)

print(neCount)

sCount = 0
for root,dirs,files in os.walk("images"):
        for f in files:
                if "HA" in f:
                        neCount += 1
                        os.rename(os.path.join(root,f),"smile/"+f)
print(sCount)

for root,dirs,files in os.walk("neutral"):
	for f in files:
		if "NE" not in f:
			continue
		ids = f.split(".")[:-2]
		subject = ids[0]
		num = ids[1].replace("NE","")
		prefix = "original"
		expression = "neutral"
		ext = ".jpeg"
		comb = prefix + subject + expression + num 
		newName = "-".join([prefix,subject,expression,num]) + ext
		#print(newName)
		os.rename(os.path.join(root,f),os.path.join(root,newName))


for root,dirs,files in os.walk("smile"):
        for f in files:
		if "HA" not in f:
			continue
                ids = f.split(".")[:-2]
                subject = ids[0]
                num = ids[1].replace("HA","")
                prefix = "original"
                expression = "smile"
                ext = ".jpeg"
                comb = prefix + subject + expression + num
                newName = "-".join([prefix,subject,expression,num]) + ext
                #print(newName)
                os.rename(os.path.join(root,f),os.path.join(root,newName))
