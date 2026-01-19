import streamlit as st



pages = {
    "Introduction": [
        st.Page("introduction.py", title="Cholera"),
    ],
    
    "Regions Analysis": [
        st.Page("africa.py", title=" African Region "),
        st.Page("America.py", title="American Region"),
        st.Page("Pacific.py", title="Western Pacific Region"),
        st.Page("East_Asia.py", title="South-East Asia Region"),
        st.Page("Meditarian.py", title="Eastern Mediterranean Region"),
    ],
    
    "Trend Analysis": [
        st.Page("Trend.py", title="Epidemic Curve"),
        st.Page("predicting.py", title=" Predicting of Spread"),
    ],
   
    
}


with st.sidebar:
    st.image(r"C:\Users\rnsdo\OneDrive\Attachments\Desktop\Python and Microsoft Certificatse\cisco networking academy\My projects\cholera\who.jpg", use_container_width=True)
    # st.markdown("### Clinical Analysis Lab")
    st.divider()




pg = st.navigation(pages)
pg.run()


