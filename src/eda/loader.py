import numpy as np
import pandas as pd
from pathlib import Path
from src.utils.config_loader import load_config


def load_raw_data(cfg):
    """
    Carrega o arquivo RAW da fase ativa, baseado no config.yaml.
    Suporta arquivos .npy (dicionário) e .csv.
    """

    raw_path = Path(cfg["paths"]["raw"])

    if not raw_path.exists():
        raise FileNotFoundError(f"Pasta RAW não encontrada: {raw_path}")

    # Arquivos suportados
    npy_files = list(raw_path.glob("*.npy"))
    csv_files = list(raw_path.glob("*.csv"))

    # -------------------------
    # 1) NPY → dict → DataFrame
    # -------------------------
    if npy_files:
        file = npy_files[0]
        print(f"📥 Carregando arquivo NPY: {file.name}")

        try:
            data = np.load(file, allow_pickle=True).item()
        except Exception as e:
            raise ValueError(f"Erro ao carregar {file}: {e}")

        df = pd.DataFrame(data)

        print(f"📊 RAW carregado (NPY) — shape: {df.shape}")
        return df

    # -------------------------
    # 2) CSV → DataFrame
    # -------------------------
    if csv_files:
        file = csv_files[0]
        print(f"📥 Carregando arquivo CSV: {file.name}")

        df = pd.read_csv(file)

        print(f"📊 RAW carregado (CSV) — shape: {df.shape}")
        return df

    # -------------------------
    # 3) Nada encontrado
    # -------------------------
    raise FileNotFoundError(
        f"Nenhum arquivo .npy ou .csv encontrado em: {raw_path}"
    )


# ==================================================
# Teste rápido (rodar: python src/eda/loader.py)
# ==================================================
if __name__ == "__main__":
    cfg = load_config()
    df = load_raw_data(cfg)
    print("\nPré-visualização:")
    print(df.head())