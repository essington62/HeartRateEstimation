import pandas as pd
from pathlib import Path
from src.utils.config_loader import load_config
from src.eda.loader import load_raw_data


def get_eda_output_dir(cfg) -> Path:
    """
    Pasta de saída do EDA depende da fase ativa (Phase0_Phase2 ou Phase4).
    Salva sempre em <Fase>/eda.
    """
    base = Path(cfg["paths"]["base"])
    phase = cfg["phase"]["active_phase"]
    out = base / phase / "eda"
    out.mkdir(parents=True, exist_ok=True)
    return out


def summarize_structure(df: pd.DataFrame) -> pd.DataFrame:
    """
    Resumo estrutural compatível com colunas que possuem listas/arrays.
    """
    rows = []

    for col in df.columns:
        non_null = df[col].dropna()

        example = non_null.iloc[0] if len(non_null) > 0 else None

        rows.append({
            "column": col,
            "dtype": type(example).__name__ if example is not None else "None",
            "n_nulls": df[col].isna().sum(),
            "n_rows": len(df),
        })

    return pd.DataFrame(rows).set_index("column")

def summarize_list_lengths(df: pd.DataFrame) -> pd.DataFrame:
    """
    Muitos campos são listas (sinais). Calcula estatísticas
    sobre o comprimento dessas listas por coluna.
    """
    stats = []
    for col in df.columns:
        lengths = df[col].dropna().apply(lambda x: len(x) if hasattr(x, "__len__") else None)
        lengths = lengths.dropna().astype(int)

        stats.append({
            "column": col,
            "count_with_list": int(lengths.shape[0]),
            "min_len": int(lengths.min()) if not lengths.empty else None,
            "max_len": int(lengths.max()) if not lengths.empty else None,
            "mean_len": float(lengths.mean()) if not lengths.empty else None,
            "std_len": float(lengths.std()) if not lengths.empty else None,
        })
    return pd.DataFrame(stats)


def basic_numeric_describe(df: pd.DataFrame) -> pd.DataFrame:
    """
    Para colunas NUMÉRICAS (se houver),
    calcula estatísticas básicas.
    """
    num_df = df.select_dtypes(include="number")
    if num_df.empty:
        return pd.DataFrame()
    return num_df.describe().T


def save_text_report(path: Path, title: str, content: str):
    with open(path, "w", encoding="utf-8") as f:
        f.write(title + "\n")
        f.write("=" * len(title) + "\n\n")
        f.write(content)


def main():
    # 1) Carrega config e dados
    cfg = load_config()
    df = load_raw_data(cfg)

    # 2) Define saída
    out_dir = get_eda_output_dir(cfg)

    # 3) Estrutura do dataframe
    struct_df = summarize_structure(df)
    struct_df.to_csv(out_dir / "basic_structure.csv")

    # 4) Tamanhos das listas (sinais)
    lengths_df = summarize_list_lengths(df)
    lengths_df.to_csv(out_dir / "basic_list_lengths.csv", index=False)

    # 5) Estatísticas básicas de colunas numéricas (se existirem)
    describe_df = basic_numeric_describe(df)
    if not describe_df.empty:
        describe_df.to_csv(out_dir / "basic_describe_numeric.csv")

    # 6) Relatório de texto curto
    report_lines = []
    report_lines.append(f"Fase ativa: {cfg['phase']['active_phase']}")
    report_lines.append(f"Shape do DataFrame RAW: {df.shape}")
    report_lines.append("\nColunas:")
    report_lines.extend([f"- {c}" for c in df.columns])
    report_lines.append("\nResumo de Nulos por Coluna:")
    for col, v in struct_df["n_nulls"].items():
        report_lines.append(f"- {col}: {int(v)}")
    report_lines.append("\nResumo dos tamanhos de listas (por coluna) salvo em basic_list_lengths.csv.")

    save_text_report(
        out_dir / "basic_report.txt",
        title="EDA Básico — Relatório",
        content="\n".join(report_lines)
    )

    # 7) Prints de validação rápida
    print("\n✅ EDA BÁSICO CONCLUÍDO")
    print(f"📁 Saída em: {out_dir}")
    print("Arquivos gerados:")
    for f in sorted(out_dir.glob("basic_*")):
        print(" -", f.name)


if __name__ == "__main__":
    main()