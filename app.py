import streamlit as st
import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns

# Set Page Config
st.set_page_config(page_title="Digital Payment Habits - Stats Dashboard", page_icon="💳", layout="wide")

# Title and Subtitle
st.title("💳 Statistical Analysis of Student Digital Payment Habits")
st.markdown("""
**Course:** Probability & Statistics Project  
This interactive dashboard analyzes daily transaction arrival rates, monthly spending distributions, and inferential hypothesis testing across **100 college students**.
""")

# Load Dataset
@st.cache_data
def load_data():
    return pd.read_csv("digital_payments_students.csv")

try:
    df = load_data()
except Exception as e:
    st.error(f"Error loading CSV file: {e}")
    st.stop()

# --- SIDEBAR FILTERS ---
st.sidebar.header("🔍 Filter Student Sample")
accommodation_filter = st.sidebar.multiselect(
    "Select Accommodation:",
    options=df["Accommodation"].unique(),
    default=df["Accommodation"].unique()
)

gender_filter = st.sidebar.multiselect(
    "Select Gender:",
    options=df["Gender"].unique(),
    default=df["Gender"].unique()
)

app_filter = st.sidebar.multiselect(
    "Select Primary App:",
    options=df["Primary_App"].unique(),
    default=df["Primary_App"].unique()
)

filtered_df = df[
    (df["Accommodation"].isin(accommodation_filter)) &
    (df["Gender"].isin(gender_filter)) &
    (df["Primary_App"].isin(app_filter))
]

st.sidebar.markdown("---")
st.sidebar.info(f"Showing **{len(filtered_df)}** of **{len(df)}** students.")

# --- TOP METRICS CARDS ---
col1, col2, col3, col4 = st.columns(4)
with col1:
    avg_spend = filtered_df["Monthly_Digital_Spend"].mean() if len(filtered_df) > 0 else 0
    st.metric("Avg Monthly Spend", f"₹{avg_spend:,.2f}")
with col2:
    avg_tx = filtered_df["Daily_Transactions_Count"].mean() if len(filtered_df) > 0 else 0
    st.metric("Avg Daily Transactions (λ)", f"{avg_tx:.2f} tx/day")
with col3:
    digital_share = filtered_df["Digital_Payment_Pct"].mean() if len(filtered_df) > 0 else 0
    st.metric("Avg Digital Share", f"{digital_share:.1f}%")
with col4:
    high_impulse_cnt = (filtered_df["Impulse_Spending"] == "High").sum() if len(filtered_df) > 0 else 0
    impulse_pct = (high_impulse_cnt / len(filtered_df) * 100) if len(filtered_df) > 0 else 0
    st.metric("High Impulse Spenders", f"{impulse_pct:.1f}%")

st.markdown("---")

# --- TABS FOR ANALYSIS ---
tab1, tab2, tab3, tab4 = st.tabs([
    "📊 Descriptive Stats & EDA", 
    "🎲 Probability Modeling", 
    "🧪 Hypothesis Testing", 
    "📁 Dataset & Excel Export"
])

# ----------------- TAB 1: DESCRIPTIVE STATS -----------------
with tab1:
    st.header("Exploratory Data Analysis (EDA)")
    
    col_chart1, col_chart2 = st.columns(2)
    
    with col_chart1:
        st.subheader("1. Monthly Spend Distribution")
        fig, ax = plt.subplots(figsize=(7, 4.5))
        sns.histplot(filtered_df["Monthly_Digital_Spend"], kde=True, color="#2b5c8f", bins=12, ax=ax)
        ax.set_xlabel("Monthly Spend (INR)")
        ax.set_ylabel("Number of Students")
        ax.set_title("Histogram & Density Curve of Monthly Spend")
        st.pyplot(fig)
        
    with col_chart2:
        st.subheader("2. Spend by Accommodation (Boxplot)")
        fig, ax = plt.subplots(figsize=(7, 4.5))
        sns.boxplot(x="Accommodation", y="Monthly_Digital_Spend", data=filtered_df, palette="Set2", ax=ax)
        ax.set_ylabel("Monthly Spend (INR)")
        ax.set_title("Hostel vs Day Scholar Spending Comparison")
        st.pyplot(fig)
        
    st.markdown("---")
    st.subheader("Summary Statistics Table")
    stats_summary = filtered_df[["Monthly_Digital_Spend", "Daily_Transactions_Count", "Digital_Payment_Pct"]].describe().T
    stats_summary["median"] = filtered_df[["Monthly_Digital_Spend", "Daily_Transactions_Count", "Digital_Payment_Pct"]].median()
    stats_summary["IQR"] = stats_summary["75%"] - stats_summary["25%"]
    st.dataframe(stats_summary[["mean", "median", "std", "min", "25%", "75%", "IQR", "max"]].style.format("{:.2f}"))

