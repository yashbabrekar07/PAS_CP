# Statistical Analysis of Digital Payment Habits Among Students

## Overview
This repository contains the complete statistical analysis, primary survey dataset, and interactive web dashboard investigating digital payment habits, transaction arrival rates, and spending behaviors among 100 college students.

---

## Repository Structure

```
├── digital_payments_students.csv  <- Primary survey response dataset (N=100)
├── dashboard.html                 <- Interactive research dashboard (Tailwind + Chart.js)
├── run_dashboard.py               <- Python launcher script (zero pip dependencies)
├── analysis.py                    <- Standalone Python statistical computation script
├── PROJECT_REPORT.md              <- Full academic project report with mathematical derivations
├── analysis_guide_excel.md        <- Step-by-step formula replication guide for Excel & Sheets
└── README.md                      <- Project documentation
```

---

## How to Run & View

### 1. View the Interactive Dashboard (Fastest)
Simply double-click `dashboard.html` in your file explorer to open it in your browser (Google Chrome, Edge, Safari, Firefox). It runs 100% client-side with zero setup.

Or run via Python:
```bash
python run_dashboard.py
```

### 2. Standalone Python Statistical Script
```bash
pip install pandas numpy scipy matplotlib seaborn
python analysis.py
```

### 3. Microsoft Excel / Google Sheets
Open `digital_payments_students.csv` in Excel and refer to `analysis_guide_excel.md` for exact formulas.
