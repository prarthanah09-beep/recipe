import streamlit as st

st.set_page_config(page_title="Pizza Recipe", page_icon="🍕")

st.title("🍕 Homemade Vegetable Pizza Recipe")

# Pizza Image
st.image(
    "images/pizza.jpg",
    caption="Delicious Homemade Vegetable Pizza",
    use_container_width=True
)

st.write("Learn how to make a tasty homemade vegetable pizza at home!")

# Ingredients
st.subheader("🧂 Ingredients")

ingredients = [
    "🍞 Pizza Base - 1",
    "🍅 Tomato Sauce / Pizza Sauce - 3 tablespoons",
    "🧀 Mozzarella Cheese - 1 cup (grated)",
    "🧅 Onion - 1 medium (sliced)",
    "🫑 Capsicum - 1 medium (sliced)",
    "🍅 Tomato - 1 medium (sliced)",
    "🌽 Sweet Corn - 1/2 cup",
    "🫒 Olives - 1/4 cup (optional)",
    "🌶️ Chilli Flakes - 1 teaspoon",
    "🌿 Oregano - 1 teaspoon",
    "🧂 Salt - as required",
    "🧈 Butter/Oil - 1 tablespoon"
]

for item in ingredients:
    st.write(item)


# Recipe Steps
st.subheader("👩‍🍳 How to Make Pizza")

steps = [
    "1. Preheat the oven to 200°C for 10 minutes.",
    "2. Take a pizza base and spread pizza sauce evenly on it.",
    "3. Add grated mozzarella cheese over the sauce.",
    "4. Place sliced onion, capsicum, tomato and sweet corn on the pizza.",
    "5. Add some salt, oregano and chilli flakes according to taste.",
    "6. Add another layer of cheese on top.",
    "7. Place the pizza in the oven and bake for 10-15 minutes.",
    "8. Bake until the cheese melts and the base becomes crispy.",
    "9. Remove the pizza, cut into slices and serve hot."
]

for step in steps:
    st.write(step)


# Cooking Details
st.subheader("⏱ Cooking Details")

st.write("""
**Preparation Time:** 15 minutes

**Cooking Time:** 15 minutes

**Total Time:** 30 minutes

**Serving:** 2-3 people
""")


# Tips
st.subheader("💡 Cooking Tips")

tips = [
    "Use fresh vegetables for better taste.",
    "Add extra cheese for a cheesy pizza.",
    "Do not overload toppings because the pizza may become soggy.",
    "Serve immediately after baking for best flavor."
]

for tip in tips:
    st.write("✅", tip)


# Nutrition
st.subheader("🥗 Approximate Nutrition")

st.write("""
- Calories: 250-300 kcal per slice
- Protein: 12g
- Carbohydrates: 35g
- Fat: 10g
""")


st.success("🍕 Your homemade vegetable pizza is ready to enjoy!")

