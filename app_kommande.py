import streamlit as st

st.set_page_config(page_title="Kommande", page_icon="✨", layout="wide")

st.title("✨ KOMMANDE ✨")
st.markdown("<p style='text-align:center; color:#DDA0DD;'>Tes commandes, simplifiées.</p>", unsafe_allow_html=True)

st.sidebar.title("📋 Menu")
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

if choix == "🏠 Accueil":
    st.header("Bienvenue sur Kommande ! 🌸")
    st.write("Kommande est ton assistant personnel pour gérer tes commandes, tes stocks, tes clients et tes bénéfices.")
    
    commandes = lire_commandes()
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("📦 Commandes", len(commandes))
    with col2:
        st.metric("💰 Bénéfice", "0 FCFA")
    with col3:
        st.metric("⭐ Clients", "0")

elif choix == "📦 Mes commandes":
    st.header("📦 Mes commandes")
    commandes = lire_commandes()
    
    if not commandes:
        st.info("📭 Aucune commande enregistrée pour le moment.")
    else:
        st.success(f"✅ {len(commandes)} commande(s) enregistrée(s)")
        for i, ligne in enumerate(commandes, 1):
            infos = ligne.strip().split(" | ")
            if len(infos) >= 6:
                st.markdown(f"**Commande #{i}**")
                st.write(f"👤 {infos[0]} | 🛍️ {infos[1]} | 💰 {infos[2]} FCFA")
                st.write(f"📞 {infos[3]} | 📍 {infos[4]} | 🏠 {infos[5]}")
                st.markdown("---")

elif choix == "💰 Bénéfice":
    st.header("💰 Bénéfice réel")
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

elif choix == "📊 Statistiques":
    st.header("📊 Statistiques")
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
        
        st.subheader("🏆 Top produits")
        top = sorted(produits.items(), key=lambda x: x[1], reverse=True)
        for i, (p, q) in enumerate(top, 1):
            st.write(f"{i}. {p} : {q} commande(s)")

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
