from pathlib import Path

from etl.extract import extract_sales
from etl.transform import clean_sales, compute_kpis
from etl.load import save_dataframe, save_summary_markdown
from etl.plots import plot_revenue_by_month, plot_revenue_by_category


def run_etl():
    base_dir = Path(__file__).parent

    raw_csv = base_dir / "data" / "raw" / "sales.csv"
    processed_dir = base_dir / "data" / "processed"
    reports_dir = base_dir / "reports"

    print("-- Extrayendo datos...")
    df_raw = extract_sales(raw_csv)

    print("-- Transformando datos...")
    df_clean = clean_sales(df_raw)
    kpis = compute_kpis(df_clean)

    print("-- Guardando datos procesados...")
    save_dataframe(df_clean, processed_dir / "sales_clean.csv")
    save_dataframe(kpis["revenue_by_month"], processed_dir / "revenue_by_month.csv")
    save_dataframe(
        kpis["revenue_by_category"], processed_dir / "revenue_by_category.csv"
    )
    save_dataframe(kpis["top_products"], processed_dir / "top_products.csv")
    save_dataframe(kpis["top_customers"], processed_dir / "top_customers.csv")

    print("-- Generando gráficos...")
    plot_revenue_by_month(
        kpis["revenue_by_month"], reports_dir / "revenue_by_month.png"
    )
    plot_revenue_by_category(
        kpis["revenue_by_category"], reports_dir / "revenue_by_category.png"
    )

    print("-- Generando resumen en Markdown...")
    save_summary_markdown(kpis, reports_dir / "summary.md")

    print("*** Proceso ETL finalizado. ***")


if __name__ == "__main__":
    run_etl()
