import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

###############################################################################
#######Read The xlsx file############

cholera_df = pd.read_excel(r"C:\Users\rnsdo\OneDrive\Attachments\Desktop\Python and Microsoft Certificatse\cisco networking academy\My projects\cholera\cholera.xlsx")


###############################################################################

###############################

st.title("Epidemic Curve Analysis")

###############################
################# Epidemic curve ##############################################
# 1. تحويل العمود إلى صيغة تاريخ مع معالجة الأخطاء
# errors='coerce' ستقوم بتحويل أي قيمة غير صالحة إلى NaT (ليس تاريخاً) بدلاً من إيقاف البرنامج
cholera_df['first_epiwk'] = pd.to_datetime(cholera_df['first_epiwk'], errors='coerce')

# 2. حذف الصفوف التي لم ينجح تحويلها لتجنب الأخطاء أثناء الرسم
cholera_df = cholera_df.dropna(subset=['first_epiwk'])

# 3. الآن يمكنك الترتيب بدون مشاكل
cholera_df = cholera_df.sort_values('first_epiwk')

# 1. ترتيب البيانات (تأكد أن هذا الجزء بعد قراءة الملف)
cholera_df = cholera_df.sort_values('first_epiwk')

# 2. إنشاء الرسم البياني (يفضل استخدامه مع متغير fig لتجنب تداخل الرسومات)
fig_epiwk, ax = plt.subplots(figsize=(14, 7))

sns.lineplot(data=cholera_df, x='first_epiwk', y='case_total', marker='o', label='Total Cases', ax=ax)
sns.lineplot(data=cholera_df, x='first_epiwk', y='death_total', marker='s', label='Total Deaths', color='red', ax=ax)

# 3. تحسين المظهر
ax.set_title('Epidemic curve: Evolution of cholera cases and deaths over the weeks', fontsize=16)
ax.set_xlabel('Epi Week', fontsize=12)
ax.set_ylabel('Count', fontsize=12)
plt.xticks(rotation=45)
ax.grid(True, linestyle='--', alpha=0.6)
ax.legend()

# 4. عرض المخطط في Streamlit
st.pyplot(fig_epiwk)

###############################################################################

# # # --- حساب وتحليل معدل الفتك (CFR) ---

# # # 1. تقسيم البيانات إلى شهر يناير وبقية الشهور
jan_df = cholera_df[cholera_df['first_epiwk'].dt.month == 1]
rest_df = cholera_df[cholera_df['first_epiwk'].dt.month != 1]

# # # 2. حساب القيم ليناير
jan_cases = jan_df['case_total'].sum()
jan_deaths = jan_df['death_total'].sum()
jan_cfr = (jan_deaths / jan_cases * 100) if jan_cases > 0 else 0

# # # 3. حساب القيم لبقية العام
rest_cases = rest_df['case_total'].sum()
rest_deaths = rest_df['death_total'].sum()
rest_cfr = (rest_deaths / rest_cases * 100) if rest_cases > 0 else 0

# --- 2. تقسيم التحليل إلى عمودين رئيسيين ---
# العمود الأول (col_analysis) للتحليل النصي
# العمود الثاني (col_metrics) للمقارنة الرقمية والمقاييس
col_analysis, col_metrics = st.columns([1.5, 1], gap="large")

with col_analysis:
    st.markdown("### 🔍 Interpretation")
    
    # استخدام Tab أو Expander صغير داخل العمود لتنظيم الفقرات
    st.markdown("**A. Outbreak Magnitude & Peak**")
    st.caption("The curve illustrates a **Point Source Outbreak**. A massive surge in January 2025 reached a peak of **72,000 cases** in one week, suggesting a widespread contamination event.")
    
    st.markdown("**B. Trend & Containment**")
    st.caption("Following the peak, a **precipitous decline** occurred. By February, the outbreak transitioned to an **endemic state** with low-level transmission.")
    
    st.success("**C. Clinical Implication**")
    st.write("The wide gap between cases and deaths indicates a low CFR, proving that healthcare response (rehydration/management) was highly effective.")
    
    st.warning("**D. Conclusion**")
    st.write("The outbreak was contained quickly without sustained high mortality, reflecting a successfully managed crisis.")

with col_metrics:
    st.markdown("### 📈 Period Metrics")
    
    # عرض المقارنة الرقمية التي حسبتها برمجياً
    tab_jan, tab_rest = st.tabs(["📌 Peak (Jan)", "✅ Stability (Feb-Nov)"])
    
    with tab_jan:
        st.metric("Total Cases", f"{int(jan_cases):,}")
        st.metric("CFR", f"{jan_cfr:.2f}%")
        st.error(f"Fatality was {jan_cfr - rest_cfr:.2f}% higher than average.")

    with tab_rest:
        st.metric("Total Cases", f"{int(rest_cases):,}")
        st.metric("CFR", f"{rest_cfr:.2f}%")
        st.info("System maintained stability despite high initial pressure.")

    # الجدول الإحصائي المختصر أسفل المقاييس
    st.markdown("#### Quick Summary Table")
    st.markdown(f"""
    | Period | Cases | Deaths | CFR |
    | :--- | :--- | :--- | :--- |
    | **Peak** | ~{int(jan_cases/1000)}k | {int(jan_deaths)} | **{jan_cfr:.1f}%** |
    | **Stable** | ~{int(rest_cases/1000)}k | {int(rest_deaths)} | **{rest_cfr:.1f}%** |
    """)

st.write("---")

###############################################################################
###############################################################################
