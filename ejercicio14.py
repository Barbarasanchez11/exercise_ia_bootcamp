import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    # Asegurarnos de que 'weight' sea de tipo int (si es necesario)
    animals['weight'] = animals['weight'].astype(int)
    
    # Filtrar los animales cuyo peso es mayor a 100
    heavy_animals = animals[animals['weight'] > 100]
    
    # Ordenar por peso en orden descendente y restablecer el índice
    return heavy_animals.sort_values(by='weight', ascending=False).reset_index(drop=True)[['name', 'weight']]


animals = pd.DataFrame({
    'name': ['Tatiana', 'Khaled', 'Alex', 'Jonathan', 'Stefan', 'Tommy'],
    'species': ['Snake', 'Giraffe', 'Leopard', 'Monkey', 'Bear', 'Panda'],
    'age': [98, 50, 6, 45, 100, 26],
    'weight': [464, 41, 328, 463, 50, 349]
})


resultado = findHeavyAnimals(animals)
print(resultado)
