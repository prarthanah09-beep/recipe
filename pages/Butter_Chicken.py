import streamlit as st

st.set_page_config(
    page_title="Butter Chicken Recipe",
    page_icon="🍗",
    layout="centered"
)

st.title("🍗 Butter Chicken Recipe")

# Butter Chicken Image
st.image(
    "images/butter_chicken.jpg",
    caption="Delicious Butter Chicken",
    use_container_width=True
)

st.write(
    "Butter Chicken is a famous North Indian dish made with tender chicken "
    "cooked in a rich, creamy tomato-based gravy."
)

# Ingredients
st.subheader("🧂 Ingredients")

ingredients = [
    "🍗 500 g Boneless Chicken",
    "🧈 2 tbsp Butter",
    "🛢️ 2 tbsp Oil",
    "🧅 2 Onions (finely chopped)",
    "🍅 3 Tomatoes (pureed)",
    "🧄 1 tbsp Ginger-Garlic Paste",
    "🥛 1/2 cup Fresh Cream",
    "🥄 1 tsp Garam Masala",
    "🌶️ 1 tsp Red Chilli Powder",
    "🟡 1/2 tsp Turmeric Powder",
    "🥄 1 tsp Coriander Powder",
    "🧂 Salt (to taste)",
    "🌿 Coriander Leaves (for garnish)"
]

for item in ingredients:
    st.write("✅", item)

# Preparation
st.subheader("👨‍🍳 How to Make Butter Chicken")

steps = [
    "1️⃣ Wash and clean the chicken pieces.",
    "2️⃣ Marinate the chicken with ginger-garlic paste, turmeric, chilli powder and salt for 30 minutes.",
    "3️⃣ Heat oil and butter in a pan.",
    "4️⃣ Add chopped onions and sauté until golden brown.",
    "5️⃣ Add tomato puree and cook for 5–7 minutes.",
    "6️⃣ Add coriander powder, garam masala and mix well.",
    "7️⃣ Add the marinated chicken and cook for 15–20 minutes.",
    "8️⃣ Pour fresh cream into the gravy and stir gently.",
    "9️⃣ Simmer for another 5 minutes until the gravy becomes thick.",
    "🔟 Garnish with coriander leaves."
]

for step in steps:
    st.write(step)

# Cooking Details
st.subheader("⏱ Cooking Information")

st.write("""
**Preparation Time:** 20 minutes

**Cooking Time:** 30 minutes

**Total Time:** 50 minutes

**Serves:** 4 People
""")

# Nutrition
st.subheader("🥗 Nutrition (Approx.)")

st.write("""
- Calories: 420 kcal
- Protein: 28 g
- Carbohydrates: 10 g
- Fat: 30 g
""")

# Best Served With
st.subheader("🍽 Best Served With")

foods = [
    "🫓 Butter Naan",
    "🫓 Garlic Naan",
    "🥖 Tandoori Roti",
    "🍚 Jeera Rice",
    "🍚 Steamed Rice"
]

for food in foods:
    st.write("✅", food)

# Tips
st.subheader("💡 Cooking Tips")

tips = [
    "Use fresh cream for a rich taste.",
    "Marinate the chicken for at least 30 minutes.",
    "Cook on medium flame for the best flavor.",
    "Garnish with fresh coriander before serving."
]

for tip in tips:
    st.write("✔️", tip)

st.success("🍗 Your delicious Butter Chicken is ready to serve. Enjoy!")