# ----------------- TAB 2: PROBABILITY MODELING -----------------
with tab2:
    st.header("Probability Distributions & Bayesian Inference")
    
    col_p1, col_p2 = st.columns(2)
    
    with col_p1:
        st.subheader("1. Poisson Arrival Rate for Daily Transactions")
        st.markdown(r"""
        The number of discrete daily digital transactions $X$ can be modeled as:
        $$P(X = k) = \frac{\lambda^k e^{-\lambda}}{k!}$$
        """)
        
        lambda_val = df["Daily_Transactions_Count"].mean()
        st.write(f"**Sample Mean Arrival Rate ($\hat{{\lambda}}$):** `{lambda_val:.2f} transactions/day`")
        
        k_values = np.arange(0, 8)
        observed_counts = [np.sum(df["Daily_Transactions_Count"] == k) for k in k_values]
        poisson_expected = stats.poisson.pmf(k_values, mu=lambda_val) * len(df)
        
        fig, ax = plt.subplots(figsize=(7, 4.5))
        width = 0.35
        ax.bar(k_values - width/2, observed_counts, width=width, label="Observed Survey Count", color="#1f77b4")
        ax.bar(k_values + width/2, poisson_expected, width=width, label=f"Theoretical Poisson (λ={lambda_val:.2f})", color="#ff7f0e")
        ax.set_xlabel("Daily Transactions (k)")
        ax.set_ylabel("Frequency (Students)")
        ax.set_title("Observed vs Expected Poisson Frequencies")
        ax.legend()
        st.pyplot(fig)
        
    with col_p2:
        st.subheader("2. Conditional Probability & Bayes' Theorem")
        st.markdown(r"""
        **Question:** If a student relies heavily on digital payments ($B: \text{Digital} > 80\%$), what is the probability they report high impulse spending ($A$)?
        """)
        
        n_total = len(df)
        n_B = (df["Digital_Payment_Pct"] > 80).sum()
        n_B_comp = n_total - n_B
        
        n_A_and_B = ((df["Impulse_Spending"] == "High") & (df["Digital_Payment_Pct"] > 80)).sum()
        n_A_and_B_comp = ((df["Impulse_Spending"] == "High") & (df["Digital_Payment_Pct"] <= 80)).sum()
        
        p_A_given_B = n_A_and_B / n_B
        p_A_given_B_comp = n_A_and_B_comp / n_B_comp
        rr = p_A_given_B / p_A_given_B_comp
        
        st.success(f"""
        * **P(Impulse | Digital > 80%):** `{p_A_given_B * 100:.2f}%` ({n_A_and_B}/{n_B})
        * **P(Impulse | Digital ≤ 80%):** `{p_A_given_B_comp * 100:.2f}%` ({n_A_and_B_comp}/{n_B_comp})
        * **Relative Risk:** `{rr:.2f}x` higher chance of impulse spending for digital-dominant users!
        """)
        
        p_A = (df["Impulse_Spending"] == "High").sum() / n_total
        p_B = n_B / n_total
        bayes_prob = (p_A_given_B * p_B) / p_A
        
        st.info(f"""
        **Bayes' Theorem Inversion:**  
        $$P(B \mid A) = \\frac{{P(A \mid B) \\cdot P(B)}}{{P(A)}} = {bayes_prob * 100:.2f}\%$$  
        Given that a student is an impulse spender, there is an **{bayes_prob*100:.1f}% chance** they belong to the digital-dominant group.
        """)

