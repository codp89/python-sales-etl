import pandas as pd


def clean_sales(df: pd.DataFrame) -> pd.DataFrame:
    """
    Limpia y normaliza el DataFrame de ventas.
    - Convierte fechas
    - Elimina filas claramente incompletas
    - Calcula columna 'total_price'
    """
    df = df.copy()

    # Normalizar nombres de columnas en minúsculas
    df.columns = [c.strip().lower() for c in df.columns]

    # Asegurar columnas mínimas
    required_cols = ["order_id", "order_date", "customer_id",
                     "category", "product", "quantity", "unit_price"]
    missing = [c for c in required_cols if c not in df.columns]
    if missing:
        raise ValueError(f"Faltan columnas obligatorias: {missing}")

    # Convertir fecha
    df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")

    # Tipos numéricos
    df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")
    df["unit_price"] = pd.to_numeric(df["unit_price"], errors="coerce")
    if "discount" in df.columns:
        df["discount"] = pd.to_numeric(df["discount"], errors="coerce").fillna(0.0)
    else:
        df["discount"] = 0.0

    # Quitar filas sin fecha, quantity o price
    df = df.dropna(subset=["order_date", "quantity", "unit_price"])

    # Calcular total
    df["total_price"] = df["quantity"] * df["unit_price"] * (1 - df["discount"])

    # Agregar columnas de año y mes
    df["year"] = df["order_date"].dt.year
    df["month"] = df["order_date"].dt.to_period("M").astype(str)

    return df


def compute_kpis(df: pd.DataFrame) -> dict:
    """
    Calcula KPIs a partir del DataFrame limpio.
    Devuelve un dict con varios DataFrames/resúmenes.
    """
    kpis: dict[str, object] = {}

    kpis["total_revenue"] = df["total_price"].sum()
    kpis["total_orders"] = df["order_id"].nunique()
    kpis["total_customers"] = df["customer_id"].nunique()

    # Ingreso por mes
    revenue_by_month = (
        df.groupby("month")["total_price"]
        .sum()
        .reset_index()
        .sort_values("month")
    )
    kpis["revenue_by_month"] = revenue_by_month

    # Ingreso por categoría
    revenue_by_category = (
        df.groupby("category")["total_price"]
        .sum()
        .reset_index()
        .sort_values("total_price", ascending=False)
    )
    kpis["revenue_by_category"] = revenue_by_category

    # Top productos
    top_products = (
        df.groupby("product")["total_price"]
        .sum()
        .reset_index()
        .sort_values("total_price", ascending=False)
        .head(10)
    )
    kpis["top_products"] = top_products

    # Top clientes
    top_customers = (
        df.groupby("customer_id")["total_price"]
        .sum()
        .reset_index()
        .sort_values("total_price", ascending=False)
        .head(10)
    )
    kpis["top_customers"] = top_customers

    return kpis
