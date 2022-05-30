# entrega1.csv se armó suponiendo que:
# 1.- Las mujeres de 1era y 2da clase sobreviven
# 2.- Los hombres de hasta 10 años Y de 1era o 2da clase sobreviven
# 3.- Los hombres de hasta 10 años Y con 0 ó 1 hermano/esposa sobreviven

import csv

import pandas as pd
gender_submission = pd.read_csv('gender_submission.csv')
test = pd.read_csv('test.csv')

from matplotlib import pyplot as plt

import warnings
warnings.simplefilter(action='ignore', category= FutureWarning) #para que no salga el warning de que el .append va a desaparecer en nuevas versiones de Python

print(gender_submission.head())
print(test.head())

entrega = pd.DataFrame(columns = ['PassengerId', 'Survived'])

#------- INICIO CREA Y ESCRIBE EN UN CSV ---------------------
e = open('entrega1.csv', 'w')
writer = csv.writer(e)
head = ['PassengerId', 'Survived']
writer.writerow(head)
#e.close()
#print(pd.read_csv('entrega1.csv'))
#------- FIN CREA Y ESCRIBE EN UN CSV ---------------------

a = test.iloc[0]
print(a['Pclass'] == 2)
print(len(test))
print(test.info)

#------------ INICIO ITERACION PARA LLENAR EL CSV DE ENTREGA --------------
for i in range(0,418):
    a = test.iloc[i]
    pass_id = a['PassengerId']
    if a['Sex'] == 'female' and a['Pclass'] in [1, 2]:
        surv = 1
    elif a['Sex'] == 'male' and a['Age'] <= 10 and (a['Pclass'] in [1, 2] or a['SibSp'] in [0,1]):
        surv = 1
    else:
        surv = 0
    writer.writerow([pass_id, surv])
#------------ FIN ITERACION PARA LLENAR EL CSV DE ENTREGA --------------
e.close()
print(pd.read_csv('entrega1.csv'))