import pandas as pd


weather = pd.DataFrame({
    'city': ['Madrid', 'Madrid', 'Barcelona', 'Barcelona', 'Madrid', 'Barcelona'],
    'month': ['January', 'February', 'January', 'February', 'March', 'March'],
    'temperature': [10, 12, 15, 18, 20, 22]
})


def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    return weather.pivot_table(index='month', columns='city', values='temperature', aggfunc='mean')


resultado = pivotTable(weather)
print(resultado)
