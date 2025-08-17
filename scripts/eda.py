
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

RAW = Path(__file__).resolve().parents[1] / "data" / "raw" / "supermart_sales.csv"
IMG = Path(__file__).resolve().parents[1] / "images"
IMG.mkdir(exist_ok=True, parents=True)

def main():
    df = pd.read_csv(RAW, parse_dates=['Order Date'])
    cat_sales = df.groupby('Category')['Sales'].sum().sort_values(ascending=False)
    ax = cat_sales.plot(kind='bar', title='Total Sales by Category')
    fig = ax.get_figure()
    fig.tight_layout()
    out = IMG / "sales_by_category.png"
    fig.savefig(out)
    print(f"Saved: {out}")

if __name__ == "__main__":
    main()
