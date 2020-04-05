# suma_diagonal
Aplicación para sumar todos los valores que encuentra en la diagonal de una tabla, 
desde una posición específica hasta la primera fila o hasta otra posición determinada.

Útil en el cálculo de la cantidad de veces que se ha conectado una cohorte a una aplicación de smartphone,
lo cual se aprecia en las estadísticas de Engagement de Google Analytics o Firebase.

Se escoge la celda de referencia en excel (csv) desde donde iniciará la sumatoria.
El programa sumará automáticamente todos los valores hasta la primera fila con datos (sentido de izquierda a derecha).

Si se escoge una celda de llegada diferente a la primera fila debe indicarse en el programa.

Ejemplo: Se toma como referencia la celda A4 y se esccribe en el programa celda_inicio= 'A4'

 |  A B C D E F
1|  1 3 4 7 9 5
2|  4 3 6 9 3 6
3|  6 9 9 5 1 0
4|  7 5 8 2 4 1

El programa sumará todos los valores en forma diagonal a partir de la referencia. El resultado será:
7+9+6+7= 29

Si se selecciona como celda_llegada= 'C2' la sumatoria será: 7+9+6= 22
