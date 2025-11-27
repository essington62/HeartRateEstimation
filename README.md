# Heart Rate Estimation

Professional machine learning pipeline for heart rate estimation using physiological signals
(**PPG and IMU**) with a clean, modular Python architecture.

This project is an evolution from notebook-based experiments into a
production-oriented pipeline with:

- Python modules (`.py`)
- Centralized configuration via `YAML`
- Phase-oriented architecture
- Full reproducibility
- Future MLflow integration
- Focus on ML engineering best practices

---

## 📁 Project Structure

HeartRateEstimation/

│
├── src/

│   ├── eda/                  # EDA modules

│   │   ├── loader.py

│   │   ├── eda_basic.py

│   │   ├── eda_stats.py

│   │   ├── feature_engineering.py

│   │   ├── splitter.py

│   │   └── oversampling.py

│   │

│   ├── pipelines/            # Training and experiment pipelines

│   │   ├── train_phase0_2.py

│   │   ├── train_phase4.py

│   │   └── train_ensemble.py

│   │
│   └── utils/

│       └── config_loader.py

│

├── Phase0_Phase2/            

│   ├── eda/

│   ├── data/

│   ├── model/

│   └── results/

│


├── Phase4/                   


│   ├── eda/

│   ├── data/

│   ├── model/

│   └── results/

│

├── Ensemble/                 # Ensemble outputs (no EDA here)

│   ├── model/

│   └── results/

│

├── data/                     # RAW data (not versioned in Git)

│

├── config.yaml               # Central pipeline configuration

├── requirements.txt

└── README.md

---

## ⚙ Environment Setup

### 1. Create virtual environment

python3 -m venv venv

source venv/bin/activate

### 2. Install dependencies

pip install -r requirements.txt

## Architecture Philosophy

| Layer           | Purpose                             |
|-----------------|-------------------------------------|
| `src/eda`       | Data exploration and analysis       |
| `src/pipelines` | Training and experiments            |
| `config.yaml`   | Execution governance                |
| `Phase*/`       | Phase-based outputs                 |


## Roadmap
	•	RAW data loader
	•	Basic EDA
	•	Statistical EDA
	•	Feature Engineering
	•	Train / Test split
	•	Oversampling strategies
	•	MLflow experiment tracking
	•	Training pipelines
	•	Ensemble modeling

Experiment Tracking with MLflow

MLflow is used to track:

	•	dataset version
	•	training parameters
	•	feature configurations
	•	split statistics
	•	oversampling settings
	•	evaluation metrics
	•	trained models
	•	comparison across experiments and phases



## Reproducibility

This project is fully reproducible through:

	•	environment via requirements.txt
	•	execution configuration via config.yaml
	•	deterministic pipelines
	•	phase-controlled outputs

  Roadmap
  
	•	Project restructuring
	•	YAML-based configuration
	•	Modular EDA
	•	Statistical EDA
	•	Feature Engineering pipeline
	•	Train / Test pipelines
	•	MLflow logging
	•	Ensemble
	•	Model validation
	•	Deployment API (FastAPI)
