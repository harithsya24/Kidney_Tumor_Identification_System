# Kidney Tumor Identification System

A state-of-the-art Deep Learning application designed to assist medical professionals in the early detection and classification of kidney tumors from CT scan images. By leveraging Convolutional Neural Networks (CNNs) and MLOps best practices, this system provides accurate, automated diagnostics to reduce the workload on radiologists and improve patient outcomes.

---

## Core Problems Solved

- **Manual Diagnosis Fatigue**: Reduces human error associated with reviewing thousands of CT scans.
- **Speed & Scalability**: Provides instant analysis results, scalable via cloud deployment.
- **Standardization**: Ensures consistent classification criteria across different medical facilities.

---

## System Architecture

The project follows a modular pipeline architecture, ensuring reproducibility and scalability.

### High-Level Components

1. **Data Ingestion** — Automated download and extraction of CT scan datasets.
2. **Data Validation** — Integrity checks to ensure input data meets training requirements.
3. **Model Training (DVC)**
   - **Base Model**: VGG16 pre-trained on ImageNet
   - **Training**: Fine-tuning on the kidney CT scan dataset
   - **Evaluation**: Accuracy and Loss tracked via MLflow + DagsHub
4. **Web Serving** — Flask-based REST API for real-time predictions.
5. **CI/CD & Deployment** — GitHub Actions, Docker, AWS ECR, and AWS EC2.

---

## Technical Stack

| Category | Tools |
|---|---|
| Language | Python 3.10 |
| Deep Learning | TensorFlow, Keras |
| Web Framework | Flask |
| MLOps | DVC, MLflow, DagsHub |
| Data | Pandas, NumPy |
| Infrastructure | Docker, AWS EC2, AWS ECR, GitHub Actions |

---

## Key Features

- **End-to-End Pipeline**: Fully scriptable training and inference process.
- **Reproducibility**: DVC ensures every data version and model experiment is tracked.
- **Experiment Tracking**: MLflow integration for comparing hyperparameters across runs.
- **Cloud Native**: Containerized and deployable on AWS.
- **User-Friendly UI**: Simple web interface for uploading CT scans and viewing results.

---

## How to Run

### STEP 01 — Clone the Repository
```bash
git clone https://github.com/harithsya24/Kidney_Tumor_Identification_System
cd Kidney_Tumor_Identification_System
```

### STEP 02 — Create and Activate Conda Environment
```bash
conda create -n kidney python=3.10 -y
conda activate kidney
```

### STEP 03 — Install Requirements
```bash
pip install -r requirements.txt
pip install -e .
```

### STEP 04 — Run the Application
```bash
python app.py
```

Open your browser at `http://localhost:5000`

---

## DVC Pipeline

```bash
dvc init
dvc repro
dvc dag
```

> Always run with `PYTHONPATH=$PWD dvc repro` if you encounter module import errors.

---

## MLflow & DagsHub Tracking

### Option 1 — Auto configuration (recommended)
```python
import dagshub
dagshub.init(repo_owner='harithsya24', repo_name='Kidney_Tumor_Identification_System', mlflow=True)
```

### Option 2 — Manual environment variables
```bash
export MLFLOW_TRACKING_URI=https://dagshub.com/harithsya24/Kidney_Tumor_Identification_System.mlflow
export MLFLOW_TRACKING_USERNAME=harithsya24
export MLFLOW_TRACKING_PASSWORD=<your_dagshub_token>
```

View experiments at: https://dagshub.com/harithsya24/Kidney_Tumor_Identification_System/experiments

---


## Workflows (Development)

1. Update `config.yaml`
2. Update `secrets.yaml` *(optional)*
3. Update `params.yaml`
4. Update the entity
5. Update the configuration manager in `src/config`
6. Update the components
7. Update the pipeline
8. Update `main.py`
9. Update `dvc.yaml`

---

## About MLflow & DVC

**MLflow**
- Production-grade experiment tracking
- Logs metrics, parameters, and model artifacts
- Remote tracking via DagsHub

**DVC**
- Lightweight data and pipeline versioning
- Tracks large files (datasets, models) outside of Git
- Orchestrates reproducible ML pipelines via `dvc repro`

---

## Future Enhancements

- **Advanced Models**: Experiment with ResNet50, InceptionV3, or Vision Transformers.
- **Explainability**: Integrate Grad-CAM to visualize tumor regions on CT scans.
- **Mobile App**: Develop a mobile-friendly frontend for remote access.
- **Multi-Class Classification**: Expand to identify specific tumor subtypes (e.g., Angiomyolipoma vs. Renal Cell Carcinoma).