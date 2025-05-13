import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['salary'] = employees['salary'] * 2
    return employees

# Prueba de la función
if __name__ == "__main__":
    # Crear un DataFrame de prueba
    df = pd.DataFrame({
        'name': ['Alice', 'Bob'],
        'salary': [1000, 1500]
    })

    # Llamar a la función
    modified_df = modifySalaryColumn(df)

    # Mostrar el resultado
    print(modified_df)
