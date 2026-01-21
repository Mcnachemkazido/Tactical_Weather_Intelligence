from fastapi import APIRouter ,HTTPException
from schemas import Location
from data_handling import create_df ,data_analysis_columns


route = APIRouter()

@route.post("/clean")
def clean_data(locations:list[Location]):
    locations_dict = [l.model_dump(mode='json') for l in locations]
    df = create_df(locations_dict)
    big_df = data_analysis_columns(df)
    print(big_df.info())
    locations_json = big_df.to_dict('records')
    print(type(locations_json[0]["timestamp"]))
    return locations_json

