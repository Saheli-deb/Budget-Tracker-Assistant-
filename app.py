# import streamlit as st
# import json
# from utils import speak, listen
# from collections import defaultdict

# # Load products
# with open('products.json') as f:
#     products = json.load(f)

# # Initialize session state
# if 'budget' not in st.session_state:
#     st.session_state.budget = None
# if 'cart' not in st.session_state:
#     st.session_state.cart = []
# if 'voice_command' not in st.session_state:
#     st.session_state.voice_command = ""
# if 'speak_message' not in st.session_state:
#     st.session_state.speak_message = None
# if 'cart_updated' not in st.session_state:
#     st.session_state.cart_updated = False

# st.title("🛒 AIShopmate – Smart Budget-Aware Cart")

# # Step 1: Budget input
# if st.session_state.budget is None:
#     budget_input = st.number_input("💸 Enter your shopping budget (₹):", min_value=0, step=50)
#     if st.button("Set Budget"):
#         st.session_state.budget = budget_input
#         st.success(f"Budget set to ₹{budget_input}")
#         st.session_state.speak_message = f"Your budget is set to {int(budget_input)} rupees"
# else:
#     st.success(f"✅ Current Budget: ₹{st.session_state.budget}")

#     # Voice command button
#     if st.button("🎙 Voice Search"):
#         st.session_state.voice_command = listen()

#     # Text + voice search
#     query = st.text_input("🔍 What product are you looking for?", value=st.session_state.voice_command)

#     # Filtered Recommendations
#     if query:
#         st.subheader(f"🤖 Recommended for '{query}':")
#         filtered = [p for p in products if query.lower() in p['name'].lower() or query.lower() in p['category'].lower()]
#         for i, product in enumerate(filtered):
#             st.image(product['image'], width=120)
#             st.write(f"{product['name']} - ₹{product['price']}")
#             if st.button(f"Add to Cart - ₹{product['price']}", key=f"rec_{i}"):
#                 st.session_state.cart.append(product)
#                 st.session_state.speak_message = f"{product['name']} added to cart."

#     # Manual Product Section
#     st.subheader("🛍️ Popular Products:")
#     for i, product in enumerate(products):
#         st.image(product['image'], width=120)
#         st.write(f"{product['name']} - ₹{product['price']}")
#         if st.button(f"Add to Cart - ₹{product['price']}", key=f"static_{i}"):
#             st.session_state.cart.append(product)
#             st.session_state.speak_message = f"{product['name']} added to cart."

#     # Cart Display
#     if st.session_state.cart:
#         st.subheader("🧺 Your Cart:")
#         total = 0
#         cat_spend = defaultdict(int)

#         new_cart = []
#         for i, item in enumerate(st.session_state.cart):
#             col1, col2 = st.columns([4, 1])
#             with col1:
#                 st.write(f"{item['name']} - ₹{item['price']} ({item['category']})")
#             with col2:
#                 if st.button(f"❌", key=f"remove_{i}"):
#                     st.session_state.speak_message = f"{item['name']} removed from cart."
#                     continue  # Skip adding this item to new cart (removes it)
#             total += item['price']
#             cat_spend[item['category']] += item['price']
#             new_cart.append(item)

#         # Update cart
#         st.session_state.cart = new_cart

#         st.write(f"💰 **Total: ₹{total}**")

#         # Category-wise spending
#         st.subheader("📊 Category-wise Spending")
#         for cat, amt in cat_spend.items():
#             st.write(f"• {cat.capitalize()}: ₹{amt}")

#         # Budget Check
#         if total > st.session_state.budget:
#             st.error(f"🚨 Over Budget by ₹{total - st.session_state.budget}")
#             st.session_state.speak_message = "You are over budget. Please remove some items."
#         else:
#             st.success(f"🟢 Within Budget! Remaining: ₹{st.session_state.budget - total}")
#             st.session_state.speak_message = "You are under budget."

# # 🔊 Speak only once
# if st.session_state.get('speak_message'):
#     speak(st.session_state.speak_message)
#     st.session_state.speak_message = None

import streamlit as st
import json
from utils import speak, listen
from collections import defaultdict

