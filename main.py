import datetime as dt
import pandas as pd
from pathlib import Path

source_file = Path(__file__).parent / 'Priziv1volna.txt'


def get_source_df():
    df = pd.read_csv(
        source_file,
        delimiter="	",
        names=[
            "name",
            "birthday",
            "address",
            "phone",
            "region",
        ],
    )
    df['birthday'] = pd.to_datetime(df['birthday'])
    df['age'] = (dt.datetime.today() - df['birthday']).dt.days / 365.25
    df['age'] = df['age'].astype(int)
    return df


df = get_source_df()

print(f"\nparsed source df:\n{df}\n")

age_distribution = df.age.value_counts()
print(f"\nage_distribution:\n{age_distribution}")
