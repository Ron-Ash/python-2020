import pandas as pd
import numpy as np
import xlwt 
from xlwt import Workbook 


TestingMultiplying = np.array([1, 2, 3, 4, 5])

OGdoc_excel = pd.read_excel(r'D:\2019-2020\CBA.AX.xlsx')
DataOriginal=OGdoc_excel['Money'].values.tolist()
Orders=OGdoc_excel['Count'].values.tolist()
# np.reshape(OGdoc_excel['No'].values.tolist(), (len(OGdoc_excel['No'].values.tolist()), 1))

Test = np.array(np.random.choice(Orders, 50, replace=False))
Orders = list(filter(lambda x: x not in Test, Orders))
Validation = np.array(np.random.choice(Orders, 100, replace=False))
Train = np.array(list(filter(lambda x: x not in Validation, Orders)))

X_Train = []
Y_Train = []

#TestingLists
# print(len(list(filter(lambda x: x not in Test, Orders))))
# print(len(list(filter(lambda x: x not in Validation, Orders))))
# print(len(list(filter(lambda x: x not in Test, Validation))))



# print(X_Train, T_X_Train)
for i in range(len(Test)):
    Y_Train.append(DataOriginal[Test[i]-1])

power = int(input('power?'))
for i in range(power):
    X_Train.append((Test**i).tolist())
X_Train = np.asmatrix(X_Train)
Y_Train = np.asmatrix(Y_Train).transpose()
T_X_Train = X_Train.transpose()

print(X_Train)
print(Y_Train)
# print(T_X_Train)

w = ((X_Train * T_X_Train)**(-1))*X_Train*Y_Train
print(w)

predictedY = T_X_Train*w
# print(predictedY)

Error = np.asmatrix((np.asarray(Y_Train-predictedY)**2).tolist())
print(sum(Error))