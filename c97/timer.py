import time 
from playsound import playsound

def timer(sec):
    while sec>0:
        min=int(sec/60)
        secs=int(sec%60)
        time=str(min)+":"+str(secs)
        print(time)
        sec=sec-1
    print("time up")
    playsound("/Users/rishi/OneDrive/Desktop/WhiteHAtJR/Python-WhiteHatjr/c97/mixkit-sound.wav")
    
timer(120)