from pathlib import Path
import pandas as pd


def save_dataframe(df: pd.DataFrame, path: str | Path) -> None:
    """
    Guarda un DataFrame como CSV.
    """
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)


def save_summary_markdown(kpis: dict, path: str | Path) -> None:
    """
    Genera un pequeño resumen de KPIs en formato Markdown.
    """
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    total_revenue = kpis.get("total_revenue", 0.0)
    total_orders = kpis.get("total_orders", 0)
    total_customers = kpis.get("total_customers", 0)

    lines = [
        "# Resumen de ventas",
        "",
        f"- Ingreso total: **{total_revenue:,.2f}**",
        f"- Cantidad de órdenes: **{total_orders}**",
        f"- Cantidad de clientes: **{total_customers}**",
        "",
        "## Ingreso por categoría (Top 5)",
        "",
    ]

    revenue_by_category: pd.DataFrame = kpis["revenue_by_category"]
    top_cat = revenue_by_category.head(5)

    for _, row in top_cat.iterrows():
        lines.append(f"- {row['category']}: {row['total_price']:,.2f}")

    path.write_text("\n".join(lines), encoding="utf-8")
