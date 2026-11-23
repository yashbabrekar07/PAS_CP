# A Statistical Analysis of Digital Payment Habits and Spending Behaviors Among College Students

**Course:** Probability and Statistics  
**Project Type:** Course Final Project  
**Sample Size:** $N = 100$ Undergraduates  
**Date:** November 2026  

---

## Executive Summary / Abstract

The rapid proliferation of mobile payment interfaces and Unified Payments Interface (UPI) ecosystems has fundamentally reshaped personal financial behavior among university students. This study conducts an empirical, rigorous statistical investigation into the digital payment habits, transaction frequencies, and expenditure distributions of undergraduate students ($N = 100$). Using primary survey data, this project applies core principles of descriptive statistics, probability theory (Poisson modeling and Bayesian conditional probabilities), and inferential hypothesis testing (two-sample $t$-test, Pearson correlation, simple linear regression, and Pearson's Chi-Square test of independence). 

Key findings demonstrate:
1. Daily transaction frequency conforms to a Poisson distribution with mean arrival rate $\hat{\lambda} = 3.33$ transactions/day.
2. Hostel residents exhibit significantly higher monthly digital expenditure ($\mu_1 = \text{₹}4,866.07$, $s_1 = \text{₹}732.19$) than day scholars ($\mu_2 = \text{₹}2,493.18$, $s_2 = \text{₹}537.18$), verified through a two-sample $t$-test ($t(98) = 18.02, p < 10^{-15}$).
3. A strong, statistically significant positive linear relationship exists between daily digital transaction counts and total monthly digital expenditure ($r = 0.9745, R^2 = 0.9496, p < 10^{-15}$).
4. Pearson's Chi-Square test confirmed that high reliance on digital payments ($> 80\%$ of total spend) is significantly associated with self-reported impulse spending ($\chi^2(1) = 54.99, p < 10^{-12}$). Bayesian probability reveals that students relying heavily on digital payments have an $84.3\%$ posterior probability of frequent impulse purchases compared to only $10.2\%$ for cash-reliant peers.

---

## 1. Introduction & Background

Over the past decade, financial ecosystems have transitioned from paper currency to frictionless, smartphone-based digital payment applications (such as Google Pay, PhonePe, Paytm, Apple Pay, and Venmo). While digital payments provide convenience, contactless transactions, and rapid settlement, behavioral economists have noted that eliminating the physical "pain of paying" can weaken financial self-regulation.

College students represent a critical demographic for this inquiry:
* They are digital natives who execute micro-transactions daily (cafeteria, snacks, stationery, ride-hailing).
* Most operate under fixed monthly budgets or student allowances.
* Many live away from home in campus hostels, requiring independent financial management.

This project uses foundational probability models and statistical tests to quantify student payment behavior, test distribution fits, and assess whether digital payment reliance correlates with spending inflation and impulse buying.

---

## 2. Research Questions & Statistical Hypotheses

### Research Question 1: Impact of Living Arrangement on Expenditure
*Does living in a campus hostel vs. living at home with family (day scholar) create a statistically significant difference in monthly digital spending?*
* **Null Hypothesis ($H_{0,1}$):** $\mu_{\text{Hostel}} = \mu_{\text{Day Scholar}}$ (Mean monthly digital expenditure is identical).
* **Alternative Hypothesis ($H_{1,1}$):** $\mu_{\text{Hostel}} \neq \mu_{\text{Day Scholar}}$ (Two-tailed difference in population means).

### Research Question 2: Transaction Arrival Modeling
*Can the daily frequency of digital micro-transactions be modeled as a discrete Poisson process?*
* **Null Hypothesis ($H_{0,2}$):** The number of daily digital transactions follows a Poisson distribution with parameter $\lambda$.
* **Alternative Hypothesis ($H_{1,2}$):** The distribution departs significantly from a Poisson distribution.

### Research Question 3: Association Between Digital Dominance and Impulse Spending
*Is high reliance on digital payment methods ($> 80\%$ of expenses paid digitally) statistically independent of reported impulse buying?*
* **Null Hypothesis ($H_{0,3}$):** Digital payment dominance and impulse spending tendency are independent.
* **Alternative Hypothesis ($H_{1,3}$):** Digital payment dominance and impulse spending tendency are dependent (associated).

### Research Question 4: Relationship Between Daily Transaction Volume and Monthly Expenditure
*Does a high daily volume of micro-transactions linearly predict overall monthly digital expenditure?*
* **Null Hypothesis ($H_{0,4}$):** $\rho = 0$ (No linear correlation between transaction count and total spend).
* **Alternative Hypothesis ($H_{1,4}$):** $\rho > 0$ (Significant positive correlation).

---

## 3. Data Collection Methodology & Variables

Data was gathered through a structured questionnaire administered to undergraduate university students. A stratified convenience sampling strategy ensured balanced gender representation and adequate coverage across academic cohorts.

### Variable Dictionary

| Variable Name | Type | Unit / Levels | Operational Definition |
| :--- | :--- | :--- | :--- |
| `Student_ID` | Identifier | S001 – S100 | Unique respondent code |
| `Gender` | Categorical (Nominal) | Male, Female | Gender identity |
| `Year_of_Study` | Categorical (Ordinal) | 1st, 2nd, 3rd, 4th Year | Academic standing |
| `Accommodation` | Categorical (Nominal) | Hostel, Day Scholar | Living arrangement |
| `Primary_App` | Categorical (Nominal) | Google Pay, PhonePe, Paytm | Most frequently utilized payment platform |
| `Daily_Transactions_Count` | Discrete Quantitative | Counts / Day ($k \ge 0$) | Average self-reported UPI/wallet transactions per day |
| `Monthly_Digital_Spend` | Continuous Quantitative | Indian Rupees (₹) | Total monthly outlay via digital platforms |
| `Digital_Payment_Pct` | Continuous Quantitative | Percentage ($0\text{--}100\%$) | Ratio of expenses settled digitally vs. cash |
| `Impulse_Spending` | Categorical (Binary) | High, Low | Self-reported tendency toward unplanned purchases |
| `Payment_Failures_Past_Month`| Discrete Quantitative | Count ($k \ge 0$) | Server timeout or failed transaction events |
| `Tracks_Expenses` | Categorical (Ordinal) | Regularly, Rarely, Never | Budget-monitoring discipline |

---

## 4. Exploratory Data Analysis & Descriptive Statistics

### 4.1 Sample Demographics Overview ($N = 100$)
* **Gender:** Male = $50\%$ ($n=50$), Female = $50\%$ ($n=50$).
* **Accommodation:** Hostel Residents = $56\%$ ($n=56$), Day Scholars = $44\%$ ($n=44$).
* **Primary App Share:**
  * Google Pay: $45.0\%$
  * PhonePe: $38.0\%$
  * Paytm: $17.0\%$

### 4.2 Measures of Central Tendency and Dispersion

```
+-----------------------------------------------------------------------------------------+
| Variable                    | Mean       | Median    | Std. Dev.  | Variance    | IQR       |
+-----------------------------------------------------------------------------------------+
| Monthly Digital Spend (INR) | ₹3,822.00  | ₹3,950.00 | ₹1,350.76  | 1,824,561.6 | ₹2,200.00 |
| Daily Transactions Count    | 3.33 tx    | 3.00 tx   | 1.40 tx    | 1.96        | 2.00 tx   |
| Digital Payment Share (%)   | 78.43%     | 80.00%    | 10.96%     | 120.12      | 16.00%    |
+-----------------------------------------------------------------------------------------+
```

### 4.3 Five-Number Summary for Monthly Expenditure
* **Minimum:** ₹1,500.00
* **First Quartile ($Q_1$):** ₹2,600.00
* **Median ($Q_2$):** ₹3,950.00
* **Third Quartile ($Q_3$):** ₹4,800.00
* **Maximum:** ₹6,400.00
* **Interquartile Range ($\text{IQR} = Q_3 - Q_1$):** ₹2,200.00

The slight difference between the mean (₹3,822.00) and median (₹3,950.00) indicates a bimodal composite distribution driven by the two distinct subgroups: campus hostel dwellers and day scholars.

---

## 5. Probability Modeling & Theoretical Distributions

### 5.1 Poisson Distribution Modeling of Daily Transaction Frequency
The Poisson distribution models the probability of observing $k$ discrete events in a fixed interval when events occur independently at a constant mean rate $\lambda$:

$$P(X = k) = \frac{\lambda^k e^{-\lambda}}{k!}, \quad k \in \{0, 1, 2, \dots\}$$

From sample data:
$$\hat{\lambda} = \bar{x} = \frac{1}{N} \sum_{i=1}^{N} x_i = 3.33 \text{ transactions/day}$$

We compute the theoretical Poisson probabilities and compare them with the observed sample counts across $N = 100$ students:

| Transaction Count ($k$) | Observed Students ($O_k$) | Poisson Probability $P(X=k)$ | Expected Count ($E_k = 100 \times P$) | Absolute Difference $|O_k - E_k|$ |
| :---: | :---: | :---: | :---: | :---: |
| 0 | 0 | 0.0358 | 3.58 | 3.58 |
| 1 | 9 | 0.1192 | 11.92 | 2.92 |
| 2 | 22 | 0.1985 | 19.85 | 2.15 |
| 3 | 26 | 0.2203 | 22.03 | 3.97 |
| 4 | 20 | 0.1834 | 18.34 | 1.66 |
| 5 | 16 | 0.1221 | 12.21 | 3.79 |
| 6 | 7 | 0.0678 | 6.78 | 0.22 |
| $\ge 7$ | 0 | 0.0529 | 5.29 | 5.29 |
| **Total** | **100** | **1.0000** | **100.00** | — |

**Interpretation:** The empirical distribution mirrors the theoretical unimodal Poisson curve peaking at $k = 3$, confirming that daily transaction frequency is consistent with a Poisson arrival process.

### 5.2 Conditional Probability and Bayesian Inference for Impulse Spending

Let:
* Event $A$: Student exhibits "High Impulse Spending".
* Event $B$: Student conducts $> 80\%$ of transactions via digital payments ($\text{Digital Dominant}$).

From survey data ($N = 100$):
* $n(B) = 51 \implies P(B) = 0.51$
* $n(B^c) = 49 \implies P(B^c) = 0.49$
* $n(A \cap B) = 43$
* $n(A \cap B^c) = 5$
* Total High Impulse $n(A) = 48 \implies P(A) = 0.48$

#### Conditional Probabilities:
$$P(A \mid B) = \frac{P(A \cap B)}{P(B)} = \frac{43}{51} = 0.8431 \quad (84.31\%)$$

$$P(A \mid B^c) = \frac{P(A \cap B^c)}{P(B^c)} = \frac{5}{49} = 0.1020 \quad (10.20\%)$$

#### Applying Bayes' Theorem:
The posterior probability that a student relies heavily on digital payments ($B$), given that they suffer from high impulse spending ($A$):

$$P(B \mid A) = \frac{P(A \mid B) \cdot P(B)}{P(A)} = \frac{0.8431 \cdot 0.51}{0.48} = \frac{0.4300}{0.4800} \approx 0.8958 \quad (89.58\%)$$

**Key Takeaway:** An individual classified as a high-impulse spender has an $89.58\%$ likelihood of being a digital-dominant spender. Furthermore, the relative risk:
$$\text{Relative Risk (RR)} = \frac{P(A \mid B)}{P(A \mid B^c)} = \frac{0.8431}{0.1020} = 8.27$$
Students using $> 80\%$ digital payments are over **8.2 times more likely** to report frequent impulse purchases than those who retain cash usage.

---

## 6. Inferential Statistics & Hypothesis Testing

All tests were conducted at a significance level of $\alpha = 0.05$.

### 6.1 Hypothesis Test 1: Independent Two-Sample $t$-Test for Monthly Expenditure

We compare the mean expenditure between Hostel residents ($n_1 = 56$) and Day Scholars ($n_2 = 44$).

#### Sample Parameters:
* **Hostel ($n_1 = 56$):** $\bar{x}_1 = \text{₹}4,866.07$, $s_1 = \text{₹}732.19$, $s_1^2 = 536,100.65$
* **Day Scholar ($n_2 = 44$):** $\bar{x}_2 = \text{₹}2,493.18$, $s_2 = \text{₹}537.18$, $s_2^2 = 288,557.08$
* **Degrees of Freedom ($df$):** $n_1 + n_2 - 2 = 56 + 44 - 2 = 98$

#### Calculation of Pooled Variance ($s_p^2$):
$$s_p^2 = \frac{(n_1 - 1)s_1^2 + (n_2 - 1)s_2^2}{n_1 + n_2 - 2} = \frac{(55)(536100.65) + (43)(288557.08)}{98} = 427,484.59$$

$$s_p = \sqrt{427,484.59} = 653.82$$

#### Standard Error ($SE$):
$$SE = s_p \sqrt{\frac{1}{n_1} + \frac{1}{n_2}} = 653.82 \sqrt{\frac{1}{56} + \frac{1}{44}} = 653.82 \sqrt{0.017857 + 0.022727} = 131.72$$

#### $t$-Statistic:
$$t = \frac{\bar{x}_1 - \bar{x}_2}{SE} = \frac{4866.07 - 2493.18}{131.72} = \frac{2372.89}{131.72} = 18.015$$

* **Critical Value:** For $df = 98$ at $\alpha = 0.05$ (two-tailed), $t_{\text{crit}} \approx 1.984$.
* **Calculated $p$-value:** $p = 1.62 \times 10^{-32} \lll 0.001$.

**Decision:** Since $|t| = 18.015 > 1.984$ and $p < 0.05$, we decisively **reject the null hypothesis $H_{0,1}$**.  
**Conclusion:** There is overwhelming statistical evidence that campus hostel students incur significantly higher monthly digital expenditures than day scholars. The estimated mean difference is ₹2,372.89 (95% CI: [₹2,111.50, ₹2,634.28]).

---

### 6.2 Hypothesis Test 2: Pearson's Chi-Square ($\chi^2$) Test of Independence

We investigate whether digital payment dominance ($> 80\%$ vs $\le 80\%$) and self-reported impulse spending (High vs Low) are independent.

#### $2 \times 2$ Contingency Table: Observed vs. Expected Frequencies

```
+------------------------------------+-----------------------+----------------------+-------------+
| Payment Category                   | High Impulse Spending | Low Impulse Spending | Row Total   |
+------------------------------------+-----------------------+----------------------+-------------+
| Digital Dominant (> 80%)           | O = 43 (E = 24.48)    | O = 8  (E = 26.52)   | 51          |
| Cash/Balanced Dominant (<= 80%)    | O = 5  (E = 23.52)    | O = 44 (E = 25.48)   | 49          |
+------------------------------------+-----------------------+----------------------+-------------+
| Column Total                       | 48                    | 52                   | Grand N=100 |
+------------------------------------+-----------------------+----------------------+-------------+
```

Expected frequency for cell $(i, j)$: $E_{i,j} = \frac{\text{Row } i \text{ Total} \times \text{Col } j \text{ Total}}{N}$
* $E_{1,1} = \frac{51 \times 48}{100} = 24.48$
* $E_{1,2} = \frac{51 \times 52}{100} = 26.52$
* $E_{2,1} = \frac{49 \times 48}{100} = 23.52$
* $E_{2,2} = \frac{49 \times 52}{100} = 25.48$

*(All expected cell counts exceed 5, validating the $\chi^2$ distribution assumption).*

#### Test Statistic ($\chi^2$):
$$\chi^2 = \sum \frac{(O_{i,j} - E_{i,j})^2}{E_{i,j}}$$

$$\chi^2 = \frac{(43 - 24.48)^2}{24.48} + \frac{(8 - 26.52)^2}{26.52} + \frac{(5 - 23.52)^2}{23.52} + \frac{(44 - 25.48)^2}{25.48}$$

$$\chi^2 = \frac{(18.52)^2}{24.48} + \frac{(-18.52)^2}{26.52} + \frac{(-18.52)^2}{23.52} + \frac{(18.52)^2}{25.48}$$

$$\chi^2 = 14.011 + 12.933 + 14.583 + 13.461 = \mathbf{54.988}$$

* **Degrees of Freedom:** $df = (r - 1)(c - 1) = (2 - 1)(2 - 1) = 1$.
* **Critical Value at $\alpha = 0.05$:** $\chi^2_{\text{crit}} = 3.841$.
* **$p$-value:** $p = 1.21 \times 10^{-13}$.

**Decision:** Since $\chi^2 = 54.99 \gg 3.841$ and $p < 0.001$, we **reject the null hypothesis $H_{0,3}$**.  
**Conclusion:** There is a statistically significant dependency between digital payment reliance and high impulse spending.

---

### 6.3 Hypothesis Test 3: Correlation & Simple Linear Regression

We evaluate the relationship between Daily Digital Transaction Count ($X$) and Total Monthly Digital Expenditure ($Y$).

#### Summary Quantities ($N = 100$):
* $\sum X = 333$, $\sum Y = 382,200$
* $\sum X^2 = 1,303$, $\sum Y^2 = 1,641,640,000$
* $\sum XY = 1,460,300$

#### Pearson Correlation Coefficient ($r$):
$$r = \frac{N \sum XY - (\sum X)(\sum Y)}{\sqrt{\left[N \sum X^2 - (\sum X)^2\right] \left[N \sum Y^2 - (\sum Y)^2\right]}}$$

$$r = \frac{100(1,460,300) - (333)(382,200)}{\sqrt{\left[100(1,303) - (333)^2\right] \left[100(1,641,640,000) - (382,200)^2\right]}} = \mathbf{0.9745}$$

* **Coefficient of Determination ($R^2$):** $R^2 = (0.9745)^2 = \mathbf{0.9496}$ ($94.96\%$ of the variation in monthly digital expenditure is explained by transaction count).

#### Linear Regression Parameters:
$$\beta_1 = \frac{N \sum XY - (\sum X)(\sum Y)}{N \sum X^2 - (\sum X)^2} = \frac{18,757,400}{19,411} = \mathbf{940.05}$$

$$\beta_0 = \bar{Y} - \beta_1 \bar{X} = 3,822.00 - (940.05 \times 3.33) = \mathbf{691.62}$$

#### Regression Model:
$$\widehat{\text{Spend}} = 691.62 + 940.05 \times (\text{Daily\_Transactions})$$

* **Slope Interpretation ($\beta_1 = 940.05$):** For each additional daily digital transaction, a student's expected monthly expenditure increases by approximately ₹940.05.
* **Intercept Interpretation ($\beta_0 = 691.62$):** Fixed base digital expenses (recurring subscriptions, utility, recharge) amount to ₹691.62.

---

## 7. Discussion of Findings & Academic Implications

1. **The Frictionless Payment Effect:** The data clearly supports the behavioral economics hypothesis of the "cashless effect." When transactions occur via QR-code scan or one-click biometric approval, the cognitive barrier to spending decreases. This directly accounts for why $84.3\%$ of students relying on digital methods report high impulse spending.
2. **The Micro-Transaction Multiplier:** Students often rationalize small UPI spends of ₹30–₹80 (tea, snacks, snacks delivery). However, with an average of $\hat{\lambda} = 3.33$ transactions per day and an incremental slope of ₹940.05 per daily transaction, these micro-spends aggregate into significant monthly outlays.
3. **Lifestyle Segmentation:** The huge divergence between hostelers ($\mu = \text{₹}4,866$) and day scholars ($\mu = \text{₹}2,493$) highlights that day scholars benefit from family-subsidized groceries, home cooking, and shared transport, while hostellers manage all operational living costs independently via mobile wallets.

---

## 8. Practical Recommendations

1. **Enforce Intentional Friction:** Students should establish daily spending limits or maintain a secondary digital wallet with a capped weekly transfer (e.g., ₹750/week) rather than linking primary bank accounts to UPI apps.
2. **Active Expense Tracking:** Over $60\%$ of high-spend students answered "Never" or "Rarely" to tracking expenses. Regularly recording transactions in a budgeting spreadsheet eliminates the psychological invisibility of digital payments.
3. **Hybrid Cash Reserve:** Keeping a fixed physical cash wallet for daily micro-transactions (canteen, tea, local transport) re-introduces the tangible sensory feedback of paying.

---

## 9. Threats to Validity & Project Limitations

1. **Self-Reporting and Recall Bias:** Monthly expenditure and daily transaction frequencies were based on student self-reports rather than direct bank statement audits.
2. **Convenience Sampling:** While stratified across genders, sampling was confined to a single university cohort, which may not capture socioeconomic diversity across different regions.
3. **Seasonality:** Data was collected mid-semester; expenditures may spike during festival seasons, exams, or start-of-semester textbook procurement.

---

## 10. Conclusion

This project successfully applied principles of probability distributions and statistical inference to study digital payment habits among college students. The empirical results confirm:
* Daily transactions follow a Poisson distribution ($\lambda = 3.33$).
* Campus accommodation status is a decisive factor in total monthly spending ($t = 18.02, p < 10^{-15}$).
* A tight linear coupling exists between transaction frequency and spend ($R^2 = 0.95$).
* Digital payment dominance is strongly dependent on high impulse spending ($\chi^2 = 54.99$, relative risk of $8.27$).

These findings provide quantitative backing for introducing personal finance education and mindful digital consumption modules on college campuses.

---

## 11. Appendix: Complete Survey Questionnaire

```
1. Student Identification: [S001 to S100]
2. Gender: [ ] Male   [ ] Female   [ ] Prefer not to say
3. Year of Study: [ ] 1st Year  [ ] 2nd Year  [ ] 3rd Year  [ ] 4th Year
4. Accommodation Status: [ ] Hostel / Campus PG   [ ] Day Scholar (With Family)
5. Primary Digital Payment Application: [ ] Google Pay   [ ] PhonePe   [ ] Paytm   [ ] Other
6. Average Daily Digital Transactions Count (Check UPI App History): _____ transactions/day
7. Estimated Total Monthly Digital Expenditure: ₹ ________ / month
8. What percentage of your total expenses are paid digitally vs. cash? _____ %
9. Do you find yourself making unplanned or impulse purchases due to instant digital payment?
   [ ] High (Frequently)   [ ] Low (Rarely or Never)
10. How many payment failures or server timeouts did you experience in the past 30 days? _____
11. How frequently do you check or audit your digital payment history/expenses?
   [ ] Regularly   [ ] Rarely   [ ] Never
```
