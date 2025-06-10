import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from calculator import UserInput, calculate_macros


def test_calculate_macros():
    user = UserInput(
        gender="Male",
        age=29,
        weight=110,
        height=176,
        activity_factor=1.2,
        fat_ratio=0.3,
        protein_per_kg=1.5,
    )
    result = calculate_macros(user)
    assert round(result.total_calories) == 2472
    assert round(result.cho.calories) == 1070
    assert round(result.fat.calories) == 742
    assert round(result.ptn.calories) == 660
    assert round(result.cho.grams) == 268
    assert round(result.fat.grams) == 82
    assert round(result.ptn.grams) == 165