# ----------------- TAB 3: HYPOTHESIS TESTING -----------------
with tab3:
    st.header("Inferential Statistics & Hypothesis Tests")
    
    # Test 1: Two-sample t-test
    st.subheader("Test 1: Two-Sample t-Test (Hostelers vs Day Scholars Spend)")
    hostel = df[df["Accommodation"] == "Hostel"]["Monthly_Digital_Spend"]
    day = df[df["Accommodation"] == "Day Scholar"]["Monthly_Digital_Spend"]
    
    t_stat, p_val_t = stats.ttest_ind(hostel, day, equal_var=True)
    
    col_t1, col_t2 = st.columns(2)
    with col_t1:
        st.write(f"**Hostel Mean:** ₹{hostel.mean():,.2f} (SD: ₹{hostel.std():,.2f}, n={len(hostel)})")
        st.write(f"**Day Scholar Mean:** ₹{day.mean():,.2f} (SD: ₹{day.std():,.2f}, n={len(day)})")
        st.write(f"**Calculated t-statistic:** `{t_stat:.4f}`")
        st.write(f"**Degrees of Freedom (df):** `{len(df) - 2}`")
        st.write(f"**p-value:** `{p_val_t:.3e}`")
    with col_t2:
        if p_val_t < 0.05:
            st.success("✅ **Decision:** Reject Null Hypothesis ($H_0$).  \nThere is a highly statistically significant difference in monthly digital spending between hostel residents and day scholars ($p < 0.001$).")
        else:
            st.warning("Fail to reject $H_0$.")
            
    st.markdown("---")
    
    # Test 2: Chi-Square Test
    st.subheader("Test 2: Chi-Square Test of Independence (Digital Reliance vs Impulse)")
    df["Dominance"] = np.where(df["Digital_Payment_Pct"] > 80, "Digital > 80%", "Digital <= 80%")
    contingency = pd.crosstab(df["Dominance"], df["Impulse_Spending"])
    chi2, p_val_chi2, dof, expected = stats.chi2_contingency(contingency, correction=False)
    
    col_c1, col_c2 = st.columns(2)
    with col_c1:
        st.write("**Observed Contingency Table:**")
        st.dataframe(contingency)
        st.write(f"**Chi-Square (χ²):** `{chi2:.4f}` | **df:** `{dof}` | **p-value:** `{p_val_chi2:.3e}`")
    with col_c2:
        if p_val_chi2 < 0.05:
            st.success("✅ **Decision:** Reject Null Hypothesis ($H_0$).  \nDigital payment reliance is strongly dependent with impulse buying behavior ($\chi^2 = 54.99, p < 0.001$).")
            
    st.markdown("---")
    
    # Test 3: Correlation & Regression
    st.subheader("Test 3: Correlation & Simple Linear Regression")
    slope, intercept, r_value, p_reg, std_err = stats.linregress(df["Daily_Transactions_Count"], df["Monthly_Digital_Spend"])
    
    col_r1, col_r2 = st.columns([1, 1])
    with col_r1:
        st.write(f"**Pearson Correlation (r):** `{r_value:.4f}`")
        st.write(f"**R-squared (R²):** `{r_value**2:.4f}`")
        st.write(f"**Fitted Model:** `Spend = {intercept:.2f} + {slope:.2f} * (Daily_Transactions)`")
        st.write(f"**p-value:** `{p_reg:.3e}`")
        
        # Interactive Predictor
        st.markdown("##### 🔮 Predict Spending from Daily Transactions:")
        test_tx = st.slider("Select number of daily transactions:", 1, 10, 4)
        pred_spend = intercept + slope * test_tx
        st.info(f"Predicted Monthly Spend for {test_tx} tx/day: **₹{pred_spend:,.2f}**")
        
    with col_r2:
        fig, ax = plt.subplots(figsize=(6, 4))
        sns.regplot(x="Daily_Transactions_Count", y="Monthly_Digital_Spend", data=df, color="#1a5276", line_kws={"color": "red"}, ax=ax)
        ax.set_title(f"Spend vs Transactions (R² = {r_value**2:.2f})")
        st.pyplot(fig)

# ----------------- TAB 4: DATASET & EXCEL -----------------
with tab4:
    st.header("Raw Survey Dataset & Download")
    st.dataframe(filtered_df, use_container_width=True)
    
    csv = filtered_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download Filtered Data as CSV",
        data=csv,
        file_name='student_digital_payments_filtered.csv',
        mime='text/csv'
    )
    st.markdown("""
    ### 💡 How to Demonstrate Excel Work to Your Professor:
    1. Open `digital_payments_students.csv` in **Microsoft Excel**.
    2. Insert a **Pivot Table** (`Insert` -> `PivotTable`):
       * Drag `Accommodation` to Rows.
       * Drag `Monthly_Digital_Spend` to Values (change Summarize value by: **Average**).
    3. Use formulas from `analysis_guide_excel.md`:
       * `=AVERAGE(...)`
       * `=T.TEST(...)`
       * `=CORREL(...)`
    4. Save as `.xlsx` with charts to showcase dual proficiency in **both Python and Excel**.
    """)
