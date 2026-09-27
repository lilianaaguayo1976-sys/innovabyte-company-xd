import streamlit as st
import pandas as pd
from datetime import date

# Configuración de la página
st.set_page_config(page_title="Ganancias carreras easy car", page_icon="🚗", layout="centered")

st.title("🚗 Control Financiero EV ")

# -------------------------------------------------------------
# 1. METRICAS Y META DIARIA (BANCO + GANANCIA)
# -------------------------------------------------------------
st.subheader("🎯 Meta del Día")

# Definir la meta calculada según la cuota del banco
meta_diaria = 20  # Puedes ajustar esta cifra según la cuota real

col1, col2 = st.columns(2)
with col1:
    monto_hoy = st.number_input("Ingreso total de hoy ($):", min_value=0.0, value=0.0, step=1.0)
with col2:
    costo_carga = st.number_input("Costo de carga EV hoy ($):", min_value=0.0, value=0.0, step=0.5)

ganancia_neta_hoy = monto_hoy - costo_carga
restante = meta_diaria - ganancia_neta_hoy

st.metric(label="Ganancia Neta Hoy", value=f"${ganancia_neta_hoy:.2f}", delta=f"-${restante:.2f}" if restante > 0 else "¡Meta alcanzada! 🎉")

if restante <= 0:
    st.balloons()
    st.success("¡Excelente trabajo hoy! Cumpliste la meta para la cuota del banco y tu ganancia.")
else:
    st.warning(f"Te faltan **${restante:.2f}** para completar la meta de hoy.")

# -------------------------------------------------------------
# 2. REGISTRO RÁPIDO DE VIAJES
# -------------------------------------------------------------
st.markdown("---")
st.subheader("📝 Registrar Carrera / Ingreso")

with st.form("form_carrera", clear_on_submit=True):
    plataforma = st.radio("Plataforma", ["Easy Car", "Uber", "Cliente Directo"], horizontal=True)
    monto_carrera = st.number_input("Valor de la carrera ($)", min_value=0.0, step=0.50)
    sector_origen = st.text_input("Sector u Origen (opcional):", placeholder="Ej. Tumbaco")
    
    submitted = st.form_submit_button("Guardar Carrera")
    
    if submitted and monto_carrera > 0:
        # Aquí luego conectamos el guardado a un archivo Excel o Base de Datos
        st.success(f"Registrada carrera de ${monto_carrera:.2f} en {plataforma}")

# -------------------------------------------------------------
# 3. COMPARATIVA Y CONSEJOS EV
# -------------------------------------------------------------
st.markdown("---")
st.subheader("⚡ Estado del Vehículo Eléctrico")
st.info("💡 **Recordatorio EV:** Mantén las cargas rápidas al mínimo si es posible para cuidar la salud de la batería a largo plazo.")