# Load products
with open('products.json') as f:
    products = json.load(f)

# Initialize session state
if 'budget' not in st.session_state:
    st.session_state.budget = None
if 'cart' not in st.session_state:
    st.session_state.cart = []
if 'voice_command' not in st.session_state:
    st.session_state.voice_command = ""
if 'speak_message' not in st.session_state:
    st.session_state.speak_message = None

st.set_page_config(page_title="AIShopmate", layout="wide")
st.title("🛒 AIShopmate – Smart Budget-Aware Cart")

# Step 1: Budget input
with st.sidebar:
    st.header("💰 Set Your Budget")
    if st.session_state.budget is None:
        budget_input = st.number_input("Enter your shopping budget (₹):", min_value=0, step=50)
        if st.button("Set Budget"):
            st.session_state.budget = budget_input
            st.success(f"Budget set to ₹{budget_input}")
            st.session_state.speak_message = f"Your budget is set to {int(budget_input)} rupees"
    else:
        st.success(f"Budget: ₹{st.session_state.budget}")
        if st.button("Reset Budget"):
            st.session_state.budget = None
            st.session_state.cart = []

# Voice command button
st.markdown("---")
col1, col2 = st.columns([6, 1])
with col1:
    query = st.text_input("🔍 What product are you looking for?", value=st.session_state.voice_command)
with col2:
    if st.button("🎙"):
        st.session_state.voice_command = listen()
        st.experimental_rerun()

# Filtered Recommendations
if query:
    st.subheader(f"🤖 Recommended for '{query}':")
    filtered = [p for p in products if query.lower() in p['name'].lower() or query.lower() in p['category'].lower()]
    if filtered:
        cols = st.columns(3)
        for i, product in enumerate(filtered):
            col = cols[i % 3]
            with col:
                st.image(product['image'], width=150)
                st.markdown(f"**{product['name']}**")
                st.markdown(f"₹{product['price']}")
                if st.button(f"Add to Cart", key=f"rec_{i}"):
                    st.session_state.cart.append(product)
                    st.session_state.speak_message = f"{product['name']} added to cart."
    else:
        st.info("No products found matching your search.")

# Manual Product Section
st.markdown("---")
st.subheader("🛍️ Popular Products")
cols = st.columns(3)
for i, product in enumerate(products):
    col = cols[i % 3]
    with col:
        st.image(product['image'], width=150)
        st.markdown(f"**{product['name']}**")
        st.markdown(f"₹{product['price']}")
        if st.button(f"Add to Cart", key=f"static_{i}"):
            st.session_state.cart.append(product)
            st.session_state.speak_message = f"{product['name']} added to cart."

# Cart Display
st.markdown("---")
if st.session_state.cart:
    st.subheader("🧺 Your Cart")
    total = 0
    cat_spend = defaultdict(int)
    new_cart = []
    for i, item in enumerate(st.session_state.cart):
        cols = st.columns([5, 1])
        with cols[0]:
            st.markdown(f"**{item['name']}** - ₹{item['price']} ({item['category']})")
        with cols[1]:
            if st.button("❌", key=f"remove_{i}"):
                st.session_state.speak_message = f"{item['name']} removed from cart."
                continue
        total += item['price']
        cat_spend[item['category']] += item['price']
        new_cart.append(item)

    st.session_state.cart = new_cart
    st.markdown(f"### 💰 Total: ₹{total}")

    st.subheader("📊 Category-wise Spending")
    for cat, amt in cat_spend.items():
        st.write(f"• {cat.capitalize()}: ₹{amt}")

    if st.session_state.budget:
        if total > st.session_state.budget:
            st.error(f"🚨 Over Budget by ₹{total - st.session_state.budget}")
            st.session_state.speak_message = "You are over budget. Please remove some items."
        else:
            st.success(f"🟢 Within Budget! Remaining: ₹{st.session_state.budget - total}")
            st.session_state.speak_message = "You are under budget."

# Speak message (only one per run)
if st.session_state.get('speak_message'):
    speak(st.session_state.speak_message)
    st.session_state.speak_message = None
