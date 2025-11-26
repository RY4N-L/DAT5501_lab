# DAT5501 Lab Portfolio

This repository contains weekly lab exercises for the DAT5501 module.  
Each folder includes Python scripts demonstrating different programming concepts and tasks.

---

## 📂 Folder Structure

- **Week-1**
  - `test.py` – simple print statements
  - `unit_testing_function.py` – basic function to add two numbers
  - `unit_testing_tests.py` – unit tests using `unittest`
  - *GitHub activity*: practice with commits, branching, and merging

- **Week-2**
  - `interest_rate.py` – compound interest calculator using loops and the Rule of 72

- **Week-3**
  - `calendar_printer.py` – terminal-based calendar printer
  - `calendar_printer_gui.py` – GUI calendar printer using Tkinter
  - **Group-Presentation/**
    - `meat_co2_analysis.py` – analysis of meat consumption vs CO₂ emissions
    - `meat_co2_data.csv` – dataset for emissions and meat consumption
    - `meat_population_analysis.py` – analysis of meat consumption vs world population
    - `meat_population_data.csv` – dataset for population and meat consumption
    
- **Week-5**
  - `duration_calculator_days.py` – CLI program: calculate days between two dates
  - `duration_calculator_days_gui.py` – GUI version of duration calculator (Tkinter + tkcalendar)
  - `US_election_histogram.py` – analyse US election data and plot histograms
  - `US-2016-primary.csv` – dataset with state, county, candidate, votes, fractions

- **Week-8**
  - `daily_price_change_sorting.py` – extended asset price analysis  
    - Calculates daily price changes  
    - Times sorting operations for n = 7 to 365 days  
    - Plots sorting time vs n days compared to *n log n* distribution  
  - `asset_price_data.csv` – 1 year of historical Nasdaq price data  
  - `fitting_forecasting.py` – polynomial fitting and forecasting of global population data  
    - Fits polynomials of order 1–9 to sub-sampled data  
    - Forecasts 10 years into the future and compares with reality  
    - Calculates χ² per degree of freedom and Bayesian Information Criterion (BIC)  
    - Plots χ²/dof and BIC vs polynomial order  
    - Identifies best model and covariance matrix for parameters  
  - `population_data_owid.csv` – dataset of global population (1900–present)

## 📂 Repository Structure (Tree View)

DAT5501_lab/
│
├── Week-1/
│   ├── test.py
│   ├── unit_testing_function.py
│   └── unit_testing_tests.py
│
├── Week-2/
│   └── interest_rate.py
│
├── Week-3/
│   ├── calendar_printer.py
│   ├── calendar_printer_gui.py
│   └── Group-Presentation/
│       ├── meat_co2_analysis.py
│       ├── meat_co2_data.csv
│       ├── meat_population_analysis.py
│       └── meat_population_data.csv
│
├── Week-5/
│   ├── duration_calculator_days.py
│   ├── duration_calculator_days_gui.py
│   ├── US_election_histogram.py
│   └── US-2016-primary.csv
│
└── Week-8/
    ├── daily_price_change_sorting.py
    ├── asset_price_data.csv
    ├── fitting_forecasting.py
    └── population_data_owid.csv

---

## ⚙️ Requirements

- Python 3.9+  
- Libraries:
  - `numpy`
  - `pandas`
  - `matplotlib`
  - `fuzzywuzzy`
  - `tkinter` (standard library)
  - `tkcalendar` (for GUI date picker)
  - `time` (standard library, for timing operations)

Install dependencies:
```bash
pip install numpy pandas matplotlib fuzzywuzzy tkcalendar
```
---

## 🚀 How to Run

Clone the repository:
```bash
git clone https://github.com/RY4N-L/DAT5501_lab.git
cd DAT5501_lab
```
Navigate to a week folder and run the script:

```bash
cd Week-2
python interest_rate.py
```
For GUI programs (e.g., Week 3):
```bash
cd Week-3
python calendar_printer_gui.py
```


