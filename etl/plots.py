from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt


def plot_revenue_by_month(df: pd.DataFrame, output_path: str | Path) -> None:
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(8, 4))
    plt.plot(df["month"], df["total_price"], marker="o")
    plt.title("Ingreso por mes")
    plt.xlabel("Mes")
    plt.ylabel("Ingreso")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()


def plot_revenue_by_category(df: pd.DataFrame, output_path: str | Path) -> None:
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(8, 4))
    plt.bar(df["category"], df["total_price"])
    plt.title("Ingreso por categoría")
    plt.xlabel("Categoría")
    plt.ylabel("Ingreso")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()
