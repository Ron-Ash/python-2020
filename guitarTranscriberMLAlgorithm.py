# visualises everything
import matplotlib.pyplot as plt
# connects to excel and handles the matrices
import pandas as pd
# handles math opperations
import numpy as np

# -------------------------------------------------------------------------------------------Preprocessing Data
np.set_printoptions(linewidth= 300)

#retrieve data
dataset = pd.read_csv(r'D:\2019_2020\PYTHON_PROJECTS\guitarDatabase.csv')

#splitting inputs (X) and outputs (Y)
X = dataset.iloc[:, :-1].values
Y = dataset.iloc[:, -1].values


#splitting data to Test and train set
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.25, random_state = 0)

# feature scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)


# Support vector machines
from sklearn.svm import SVC
classifier = SVC(kernel = 'rbf', random_state = 0)
classifier.fit(X_train, Y_train)

Y_pred = classifier.predict(X_test)

# K-Nearest neighbor
# from sklearn.neighbors import KNeighborsClassifier
# classifier = KNeighborsClassifier(n_neighbors = 5, metric = 'minkowski', p = 2)
# classifier.fit(X_train, Y_train)

# Y_pred = classifier.predict(X_test)


# Cofusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(Y_test, Y_pred)
print(cm, np.sum(np.abs(Y_pred - Y_test)))


# # Visualizing clasifieres barrier
# from matplotlib.colors import ListedColormap
# X_set, Y_set = X_train, Y_train
# X1, X2 = np.meshgrid(np.arange(start = X_set[:, 0].min()-1, stop = X_set[:, 0].max()+1, step = 0.01), np.arange(start = X_set[:, 1].min()-1, stop = X_set[:, 1].max()+1, step = 0.01))
# print(len(X1.ravel()), len(X2.ravel()))
# plt.contourf(X1, X2, classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape), alpha = 0.75, cmap = ListedColormap(('red', 'green')))
# plt.xlim(X1.min(), X1.max())
# plt.ylim(X2.min(), X2.max())
# for i, j in enumerate(np.unique(Y_set)):
#     plt.scatter(X_set[Y_set == j, 0], X_set[Y_set == j, 1], c = ListedColormap(('red', 'green'))(i), label = j)
# plt.legend()
# plt.show()