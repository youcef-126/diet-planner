# Diet Planner

A minimal Streamlit application that calculates daily calorie and macronutrient
targets and stores them in Supabase.

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Provide Supabase credentials via environment variables:
   ```bash
   export SUPABASE_URL=YOUR_SUPABASE_URL
   export SUPABASE_KEY=YOUR_SERVICE_ROLE_KEY
   ```
3. Run the application:
   ```bash
   streamlit run app.py
   ```

See [PLAN.md](./PLAN.md) for the design overview.
