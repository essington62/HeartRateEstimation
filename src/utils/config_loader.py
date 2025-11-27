import yaml
from pathlib import Path

def load_config(config_path="config.yaml"):
    # Caminho do diretório onde este arquivo está (src/utils)
    loader_dir = Path(__file__).resolve().parent

    # raiz do projeto = subir 2 níveis (src → root)
    project_root = loader_dir.parent.parent

    config_file = project_root / config_path

    if not config_file.exists():
        raise FileNotFoundError(f"config.yaml não encontrado em: {config_file}")

    with open(config_file, "r") as f:
        cfg = yaml.safe_load(f)

    base = Path(cfg["paths"]["base"]).resolve()

    cfg["paths"]["raw"] = base / cfg["paths"]["raw"]

    phase_name = cfg["phase"]["active_phase"]
    phase_root = base / phase_name

    cfg["paths"]["processed"] = phase_root / "data" / "processed"
    cfg["paths"]["split"]     = phase_root / "data" / "split"
    cfg["paths"]["results"]   = phase_root / "results"
    cfg["paths"]["models"]    = phase_root / "model"
    cfg["paths"]["notebooks"] = phase_root / "notebooks"

    for p in cfg["paths"].values():
        Path(p).mkdir(parents=True, exist_ok=True)

    return cfg