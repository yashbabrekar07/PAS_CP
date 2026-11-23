"""
Statistical Analysis of Digital Payment Habits Among Students
Course Project: Probability and Statistics
Dataset: digital_payments_students.csv
"""

import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns

# Set visual style
sns.set_theme(style="whitegrid")
plt.rcParams['font.sans-serif'] = 'Arial'
plt.rcParams['font.family'] = 'sans-serif'

# 1. Load Dataset
df = pd.read_csv("digital_payments_students.csv")
print("=== DATASET OVERVIEW ===")
print(df.info())
print("\nFirst 5 records:\n", df.head())

# 2. Descriptive Statistics
print("\n=== DESCRIPTIVE STATISTICS FOR MONTHLY SPEND ===")
spend = df['Monthly_Digital_Spend']
print(f"Mean: {spend.mean():.2f}")
print(f"Median: {spend.median():.2f}")
print(f"Std Dev: {spend.std():.2f}")
print(f"Variance: {spend.var():.2f}")
print(f"Q1: {spend.quantile(0.25):.2f}, Q3: {spend.quantile(0.75):.2f}, IQR: {spend.quantile(0.75)-spend.quantile(0.25):.2f}")
print(f"Min: {spend.min()}, Max: {spend.max()}")

print("\n=== DESCRIPTIVE STATISTICS FOR DAILY TRANSACTIONS ===")
tx = df['Daily_Transactions_Count']
lambda_est = tx.mean()
print(f"Sample Mean (Lambda): {lambda_est:.4f}")
print(f"Sample Variance: {tx.var():.4f}")
print(f"Sample Std Dev: {tx.std():.4f}")

# 3. Two-Sample t-Test: Hostellers vs Day Scholars
hostel_spend = df[df['Accommodation'] == 'Hostel']['Monthly_Digital_Spend']
day_spend = df[df['Accommodation'] == 'Day Scholar']['Monthly_Digital_Spend']

t_stat, p_val_t = stats.ttest_ind(hostel_spend, day_spend, equal_var=True)
print("\n=== TWO-SAMPLE T-TEST (ACCOMMODATION SPEND) ===")
print(f"Hostel: n={len(hostel_spend)}, Mean={hostel_spend.mean():.2f}, SD={hostel_spend.std():.2f}")
print(f"Day Scholar: n={len(day_spend)}, Mean={day_spend.mean():.2f}, SD={day_spend.std():.2f}")
print(f"t-statistic: {t_stat:.4f}, p-value: {p_val_t:.4e} (df={len(df)-2})")

# 4. Chi-Square Test of Independence
# Group: Digital Payment Pct > 80% vs <= 80%
df['Digital_Dominant'] = np.where(df['Digital_Payment_Pct'] > 80, '> 80%', '<= 80%')
contingency_table = pd.crosstab(df['Digital_Dominant'], df['Impulse_Spending'])

chi2, p_val_chi2, dof, expected = stats.chi2_contingency(contingency_table, correction=False)
print("\n=== CHI-SQUARE TEST OF INDEPENDENCE ===")
print("Observed Contingency Table:\n", contingency_table)
print("Expected Frequencies:\n", expected)
print(f"Chi-square Statistic: {chi2:.4f}, df: {dof}, p-value: {p_val_chi2:.4e}")

# 5. Pearson Correlation and Linear Regression
slope, intercept, r_value, p_val_reg, std_err = stats.linregress(tx, spend)
print("\n=== CORRELATION AND REGRESSION ===")
print(f"Pearson Correlation (r): {r_value:.4f}")
print(f"Coefficient of Determination (R^2): {r_value**2:.4f}")
print(f"Regression Equation: Spend = {intercept:.2f} + {slope:.2f} * (Daily_Transactions)")
print(f"p-value: {p_val_reg:.4e}, Standard Error: {std_err:.4f}")

# 6. Poisson Distribution Goodness-of-Fit Comparison
print("\n=== POISSON DISTRIBUTION MODELING ===")
k_vals = np.arange(0, 7)
obs_counts = [np.sum(tx == k) for k in k_vals]
poisson_probs = stats.poisson.pmf(k_vals, mu=lambda_est)
exp_counts = poisson_probs * len(df)

poisson_df = pd.DataFrame({
    'k (Daily Transactions)': k_vals,
    'Observed Count': obs_counts,
    'Poisson P(X=k)': np.round(poisson_probs, 4),
    'Expected Count': np.round(exp_counts, 2)
})
print(poisson_df)

# 7. Generate Plots (Saved to files)
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Subplot 1: Histogram of Monthly Spend
sns.histplot(df['Monthly_Digital_Spend'], kde=True, ax=axes[0, 0], color='skyblue', bins=12)
axes[0, 0].set_title('Distribution of Monthly Digital Spend (INR)', fontsize=13, fontweight='bold')
axes[0, 0].set_xlabel('Spend (INR)')
axes[0, 0].set_ylabel('Frequency')

# Subplot 2: Boxplot by Accommodation
sns.boxplot(x='Accommodation', y='Monthly_Digital_Spend', data=df, ax=axes[0, 1], palette='Set2')
axes[0, 1].set_title('Monthly Spend: Hostel vs Day Scholar', fontsize=13, fontweight='bold')
axes[0, 1].set_xlabel('Accommodation Status')
axes[0, 1].set_ylabel('Spend (INR)')

# Subplot 3: Scatter Plot + Regression Line
sns.regplot(x='Daily_Transactions_Count', y='Monthly_Digital_Spend', data=df, ax=axes[1, 0],
            scatter_kws={'alpha': 0.7, 'color': 'darkblue'}, line_kws={'color': 'red', 'linewidth': 2})
axes[1, 0].set_title(f'Linear Regression: Spend vs Daily Transactions (R²={r_value**2:.2f})', fontsize=13, fontweight='bold')
axes[1, 0].set_xlabel('Daily Transactions Count')
axes[1, 0].set_ylabel('Monthly Digital Spend (INR)')

# Subplot 4: Observed vs Theoretical Poisson Distribution
axes[1, 1].bar(k_vals - 0.15, obs_counts, width=0.3, label='Observed Count', color='steelblue')
axes[1, 1].bar(k_vals + 0.15, exp_counts, width=0.3, label='Poisson Expected Count (λ=3.33)', color='orange')
axes[1, 1].set_title('Poisson Fit: Daily Transactions Count', fontsize=13, fontweight='bold')
axes[1, 1].set_xlabel('Number of Daily Transactions (k)')
axes[1, 1].set_ylabel('Frequency')
axes[1, 1].legend()

plt.tight_layout()
plt.savefig("analysis_charts.png", dpi=300)
print("\nAll statistical analyses completed. Plots saved to 'analysis_charts.png'.")
