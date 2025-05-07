import pandas as pd


#employees: pd.DataFrame: Este es el argumento de la función. La función espera recibir una tabla de datos (un DataFrame de pandas) que contiene información sobre empleados, y lo llamamos employees.

#-> pd.DataFrame: Esto es una anotación que indica que la función devolverá un DataFrame, es decir, una tabla de datos.
def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    #head es un método que devuelve filas de pandas, si no se le especifica ningún número devuelve 5 por defecto
    return employees.head(3)