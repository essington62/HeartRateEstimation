from utils.config_loader import load_config

cfg = load_config()

print("CONFIG CARREGADO!")
for k, v in cfg["paths"].items():
    print(f"{k}: {v}")