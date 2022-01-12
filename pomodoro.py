import time
from playsound import playsound
#Pomodoro Timer, prompts 3 queries, the first two asks the work & rest time and the last asks how many cycles of the timer you want 
#soundfiles courtesy of some random thing I found online
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
      

def pomodoro(t1,t2,t3):
    for i in range(t3):
        countdown(t1)
        playsound('.\Alarm-Fast-High-Pitch-B1-www.fesliyanstudios.com-www.fesliyanstudios.com.mp3')
        print("rest time")
        countdown(t2)
        playsound('.\Alarm-Fast-High-Pitch-B1-www.fesliyanstudios.com-www.fesliyanstudios.com.mp3')
        print("back to work :(")
        
  
# input time in seconds
t1 = int(input("How long would you like to work?")) * 60
t2 = int(input("How long would you like to rest?")) * 60
t3 = int(input("How many cycles would you like to work?"))
  
# function call
pomodoro(t1,t2,t3)
