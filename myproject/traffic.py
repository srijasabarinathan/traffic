import time

signal1=["Red","Yellow","Green"]
signal2=["Red","Yellow","Green"]
signal3=["Red","Yellow","Green"]
signal4=["Red","Yellow","Green"]
#trafff
man=int(input())
aut=int(input())
#comment
def manual(direction):
    while true:
        direct=direction[int(input())]
        if direct == "East":
            print("sig1",signal1[2])
            print("oth1",signal2[0],signal3[0],signal4[0])
            time.slee(2)
            continue
        if direct=="West":
            print("sig2",signal2[2])
            print("oth2",signal1[0],signal3[0],signal4[0])
            time.slee(2)
            continue
        if direct=="North":
            print("sig3",signal3[2])
            print("oth3",signal2[0],signal1[0],signal4[0])
            time.slee(2)
            continue
        if direct=="South":
            print("sig4",signal4[2])
            print("oth4",signal2[0],signal3[0],signal1[0])
            time.slee(2)
            continue

if man ==0 and aut==1:
    aut(["East","West","North","South"])

if man==1 and aut==0:
    man(["East","West","North","South"])
