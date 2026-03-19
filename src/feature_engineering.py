import numpy as np

def add_features(df):
    # Unit conversions
    df["Production_tonnes"] = (
        df["Production_thousand_cwt"] * 1000 * 45.3592 / 1000
    )
    df["Area_ha"] = df["Area_acres_raw"] / 2.47105
    df["Yield_t_per_ha"] = df["Production_tonnes"] / df["Area_ha"]

    df = df.sort_values(["Province", "Year"])

    # Lag
    df["Prev_Production"] = df.groupby("Province")["Production_tonnes"].shift(1)

    # Rolling
    df["Yield_3yr_avg"] = df.groupby("Province")["Yield_t_per_ha"]\
                            .rolling(3).mean().reset_index(0, drop=True)

    # Change
    df["Yield_pct_change"] = df.groupby("Province")["Yield_t_per_ha"].pct_change()

    return df


def add_weather_features(df):
    df["Rainfall_dev"] = df["Total_Rainfall"] - \
        df.groupby("Province")["Total_Rainfall"].transform("mean")

    df["Temp_dev"] = df["Avg_Temp"] - \
        df.groupby("Province")["Avg_Temp"].transform("mean")

    return df


def add_disease_risk(df):
    df["High_Rain"] = df["Total_Rainfall"] > \
        df.groupby("Province")["Total_Rainfall"].transform("mean")

    df["Yield_Drop"] = df["Yield_pct_change"] < -0.05

    df["Disease_Risk"] = (df["High_Rain"] & df["Yield_Drop"]).astype(int)

    return df