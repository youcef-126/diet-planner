"""Macronutrient and calorie calculations."""
from dataclasses import dataclass

@dataclass
class UserInput:
    gender: str
    age: int
    weight: float  # kg
    height: float  # cm
    activity_factor: float
    fat_ratio: float  # portion of calories from fat, e.g. 0.3
    protein_per_kg: float  # grams of protein per kg body weight

@dataclass
class MacroResult:
    calories: float
    grams: float

@dataclass
class CalculationResult:
    cho: MacroResult
    fat: MacroResult
    ptn: MacroResult
    total_calories: float


def calculate_bmr(user: UserInput) -> float:
    """Calculate basal metabolic rate using Mifflin-St Jeor formula."""
    if user.gender.lower() == "male":
        s = 5
    else:
        s = -161
    return 10 * user.weight + 6.25 * user.height - 5 * user.age + s


def calculate_tdee(user: UserInput) -> float:
    """Calculate total daily energy expenditure."""
    bmr = calculate_bmr(user)
    return bmr * user.activity_factor


def calculate_macros(user: UserInput) -> CalculationResult:
    """Calculate macronutrients based on user input."""
    total_cal = calculate_tdee(user)
    protein_g = user.weight * user.protein_per_kg
    protein_cal = protein_g * 4

    fat_cal = total_cal * user.fat_ratio
    fat_g = fat_cal / 9

    cho_cal = total_cal - protein_cal - fat_cal
    cho_g = cho_cal / 4

    return CalculationResult(
        cho=MacroResult(calories=round(cho_cal, 2), grams=round(cho_g, 2)),
        fat=MacroResult(calories=round(fat_cal, 2), grams=round(fat_g, 2)),
        ptn=MacroResult(calories=round(protein_cal, 2), grams=round(protein_g, 2)),
        total_calories=round(total_cal, 2),
    )
