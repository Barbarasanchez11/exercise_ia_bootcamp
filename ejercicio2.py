import pandas as pd

def get_shape_as_matrix(df):
    filas, columnas = df.shape
    return [[filas, columnas]]

data = [
    [846, "Mason", 21, "Forward", "RealMadrid"],
    [749, "Riley", 30, "Winger", "Barcelona"],
    [155, "Bob", 28, "Striker", "ManchesterUnited"],
    [583, "Isabella", 32, "Goalkeeper", "Liverpool"],
    [388, "Zachary", 24, "Midfielder", "BayernMunich"],
    [883, "Ava", 23, "Defender", "Chelsea"],
    [355, "Violet", 18, "Striker", "Juventus"],
    [247, "Thomas", 27, "Striker", "ParisSaint-Germain"],
    [761, "Jack", 33, "Midfielder", "ManchesterCity"],
    [642, "Charlie", 36, "Center-back", "Arsenal"]
]

players = pd.DataFrame(data, columns=["player_id", "name", "age", "position", "team"])

# Llamar a la función
resultado = get_shape_as_matrix(players)
print(resultado)
