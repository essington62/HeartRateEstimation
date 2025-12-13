# Heart Rate Estimation — Governed ML Pipeline

A **Heart Rate (HR) Estimation** project based on **PPG + IMU** signals, with a strong focus on  
**robustness under motion**, **experimental governance**, and **reproducibility**.

The project is developed using an iterative, *round-based* approach, preserving a complete history
of decisions, results, adjustments, and lessons learned over time.

---

## 🎯 Project Objectives

- Estimate HR across different physiological domains:
  - **Rest / Light Activity (Phases 0 and 2)**
  - **Exercise / High Effort (Phase 4)**
- Reduce Mean Absolute Error (MAE) in a **controlled and explainable** manner
- Build **domain-specialist models**
- Prepare the foundation for a **Governed Ensemble**
- Ensure **full traceability** of the experimental process

---

## 🧠 Core Principles

### ✔ Governance from Day One
- No data, trained model, or result is overwritten
- Every experiment produces:
  - artifacts named by *round*
  - `.txt` reports with metrics, errors, and decisions
- Complete history preserved locally

### ✔ Parameterized Notebooks
- Reusable notebooks
- Explicit parameters (round, prefixes, paths)
- Easy re-execution and comparison across versions

### ✔ Living Knowledge Base (NotebookLM)
- Consolidation of reports, metrics, analyses, and decisions
- Ability to:
  - compare rounds
  - identify critical failures
  - justify technical decisions
- Acts as the **project’s memory**, not just static documentation

---

## 🗂 Repository Structure

```text
HeartRateEstimation/
├── assessment/          # Initial audits and dataset exploration
│   └── assessment.ipynb
│
├── rest/                # Full pipeline for HR at rest
│   ├── config/
│   ├── eda/
│   ├── notebooks/
│   ├── utils/
│   └── README.md
│
├── exercise/            # Pipeline for HR under intense exercise
│   ├── config/
│   ├── eda/
│   ├── notebooks/
│   ├── utils/
│   └── README.md
│
├── Ensemble/            # Strategy for combining specialist models
│   ├── notebooks/
│   └── utils/
│
├── utils/               # Shared utility functions
│   └── __init__.py
│
├── .gitignore
└── README.md