import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather['recordDate'] = pd.to_datetime(weather['recordDate'])
    weather.sort_values(by="recordDate", inplace=True)
    is_temp_higher = weather['temperature'].diff() > 0
    is_next_day = weather['recordDate'].diff() == pd.Timedelta(days=1)
    return weather[is_temp_higher & is_next_day][['id']]