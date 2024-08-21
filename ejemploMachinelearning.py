import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay
from sklearn import tree
import matplotlib.pyplot as plt
import seaborn as sn

def machinaejemplo():
    archivo=pd.read_csv('modeloPrueba.csv')

    X=archivo.drop("diagnosis",axis=1)

    y=archivo.diagnosis

    arbol=DecisionTreeClassifier(max_depth=14,random_state=1)
    arbol.fit(X,y)

    predicciony=arbol.predict(X)

    print(accuracy_score(predicciony,y))
    #matriz de confucion
    matriz=confusion_matrix(y,predicciony)
    print(matriz)
    plt.matshow(matriz,cmap="binary")
    plt.xlabel("hola")
    plt.ylabel("adios")

    plt.show()
    tree.plot_tree(arbol, filled=True, feature_names=X.columns)
    plt.show()
