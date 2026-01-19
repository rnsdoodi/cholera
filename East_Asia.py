import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import glob
import plotly.express as px

#####################################################################
st.markdown("""
<style>
.metric-card {
    background-color: #ffffff;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.08);
    text-align: center;
    border-left: 6px solid #e63946;
}

.metric-title {
    font-size: 14px;
    color: #6c757d;
    font-weight: 600;
}

.metric-value {
    font-size: 32px;
    font-weight: 700;
    color: #1d3557;
    margin-top: 5px;
}

.metric-sub {
    font-size: 13px;
    color: #457b9d;
}
</style>
""", unsafe_allow_html=True)

#####################################################################


# إعداد الصفحة لتكون بعرض كامل (مهم جداً لترتيب العناصر بجانب بعضها)
st.set_page_config(page_title="Cholera Dashboard", layout="wide")

# --- 1. العنوان ---
col_title1, col_title2 = st.columns([0.1, 0.9])
with col_title1:
  st.image("https://img.icons8.com/color/96/globe-asia.png", width=70)
  
  
  
   
with col_title2:
    st.title("South-East Asia Region")


##############################################################################

st.divider()

emp1, col1, col2, col3, emp2 = st.columns([1, 2, 2, 2, 1])

with col1:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-title">TOTAL CASES</div>
        <div class="metric-value">6430</div>
        <div class="metric-sub">Confirmed Cases</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-card" style="border-left-color:#457b9d;">
        <div class="metric-title">TOTAL DEATHS</div>
        <div class="metric-value">5</div>
        <div class="metric-sub">Deaths</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-card" style="border-left-color:#2a9d8f;">
        <div class="metric-title">CFR</div>
        <div class="metric-value">0.0777%</div>
        <div class="metric-sub">Case Fatality Rate</div>
    </div>
    """, unsafe_allow_html=True)



st.divider()

###############################################################################
###############################################################################


# --- 3. ترتيب المحتوى في صف واحد (الصف الثاني) ---
# سنقسم الشاشة إلى عمودين: الأول للمخططات الدائرية والثاني للخريطة
main_col1, main_col2 = st.columns([0.5, 0.5]) # 40% للمخططات و 60% للخريطة

with main_col1:
    st.subheader("Risk Analysis", text_alignment="center")
    
    total_cases = 6430
    total_deaths = 5
    cfr = 0.0777

    # إنشاء المخططات بشكل رأسي لتناسب العمود
    fig_stats = make_subplots(rows=2, cols=1, specs=[[{"type": "bar"}], [{"type": "pie"}]],
                            subplot_titles=("Confirmed Cases vs Total Deaths", "CFR %"))

    fig_stats.add_trace(
    go.Funnel(
        y=["Confirmed Cases", "Total Deaths"],
        x=[total_cases, total_deaths],
        textinfo="value+percent initial", # يعرض الرقم ونسبة الوفيات من الحالات تلقائياً
        marker={"color": ["#2E86C1", "#C0392B"]},
        connector={"line": {"color": "gray", "width": 2}}
    ),
    row=1, col=1
)
    
    fig_stats.add_trace(
    go.Indicator(
        mode = "gauge+number",
        value = cfr,
        number = {'suffix': "%"},
        title = {'text': "Case Fatality Rate", 'font': {'size': 16}},
        gauge = {
            'axis': {'range': [None, 10]}, # المدى حتى 10% مثلاً
            'bar': {'color': "#C0392B"},
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "gray",
        }
    ),
    row=2, col=1
 )
    
    
    

    fig_stats.update_layout(height=600, showlegend=False)
    st.plotly_chart(fig_stats, use_container_width=True)
    
    
###############################################################################

with main_col2:
    st.subheader("Geographic Spread", text_alignment="center")
    
    try:
        # قراءة ومعالجة البيانات
        file_name = glob.glob("cholera*.xlsx")[0]
        cholera_df = pd.read_excel(file_name, engine="openpyxl")
        cholera_df.dropna(subset=['iso_code', 'case_total'], inplace=True)
        
        country_data = cholera_df.groupby(['country', 'iso_code'])[['case_total', 'death_total']].sum().reset_index()
        country_data['CFR (%)'] = (country_data['death_total'] / country_data['case_total'] * 100).round(2)
        
        
###############################################################################
###############################################################################
######################### Africa Map ##########################################

        # رسم الخريطة مع خلفية داكنة
        fig_map = px.choropleth(
            country_data,
            locations="iso_code",
            color="case_total",
            hover_name="country",
            hover_data=["death_total", "CFR (%)"],
            color_continuous_scale=px.colors.sequential.YlOrRd,
            scope="asia",
            template="plotly_dark"  # هذا السطر يجعل خلفية الخريطة سوداء/داكنة
        )
        
        # لضبط لون المحيطات أو الخلفية الخارجية لتكون سوداء تماماً
        fig_map.update_geos(
            showcoastlines=True, 
            coastlinecolor="Gray",
            showland=True, 
            landcolor="#ECF7FF", # لون اليابسة للدول التي ليس بها بيانات
            showocean=True, 
            oceancolor="#6CBEFD", # لون المحيط (أسود)
            showlakes=True, 
            lakecolor="#2F8ED7"   # لون البحيرات (أسود)
        )
        
        fig_map.update_layout(
            height=600, # قمت بزيادة الارتفاع ليتناسق مع المخططات بجانبه
            margin={"r":0,"t":0,"l":0,"b":0},
            paper_bgcolor='rgba(0,0,0,0)', # يجعل خلفية الرسم شفافة لتندمج مع Dashboard
            plot_bgcolor='rgba(0,0,0,0)'
        )
        st.plotly_chart(fig_map, use_container_width=True)
        
        # fig_map.update_layout(height=400, margin={"r":0,"t":0,"l":0,"b":0})
        # st.plotly_chart(fig_map, use_container_width=True)
        
    except Exception as e:
        st.error(f"Error loading map data: {e}")


