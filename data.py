import numpy as np
import pandas as pd
import plotly.graph_objects as go
import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Rendimiento de Portafolio", layout="centered")


# 1. Generación de datos de prueba
@st.cache_data
def generar_datos():
    np.random.seed(42)
    fechas = pd.date_range(end=pd.Timestamp.today(), periods=365)
    
    # Simular retornos diarios estilo caminata aleatoria
    retornos = np.random.normal(loc=0.0008, scale=0.015, size=len(fechas))
    precio_inicial = 1000.0
    precios = precio_inicial * np.exp(np.cumsum(retornos))

    df = pd.DataFrame({"Fecha": fechas, "Valor": precios})
    return df


df = generar_datos()

# 2. Selector de periodo (1M, 3M, 6M, 1Y, ALL)
st.title("Mi Portafolio")

col_periodos, _ = st.columns([2, 1])
with col_periodos:
    periodo = st.radio(
        label="Periodo",
        options=["1M", "3M", "6M", "1Y", "ALL"],
        horizontal=True,
        label_visibility="collapsed",
        index=3,
    )

# Filtrar datos según la opción seleccionada
dias_map = {"1M": 30, "3M": 90, "6M": 180, "1Y": 365, "ALL": len(df)}
dias = dias_map[periodo]
df_filtrado = df.tail(dias).copy()

# 3. Cálculo de métricas
valor_inicial = df_filtrado["Valor"].iloc[0]
valor_actual = df_filtrado["Valor"].iloc[-1]
ganancia = valor_actual - valor_inicial
rendimiento_pct = (ganancia / valor_inicial) * 100

# Color dinámico (verde si sube, rojo si baja)
es_positivo = ganancia >= 0
color_linea = "#00C805" if es_positivo else "#FF3B30"  # Verdes / Rojos estilo trading
color_area = (
    "rgba(0, 200, 5, 0.12)" if es_positivo else "rgba(255, 59, 48, 0.12)"
)

# 4. Encabezado estilo Hapi (Valor actual + rendimiento)
st.metric(
    label="Valor Total",
    value=f"${valor_actual:,.2f}",
    delta=f"${ganancia:+,.2f} ({rendimiento_pct:+.2f}%) en {periodo}",
)

# 5. Creación del gráfico con Plotly
fig = go.Figure()

# Añadir la línea con relleno (Área)
fig.add_trace(
    go.Scatter(
        x=df_filtrado["Fecha"],
        y=df_filtrado["Valor"],
        mode="lines",
        line=dict(color=color_linea, width=2),
        fill="tozeroy",
        fillcolor=color_area,
        hovertemplate="<b>%{x|%b %d, %Y}</b><br>Valor: $%{y:,.2f}<extra></extra>",
    )
)

# Estilo minimalista tipo App móvil
fig.update_layout(
    xaxis=dict(
        showgrid=False,
        showline=False,
        showticklabels=True,
        zeroline=False,
    ),
    yaxis=dict(
        showgrid=True,
        gridcolor="rgba(128, 128, 128, 0.1)",  # Grilla sutil
        showline=False,
        showticklabels=False,  # En Hapi no se suelen mostrar los números del eje Y
        zeroline=False,
    ),
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    margin=dict(l=0, r=0, t=10, b=0),
    height=320,
    hovermode="x unified",
)

# Desactivar barra de herramientas flotante de Plotly
st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})