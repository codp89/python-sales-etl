import pandas as pd
from pathlib import Path


def extract_sales(csv_path: str | Path) -> pd.DataFrame:
    """
    Lee el archivo CSV de ventas y lo devuelve como DataFrame.
    """
    csv_path = Path(csv_path)
    if not csv_path.exists():
        raise FileNotFoundError(f"No se encontró el archivo: {csv_path}")

    df = pd.read_csv(csv_path)
    return df
