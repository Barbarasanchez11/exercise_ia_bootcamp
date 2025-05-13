import pandas as pd


report = pd.DataFrame({
    'product': ['A', 'B', 'C'],
    'quarter_1': [100, 200, 300],
    'quarter_2': [110, 210, 310],
    'quarter_3': [120, 220, 320],
    'quarter_4': [130, 230, 330]
})


def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    return pd.melt(report, id_vars=['product'], var_name='quarter', value_name='sales')

resultado = meltTable(report)
print(resultado)
