import webbrowser
import time
#for x in range(0, 3):

totle_breaks = 3
break_count = 0
print("This program startd ")
while(break_count < totle_breaks):
    time.sleep(10)
    webbrowser.open("http://www.baidu.com")
    break_count = break_count + 1
