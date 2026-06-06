# Engine ML Prediction System
# Main Author Dr. Mahesh Nadda, Dr. Aksaky Jain
# Code is developed on the main experimental data
## Complete Guide — Installation, Execution & Troubleshooting

---

## Project Overview

A complete Python machine learning project for engine experimental data analysis,
including Monte Carlo simulation, 15 ML models, and a professional desktop GUI.

**Inputs :** Engine Load (EL, %), Injection Timing (IT, ° BTDC)
**Outputs:** BTE, EGT, PCP, NHRR, ID, CO, HC, CO₂, NOx

---

## Project Structure

```
EngineML_Project/
│
├── run_all.py                        ← Master run script
├── requirements.txt                  ← Python dependencies
│
├── Data/
│   ├── engine_original_data.csv      ← Original 45-row dataset
│   └── augmented_dataset.csv         ← Generated after Task 1
│
├── Models/
│   ├── scaler_X.joblib               ← Input feature scaler
│   ├── scaler_y.joblib               ← Output target scaler
│   ├── best_model.json               ← Best model name & R²
│   ├── LinearRegression.joblib
│   ├── Ridge.joblib
│   ├── Lasso.joblib
│   ├── ElasticNet.joblib
│   ├── RandomForest.joblib
│   ├── ExtraTrees.joblib
│   ├── GradientBoosting.joblib
│   ├── XGBoost.joblib
│   ├── LightGBM.joblib
│   ├── CatBoost.joblib
│   ├── SVR.joblib
│   ├── KNN.joblib
│   ├── MLP_sklearn.joblib
│   ├── ANN.keras / ANN.h5
│   └── DNN.keras / DNN.h5
│
├── Results/
│   ├── Task1/
│   │   ├── statistical_summary.csv
│   │   ├── comparison_statistics.csv
│   │   ├── histogram_kde.png
│   │   ├── boxplots.png
│   │   ├── correlation_heatmaps.png
│   │   ├── ecdf_comparison.png
│   │   ├── pairplot_key_vars.png
│   │   ├── scatter_EL_IT.png
│   │   └── ks_statistics.png
│   │
│   └── Task2/
│       ├── model_comparison.csv
│       ├── model_comparison_bar.png
│       ├── r2_heatmap.png
│       ├── loss_curves.png
│       ├── parity_*.png
│       ├── residuals_*.png
│       ├── feature_importance.png
│       └── shap_summary_*.png
│
├── GUI/
│   └── engine_gui.py                 ← PyQt5 desktop application
│
├── Reports/                          ← PDF/Excel exports (auto-created)
│
└── Scripts/
    ├── task1_monte_carlo.py
    ├── task2_ml_models.py
    └── load_models.py
```

---

## Prerequisites

