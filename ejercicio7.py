import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    return students.rename(columns={
        'id': 'student_id',
        'first': 'first_name',
        'last': 'last_name',
        'age': 'age_in_years'
    })

# Bloque de prueba
if __name__ == "__main__":
    # Creamos un DataFrame de ejemplo
    data = {
        'id': [101, 102],
        'first': ['Ana', 'Luis'],
        'last': ['Gómez', 'Martínez'],
        'age': [22, 23]
    }

    df = pd.DataFrame(data)
    renamed_df = renameColumns(df)

    # Mostrar el DataFrame renombrado
    print(renamed_df)
