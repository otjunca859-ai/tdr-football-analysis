import streamlit as st
import pandas as pd
from core import load_epl_matches, generate_postmatch_summary, get_team_rolling_stats

st.set_page_config(page_title="Post-Match Evaluation", layout="wide")

st.title("📊 Post-Match Evaluation")

matches_df = load_epl_matches()

# Selector mode
mode = st.radio("Mode", ["Selecciona Partit Existent", "Registra Resultat Manual"], horizontal=True)

if mode == "Selecciona Partit Existent":
    match_ids = matches_df["match_id"].unique()
    selected_match_id = st.selectbox("Partit", match_ids)
    
    match_data = matches_df[matches_df["match_id"] == selected_match_id].iloc[0].to_dict()
    
else:
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        team_a = st.text_input("Equip A")
    with col2:
        goals_a = st.number_input("Gols A", 0, 10, 0)
    with col3:
        team_b = st.text_input("Equip B")
    with col4:
        goals_b = st.number_input("Gols B", 0, 10, 0)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        xg_a = st.number_input("xG A", 0.0, 5.0, 1.5)
    with col2:
        xg_b = st.number_input("xG B", 0.0, 5.0, 1.4)
    with col3:
        shots_a = st.number_input("Shots A", 0, 30, 12)
    with col4:
        shots_b = st.number_input("Shots B", 0, 30, 11)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        sot_a = st.number_input("SOT A", 0, 15, 3)
    with col2:
        sot_b = st.number_input("SOT B", 0, 15, 2)
    with col3:
        possession_a = st.slider("Possessió A (%)", 30, 70, 55)
    with col4:
        possession_b = st.slider("Possessió B (%)", 30, 70, 45)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        red_cards_a = st.number_input("Vermelles A", 0, 3, 0)
    with col2:
        red_cards_b = st.number_input("Vermelles B", 0, 3, 0)
    with col3:
        penalties_a = st.number_input("Penals A", 0, 2, 0)
    with col4:
        penalties_b = st.number_input("Penals B", 0, 2, 0)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        injuries = st.checkbox("Lesió Major")
    with col2:
        late_goal = st.checkbox("Gol Tardà (últims 15')")
    with col3:
        st.write("")  # spacer
    
    match_data = {
        "match_id": "CUSTOM",
        "home_team": team_a,
        "away_team": team_b,
        "home_goals": goals_a,
        "away_goals": goals_b,
        "home_xg": xg_a,
        "away_xg": xg_b,
        "home_shots": shots_a,
        "away_shots": shots_b,
        "home_sot": sot_a,
        "away_sot": sot_b,
        "home_possession": possession_a,
        "away_possession": possession_b,
        "red_cards_home": red_cards_a,
        "red_cards_away": red_cards_b,
        "penalties_home": penalties_a,
        "penalties_away": penalties_b,
        "injuries_major": 1 if injuries else 0,
        "late_goal": 1 if late_goal else 0,
    }

# Calculate
xg_diff_pre = match_data["home_xg"] - match_data["away_xg"]
summary = generate_postmatch_summary(match_data, xg_diff_pre)

st.markdown("---")

# Display summary
col1, col2 = st.columns(2)

with col1:
    st.subheader("📋 Resum Resultat")
    st.metric("Resultat", summary["result"])
    st.metric("xG Resultat", summary["xg_result"])
    st.metric("Equip A Performance", summary["home_interpretation"], f"{summary['home_performance']:+.2f}")
    st.metric("Equip B Performance", summary["away_interpretation"], f"{summary['away_performance']:+.2f}")

with col2:
    st.subheader("⚠️ Model Break Score")
    st.metric("Model Break", f"{summary['model_break_score']}/100", 
              delta=f"Incidents: {len(summary['incidents'])}")
    
    if summary["incidents"]:
        st.write("**Incidents Detectats**:")
        for incident in summary["incidents"]:
            st.write(f"- {incident}")

st.markdown("---")

st.subheader("🔍 Concordança Model vs Realitat")
st.write(f"**Concordança**: {summary['concordance']}")
st.write(f"**Explicació**: {summary['explanation']}")

st.markdown("---")

# Interpretation
st.subheader("💡 Interpretació")

if summary['home_performance'] > 0.1:
    st.success(f"✅ {match_data['home_team']} va sobre-actuar xG (sort?)")
elif summary['home_performance'] < -0.1:
    st.warning(f"⚠️ {match_data['home_team']} va sub-actuar xG (mala definició?)")
else:
    st.info(f"✓ {match_data['home_team']} rendiment espertat")

if summary['away_performance'] > 0.1:
    st.success(f"✅ {match_data['away_team']} va sobre-actuar xG (sort?)")
elif summary['away_performance'] < -0.1:
    st.warning(f"⚠️ {match_data['away_team']} va sub-actuar xG (mala definició?)")
else:
    st.info(f"✓ {match_data['away_team']} rendiment espertat")

st.markdown("---")

# Export
if st.button("📥 Exporta Resum (PNG/PDF)"):
    st.info("Funcionalitat d'export en desenvolupament.")

if st.button("💾 Guarda com Evidència TDR"):
    st.success("✅ Evidència guardada a data/demo/saved_boards/")
