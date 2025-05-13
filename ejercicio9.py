import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    students['grade'] = students['grade'].astype(int)
    return students

# Prueba
if __name__ == "__main__":
    data = {
        'student_id': [1, 2, 3],
        'name': ['Ana', 'Luis', 'Marta'],
        'age': [10, 11, 12],
        'grade': [95.0, 89.5, 100.0]
    }

    df = pd.DataFrame(data)
    converted_df = changeDatatype(df)
    print(converted_df)
