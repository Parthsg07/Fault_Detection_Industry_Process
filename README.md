# Fault Detection in Industrial Process using TEP Dataset 

## Overview

This project implements an anomaly detection framework on the **Tennessee Eastman Process (TEP) dataset**, a benchmark for process monitoring and fault diagnosis. Using an ensemble of **Linear regression models** built in Python, the approach reconstructs process variables under normal operating conditions and quantifies deviations through reconstruction loss to detect faults. The workflow integrates data preprocessing, ensemble modeling, anomaly detection, and visualization, demonstrating a robust and interpretable method for identifying abnormal process behavior in complex chemical systems.

## Accessing the Dataset  
The dataset can be accessed from Kaggle:  
[Tennessee Eastman Process Simulation Dataset (Kaggle)](https://www.kaggle.com/datasets/averkij/tennessee-eastman-process-simulation-dataset?resource=download&select=TEP_FaultFree_Testing.RData)  

## Dataset Description  

The project uses the **Tennessee Eastman Process (TEP) Simulation Dataset**, a widely adopted benchmark for fault detection and process monitoring.  

- Each `.RData` file is an external representation of an R dataframe that can be loaded into R or read in Python (via `pyreadr`).  
- Variables available:  
  - `fault_free_training`  
  - `fault_free_testing`  
  - `faulty_training`  
  - `faulty_testing`  

### Structure of DataFrames  
- **55 Columns Total**  
  - **Column 1: `faultNumber`**  
    - Encodes fault type.  
    - `0` → normal operating condition.  
    - `1–20` → different fault modes.  
  - **Column 2: `simulationRun`**  
    - Values `1–500`, representing different random seeds for simulation.  
    - Training vs. testing datasets use non-overlapping seeds.  
  - **Column 3: `sample`**  
    - Index of time-steps.  
    - Training: `1–500` samples (≈25 hours).  
    - Testing: `1–960` samples (≈48 hours).  
    - Fault introduced after 1 hour in training and 8 hours in testing datasets.  
  - **Columns 4–55: Process Variables**  
    - 52 process variables (measurements and manipulated variables).  
    - Retain original TEP variable names.  
## Preprocessing  

- Loaded the Tennessee Eastman Process `.RData` files using the `pyreadr` library.  
- Combined **fault-free** and **faulty** datasets for unified processing.  
- Standardized all process variables (columns 4–55) using `StandardScaler` from scikit-learn to ensure zero-mean and unit variance.  
- Created separate subsets for:  
  - Fault-free data (baseline for reconstruction).  
  - Faulty data (evaluation of anomaly detection).  

## Modeling Approach  

- Implemented an **ensemble of Linear regression models** to reconstruct process variables:  
  - `LinearRegression`  
  - `HistGradientBoostingRegressor`  
- For each variable, trained multiple regressors to predict it using the remaining variables as features.  
- Combined predictions from the ensemble to reconstruct the full multivariate time-series.  
- Designed a modular workflow with functions for:  
  - Training and storing ensemble models.  
  - Reconstructing variables from ensemble predictions.  
  - Exporting results for downstream analysis.  

## Anomaly Detection  

- Defined **reconstruction loss** as the deviation between reconstructed signals and actual process data.  
- Evaluated reconstruction error for:  
  - **Fault-free data** → low reconstruction loss.  
  - **Faulty data** → significantly higher loss.  
- Used reconstruction error as the anomaly detection criterion, with clear separation between normal and fault conditions.  
- Quantified anomalies across multiple fault types (fault numbers 1–20) to demonstrate generalizability of the approach.  


## Visualization and Analysis  

- Generated **time-series plots** of:  
  - Actual vs. reconstructed variables (to evaluate accuracy).  
  - Reconstruction loss for fault-free and faulty conditions.  
- Visualized ensemble model performance across different fault numbers.  
- Exported computed metrics (e.g., reconstruction error, R² scores, process variable deviations) for further analysis.  
- Highlighted the correlation between increasing reconstruction error and onset of faults, demonstrating the method’s robustness for anomaly detection.  

## Results  

- Ensemble regression models successfully reconstructed fault-free process data with high fidelity.  
- Reconstruction loss remained consistently low under normal operating conditions but increased sharply when faults were introduced.  
- The anomaly detection framework was able to separate fault-free and faulty runs across multiple fault types, validating its robustness.  
- Time-series evaluation of selected process variables showed strong agreement between reconstructed and actual values in the absence of faults.  
