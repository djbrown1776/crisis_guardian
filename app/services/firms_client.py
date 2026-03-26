import httpx
import pandas as pd
from io import StringIO
from app.config import settings

async def fetch_fires_usa():
    bbox = "-125,24,-66,50" # continental U.S.

    source = "VIIRS_NOAA20_NRT"

    day_range = 1

    url= (
        f"https://firms.modaps.eosdis.nasa.gov/api/area/csv/"
               f"{settings.firms_map_key}/{source}/{bbox}/{day_range}"
    )

    async with httpx.AsyncClient() as client:
        response = await client.get(url, timeout=300)
        response.raise_for_status()

    df = pd.read_csv(StringIO(response.text))

    return df
