# Step-by-Step Excel & Google Sheets Replication Guide

This guide provides exact formulas to replicate the entire statistical project directly in **Microsoft Excel** or **Google Sheets** using the primary survey dataset `digital_payments_students.csv`.

---

## 1. Column Layout in `digital_payments_students.csv`

| Column | Header | Description |
| :---: | :--- | :--- |
| **A** | `Timestamp` | Form submission time |
| **B** | `Student_Name` | Respondent name |
| **C** | `Gender` | Male / Female |
| **D** | `Department` | Academic branch (CSE, ECE, Mech, IT, etc.) |
| **E** | `Year_of_Study` | 1st to 4th Year |
| **F** | `Accommodation` | Hostel / Day Scholar |
| **G** | `Primary_App` | Google Pay, PhonePe, Paytm |
| **H** | `Daily_Transactions_Count` | Number of daily transactions (discrete) |
| **I** | `Monthly_Digital_Spend` | Total monthly digital expenditure (INR) |
| **J** | `Digital_Payment_Pct` | Share of total spend paid digitally (%) |
| **K** | `Impulse_Spending` | High / Low |
| **L** | `Payment_Failures_Past_Month`| Server / network timeouts |

---

## 2. Descriptive Statistics Formulas

Assume the dataset spans rows `2` to `101`:

| Metric | Excel / Google Sheets Formula | Calculated Value |
| :--- | :--- | :--- |
| **Mean Monthly Spend** | `=AVERAGE(I2:I101)` | ₹3,822.00 |
| **Median Monthly Spend** | `=MEDIAN(I2:I101)` | ₹3,950.00 |
| **Standard Deviation** | `=STDEV.S(I2:I101)` | ₹1,350.76 |
| **Variance** | `=VAR.S(I2:I101)` | 1,824,561.62 |
| **Q1 (25th Percentile)** | `=QUARTILE.INC(I2:I101, 1)` | ₹2,600.00 |
| **Q3 (75th Percentile)** | `=QUARTILE.INC(I2:I101, 3)` | ₹4,800.00 |
| **Interquartile Range (IQR)**| `=QUARTILE.INC(I2:I101, 3) - QUARTILE.INC(I2:I101, 1)` | ₹2,200.00 |
| **Mean Daily Transactions ($\lambda$)** | `=AVERAGE(H2:H101)` | 3.33 tx/day |
| **Variance Daily Transactions** | `=VAR.S(H2:H101)` | 1.96 |

---

## 3. Two-Sample $t$-Test (Hostelers vs. Day Scholars)

1. Separate hostellers' spend and day scholars' spend into two ranges (or use `=FILTER()` in Excel 365 / Google Sheets):
   * Hostel Spend ($n_1 = 56$): `=FILTER(I2:I101, F2:F101="Hostel")`
   * Day Scholar Spend ($n_2 = 44$): `=FILTER(I2:I101, F2:F101="Day Scholar")`
2. **Two-tailed $t$-Test (Equal Variances):**
   ```excel
   =T.TEST(range_hostel, range_day_scholar, 2, 2)
   ```
   * Result: $p < 0.00001$ ($1.62 \times 10^{-32}$) $\implies$ Reject $H_0$.

---

## 4. Pearson Correlation and Simple Linear Regression

* **Pearson Correlation ($r$):**
  ```excel
  =CORREL(H2:H101, I2:I101)
  ```
  Result: `0.9745` (strong positive linear correlation).
* **Coefficient of Determination ($R^2$):**
  ```excel
  =RSQ(I2:I101, H2:H101)
  ```
  Result: `0.9496` ($95.0\%$ variance explained).
* **Slope ($\beta_1$):**
  ```excel
  =SLOPE(I2:I101, H2:H101)
  ```
  Result: `940.05`
* **Intercept ($\beta_0$):**
  ```excel
  =INTERCEPT(I2:I101, H2:H101)
  ```
  Result: `691.62`

---

## 5. Poisson Distribution Fitting

To compute theoretical Poisson probabilities for transaction frequency $k \in \{0, 1, 2, 3, 4, 5, 6\}$ where $\lambda = 3.33$:
* Probability $P(X = k)$:
  ```excel
  =POISSON.DIST(k_cell, 3.33, FALSE)
  ```
* Expected Frequency ($N = 100$):
  ```excel
  =POISSON.DIST(k_cell, 3.33, FALSE) * 100
  ```

---

## 6. Chi-Square Test of Independence ($\chi^2$)

Create a $2 \times 2$ table of Observed Counts:
| | High Impulse | Low Impulse | Total |
| :--- | :--- | :--- | :--- |
| **Digital Pct > 80%** | 43 | 8 | 51 |
| **Digital Pct $\le$ 80%** | 5 | 44 | 49 |
| **Total** | 48 | 52 | 100 |

Compute the Expected table using: $\text{Expected} = \frac{\text{Row Total} \times \text{Column Total}}{\text{Grand Total}}$.
* Expected Table:
  * Cell (1,1): `(48 * 51) / 100 = 24.48`
  * Cell (1,2): `(48 * 49) / 100 = 23.52`
  * Cell (2,1): `(52 * 51) / 100 = 26.52`
  * Cell (2,2): `(52 * 49) / 100 = 25.48`

Run the Chi-Square test:
```excel
=CHISQ.TEST(observed_range, expected_range)
```
* Result: $p = 1.21 \times 10^{-13}$ (Reject $H_0$).
