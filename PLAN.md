# Diet Planner Web App Plan

This document outlines a minimal viable product (MVP) to build a diet planner that calculates daily calorie and macronutrient targets then produces a simple meal plan suggestion. The goal is to rely on free tools.

## 1. Tech Stack

- **Streamlit** – for building a lightweight web interface quickly.
- **Supabase** – to handle authentication and store user profiles along with their calculation results.

Both services offer free tiers that are suitable for a small hobby project or demo.

## 2. Inputs

Collect the following information from the user:

- Gender
- Age
- Weight (kg)
- Height (cm)
- Activity factor
- Body fat percentage
- Desired protein (g/kg)
- Optional: sport type and duration

## 3. Calculations

A basic example using sample numbers is shown below. These values can be adjusted depending on your formulas.

| Macro | Calories | Grams |
|------|---------|------|
| CHO  | 1324    | 331  |
| FAT  | 850     | 94   |
| PTN  | 660     | 165  |
| **Total** | **2834** |      |

To translate calories into portions you can provide rules similar to the example:

| Macro | Portions | % of total |
|------|---------|-----------|
| CHO  | 4 | 46.7% |
| FAT  | 9 | 30.0% |
| PTN  | 4 | 23.3% |

Use the user inputs to calculate personalized values based on the same approach.

## 4. Application Flow

1. **User submits data** through the Streamlit form.
2. **Calculate** daily calorie needs and macro split with Python.
3. **Store** the results along with the profile in Supabase so the user can return later.
4. **Display** the daily targets and a simple list of meal ideas. You can optionally call an AI API to translate calories/macros into full meal plans.

## 5. Future Ideas

- Add user login with Supabase auth so each person can save multiple plans.
- Let users tweak the macro percentages.
- Incorporate AI suggestions for meal planning based on stored data.

This plan keeps the focus on a simple MVP using free tools while leaving room to expand in the future.

