import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



###############################################################################
#######Read The xlsx file############

cholera_df = pd.read_excel(r"C:\Users\rnsdo\OneDrive\Attachments\Desktop\Python and Microsoft Certificatse\cisco networking academy\My projects\cholera\cholera.xlsx")


###############################################################################
st.subheader("🔮 Trend Analysis & Future Prediction")

# 1. تجهيز البيانات للتنبؤ
# يجب التأكد أن cholera_df مرتبة حسب التاريخ بالفعل
x = np.arange(len(cholera_df))
y = cholera_df['case_total'].values

# 2. حساب خط الاتجاه (معادلة الدرجة الأولى)
z = np.polyfit(x, y, 1)
p = np.poly1d(z)

# 3. إنشاء الرسم البياني لخط الاتجاه (باستخدام Matplotlib)
fig_trend, ax_trend = plt.subplots(figsize=(12, 6))

ax_trend.plot(x, y, 'o-', label='Actual cases')
ax_trend.plot(x, p(x), '--', color='red', label='Trendline')

ax_trend.set_title('Predicting of disease spread (Trend Analysis)')
ax_trend.set_xlabel('Epi Week Index')
ax_trend.set_ylabel('Total Cases')
ax_trend.legend()
ax_trend.grid(True, linestyle='--', alpha=0.6)

# 4. عرض المخطط في Streamlit
st.pyplot(fig_trend)

# 5. إضافة تحليل بسيط للمخطط الجديد (في عمودين)
st.write("#### Interpretation of the Trend Analysis:")
trend_col1, trend_col2 = st.columns(2)

with trend_col1:
    st.info("**Trendline Equation:**")
    st.code(f"y = {p.coeffs[0]:.2f}x + {p.coeffs[1]:.2f}")
    
    if p.coeffs[0] < 0:
        st.success("The trendline shows a **decreasing slope**, indicating a positive long-term outlook for disease control.")
    else:
        st.warning("The trendline shows an **increasing slope**, suggesting a need for continued vigilance.")

with trend_col2:
    st.info("**Key Insights:**")
    st.write(f"- The predicted change per week is **{p.coeffs[0]:.2f} cases**.")
    st.write("- This linear model helps visualize the overall direction of the epidemic.")
    st.markdown("Use this as a guide for strategic planning.")

st.write("---")
