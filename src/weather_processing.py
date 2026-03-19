import pandas as pd

def process_weather_file(path, province_name):
    df = pd.read_csv(path)

    # Keep only relevant columns
    df = df[[
        "LOCAL_YEAR",
        "MEAN_TEMPERATURE",
        "TOTAL_PRECIPITATION"
    ]]

    # Drop missing values
    df = df.dropna()

    # Aggregate yearly
    df_yearly = df.groupby("LOCAL_YEAR").agg({
        "MEAN_TEMPERATURE": "mean",
        "TOTAL_PRECIPITATION": "sum"
    }).reset_index()

    # Rename columns
    df_yearly.rename(columns={
        "LOCAL_YEAR": "Year",
        "MEAN_TEMPERATURE": "Avg_Temp",
        "TOTAL_PRECIPITATION": "Total_Rainfall"
    }, inplace=True)

    df_yearly["Province"] = province_name

    return df_yearly


def build_weather_dataset():
    nb = process_weather_file(
        "data/climate-daily_Fredericton_NB_2015-2025.csv",
        "New Brunswick"
    )

    ns = process_weather_file(
        "data/climate-daily_Halifax_NS_2015-2025.csv",
        "Nova Scotia"
    )

    pei = process_weather_file(
        "data/climate-daily_Harrington_PEI_2015-2025.csv",
        "Prince Edward Island"
    )

    weather = pd.concat([nb, ns, pei])

    weather = weather.sort_values(["Province", "Year"])

    return weather


if __name__ == "__main__":
    weather = build_weather_dataset()
    weather.to_csv("data/weather_processed.csv", index=False)

    print("Weather dataset created successfully!")
    print(weather.head())