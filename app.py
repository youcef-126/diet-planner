"""Streamlit interface for the diet planner."""
import streamlit as st
from calculator import UserInput, calculate_macros
from supabase_client import save_results

st.title("Diet Planner")

with st.form("inputs"):
    gender = st.selectbox("Gender", ["Male", "Female"])
    age = st.number_input("Age", min_value=0, value=25)
    weight = st.number_input("Weight (kg)", min_value=0.0, value=70.0, step=0.1)
    height = st.number_input("Height (cm)", min_value=0.0, value=170.0, step=0.1)
    activity = st.number_input("Activity Factor", min_value=1.0, value=1.2)
    fat_ratio = st.number_input("Fat Portion (0-1)", min_value=0.0, max_value=1.0, value=0.3)
    protein_per_kg = st.number_input("Protein (g/kg)", min_value=0.0, value=1.5)
    submitted = st.form_submit_button("Calculate")

if submitted:
    user = UserInput(
        gender=gender,
        age=int(age),
        weight=float(weight),
        height=float(height),
        activity_factor=float(activity),
        fat_ratio=float(fat_ratio),
        protein_per_kg=float(protein_per_kg),
    )
    result = calculate_macros(user)

    st.subheader("Results")
    st.write(f"Total Calories: {result.total_calories}")
    st.write(
        f"Carbs: {result.cho.grams} g ({result.cho.calories} kcal)")
    st.write(
        f"Fat: {result.fat.grams} g ({result.fat.calories} kcal)")
    st.write(
        f"Protein: {result.ptn.grams} g ({result.ptn.calories} kcal)")

    save_results(
        {
            "gender": gender,
            "age": int(age),
            "weight": float(weight),
            "height": float(height),
            "activity_factor": float(activity),
            "fat_ratio": float(fat_ratio),
            "protein_per_kg": float(protein_per_kg),
            "total_calories": result.total_calories,
            "cho_calories": result.cho.calories,
            "cho_grams": result.cho.grams,
            "fat_calories": result.fat.calories,
            "fat_grams": result.fat.grams,
            "ptn_calories": result.ptn.calories,
            "ptn_grams": result.ptn.grams,
        }
    )
    st.success("Results saved to Supabase")
