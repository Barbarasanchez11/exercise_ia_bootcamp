import pandas as pd

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    products['quantity'] = products['quantity'].fillna(0)
    return products

if __name__ == "__main__":
    data = {
        'name': ['Manzana', 'Banana', 'Pera'],
        'quantity': [10, None, 5],
        'price': [100, 50, 80]
    }

    df = pd.DataFrame(data)
    filled_df = fillMissingValues(df)
    print(filled_df)
