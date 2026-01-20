import pandas as pd
from only_tst import ingest_weather_for_location

my_data = ingest_weather_for_location("london")

def create_df(data):
    df = pd.DataFrame(data)
    return df


def data_analysis_columns(df):
    df["temperature_category"] =  pd.cut(x= df["temperature"] ,bins= [-float('inf'),18,25,float('inf')] ,labels=["cold","moderate","hot"])
    df["wind_status"] = pd.cut(x=df["wind_speed"], bins= [-float('inf'),10,float('inf')],labels=["calm","windy"])
    return df


my_data = create_df(my_data)
print(data_analysis_columns(my_data))
print(my_data.info())