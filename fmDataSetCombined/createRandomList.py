import os, sys, re, random

# n = sys.argv[1] #number of random choices

for i in range(0,100):
    f = random.choice(os.listdir("neutral"))
    while "jpg" not in f:
        f = random.choice(os.listdir("neutral"))
    print(f.split("-")[1])
