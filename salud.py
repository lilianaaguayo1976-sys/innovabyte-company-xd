import pandas as pd
import plotly.graph_objects as go
import streamlit as st
import yfinance as yf

st.set_page_config(page_title="Rendimiento Estilo Hapi", layout="centered")

# --- 1. BUSCADOR Y SELECTORES ---
col_ticker, col_periodos = st.columns([1, 2])

with col_ticker:
    # Campo para cambiar de acción (AAPL, TSLA, NVDA, BTC-USD, etc.)
    ticker_input = st.text_input(
        "Acción/Cripto", value="AAPL", label_visibility="collapsed"
    ).upper()

with col_periodos:
    # Selector de periodos estilo Hapi
    periodo_seleccionado = st.radio(
        label="Periodo",
        options=["1M", "3M", "6M", "1Y", "ALL"],
        horizontal=True,
        label_visibility="collapsed",
        index=3,  # Por defecto '1Y'
    )

# Mapeo de periodos para yfinance
mapa_periodos = {"1M": "1mo", "3M": "3mo", "6M": "6mo", "1Y": "1y", "ALL": "max"}
periodo_yf = mapa_periodos[periodo_seleccionado]


# --- 2. CONSULTA A YFINANCE CON CACHÉ ---
@st.cache_data(ttl="1m")
def obtener_datos(simbolo, periodo):
    try:
        data = yf.Ticker(simbolo)
        df = data.history(period=periodo).reset_index()
        if df.empty:
            return None, None
        df = df[["Date", "Close"]].rename(
            columns={"Date": "Fecha", "Close": "Valor"}
        )

        # Nombre de la empresa / activo
        info = data.info
        nombre_empresa = info.get(
            "shortName", info.get("longName", simbolo)
        )
        return df, nombre_empresa
    except Exception:
        return None, None


df, nombre_empresa = obtener_datos(ticker_input, periodo_yf)

# --- 3. RENDERIZADO DEL GRÁFICO Y MÉTRICAS ---
if df is not None and not df.empty:
    valor_inicial = df["Valor"].iloc[0]
    valor_actual = df["Valor"].iloc[-1]
    ganancia = valor_actual - valor_inicial
    pct = (ganancia / valor_inicial) * 100

    # Determinar verde o rojo según el periodo activo
    es_positivo = ganancia >= 0
    color_linea = "#00C805" if es_positivo else "#FF3B30"
    color_area = (
        "rgba(0, 200, 5, 0.12)" if es_positivo else "rgba(255, 59, 48, 0.12)"
    )

    # Encabezado dinámico
    st.caption(f"{nombre_empresa} ({ticker_input})")
    st.metric(
        label="Precio",
        value=f"${valor_actual:,.2f}",
        delta=f"${ganancia:+,.2f} ({pct:+.2f}%) en {periodo_seleccionado}",
    )

    # Gráfico Plotly
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=df["Fecha"],
            y=df["Valor"],
            mode="lines",
            line=dict(color=color_linea, width=2.5),
            fill="tozeroy",
            fillcolor=color_area,
            hovertemplate="<b>%{x|%b %d, %Y}</b><br>Valor: $%{y:,.2f}<extra></extra>",
        )
    )

    fig.update_layout(
        xaxis=dict(
            showgrid=False, showline=False, showticklabels=True, zeroline=False
        ),
        yaxis=dict(
            showgrid=False,
            showline=False,
            showticklabels=False,
            zeroline=False,
        ),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=0, r=0, t=10, b=0),
        height=320,
        hovermode="x unified",
    )

    st.plotly_chart(
        fig, use_container_width=True, config={"displayModeBar": False}
    )
else:
    st.error(
        f"No se encontraron datos para '{ticker_input}'. Verifica que el símbolo sea correcto."
    )