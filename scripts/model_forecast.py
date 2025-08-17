
import pandas as pd
import numpy as np
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from pathlib import Path
import matplotlib.pyplot as plt

RAW = Path(__file__).resolve().parents[1] / "data" / "raw" / "supermart_sales.csv"
IMG = Path(__file__).resolve().parents[1] / "images"

def main():
    df = pd.read_csv(RAW, parse_dates=['Order Date'])
    cat = 'Beverages'
    ts = (df[df['Category']==cat]
          .groupby(pd.Grouper(key='Order Date', freq='M'))['Sales']
          .sum()
          .reset_index())
    ts['t'] = np.arange(len(ts))
    ts['month'] = ts['Order Date'].dt.month
    ts['year'] = ts['Order Date'].dt.year
    X = ts[['t','month','year']]
    y = ts['Sales']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)
    m = Ridge(alpha=1.0).fit(X_train, y_train)
    preds = m.predict(X_test)
    mae = mean_absolute_error(y_test, preds)
    print("MAE:", round(mae,2))

    plt.figure()
    plt.plot(ts['Order Date'], ts['Sales'], label='Actual')
    plt.plot(ts.loc[X_test.index, 'Order Date'], preds, label='Predicted')
    plt.legend()
    plt.title('Monthly Sales – Actual vs Predicted (Ridge baseline)')
    IMG.mkdir(parents=True, exist_ok=True)
    out = IMG / "forecast_beverages.png"
    plt.tight_layout()
    plt.savefig(out)
    print(f"Saved: {out}")

if __name__ == "__main__":
    main()
