
import pandas as pd
from pathlib import Path

RAW = Path(__file__).resolve().parents[1] / "data" / "raw" / "supermart_sales.csv"
OUT = Path(__file__).resolve().parents[1] / "data" / "processed" / "supermart_sales_processed.csv"

def main():
    df = pd.read_csv(RAW)
    # basic cleaning
    df = df.drop_duplicates()
    df = df[df['Sales'] >= 0]
    df['Return Rate'] = df.groupby('Product ID')['Returned'].transform('mean')
    df.to_csv(OUT, index=False)
    print(f"Saved cleaned data to: {OUT}")

if __name__ == "__main__":
    main()
