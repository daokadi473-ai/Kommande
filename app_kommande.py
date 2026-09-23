
import streamlit as st

st.set_page_config(
    page_title="Kommande",
    page_icon="✨",
    layout="wide"
)

st.markdown("""
    <style>
    .main { background-color: #FFF0F5; }
    .title { color: #FF69B4; font-size: 50px; font-weight: bold; text-align: center; }
    .subtitle { color: #DDA0DD; font-size: 20px; text-align: center; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<p class="title">✨ KOMMANDE ✨</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Tes commandes, simplifiées.</p>', unsafe_allow_html=True)
st.markdown("---")

st.sidebar.title("📋 Menu")
choix = st.sidebar.radio(
    "Choisis une option :",
    ["🏠 Accueil", "📦 Mes commandes", "💰 Bénéfice", "📊 Statistiques", "⭐ Clients fidèles", "📦 Stocks", "⭐ Avis clients", "🎁 Parrainage", "💱 Devises", "🏆 Badges", "📤 Export", "💬 Aide"]
)

if choix == "🏠 Accueil":
    st.header("Bienvenue sur Kommande ! 🌸")
    st.write("Kommande est ton assistant personnel pour gérer tes commandes, tes stocks, tes clients et tes bénéfices.")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("📦 Commandes", "0", "0%")
    with col2:
        st.metric("💰 Bénéfice", "0 FCFA", "0%")
    with col3:
        st.metric("⭐ Clients", "0", "0%")
elif choix == "📦 Mes commandes":
    st.header("📦 Mes commandes")
elif choix == "💰 Bénéfice":
    st.header("💰 Bénéfice réel")
elif choix == "📊 Statistiques":
    st.header("📊 Statistiques")
elif choix == "⭐ Clients fidèles":
    st.header("⭐ Clients fidèles")
elif choix == "📦 Stocks":
    st.header("📦 Stocks")
elif choix == "⭐ Avis clients":
    st.header("⭐ Avis clients")
elif choix == "🎁 Parrainage":
    st.header("🎁 Parrainage")
elif choix == "💱 Devises":
    st.header("💱 Devises")
elif choix == "🏆 Badges":
    st.header("🏆 Badges")
elif choix == "📤 Export":
    st.header("📤 Export")
elif choix == "💬 Aide":
    st.header("💬 Aide")
