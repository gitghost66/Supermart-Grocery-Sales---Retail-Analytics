
import pandas as pd
from pathlib import Path

def test_raw_has_expected_columns():
    raw = Path(__file__).resolve().parents[1] / "data" / "raw" / "supermart_sales.csv"
    df = pd.read_csv(raw)
    expected = {'Order ID','Order Date','Customer ID','Product ID','Category','Sales','Profit','Quantity'}
    assert expected.issubset(set(df.columns))
