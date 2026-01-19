import streamlit as st


# إعدادات الصفحة
st.set_page_config(page_title="Cholera Overview", layout="wide")

# العنوان الرئيسي مع أيقونة طبية
# إنشاء عمودين: واحد صغير للصورة وواحد كبير للعنوان
col_logo, col_text = st.columns([1, 5])

with col_logo:
    # رابط شعار منظمة الصحة العالمية (أيقونة ملونة)
    st.image("https://img.icons8.com/color/96/world-health-organization.png", width=80)

with col_text:
    st.title("Cholera: Global Public Health Overview")

st.divider()





# قسم الملخص العام (Overview)
st.header("Overview")
st.info("""
**Cholera** is an acute diarrheal infection caused by consuming food or water contaminated with the bacterium *Vibrio cholerae*. 
It remains a global public health threat and a key indicator of inequity and lack of social and economic development. 
Access to safe water, basic sanitation, and hygiene (WASH) is essential to prevent cholera outbreaks.
""")

# تقسيم الأعمدة للمعلومات الحيوية
col1, col2 = st.columns(2)

with col1:
    st.subheader("🌡️ Symptoms & Incubation")
    st.write("- **Incubation Period:** Symptoms appear between 12 hours to 5 days after infection.")
    st.write("- **Severity:** Most cases are mild to moderate, but a minority develop severe acute watery diarrhoea leading to life-threatening dehydration.")
    st.write("- **Asymptomatic Spread:** Infected individuals can spread bacteria through faeces for 1–10 days even without symptoms.")

with col2:
    st.subheader("💊 Treatment & Care")
    st.write("- **Mild/Moderate:** Treated effectively with **Oral Rehydration Solution (ORS)**.")
    st.write("- **Severe Cases:** Require rapid intervention with intravenous fluids, ORS, and antibiotics.")
    st.warning("Starting treatment quickly is vital to save lives.")

st.divider()

# قسم الإحصائيات (Epidemiology)
st.header("Global Burden (2023 Statistics)")
st.markdown("""
According to WHO reports for 2023:
* **Total Reported Cases:** 535,321
* **Total Reported Deaths:** 4,007
* **Affected Countries:** 45 countries
""")
st.caption("Note: Actual numbers may be higher due to limited surveillance systems in some regions.")

# قسم الوقاية والسيطرة
st.header("🛡️ Prevention and Control")
st.write("Effective control involves a multi-sectoral approach:")
st.success("""
1. **WASH Improvements:** Better water, sanitation, and hygiene infrastructure.
2. **Surveillance:** Strengthening laboratory and epidemiological detection.
3. **Vaccination:** Implementing Oral Cholera Vaccine (OCV) campaigns.
4. **Community Engagement:** Increasing risk communication.
""")

# قسم السلالات (Strains)
with st.expander("🧬 Vibrio cholerae Strains"):
    st.write("Only two serogroups cause outbreaks: **O1** and **O139**.")
    st.write("- **O1:** Responsible for all recent global outbreaks.")
    st.write("- **O139:** Previously caused outbreaks in Asia; now only identified in sporadic cases.")