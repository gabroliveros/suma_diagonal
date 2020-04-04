## SUMADORA DE VALORES DE DIAGONAL

# Permite realizar el conteo de todas las conexiones de
# de una misma cohorte de Google Analytics.
########################################################

# Desarrollado por: Gabriel Oliveros D.

########################################################


import pandas as pd
import numpy as np

df=pd.read_csv('nombre_del_archivo.csv')


## DATOS DE ENTRADA
##=================

def posicion(celda):
    x=('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
    y=('0','1','2','3','4','5','6','7','8','9')
    celda=celda.lower()
    lista=list(celda)

    cuenta=0
    columna=0
    for car in lista:
        for letra in x:
            cuenta+=1
            if car==letra:
                columna=cuenta #referencia en números de la columna (((AL LLEGAR A BA NO FUNCIONA)))
    
    fila=[]
    for car in lista:
        for num in y:
            if car==num:
                fila.append(car)
    fila=int(''.join(fila))
    return columna, fila


# Celda de partida. Se indica la celda de referencia de Excel
# desde donde comezará a sumar. La suma se realiza de izquierda
# a derecha y de abajo hacia arriba.

celda='g7'

columna=posicion(celda)[0]
fila=posicion(celda)[1]

x=columna-1  #Valor de columna en pd a partir de Excel
y=fila-2     #Valor de fila en pd a partir de Excel  


# Celda de llegada. Se indica la celda hasta donde se sumará.
# Si no se indica este valor sumará todos los datos de esa diagonal.

celda='h6'
x2=0
y2=0
try:
    columna=posicion(celda)[0]
    fila=posicion(celda)[1]

    x2=columna-1   #Valor de columna, tal como en Excel
    y2=fila-2      #Valor de fila, tal como en Excel  
except ValueError:
    exit 


## GUARDO NOMBRES DE COLUMNAS DEL DATAFRAME
##=========================================
titulos=df.columns


## SE SUSTITUYEN LOS NOMBRES DE COLUMNA DEL DATAFRAME
##===================================================
cuenta=0
for columns in df:
    df=df.rename(columns={columns:'r'+str(cuenta)})
    cuenta+=1


## ITERACIÓN POR FILA Y COLUMNA
##=============================
count=0 
column_actual='r'+str(x)
fila_actual=y+1
suma=0

for i in range(fila_actual): 
    try:
        if x2==0 and y2==0: #Cuando no existe celda de llegada
            column_actual='r'+str(x+count)
            count+=1
            fila_actual=fila_actual-1
            celda_actual=df.iloc[fila_actual][column_actual]
            suma+=celda_actual
        elif x2!=0 or y2!=0: #Cuando existe celda de llegada
            column_actual='r'+str(x+count)
            count+=1
            fila_actual=fila_actual-1
            celda_actual=df.iloc[fila_actual][column_actual]
            suma+=celda_actual
            if celda_actual==df.iloc[y2][x2]:
                break
    except KeyError: #Cuando llega a la columna final y no encuentra otra
        break
print('El resultado de la suma en la diagonal es: ', suma)


## SE RESTITUYEN LOS NOMBRES DE COLUMNAS DEL DATAFRAME
##====================================================
df.columns=titulos #Se restablecen los títulos después de haber sido cambiados
