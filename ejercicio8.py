import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    return students.dropna(subset=['name'])

# Bloque de prueba
if __name__ == "__main__":
    # Crear un DataFrame de ejemplo con un valor faltante
    data = {
        'student_id': [32, 217, 779, 849],
        'name': ['Piper', None, 'Georgia', 'Willow'],
        'age': [5, 19, 20, 14]
    }

    df = pd.DataFrame(data)

    # Llamar a la función para eliminar filas con nombre faltante
    cleaned_df = dropMissingData(df)

    # Mostrar resultado
    print(cleaned_df)
