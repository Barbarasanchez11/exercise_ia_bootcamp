#pandas se usa para trabajar con datos en forma de tabla
import pandas as pd

student_data = [
  [1, 15],
  [2, 11],
  [3, 11],
  [4, 20]
]

#Cuando alguien llame a esta función, deberá pasarle una lista de estudiantes, y esa lista será llamada list_students dentro de la función.list_students es el nombre del parámetro que se usa dentro de la función.
def createDataframe(list_students):
    df = pd.DataFrame(list_students, columns=["student_id", "age"])
    return df



df_resultado = createDataframe(student_data)#student_data (la lista real) se pasa como valor al parámetro list_students

#imprimir para verlo en consola
print(df_resultado) 