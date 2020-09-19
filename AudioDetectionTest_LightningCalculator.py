import pyaudio
import numpy as np
import matplotlib.pyplot as plt

CHUNK = 2**10
RATE = 44100
i = 0
pa=pyaudio.PyAudio()
stream=pa.open(format=pyaudio.paInt16,channels=1,rate=RATE,input=True,
              frames_per_buffer=CHUNK)

peak = []
count = []

while(True):
    count.append(i)
    i += 1

    data = np.fromstring(stream.read(CHUNK),dtype=np.int16)
    peak.append(np.average(np.abs(data)))
    

    plt.plot(count, peak, color = 'blue')
    plt.pause(0.00000000000000000000000000000000000000000000000000000000000000000005)
plt.show()
stream.stop_stream()
stream.close()
pa.terminate()