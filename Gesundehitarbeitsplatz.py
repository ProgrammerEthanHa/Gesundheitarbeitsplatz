import streamlit as st
import pandas as pd
import altair as alt

st.header("Mentale Gesundheit Statistiken & Trends im Jahr 2023")
st.subheader("Statistiken zur mentalen Gesundheit am Arbeitsplatz")

source = pd.DataFrame({
        'Anteil(%)': [80, 67],
        ' ': ['Der Tech-Mitarbeiter haben eine psychische Krise erlebt', 'Von den Fachleuten aus dem technischen Bereich gaben an, dass sie sich von ihrer Arbeit überfordert und gestresst fühlen']
     })
 
bar_chart = alt.Chart(source).mark_bar().encode(
        y='Anteil(%):Q',
        x=' :O',
    )
st.altair_chart(bar_chart, use_container_width=True)


txt = st.text_area('', '''
    Keine Angabe
    ''')
st.text("Klicke an die Balken um die Daten genauer anzuschauen. Du kannst auch die Diagramm vergrößern und ein Bild davon machen")
st.text("Quelle:  /")