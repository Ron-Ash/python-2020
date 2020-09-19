import matplotlib.pyplot as plt
import pyaudio
import numpy as np
import time
import xlwt 
from xlwt import Workbook
import pandas as pd 




CHUNK = 2**13
RATE = 44100
peak = []
count = []

pa=pyaudio.PyAudio()
stream=pa.open(format=pyaudio.paInt16,channels=1,rate=RATE,input=True,frames_per_buffer=CHUNK)

x = True
totalData = []
flattenData = []
repeats = []

for w in range(100):
    totalData = []
    flattenData = []
    print("recording...ON", w+1)
    for i in range(5):
        data = np.fromstring(stream.read(CHUNK),dtype=np.int16)
        print(len(data))
        totalData.append(data[::])
    print("recording...OFF")

    for i in range(len(totalData)):
        for j in range(len(totalData[0])):
            flattenData.append(totalData[i][j])

    repeats.append(flattenData[::])
    time.sleep(2)

pa.close(stream)

noiceReduced = []

for i in range(len(repeats)):
    subNoiceReduced = []
    for j in range(len(repeats[0])):
        if repeats[i][j] > 150:
            subNoiceReduced.append(repeats[i][j])
        else:
            subNoiceReduced.append(0)

    noiceReduced.append(subNoiceReduced)

ReducedData = []

for j in range(len(noiceReduced)):
    subReduced = []
    for i in range(int(len(noiceReduced[0])/160)):
        subReduced.append(np.average(noiceReduced[j][i*160:i*160+160]))
    ReducedData.append(subReduced)

for i in range(len(ReducedData[0])):
    count.append(i)


wb = Workbook() 
sheet1 = wb.add_sheet('Sheet 1', cell_overwrite_ok=True) 
for i in range(len(ReducedData)):
    for j in range(len(ReducedData[0])-1):
        sheet1.write(i, j, int(ReducedData[i][j]))

wb.save("1_2.xls")


print(len(ReducedData[0]))


for i in range(len(ReducedData)):
    plt.plot(count, ReducedData[i], color = 'red', alpha = 0.333)
plt.show()


