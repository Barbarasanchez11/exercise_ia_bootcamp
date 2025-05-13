import pandas as pd


df1 = pd.DataFrame({
    'student_id': [1, 2],
    'name': ['Alice', 'Bob'],
    'age': [20, 21]
})

df2 = pd.DataFrame({
    'student_id': [3, 4],
    'name': ['Charlie', 'David'],
    'age': [22, 23]
})

# Llamar a la función de concatenación
resultado = concatenarTablas(df1, df2)
print(resultado)
