import streamlit as st
import pandas as pd

st.title("🍽️ Recipe Recommendation System")

# Load CSV
df = pd.read_csv("recipes.csv")

# Remove extra spaces from column names
df.columns = df.columns.str.strip()

# Convert ingredients to lowercase
df["Ingredients"] = df["Ingredients"].astype(str).str.lower()

# Search ingredient
ingredient = st.text_input("Enter ingredient")

if ingredient:
    ingredient = ingredient.lower().strip()

    result = df[df["Ingredients"].str.contains(ingredient, case=False, na=False)]

    if len(result) > 0:
        st.success("Recipes Found")

        for i, row in result.iterrows():

            st.subheader("🍴 " + row["Recipe"])

            st.write("Ingredients:", row["Ingredients"])
            st.write("Cuisine:", row["Cuisine"])
            st.write("Region:", row["Region"])

            # Open Recipe Pages

            if row["Recipe"].strip() == "Pizza":
                st.page_link(
                    "pages/Pizza.py",
                    label="🍕 Open Pizza Recipe"
                )

            elif row["Recipe"].strip() == "Veg Fried Rice":
                st.page_link(
                    "pages/Veg_Fried_Rice.py",
                    label="🍚 Open Veg Fried Rice Recipe"
                )
            elif row["Recipe"].strip() == "Butter Chicken":
             st.page_link(
        "pages/Butter_chicken.py",
        label="🍗 Open Butter Chicken Recipe"
    )

            st.divider()

    else:
        st.error(f"No matches found for {ingredient}")


# Display database
st.subheader("📋 Recipe Database")
st.dataframe(df)

