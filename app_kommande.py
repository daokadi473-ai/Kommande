# Kommande - Interface Web (version girly)
# Design rose pastel + violet + doré

import streamlit as st

st.set_page_config(page_title="Kommande ✨", page_icon="✨", layout="wide")

# --- CSS personnalisé girly ---
st.markdown("""
<style>
    /* Fond principal */
    .stApp {
        background: linear-gradient(135deg, #FFF0F5 0%, #F5E6FF 100%);
    }
    
    /* Titre principal */
    h1 {
        color: #FF69B4 !important;
        text-align: center;
        font-family: 'Comic Sans MS', cursive;
        text-shadow: 2px 2px 4px rgba(255, 105, 180, 0.3);
    }
    
    /* Sous-titres */
    h2 {
        color: #DDA0DD !important;
        font-family: 'Comic Sans MS', cursive;
    }
    
    /* Métriques */
    .stMetric {
        background-color: #FFFFFF;
        border-radius: 15px;
        padding: 15px;
        box-shadow: 0 4px 6px rgba(255, 105, 180, 0.2);
        border: 2px solid #FFB6C1;
    }
    
    /* Sidebar */
    .css-1d391kg {
        background-color: #FFE4E9;
    }
    
    /* Boutons */
    .stButton>button {
        background-color: #FF69B4;
        color: white;
        border-radius: 20px;
        border: none;
        padding: 10px 20px;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# --- En-tête ---
st.markdown("# ✨ KOMMANDE ✨")
st.markdown("<p style='text-align:center; color:#DDA0DD; font-size:20px;'>🎀 Tes commandes, simplifiées 🎀</p>", unsafe_allow_html=True)

st.markdown("---")

# --- Menu ---
st.sidebar.markdown("## 📋 Menu")
st.sidebar.markdown("---")
choix = st.sidebar.selectbox(
    "Choisis une option :",
    ["🏠 Accueil", "📦 Mes commandes", "💰 Bénéfice", "📊 Statistiques", "⭐ Clients fidèles", "📦 Stocks", "⭐ Avis clients", "🎁 Parrainage", "💱 Devises", "🏆 Badges", "📤 Export", "💬 Aide"]
)

def lire_commandes():
    try:
        with open("commandes.txt", "r", encoding="utf-8") as f:
            return f.readlines()
    except FileNotFoundError:
        return []

# --- Page Accueil ---
if choix == "🏠 Accueil":
    st.markdown("## 🌸 Bienvenue sur Kommande ! 🌸")
    st.write("Kommande est ton assistant personnel pour gérer tes commandes, tes stocks, tes clients et tes bénéfices.")
    
    commandes = lire_commandes()
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("📦 Commandes", len(commandes))
    with col2:
        st.metric("💰 Bénéfice", "0 FCFA")
    with col3:
        st.metric("⭐ Clients", "0")

# --- Page Commandes ---
elif choix == "📦 Mes commandes":
    st.markdown("## 📦 Mes commandes")
    commandes = lire_commandes()
    
    if not commandes:
        st.info("📭 Aucune commande enregistrée pour le moment.")
    else:
        st.success(f"✅ {len(commandes)} commande(s) enregistrée(s)")
        for i, ligne in enumerate(commandes, 1):
            infos = ligne.strip().split(" | ")
            if len(infos) >= 6:
                st.markdown(f"### ✨ Commande #{i}")
                st.write(f"👤 **{infos[0]}** | 🛍️ {infos[1]} | 💰 {infos[2]} FCFA")
                st.write(f"📞 {infos[3]} | 📍 {infos[4]} | 🏠 {infos[5]}")
                st.markdown("---")

# --- Page Bénéfice ---
elif choix == "💰 Bénéfice":
    st.markdown("## 💰 Bénéfice réel")
    commandes = lire_commandes()
    
    ca = 0
    for ligne in commandes:
        infos = ligne.strip().split(" | ")
        if len(infos) >= 3:
            try:
                ca += int(infos[2])
            except:
                pass
    
    st.metric("💰 Chiffre d'affaires", f"{ca} FCFA")
    st.metric("💸 Dépenses", "0 FCFA")
    st.metric("📊 BÉNÉFICE RÉEL", f"{ca} FCFA")

# --- Page Statistiques ---
elif choix == "📊 Statistiques":
    st.markdown("## 📊 Statistiques")
    commandes = lire_commandes()
    
    if not commandes:
        st.info("📭 Aucune commande enregistrée.")
    else:
        produits = {}
        for ligne in commandes:
            infos = ligne.strip().split(" | ")
            if len(infos) >= 2:
                produit = infos[1]
                produits[produit] = produits.get(produit, 0) + 1
        
        st.markdown("### 🏆 Top produits")
        top = sorted(produits.items(), key=lambda x: x[1], reverse=True)
        for i, (p, q) in enumerate(top, 1):
            st.write(f"{i}. {p} : {q} commande(s)")

# --- Autres pages ---
elif choix == "⭐ Clients fidèles":
    st.markdown("## ⭐ Clients fidèles")
elif choix == "📦 Stocks":
    st.markdown("## 📦 Stocks")
elif choix == "⭐ Avis clients":
    st.markdown("## ⭐ Avis clients")
elif choix == "🎁 Parrainage":
    st.markdown("## 🎁 Parrainage")
elif choix == "💱 Devises":
    st.markdown("## 💱 Devises")
elif choix == "🏆 Badges":
    st.markdown("## 🏆 Badges")
elif choix == "📤 Export":
    st.markdown("## 📤 Export")
elif choix == "💬 Aide":
    st.markdown("## 💬 Aide")
