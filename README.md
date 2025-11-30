# DAT5501 Lab Portfolio

This repository contains weekly lab exercises for the DAT5501 module. 

---

---

## Highlights

- Implemented **unit testing** to validate calculations (Week‑1).  
- Built **GUI applications** with Tkinter and tkcalendar (Week‑3 & Week‑5).  
- Conducted a **group project** analysing global meat consumption using data from Our World in Data (https://ourworldindata.org/) (Week‑3).  
- Analysed **US election data** with fuzzy matching and histograms (Week‑5).  
- Extended **asset price analysis** to test sorting performance against *n log n* complexity (Week‑8).  
- Performed **polynomial fitting and forecasting** on global population trends, calculating χ²/dof and BIC to evaluate models (Week‑8).
- Built decision tree classifiers for 2 datasets (Car Evaluation & Mushroom data) with precision analysis (Week‑10)

---


## Folder Structure

- **Week-1**
  - `test.py` – simple print statements
  - `unit_testing_function.py` – basic function to add two numbers
  - `unit_testing_tests.py` – unit tests using `unittest`
  - GitHub activity: practiced commits, branching, and merging

- **Week-2**
  - `interest_rate.py` – compound interest calculator using loops and the Rule of 72

- **Week-3**
  - `calendar_printer.py` – CLI-based calendar printer
  - `calendar_printer_gui.py` – GUI calendar printer using Tkinter
  - **Group-Presentation/**
    - `meat_co2_analysis.py` – analysis of meat consumption vs CO₂ emissions
    - `meat_co2_data.csv` – dataset for emissions and meat consumption
    - `meat_population_analysis.py` – analysis of meat consumption vs world population
    - `meat_population_data.csv` – dataset for population and meat consumption
    
- **Week-5**
  - `duration_calculator_days.py` – CLI-based program to calculate days between two dates
  - `duration_calculator_days_gui.py` – GUI version of duration calculator (Tkinter + tkcalendar)
  - `us_election_histogram.py` – analysis of US election data with histogram plots and fuzzy matching
  - `US-2016-primary.csv` – dataset for US candidate election statistics

- **Week-8**
  - `daily_price_change_sorting.py` – daily asset price changes sorting time analysis. Plots sorting time vs n days of price changes
  - `asset_price_data.csv` – 1 year of historical Nasdaq price data 
  - `fitting_forecasting.py` – polynomial fitting and forecasting of global population data. Calculates χ² per degree of freedom and Bayesian Information Criterion (BIC) for model analysis.  
  - `population_data_owid.csv` – dataset of global population (used for 1900–present)

- **Week-10**
  - `decision_tree_car_evaluation.py` – trains a decision tree classifier on the Car Evaluation dataset from https://archive.ics.uci.edu/dataset/19/car+evaluation
  - `decision_tree_mushroom.py` – trains a decision tree classifier on the Mushroom dataset from  https://archive.ics.uci.edu/dataset/73/mushroom
  - `car.data` – sample dataset format (not directly used in code, but clarifies categorical feature values)
---

## Requirements

- Python 3.9+  
- Libraries:
  - `numpy`
  - `pandas`
  - `matplotlib`
  - `tkinter` (standard library)
  - `fuzzywuzzy` (Week-5)
  - `tkcalendar` (for GUI date picker, Week-5)
  - `time` (standard library, for timing operations, Week-8)
  - `scikit-learn` (for decision tree classifiers, metrics, and plotting, Week-10)
  - `ucimlrepo` (to fetch datasets from the UCI Machine Learning Repository, Week-10)

Install dependencies:
```bash
pip install numpy pandas matplotlib fuzzywuzzy tkcalendar scikit-learn ucimlrepo
```
---

## How to Run

Clone the repository:
```bash
git clone https://github.com/RY4N-L/DAT5501-WeeklyLabWork.git
cd DAT5501-WeeklyLabWork
```
Navigate to a week folder and run the script:

```bash
cd Week-2
python interest_rate.py
```
PLEASE NOTE: for files in the Week 3 Group Presentation folder, navigate to Week-3/Group-Presentation and run scripts:
```bash
cd Week-3/Group-Presentation
python meat_co2_analysis.py
```

---
## Outstanding Tasks / To‑Do
- [ ] Extend GUI functionality with additional features (e.g., error handling, styling, Week-3 and Week-5)
- [ ] Complete parameter extraction and covariance matrix analysis for the best polynomial model (Week‑8)  
- [ ] Estimate uncertainties in parameter values (Week-8)
- [ ] Explore alternative models (e.g., exponential fits) for forecasting (Week-8)
- [ ] Encode categorical features in decision tree classifier to observe for imporvements (Week-10)
- [ ] Compare precision, recall, and F1 score across various depths (Week-10)
- [ ] Add more unit tests for robustness across all weeks

---
