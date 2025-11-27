import os
import yaml

REQUIREMENTS_CONTENT = """numpy==2.0.2
pandas==2.2.2
scikit-learn==1.6.1
xgboost==3.1.2
lightgbm==4.6.0
matplotlib==3.10.0
seaborn==0.13.2
pyyaml==6.0.2
mlflow==2.12.1
tqdm==4.66.4
joblib==1.4.2
fastapi==0.115.0
uvicorn==0.30.0
"""

def create_structure_from_yaml(yaml_file):
    with open(yaml_file, "r") as f:
        config = yaml.safe_load(f)

    base_path = config["base_path"]
    folders = config["folders"]

    print(f"\n📁 Criando estrutura do projeto em:\n{base_path}\n")

    # Criar pastas e arquivos definidos no YAML
    for folder in folders:
        full_path = os.path.join(base_path, folder)

        # Caso seja arquivo (ex: results.txt)
        if "." in os.path.basename(folder):
            os.makedirs(os.path.dirname(full_path), exist_ok=True)
            if not os.path.exists(full_path):
                open(full_path, "w").close()
                print(f"📝 Arquivo criado: {full_path}")
            else:
                print(f"✔ Arquivo já existe: {full_path}")
        else:
            os.makedirs(full_path, exist_ok=True)
            print(f"📂 Pasta criada: {full_path}")

    # Criar requirements.txt no raiz
    requirements_path = os.path.join(base_path, "requirements.txt")
    if not os.path.exists(requirements_path):
        with open(requirements_path, "w") as req_file:
            req_file.write(REQUIREMENTS_CONTENT)
        print(f"📌 requirements.txt criado em: {requirements_path}")
    else:
        print(f"✔ requirements.txt já existe: {requirements_path}")

    print("\n✅ Estrutura concluída com sucesso!\n")


if __name__ == "__main__":
    create_structure_from_yaml("template_xgboost_ensemble.yaml")