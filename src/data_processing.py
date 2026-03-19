import pandas as pd

def load_and_clean_data(path):
    df = pd.read_csv(path)

    df = df[(df["REF_DATE"] >= 2015) & (df["REF_DATE"] <= 2025)]

    maritimes = ["New Brunswick", "Prince Edward Island", "Nova Scotia"]
    df = df[df["GEO"].isin(maritimes)]

    metrics = ["Seeded area", "Average yield", "Production"]
    df = df[df["Area, production and farm value of potatoes"].isin(metrics)]

    df_pivot = df.pivot_table(
        index=["REF_DATE", "GEO"],
        columns="Area, production and farm value of potatoes",
        values="VALUE"
    ).reset_index()

    df_pivot.columns.name = None

    df_pivot.rename(columns={
        "REF_DATE": "Year",
        "GEO": "Province",
        "Seeded area": "Area_acres_raw",
        "Average yield": "Yield_cwt_per_acre",
        "Production": "Production_thousand_cwt"
    }, inplace=True)

    return df_pivot