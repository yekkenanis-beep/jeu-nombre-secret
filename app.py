import streamlit as st
import random

# Configuratio de la pag
st.set_page_config(
    page_title="Jeu du Nombre Secret",
    page_icon="🎲",
    layout="centered"
)

# Titre du jeu
st.title("🎲 Jeu du Nombre Secret")
st.markdown("### Devine le nombre secret entre **1** et **100**")

#  Initialisation de l'état du jeu 

if "nombre_secret" not in st.session_state:
    st.session_state.nombre_secret = random.randint(1, 100)
    st.session_state.tentatives = 0
    st.session_state.jeu_termine = False
    st.session_state.message = ""
    st.session_state.historique = []

#  Interface principale 

st.metric("📊 Nombre de tentatives", st.session_state.tentatives)

if st.session_state.message:
    if "Félicitations" in st.session_state.message:
        st.success(st.session_state.message)
    else:
        st.info(st.session_state.message)

if st.session_state.historique:
    with st.expander("📜 Historique de tes tentatives"):
        for i, tentative in enumerate(st.session_state.historique, 1):
            st.write(f"{i}. {tentative}")

st.divider()

#  Zone de jeu 

if not st.session_state.jeu_termine:
    
    estimation = st.number_input(
        "🔢 Entre ton estimation :",
        min_value=1,
        max_value=100,
        step=1,
        value=50,
        key="estimation"
    )
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🎯 Deviner", use_container_width=True):
            st.session_state.tentatives += 1
            st.session_state.historique.append(estimation)
            
            if estimation == st.session_state.nombre_secret:
                st.session_state.message = f"🎉 Félicitations ! Tu as trouvé en {st.session_state.tentatives} tentatives ! 🎉"
                st.session_state.jeu_termine = True
            elif estimation < st.session_state.nombre_secret:
                st.session_state.message = "📈 Le nombre secret est **plus grand** que ton estimation."
            else:
                st.session_state.message = "📉 Le nombre secret est **plus petit** que ton estimation."
            
            st.rerun()
    
    with col2:
        if st.button("🔄 Nouvelle partie", use_container_width=True):
            st.session_state.nombre_secret = random.randint(1, 100)
            st.session_state.tentatives = 0
            st.session_state.jeu_termine = False
            st.session_state.message = ""
            st.session_state.historique = []
            st.rerun()

#  Affichage de la victoire 

if st.session_state.jeu_termine:
    st.balloons()
    st.markdown(f"### 🎉 Bravo ! Tu as réussi en {st.session_state.tentatives} tentatives ! 🎉")
    
    if st.button("🎮 Rejouer", use_container_width=True):
        st.session_state.nombre_secret = random.randint(1, 100)
        st.session_state.tentatives = 0
        st.session_state.jeu_termine = False
        st.session_state.message = ""
        st.session_state.historique = []
        st.rerun()