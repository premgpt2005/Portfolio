import streamlit as st

# 1. PAGE CONFIGURATION
st.set_page_config(
    page_title="Prem Gupta | Portfolio",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. HERO SECTION
st.markdown("<h1 style='text-align: center;'>Prem Gupta</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: #60a5fa;'>Data Analyst | AI/ML Engineer | B.Tech CSE Student</h4>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #cbd5e1; font-size: 1.1rem;'>Passionate about data storytelling, predictive modeling, and building scalable data pipelines.</p>", unsafe_allow_html=True)

# Contact Links (Centered using columns)
col1, col2, col3, col4, col5 = st.columns([2, 1, 1, 1, 2])
with col2:
    st.link_button("📧 Email Me", "mailto:premgpt2005@gmail.com", use_container_width=True)
with col3:
    st.link_button("💼 LinkedIn", "https://linkedin.com/in/prem-gupta-68826a245", use_container_width=True)
with col4:
    st.link_button("🐙 GitHub", "https://github.com/premgpt2005", use_container_width=True)

st.divider()

# 3. TECHNICAL SKILLS SECTION
st.subheader("🛠️ Technical Skills")
# Using Streamlit's native markdown code blocks for a clean "badge" look
st.markdown("""
`Python` &nbsp; `SQL (PostgreSQL)` &nbsp; `R` &nbsp; `Generative AI` &nbsp; `Machine Learning` &nbsp; `Power BI & Excel` &nbsp; `A/B Testing` &nbsp; `Pandas & Scikit-Learn` &nbsp; `Data Visualization`
""")

st.divider()

# 4. PROJECTS SECTION
st.subheader("🚀 Projects")

# Creating a 2-column grid for project cards
proj_col1, proj_col2 = st.columns(2)

with proj_col1:
    with st.container(border=True):
        st.markdown("### E-Commerce Sales Prediction & A/B Testing")
        st.caption("**Tools:** Python (Pandas, Scikit-learn, Sci-Py), EDA")
        st.markdown("""
        * Engineered an end-to-end Python workflow for daily sales forecasting, including data cleaning and feature extraction.
        * Built machine learning pipelines to train regression models and designed an A/B testing simulation to statistically evaluate prediction errors.
        """)
        st.link_button("🔗 View Repository", "https://github.com/premgpt2005/Predictive-Modeling-A-B-Testing-for-E-Commerce-Sales")

    with st.container(border=True):
        st.markdown("### IBM HR Attrition Analytics Prediction")
        st.caption("**Tools:** Python, Machine Learning, Scikit-Learn")
        st.markdown("""
        * Engineered predictive machine learning models to forecast employee attrition and identify the root causes of turnover.
        * Performed extensive feature engineering and statistical analysis to extract key business insights for HR retention.
        """)
        st.link_button("🔗 View Repository", "https://github.com/premgpt2005/IBM-HR-Attrition-Analytics-Prediction")

    with st.container(border=True):
        st.markdown("### Advanced SQL Data Cleaning & Analysis")
        st.caption("**Tools:** PostgreSQL")
        st.markdown("""
        * Cleaned and normalized a 3,000+ row dataset, removing duplicates, fixing nulls, and standardizing date formats.
        * Authored 15+ complex SQL queries utilizing CTEs, window functions, and subqueries to uncover granular data insights.
        """)
        st.link_button("🔗 View Repository", "https://github.com/premgpt2005/SQL-Data-Cleaning-and-EDA")

with proj_col2:
    with st.container(border=True):
        st.markdown("### HR Attrition Analytics Dashboard")
        st.caption("**Tools:** Power BI")
        st.markdown("""
        * Developed an interactive dashboard analyzing data for 1,470 employees to track attrition across departments and demographics.
        * Identified key turnover drivers related to salary, tenure, and job level to recommend retention strategies.
        """)
        st.link_button("🔗 View Repository", "https://github.com/premgpt2005/IBM-HR-Attrition-Analytics-Dashboard")

    with st.container(border=True):
        st.markdown("### Customer Churn Analytics")
        st.caption("**Tools:** Python, Data Visualization, Predictive Modeling")
        st.markdown("""
        * Executed predictive modeling to identify at-risk customers and forecast potential churn rates.
        * Uncovered key business insights and retention drivers through comprehensive exploratory data analysis.
        """)
        st.link_button("🔗 View Repository", "https://github.com/premgpt2005/Customer-Churn-Analytics")

    with st.container(border=True):
        st.markdown("### Netflix Subscription Analytics")
        st.caption("**Tools:** Excel, Pivot Tables")
        st.markdown("""
        * Analyzed large-scale subscription datasets using advanced Excel functionalities to map user growth and revenue trends.
        * Generated structured pivot tables and visual reports to evaluate regional viewing preferences and churn metrics.
        """)
        st.link_button("🔗 View Repository", "https://github.com/premgpt2005/Netflix-Subscription-Analytics-Using-Excel")

st.divider()

# 5. EXPERIENCE SECTION
st.subheader("💼 Virtual Experience")

with st.container(border=True):
    col_a, col_b = st.columns([3, 1])
    with col_a:
        st.markdown("### GenAI Data Analytics Virtual Internship")
        st.caption("**Tata iQ**")
    with col_b:
        st.markdown("<p style='text-align: right; color: gray; margin-top: 1rem;'>June 2026</p>", unsafe_allow_html=True)
    
    st.markdown("""
    * Leveraged Generative AI tools to conduct EDA and architect a no-code predictive modeling framework for customer delinquency risk.
    * Designed an automated collections strategy utilizing agentic AI with ethical AI principles.
    """)
    st.link_button("🔗 View Work Repository", "https://github.com/premgpt2005/AI-Powered-Credit-Risk-Analytics")

with st.container(border=True):
    col_c, col_d = st.columns([3, 1])
    with col_c:
        st.markdown("### Data Analytics Internship")
        st.caption("**Codec Technologies**")
    with col_d:
        st.markdown("<p style='text-align: right; color: gray; margin-top: 1rem;'>May 2026 - June 2026</p>", unsafe_allow_html=True)
    
    st.markdown("""
    * Executed real-world ML projects including IBM HR Attrition Analysis and Customer Churn Prediction.
    * Performed feature engineering and predictive modeling using Python, Excel, and Power BI.
    """)
    st.link_button("🔗 View Work Repository", "https://github.com/premgpt2005/CodecTechnologies-Internship")