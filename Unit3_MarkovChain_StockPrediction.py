# IMPORTING TEH LAIBRARIES IN ORDER TO UTILISE MATRIX OPERATIONS
import pandas as pd
import numpy as np
import xlwt 
from xlwt import Workbook 

np.set_printoptions(linewidth= 200)
# SETTING VARIABLES TO KEEP CODE EASY TO REED AND MATRICES ORGINISED
Outcomes = [
    'HiHi','NiHi', 'LiHi', 'ZHi', 'LdHi', 'NdHi', 'HdHi',
    'HiNi','NiNi', 'LiNi', 'ZNi', 'LdNi', 'NdNi', 'HdNi',
    'HiLi','NiLi', 'LiLi', 'ZLi', 'LdLi', 'NdLi', 'HdLi',
     'HiZ', 'NiZ',  'LiZ',  'ZZ',  'LdZ',  'NdZ',  'HdZ',
    'HiLd','NiLd', 'LiLd', 'ZLd', 'LdLd', 'NdLd', 'HdLd',
    'HiNd','NiNd', 'LiNd', 'ZNd', 'LdNd', 'NdNd', 'HdNd',
    'HiHd','NiHd', 'LiHd', 'ZHd', 'LdHd', 'NdHd', 'HdHd', 
    ]

Jan, Feb, Mar, May, Apr, Jun, Jul, Aug, Sep, Oct, Nov, Dec = [], [], [], [], [], [], [], [], [], [], [], []
YearRawGeneralised = [Jan, Feb, Mar, May, Apr, Jun, Jul, Aug, Sep, Oct, Nov, Dec]

JanMarkov, FebMarkov, MarMarkov, MayMarkov, AprMarkov, JunMarkov, JulMarkov, AugMarkov, SepMarkov, OctMarkov, NovMarkov, DecMarkov = [[],[],[],[],[]], [[],[],[],[],[]], [[],[],[],[],[]], [[],[],[],[],[]], [[],[],[],[],[]], [[],[],[],[],[]], [[],[],[],[],[]], [[],[],[],[],[]], [[],[],[],[],[]], [[],[],[],[],[]], [[],[],[],[],[]], [[],[],[],[],[]]
YearMarkov = [JanMarkov, FebMarkov, MarMarkov, MayMarkov, AprMarkov, JunMarkov, JulMarkov, AugMarkov, SepMarkov, OctMarkov, NovMarkov, DecMarkov]

TransitionsNum = [[],[],[], [], []]

TransitionsProb = [[],[],[], [], []]

# FUNCTION TO RETRIEVE THE DATA FROM AN EXCEL SPREADSHEET AND ASSIGN EACH DATAPOINT TO A SPESIFIC MOVEMENT 
def SorttingTheData():
    
    OGdoc_excel = pd.read_excel (r'D:\2019-2020\CBA.AX.xlsx')
    DataOriginal=OGdoc_excel['Change'].values.tolist()
    DataMonths=OGdoc_excel['Month'].values.tolist()
    DataGeneralised = []

    for i in range(len(DataOriginal)):
        if DataOriginal[i] <= 0.99:
            DataGeneralised.append('Hd')
        elif DataOriginal[i] <= 0.999 and DataOriginal[i] > 0.99:
            DataGeneralised.append('Nd')
        elif DataOriginal[i] < 1 and DataOriginal[i] > 0.999:
            DataGeneralised.append('Ld')
        elif DataOriginal[i] == 1:
            DataGeneralised.append('Z')
        elif DataOriginal[i] < 1.001 and DataOriginal[i] > 1:
            DataGeneralised.append('Li')
        elif DataOriginal[i] < 1.01 and DataOriginal[i] >= 1.001:
            DataGeneralised.append('Ni')
        elif DataOriginal[i] >= 1.01:
            DataGeneralised.append('Hi')
        else:
            # IF AN ERROR OCCURS, PRINT THE VALUE WHICH CAUSED THE ERROR AND ITS POSITION IN TEH DATASET
            print(i,DataOriginal[i])

    # SPLIT THE TOTAL DATASET INTO THE MONTHLYBASED DATASETS
    for i in range(len(DataGeneralised)):
        if DataMonths[i] == 1:
            YearRawGeneralised[0].append(DataGeneralised[i])
        elif DataMonths[i] == 2:
            YearRawGeneralised[1].append(DataGeneralised[i])
        elif DataMonths[i] == 3:
            YearRawGeneralised[2].append(DataGeneralised[i])
        elif DataMonths[i] == 4:
            YearRawGeneralised[3].append(DataGeneralised[i])
        elif DataMonths[i] == 5:
            YearRawGeneralised[4].append(DataGeneralised[i])
        elif DataMonths[i] == 6:
            YearRawGeneralised[5].append(DataGeneralised[i])
        elif DataMonths[i] == 7:
            YearRawGeneralised[6].append(DataGeneralised[i])
        elif DataMonths[i] == 8:
            YearRawGeneralised[7].append(DataGeneralised[i])
        elif DataMonths[i] == 9:
            YearRawGeneralised[8].append(DataGeneralised[i])
        elif DataMonths[i] == 10:
            YearRawGeneralised[9].append(DataGeneralised[i])
        elif DataMonths[i] == 11:
            YearRawGeneralised[10].append(DataGeneralised[i])
        elif DataMonths[i] == 12:
            YearRawGeneralised[11].append(DataGeneralised[i])

    # ADD FOR EACH MONTHLY DATASET AN 'END' VARIABLE AT THE END FO THE LIST
    # THIS WILL INSURE THAT THE FOLLOWING CODE WILL RUN UNTIL THE END BY TELLING THE CODE ONLY TO STOP WHEN ENCOUTERING THE VARIABLE 'END' 
    for i in range(len(YearRawGeneralised)):
        YearRawGeneralised[i].append('END')

