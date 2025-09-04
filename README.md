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

This structure provides both **fault-free baselines** and **fault-injected datasets**, enabling effective benchmarking of anomaly detection methods.

