# Heart Rate Estimation — Governed ML Pipeline

Projeto de **Estimativa de Frequência Cardíaca (HR)** a partir de sinais **PPG + IMU**, 
com foco em **robustez sob movimento**, **governança experimental** e **reprodutibilidade**.

O projeto foi desenvolvido com uma abordagem iterativa por *rounds*, mantendo histórico completo
de decisões, resultados, ajustes e aprendizados ao longo do tempo.

---

## 🎯 Objetivos do Projeto

- Estimar HR em diferentes domínios fisiológicos:
  - **Repouso / Atividade Leve (Phases 0 e 2)**
  - **Exercício / Esforço Intenso (Phase 4)**
- Reduzir erro médio absoluto (MAE) de forma **controlada e explicável**
- Construir modelos **especialistas por domínio**
- Preparar a base para um **Ensemble Governado**
- Garantir **rastreabilidade completa** do processo experimental

---

## 🧠 Princípios-Chave

### ✔ Governança desde o início
- Nenhum dado, modelo treinado ou resultado é versionado
- Todo experimento gera:
  - artefatos nomeados por *round*
  - relatórios `.txt` com métricas, erros e decisões
- Histórico completo preservado localmente

### ✔ Notebooks parametrizados
- Notebooks reutilizáveis
- Parâmetros explícitos (round, prefixos, caminhos)
- Fácil reexecução e comparação entre versões

### ✔ Base de Conhecimento Viva (NotebookLM)
- Relatórios, métricas, análises e decisões consolidados
- Capacidade de:
  - cruzar rounds
  - identificar falhas críticas
  - justificar decisões técnicas
- Funciona como **memória do projeto**, não apenas documentação estática

---

## 🗂 Estrutura do Repositório

```text
HeartRateEstimation/
├── assessment/          # Auditorias iniciais e exploração do dataset
│   └── assessment.ipynb
│
├── repouso/             # Pipeline completo para HR em repouso
│   ├── config/
│   ├── eda/
│   ├── notebooks/
│   ├── utils/
│   └── README.md
│
├── exercicio/           # Pipeline para HR sob exercício intenso
│   ├── config/
│   ├── eda/
│   ├── notebooks/
│   ├── utils/
│   └── README.md
│
├── Ensemble/            # Estratégia de combinação de modelos especialistas
│   ├── notebooks/
│   └── utils/
│
├── utils/               # Funções utilitárias compartilhadas
│   └── __init__.py
│
├── .gitignore
└── README.md