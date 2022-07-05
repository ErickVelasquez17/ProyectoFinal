import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def getColumnsDataTypes(df):
    """
    Auto: Preng Biba
    Version: 1.0.0
    Descripción: Función para obtener los tipos de datos de cada columna de un dataframe.
    """

    categoric_vars = []
    discrete_vars = []
    continues_vars = []

    for colname in df.columns:
        if(df[colname].dtype == 'object'):
            categoric_vars.append(colname)
        else:
            cantidad_valores = len(df[colname].value_counts())
            if(cantidad_valores <= 30):
                discrete_vars.append(colname)
            else:
                continues_vars.append(colname)

    return categoric_vars, discrete_vars, continues_vars



def plotCategoricalVals(df, categoric_vars, y):
    """
    Auto: Preng Biba
    Version: 1.0.1
    Descripción: Función para desplegar variables categoricas.
    Modificación: Se le agrego el titulo al gráfico.
    """

    for column in categoric_vars:
        plt.figure(figsize=(12,6))
        plot = sns.countplot(x=df[column], hue=df[y], title=[column])
        plt.show()