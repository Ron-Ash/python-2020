import matplotlib.pyplot as plt
import numpy as np
import PIL as pl
import pyaudio
import time
import cv2

# worked pretty well on the field at exposure = 2, gate = 2

def Measure(timeLightning, timeThunder):
    light = 299792458 
    sound = 343
    delayTime = timeThunder-timeLightning

    RealDistance = (light*sound*delayTime)/(light-sound)

    #check
    timeBefore = ((sound/light)*delayTime)/(1-(sound/light))
    distanceLight = light*timeBefore
    distanceSound = sound*(timeBefore+delayTime)
    error = 2 * RealDistance - (distanceLight + distanceSound)  

    return (RealDistance, error)

def Sensors():
    i = 0
    CHUNK = 2**10
    RATE = 44100
    peak = []
    count = []
    brightArray = ['brightness']
    exposure = -5
    brightGate = 2
    loudGate = 250
    timeLightning = 0
    timeThunder = 0
    isLightning = False
    isThunder = False
    pa=pyaudio.PyAudio()
    stream=pa.open(format=pyaudio.paInt16,channels=1,rate=RATE,input=True,frames_per_buffer=CHUNK)
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_AUTO_EXPOSURE, 0)
    cap.set(cv2.CAP_PROP_EXPOSURE, exposure)
    while(True):
        count.append(i)

        i += 1

        # Capture frame-by-frame
        ret, frame = cap.read()
        data = np.fromstring(stream.read(CHUNK),dtype=np.int16)
        peak.append(np.average(np.abs(data)))

        brightArray.append(frame.mean())

        if(len(brightArray)>2 and isLightning == False):
            if((brightArray[i]/brightArray[i-1])>brightGate):
                timeLightning = time.time()
                print('LIGHTNING: ', time.time())
                isLightning = True
        
        if(len(peak)>2):
            if((peak[i-1] - peak[i-2])>loudGate):
                timeThunder = time.time()
                print('THUNDER: ',time.time())
                isThunder = True
                if(isLightning == True and isThunder == True):
                    distance, error = Measure(timeLightning, timeThunder)
                    print(f"THE LIGHTNING STRIKE IS {distance}m AWAY\n---error in measurement is: {error}---")
                    isLightning = False
                    isThunder = False


        cv2.imshow('frame',cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY))
        plt.plot(count, peak, color = 'blue')
        plt.plot(count, brightArray[1:], color = 'red')
        plt.pause(0.00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000005)

        if (cv2.waitKey(1) & 0xFF == ord('q')):
            cap.release()
            cv2.destroyAllWindows
            stream.close()
            pa.terminate()

Sensors()