import os

import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="¿QUIERES UNA BECA EN INNOVABITE PRODUCTIONS COMPANY INC?",
    page_icon="🗿",
    layout="wide"
)

st.markdown(
    """
    <style>
        .main {
            background: linear-gradient(180deg, #f5f7ff 0%, #ffffff 100%);
        }
        .hero {
            background: linear-gradient(135deg, #1f3b8f 0%, #2e6eea 100%);
            padding: 2.2rem 2rem;
            border-radius: 1.2rem;
            color: white;
            box-shadow: 0 12px 30px rgba(34, 92, 196, 0.18);
        }
        .feature-card {
            background: #f7f9ff;
            border: 1px solid #e5ebff;
            border-radius: 0.9rem;
            padding: 1.2rem;
            height: 100%;
        }
        .kicker {
            letter-spacing: 0.12em;
            text-transform: uppercase;
            font-size: 0.72rem;
            opacity: 0.8;
            margin-bottom: 0.8rem;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("¿QUIERES UNA BECA EN INNOVABITE PRODUCTIONS COMPANY INC?")

# Load data safely
excel_path = "Six Seven.xlsx"
if os.path.exists(excel_path):
    df = pd.read_excel(excel_path)
else:
    df = pd.DataFrame({
        "Status": ["Excel file not found"],
        "Message": ["Add Six Seven.xlsx to the app folder."]
    })

with st.container():
    st.markdown(
        """
        <div class="hero">
            <div class="kicker">Advertencia esta pagina tiene virus</div>
            <h2 style="margin:0; font-size:2.4rem;">CONVIERTETE EN UN EXITOSO CON NUESTRO PROGRAMA DE BECAS EN INNOVABITE PRODUCTIONS COMPANY INC</h2>
            <p style="font-size:1.05rem; max-width:650px; margin-top:0.8rem; margin-bottom:1.2rem;">
                GRACIAS A NUESTRO EXITO EN LA CONTRATACIÓN DE CHAMBEADORES PROFESIONALES HEMOS DESARROLLADO UN PROGRAMA DE BECAS QUE TE PERMITE CONVERTIRTE EN UN EXITOSO EN NUESTRA EMPRESA.
            </p>
            <div style="display:flex; gap:0.8rem; flex-wrap:wrap;">
                <a href="#overview" style="text-decoration:none;">
                    <button style="background:#ffffff; color:#1f3b8f; border:none; border-radius:0.7rem; padding:0.75rem 1.2rem; font-weight:700; cursor:pointer;">Explore overview</button>
                </a>
                <a href="#contact" style="text-decoration:none;">
                    <button style="background:transparent; color:#ffffff; border:1px solid rgba(255,255,255,0.60); border-radius:0.7rem; padding:0.75rem 1.2rem; font-weight:700; cursor:pointer;">Contact us</button>
                </a>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("<br>", unsafe_allow_html=True)

if not df.empty:
    numeric_cols = df.select_dtypes(include="number").columns.tolist()
    total_records = len(df)
    total_columns = len(df.columns)
    sample_value = "—"
    if numeric_cols:
        sample_value = f"{df[numeric_cols[0]].mean():,.2f}"

    cols = st.columns(4)
    cols[0].metric("Records", f"{total_records:,}")
    cols[1].metric("Columns", total_columns)
    cols[2].metric("Insights", "Live")
    cols[3].metric("Sample avg", sample_value)

st.markdown("<br>", unsafe_allow_html=True)

st.subheader("Por que puedes contar con nosotros en tus estudios y en tu vida laboral")

features = [
    ("Becas de Éxito", "Queremos que nuestro proyecto de Becas sea un éxito y por eso queremos que cuentes con nosotros."),
    ("Proyectos Voladores", "Crea e ingenia tus propios proyectos como el six seven volador y el aura poderosa te recompensara."),
    ("Maxima Aura", "Podras tener la mas grande aura de todos los trabajadores si es que te aplicas mucho y te esfuerzas mas."),
]

feature_cols = st.columns(3)
for col, (title, body) in zip(feature_cols, features):
    with col:
        st.markdown(
            f"""
            <div class="feature-card">
                <h4>{title}</h4>
                <p>{body}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
st.markdown("<br>", unsafe_allow_html=True)

st.subheader("Overview")

if df.empty:
    st.info("No data is available yet. Add your Excel file to display the dataset.")
else:
    st.dataframe(df.head(10), use_container_width=True)

st.markdown("<br>", unsafe_allow_html=True)

st.subheader("Nada es mejor que empezar tu carrera profesional con nosotros y no con otra empresa")

with st.container():
    left, right = st.columns([1.3, 1])
    with left:
        st.write(
            "- Tenemos todo tipo de carreras las cuales te encantaran  \n"
            "- si nos llegas a demandar te descuartizamos putito \n"
            "- Gracias a nuestro programa de becas podras tener un futuro brillante y lleno de oportunidades \n"
            "- Vamos bendecidos con Dios para que no nos falte nada y podamos seguir creciendo como empresa \n"
        )
    with right:
        st.info("Por favor no ligues con nadie ni con el axel que esta secuestrado en una esquina de nuestro campus xd.")

st.markdown("<br>", unsafe_allow_html=True)

st.subheader("Contact")

contact_html = """
<div id="contact" style="background:#eef3ff; border:1px solid #d9e4ff; border-radius:0.9rem; padding:1.4rem;">
    <h4 style="margin-top:0;">Let's talk</h4>
    <p>tambien ofrecemos servicio para sacarte la virginidad o solo los pelos de tu coño.</p>
</div>
"""
st.markdown(contact_html, unsafe_allow_html=True)

st.caption("Se ya el primer paso para tu futuro profesional y personal con nosotros, no te arrepentiras de unirte a nuestra empresa.")
