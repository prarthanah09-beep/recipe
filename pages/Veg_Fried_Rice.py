import streamlit as st

st.set_page_config(
    page_title="Vegetable Fried Rice",
    page_icon="🍚"
)

st.title("🍚 Vegetable Fried Rice")

st.image("images/vegetable_fried_rice.jpg", use_container_width=True)

st.subheader("Description")
st.write("""
Vegetable Fried Rice is a delicious Indo-Chinese dish made with cooked rice,
fresh vegetables, and simple seasonings. It is quick, healthy, and easy to prepare.
""")

st.subheader("Ingredients")

ingredients = [
    "2 cups cooked rice",
    "1 carrot (chopped)",
    "10 beans (chopped)",
    "1 onion (sliced)",
    "1 capsicum (chopped)",
    "2 tablespoons oil",
    "1 teaspoon ginger-garlic paste",
    "1 teaspoon soy sauce",
    "1 teaspoon vinegar",
    "1/2 teaspoon black pepper",
    "Salt to taste",
    "Spring onions"
]

for item in ingredients:
    st.write("✅", item)

st.subheader("Preparation Time")
st.info("20 Minutes")

st.subheader("Cooking Instructions")

steps = [
    "Heat oil in a pan.",
    "Add ginger-garlic paste and sauté.",
    "Add onion and fry until soft.",
    "Add carrot, beans, and capsicum.",
    "Cook vegetables for 5 minutes.",
    "Add soy sauce, vinegar, salt, and pepper.",
    "Add cooked rice and mix well.",
    "Cook for another 3 minutes.",
    "Garnish with spring onions.",
    "Serve hot."
]

for i, step in enumerate(steps, 1):
    st.write(f"**Step {i}:** {step}")

st.subheader("Nutrition Information")

col1, col2 = st.columns(2)

with col1:
    st.metric("Calories", "280 kcal")
    st.metric("Protein", "6 g")

with col2:
    st.metric("Carbohydrates", "45 g")
    st.metric("Fat", "8 g")

st.success("🍽️ Enjoy your homemade Vegetable Fried Rice!")