- **Python 3.11 or higher** ([python.org](https://www.python.org/downloads/))
- **pip** (comes with Python)
- **4 GB RAM minimum** (8 GB recommended for DNN training)
- **Windows 10/11** (also works on Linux/macOS)

---

## Installation

### Step 1 — Clone / Download the Project

```
Place the EngineML_Project folder anywhere on your PC, e.g.:
  C:\Users\YourName\EngineML_Project\
```

### Step 2 — Open a Command Prompt / PowerShell

```
Press Win+R → type cmd → Enter
cd C:\Users\YourName\EngineML_Project
```

### Step 3 — (Recommended) Create a Virtual Environment

```cmd
python -m venv venv
venv\Scripts\activate
```

### Step 4 — Install Dependencies

```cmd
pip install -r requirements.txt
```

> **Note:** TensorFlow installation may take 5–10 minutes.
> For CPU-only systems, use `tensorflow-cpu` instead of `tensorflow`.

---

## Running the Project

### Option A — Run Everything (Recommended for first-time)

```cmd
python run_all.py
```

This runs Task 1 and Task 2 automatically (approximately 5–10 minutes).

### Option B — Run Tasks Individually

```cmd
python run_all.py --task 1      # Monte Carlo Simulation & Analysis
python run_all.py --task 2      # ML Model Training
```

### Option C — Launch the GUI

After Tasks 1 and 2 are complete:

```cmd
python run_all.py --gui
# or directly:
python GUI\engine_gui.py
```

---

## GUI Usage Guide

### Loading Models

Models load automatically when the GUI starts. You'll see "X models loaded" in the status bar.

### Making a Prediction

1. Select a model from the dropdown (e.g., `MLP_sklearn` or `RandomForest`)
2. Set **EL** (Engine Load %) using the spinner or slider
3. Set **IT** (Injection Timing °BTDC) using the spinner or slider
4. Click **🔮 Predict**
5. Results appear in the table, bar chart, and radar chart

### Comparing Models

1. Run a prediction with Model A
2. Click **➕ Add Current Prediction to Comparison** on the Compare tab
3. Switch to a different model, run another prediction, add to comparison
4. View side-by-side bar charts for all outputs

### Exporting Results

| Action | How |
|--------|-----|
| Export to Excel | File → Save Predictions (Excel) |
| Export PDF Report | Click 📄 Export PDF or File → Export PDF Report |
| Save to comparison history | Click 💾 Save |

---

## Machine Learning Models

| Model | Type | Notes |
|-------|------|-------|
| LinearRegression | Linear | Baseline |
| Ridge | Linear + L2 | Regularised |
| Lasso | Linear + L1 | Sparse |
| ElasticNet | Linear + L1+L2 | Mixed regularisation |
| RandomForest | Ensemble | 300 trees |
| ExtraTrees | Ensemble | Extra-randomised |
| GradientBoosting | Boosting | Slow learning |
| XGBoost | Boosting | Column & row subsampling |
| LightGBM | Boosting | Leaf-wise growth |
| CatBoost | Boosting | Robust tabular |
| SVR | Kernel | RBF kernel |
| KNN | Instance | Distance-weighted |
| MLP_sklearn | Neural Net | 3-layer, sklearn |
| ANN | Deep Learning | Keras, 2 hidden layers |
| DNN | Deep Learning | Keras, 4 hidden layers + Batch Norm |

---

## Understanding Key Parameters

### Task 1 — Monte Carlo Simulation
- **Cholesky decomposition**: ensures synthetic data preserves pairwise correlations
- **KS test**: two-sample Kolmogorov–Smirnov — p > 0.05 means distributions match
- **1200 synthetic points** generated in addition to the 45 originals

### Task 2 — ML Hyperparameters
- **Learning rate (0.05)**: small LR → slower but more stable training
- **Dropout (10–20%)**: randomly zeroes neurons during training → prevents overfitting
- **Batch Normalization**: normalises layer activations → faster convergence
- **Early Stopping (patience=25)**: stops training when validation loss stagnates
- **RobustScaler**: uses median/IQR → less sensitive to outliers than StandardScaler

### Metrics Explained
| Metric | Formula | Best |
|--------|---------|------|
| R² | 1 - SS_res/SS_tot | Closer to 1 |
| MAE | mean(\|y_true - y_pred\|) | Lower |
| RMSE | √MSE | Lower |
| MAPE | mean(\|y_true-y_pred\|/\|y_true\|)×100 | Lower (%) |

---

## Troubleshooting

### "No models found" in GUI
→ Run `python run_all.py` first to train and save models.

### TensorFlow / CUDA warnings
→ These are informational only. The models run on CPU by default.
→ Add `os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"` if warnings are excessive.

### PyQt5 not installed
```cmd
pip install PyQt5 PyQt5-Qt5 PyQt5-sip
```

### CatBoost installation fails (Windows)
```cmd
pip install catboost --pre
```

### LightGBM installation fails
```cmd
pip install lightgbm --no-cache-dir
```

### Memory error during DNN training
→ Reduce `batch_size` in `task2_ml_models.py` (line `batch_size=32` → try `16`)

### ModuleNotFoundError for shap
```cmd
pip install shap
```

### GUI shows blank charts
→ Ensure `matplotlib` backend is set to `Qt5Agg` (already set in the GUI code).

---

## Loading Saved Models (Custom Code)

```python
import joblib, numpy as np

# Load scaler and model
scaler_X = joblib.load("Models/scaler_X.joblib")
scaler_y = joblib.load("Models/scaler_y.joblib")
model    = joblib.load("Models/RandomForest.joblib")

# Predict
X = np.array([[75.0, 20.0]])      # EL=75%, IT=20°
X_scaled = scaler_X.transform(X)
y_pred   = scaler_y.inverse_transform(model.predict(X_scaled))
targets  = ["BTE","EGT","PCP","NHRR","ID","CO","HC","CO2","NOx"]
print(dict(zip(targets, y_pred[0])))
```

---

## System Requirements

| Component | Minimum | Recommended |
|-----------|---------|-------------|
| Python | 3.11 | 3.12 |
| RAM | 4 GB | 8 GB |
| Storage | 2 GB | 5 GB |
| OS | Windows 10 | Windows 11 |
| GPU | Not needed | CUDA 12+ for faster training |

---

*Engine ML Prediction System — Built with Python, Scikit-Learn, TensorFlow & PyQt5*
