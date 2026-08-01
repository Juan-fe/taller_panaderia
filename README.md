# Analisis panaderia

### Integrantes
* David Nicolas Sotelo
* Juan Felipe Sánchez
* Zary Valentina Velasco

## Ajustes

1. Creación carpeta `src`para alojar documentos `.py`.   
2. Cambio de nombre de archivo `analisis.py` por `train.py`, y cambiamos su ubicación, alojándolo en la carpeta `src`.  
3. Creación de carpeta `data`, y almancenamos allí el documento `datos_panaderia.csv`.  
4. Creación de archivo `data.py` para realizar la lectura y carga de datos, y cambiamos su ubicación, alojándolo en la carpeta `src`.  
5. Indicar versiones de librerías usadas en archivo requirements.txt.  
6. Creación de archivo `.gitignore`.  
7. Separación de la lógica para la carga de datos y de entrenamiento del modelo. La parte de carga queda en data.py, la de entrenamiento en train.py.  
8. Corrección de la codificación para la lectura del archivo, y asignación del separador de los datos como ;.  
9. En la versión utilizada de pandas, no funciona append para los dataframes. Esta opción se eliminó en las nuevas versiones porque era poco eficiente porque creaba un nuevo DataFrame en cada iteración. Se ajusta ese fragmento, utilizando la función groupby de pandas.  
10. En el dataset original, habían valores en la columna `temperatura_c` que tenía el valor `SIN DATO`. Se realizó una revisión de todas las columnas para observar si habían más datos con un comportamiento similar, y se evidenció que solamente esta columna tenía el error. Para corregirlo, se realizó la imputación de la mediana.
11. Adicionalmente, en el traceback, al final, aparecía una sugerencia para cambiar la forma en que se asignaba la variable que indicaba si el día de la semana correspondía con un fin de semana, debido a que podría estarse asignando los valores a una copia del df, pero no al original. Se realizó el cambió usando una función directamente de pandas sobre el dataframe.  


# Bonus
1. Se agrega validación entre filas 17 y 20, del archivo data.py.  
2. Se imprime cantidad de filas con valores `SIN DATO`, pero como se realizó imputación de la mediana, se tomaron las 90 filas para el entrenamiento.  

# Decisiones
Realizamos la imputación de la mediana para el caso de los datos faltates (`SIN DATO`) en la columna `temperatura_c`, porque es el mecanismo estandar y recomendado para no añadir sesgo en la muestra que será analizada. Podría usarse la media, pero en caso de que existan brechas muy grandes entre los datos, se podría añadir un sesgo lo que generaría un impacto en el modelo.
