
import os
import pandas as pd
import matplotlib.pyplot as plt
from glob import glob

DATA_DIR = "data"
OUTPUT_IMAGE = "images/china_avg_temp_trend_2011_2020_resized.png"

def read_isd_file(filepath):
    try:
        df = pd.read_csv(
            filepath, 
            delim_whitespace=True, 
            header=None,
            names=[
                'year', 'month', 'day', 'hour',
                'air_temp', 'dew_point', 'sea_level_pressure',
                'wind_speed', 'wind_direction', 'sky_condition',
                'precip_1hr', 'precip_6hr'
            ],
            na_values=[9999.9, 999.9, 999.99]
        )
        return df[['year', 'air_temp']].dropna()
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return None

def load_all_data():
    filepaths = glob(os.path.join(DATA_DIR, "**", "*"), recursive=True)
    dfs = []
    for fp in filepaths:
        if os.path.isfile(fp):
            df = read_isd_file(fp)
            if df is not None:
                dfs.append(df)
    if dfs:
        return pd.concat(dfs, ignore_index=True)
    else:
        raise RuntimeError("No valid data files found.")

def compute_annual_avg(df):
    df['air_temp_c'] = df['air_temp'] / 10
    return df.groupby('year')['air_temp_c'].mean().reset_index()

def plot_trend(df):
    os.makedirs("images", exist_ok=True)
    plt.figure(figsize=(12, 7))
    plt.plot(df['year'], df['air_temp_c'], marker='o', linewidth=2.5)
    plt.title('Average Annual Temperature in China (2011–2020)', fontsize=18)
    plt.xlabel('Year', fontsize=14)
    plt.ylabel('Average Temperature (°C)', fontsize=14)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.savefig(OUTPUT_IMAGE)
    print(f"Saved figure to {OUTPUT_IMAGE}")

if __name__ == "__main__":
    print("Loading and processing data...")
    df_all = load_all_data()
    df_annual = compute_annual_avg(df_all)
    plot_trend(df_annual)
    print("Done.")