# WILL CREATE 5 DIFFERENT TRANSITION MATRICES FOR EACH MONTH, FOR INCREASINGLY LARGER DAY GAPS: 1, 2, 3, 4, 5
def SortingMarkovs():
    for x in range(len(JanMarkov)):
        for y in range(len(YearRawGeneralised)):
            GlueingTheData(x, y)

# CREATE A NEW ARRAY AND GLUEING A VALUE TO ITS FOLLOWING VALUE (DEPENDENT ON WHICH TRANSITION MATRIX IT IS FOR)           
def GlueingTheData(x, y):
    for z in range(len(YearRawGeneralised[y])):
                YearMarkov[y][x].append(YearRawGeneralised[y][z]+YearRawGeneralised[y][z+x+1])
                # WILL STOP THE PROCESS WHEN ENCOUNTERING THE VALUE 'END'
                if  YearRawGeneralised[y][z+x+2] == 'END':
                    break

# TEH FUNCTION THAT CREATES THE INITIAL TRANSITION MATRIX WHEN TEH COLUMNS HAVE NOT YET BEEN DIVIDED
def MarkovingTheGluedData():
    for i in range(len(TransitionsNum)):
        for n in range(12):
            MatrixV = YearMarkov[n][i]
            TransitionsNum[i].append(np.matrix(
                [[MatrixV.count(Outcomes[0]),MatrixV.count(Outcomes[1]),MatrixV.count(Outcomes[2]),MatrixV.count(Outcomes[3]),MatrixV.count(Outcomes[4]),MatrixV.count(Outcomes[5]),MatrixV.count(Outcomes[6])],[MatrixV.count(Outcomes[7]),MatrixV.count(Outcomes[8]),MatrixV.count(Outcomes[9]),MatrixV.count(Outcomes[10]),MatrixV.count(Outcomes[11]),MatrixV.count(Outcomes[12]),MatrixV.count(Outcomes[13])],[MatrixV.count(Outcomes[14]),MatrixV.count(Outcomes[15]),MatrixV.count(Outcomes[16]),MatrixV.count(Outcomes[17]),MatrixV.count(Outcomes[18]),MatrixV.count(Outcomes[19]),MatrixV.count(Outcomes[20])],[MatrixV.count(Outcomes[21]),MatrixV.count(Outcomes[22]),MatrixV.count(Outcomes[23]),MatrixV.count(Outcomes[24]),MatrixV.count(Outcomes[25]),MatrixV.count(Outcomes[26]),MatrixV.count(Outcomes[27])],[MatrixV.count(Outcomes[28]),MatrixV.count(Outcomes[29]),MatrixV.count(Outcomes[30]),MatrixV.count(Outcomes[31]),MatrixV.count(Outcomes[32]),MatrixV.count(Outcomes[33]),MatrixV.count(Outcomes[34])],[MatrixV.count(Outcomes[35]),MatrixV.count(Outcomes[36]),MatrixV.count(Outcomes[37]),MatrixV.count(Outcomes[38]),MatrixV.count(Outcomes[39]),MatrixV.count(Outcomes[40]),MatrixV.count(Outcomes[41])],[MatrixV.count(Outcomes[42]),MatrixV.count(Outcomes[43]),MatrixV.count(Outcomes[44]),MatrixV.count(Outcomes[45]),MatrixV.count(Outcomes[46]),MatrixV.count(Outcomes[47]),MatrixV.count(Outcomes[48])]]))

