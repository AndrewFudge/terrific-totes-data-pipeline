import pandas as pd


def create_dataset():
    """Generate a dim_date table in parquet
    and write to a file in the /tmp/ folder.
    """
    # creates dataset
    df = pd.DataFrame({"date_id": pd.date_range("2022-01-01", "2030-12-31")})
    df["year"] = df.date_id.dt.year
    df["month"] = df.date_id.dt.month
    df["day"] = df.date_id.dt.day_of_year
    df["day_of_week"] = df.date_id.dt.weekday + 1
    df["day_name"] = df.date_id.dt.strftime("%A")
    df["month_name"] = df.date_id.dt.strftime("%B")
    df["quarter"] = df.date_id.dt.quarter
    df['date_id'] = df.date_id.dt.date

    df.to_parquet("/tmp/formatted_dim_date.parquet")
