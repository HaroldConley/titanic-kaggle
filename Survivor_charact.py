import csv

import numpy
import pandas as pd
gender_submission = pd.read_csv('gender_submission.csv')
test = pd.read_csv('test.csv')
train = pd.read_csv('train.csv')

from matplotlib import pyplot as plt

import warnings
warnings.simplefilter(action='ignore', category= FutureWarning) #para que no salga el warning de que el .append va a desaparecer en nuevas versiones de Python

#print(train.iloc[0].Name)
comb = pd.DataFrame(columns = ['Pclass', 'Sex', 'Age_range'])#, 'SibSp', 'Parch']) #guarda la combinacion de esos factores que generó un Survived=1


#---------- INICIO ITERACION PARA DETECTAR COMBINACIONES DE CARACT QUE PERMITEN QUE SURVIVE = 1 Y ALMACENARLAS EN UN DF----------------------
l = len(train)
for i in range(0,l):
    if train.iloc[i].Survived == 1:
        j = 1
        while j < 100:
            if train.iloc[i].Age <= j:
                rango_edad = j
                j = 100
            j = j+1
        if not numpy.isnan(train.iloc[i].Age): #para que no incluya filas con datos faltantes
            fila = [train.iloc[i].Pclass, train.iloc[i].Sex, rango_edad] #, train.iloc[i].SibSp, train.iloc[i].Parch]
            comb.loc[i+1] = fila

# ---------- FIN ITERACION PARA DETECTAR COMBINACIONES DE CARACT QUE PERMITEN QUE SURVIVE = 1 Y ALMACENARLAS EN UN DF----------------------


comb = comb.drop_duplicates(subset= ['Pclass', 'Sex', 'Age_range'])#, 'SibSp', 'Parch']) #elimina combinaciones repetidas
print(comb.info())


#---------- INICIO ITERACION PARA SABER QUE PROPORCION DE SURVIVED=1 LE CORRESPONDE A CADA COMBINACION -----------------------------------
col_prop_surv = [] #será la columna de prop_surv para agregar al final del DF Comb.
col_num_casos = [] #será la columna de numero de veces que se repite una combinacion del DF Comb.
l_train = len(train)
l_comb = len(comb)
for i in range(0,l_comb):
    surv = 0
    no_surv = 0
    for j in range(0, l_train):
        if train.iloc[j].Pclass == comb.iloc[i].Pclass and train.iloc[j].Sex == comb.iloc[i].Sex and train.iloc[j].Age <= comb.iloc[i].Age_range:# and train.iloc[j].SibSp == comb.iloc[i].SibSp and train.iloc[j].Parch == comb.iloc[i].Parch:
            if train.iloc[j].Survived == 1:
                surv = surv +1
            elif train.iloc[j].Survived == 0:
                no_surv = no_surv +1
    if (surv + no_surv == 0):
        print(comb.iloc[i])
    prop_surv = surv / (surv + no_surv)
    col_prop_surv = col_prop_surv + [prop_surv]
    col_num_casos = col_num_casos + [(surv+no_surv)]
comb['Prop_Surv'] = col_prop_surv
comb['Num_Casos'] = col_num_casos
#---------- FIN ITERACION PARA SABER QUE PROPORCION DE SURVIVED=1 LE CORRESPONDE A CADA COMBINACION -----------------------------------







#entrega = pd.DataFrame(columns = ['PassengerId', 'Survived'])


#---------- INICIO ITERACION QUE COMPARA CADA FILA DE TEST.CSV CON LAS COMBINACIONES QUE DAN SURVIVED=1 (CON UN NUMERO MINIMO DE REPETICIONES DE CASOS Y PROPORCION DE SOBREVIVIENTES GUARDADAS EN EL DF COMB. Y GENERA EL ENTREGABLE ------------
l_test = len(test)
l_comb = len(comb)
# ------- INICIO CREA Y ESCRIBE EN UN CSV ---------------------
e = open('entrega2.csv', 'w')
writer = csv.writer(e)
head = ['PassengerId', 'Survived']
writer.writerow(head)
# ------- FIN CREA Y ESCRIBE EN UN CSV ---------------------
for i in range(0,l_test):
    a = test.iloc[i]
    pass_id = a['PassengerId']
    for j in range(0,l_comb):
        if test.iloc[i].Pclass == comb.iloc[j].Pclass and test.iloc[i].Sex == comb.iloc[j].Sex and test.iloc[i].Age <= comb.iloc[j].Age_range and comb.iloc[j].Num_Casos >= 1 and comb.iloc[j].Prop_Surv >= 1:# and test.iloc[i].SibSp == comb.iloc[j].SibSp and test.iloc[i].Parch == comb.iloc[j].Parch:
            surv = 1
            break
        else:
            surv = 0
    writer.writerow([pass_id, surv])
e.close()
#print(pd.read_csv('entrega2.csv').head())
print('El archivo generado dice: \n')
print(pd.read_csv('entrega2.csv')['Survived'].value_counts())
#---------- FIN ITERACION QUE COMPARA CADA FILA DE TEST.CSV CON LAS COMBINACIONES QUE DAN SURVIVED=1 (CON UN NUMERO MINIMO DE REPETICIONES DE CASOS Y PROPORCION DE SOBREVIVIENTES GUARDADAS EN EL DF COMB. Y GENERA EL ENTREGABLE ------------