# TEH FUNCTION THAT DIVIDEDS TEH COLUMN BY ITS SUM
def get_row(skippingdistance, matrixIndex, rowIndex):
  row = TransitionsNum[skippingdistance][matrixIndex][:,rowIndex]
  sum = np.sum(TransitionsNum[skippingdistance][matrixIndex][:,rowIndex])
  if sum == 0:
    return row 
  else:
    return row/sum

# THE FUNCTION THAT CREATES THE FINAL TRANSITION MATRIX
def Probability():
    for i in range(len(TransitionsProb)):
        for n in range(len(TransitionsNum[0])):
            TransitionsProb[i].append(np.concatenate([
            get_row(i,n,0),
            get_row(i,n,1),
            get_row(i,n,2),
            get_row(i,n,3),
            get_row(i,n,4),
            get_row(i,n,5),
            get_row(i,n,6)], axis = 1 ))

# ACTIVATING THE FUNCTIONS ABOVE IN ORDER TO CREATE TEH TRANSITION MATRICES 
SorttingTheData()
SortingMarkovs()
MarkovingTheGluedData()
Probability() 

# FUNCTION WHICH CALCULATES MODEL A
def TrackMarkov(TransitionsProb, month, daytrack, initialmatrix):
  wb = xlwt.Workbook()
  ws = wb.add_sheet('sheet 1', cell_overwrite_ok=True)
  for i in range(daytrack):
    for n in range (7):
      ws.write(i,n,(TransitionsProb[0][month-1]**(i)*initialmatrix).tolist()[n][0])
  wb.save('MATRIX_DATA.xls')

# FUNCTION WHICH CALCULATES MODEL B
def CalculatorWithPrev(Yesterday, InitialMatrix, month, constant):
    TotalMatrix = np.matrix('0.0;0.0;0.0;0.0;0.0;0.0;0.0')
    TotalMatrix += (constant*(np.flipud(Yesterday))+(TransitionsProb[0][month]*InitialMatrix))
    print(TotalMatrix/np.sum(TotalMatrix))


# WILL ACTIVATE MODEL A WITH A SET OF PARAMETERS WHICH THE USER ENTER
TrackMarkov(TransitionsProb, int(input('what month?')), int(input('how many days to track?')), np.matrix(input('what is the initial matrix?')))
# WILL ACTIVATE MODEL B WITH A SET OF PARAMETERS WHICH THE USER ENTER
# CalculatorWithPrev(np.matrix(input("what was yesterday's matrix?")), np.matrix(input("what is today's matrix?")), int(input('what month is it occuring on?'))-1, 0.5)


# import matplotlib.pyplot as plt
# import pandas as pd
# import numpy as np

# np.set_printoptions(linewidth= 300)

# #retrieve data
# dataset = pd.read_csv(r'D:\ML\ML_Stock.csv')

# #splitting inputs (X) and outputs (Y)
# X = dataset.iloc[:, 1:-1].values
# Y = dataset.iloc[:, -1].values

# #filling missing data
# from sklearn.impute import SimpleImputer
# imputer = SimpleImputer(missing_values = np.nan,strategy = "mean")
# imputer = imputer.fit(X[:,:])
# X[:, :] = imputer.transform(X[:,:])


# from sklearn.model_selection import train_test_split
# X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2)

# #  Multiple Linear Regression
# from sklearn.linear_model import LinearRegression
# regressor = LinearRegression()
# regressor.fit(X_train, Y_train)

# # Testing = int(input('number?'))
# # # predicting test set
# Y_pred = regressor.predict(X_test)
# print((sum(Y_test - Y_pred))/len(Y_test))

# plt.scatter(X_test[:, 0], Y_test, color = 'red')
# plt.scatter(X_test[:, 0], Y_pred, color = 'blue')
# plt.title('Share prices CBA.AX')
# plt.xlabel('Days since 4/1/2005')
# plt.ylabel('Share prices')
# plt.show()