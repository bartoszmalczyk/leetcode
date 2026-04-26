import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    person.set_index('id', inplace= True)
    df = person[person.duplicated()]
    df = df['email'].unique()
    df = pd.DataFrame(df)
    df.columns = ['Email']
    return df
