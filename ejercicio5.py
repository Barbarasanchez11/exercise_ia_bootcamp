import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    return customers.drop_duplicates(subset=['email'], keep='first')

# Crear un DataFrame de prueba basado en el ejemplo
data = {
    'customer_id': [1, 2, 3, 4, 5, 6],
    'name': ['Ella', 'David', 'Zachary', 'Alice', 'Finn', 'Violet'],
    'email': ['emily@example.com', 'michael@example.com', 'sarah@example.com', 
              'john@example.com', 'john@example.com', 'alice@example.com']
}
customers = pd.DataFrame(data)

# Aplicar la función
result = dropDuplicateEmails(customers)

# Mostrar el resultado
print("DataFrame original:")
print(customers)
print("\nDataFrame después de eliminar duplicados:")
print(result)