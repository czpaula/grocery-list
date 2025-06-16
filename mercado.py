import streamlit as st
import json
import os

PRODUCTS_FILE = 'products.json'
CART_FILE = 'cart.json'

# Functions
def load_products():
    if os.path.exists(PRODUCTS_FILE):
        with open(PRODUCTS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        return "Empty list"

def load_cart():
    if os.path.exists(CART_FILE):
        with open(CART_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)            
    else:
        return "Empty list"
    
def save_cart(cart_list):
    with open(CART_FILE, 'w', encoding='utf-8') as f:
        json.dump(cart_list, f, ensure_ascii=False, indent=2)

def add_item(selected_item, quantity):
    for item in cart_list:
        if item == {"item": selected_item, "quantity": f"{quantity}"}: 
            st.error(f"⚠️ The item '{selected_item}' is already in the list.\n")
            return
    new_item = {"item": selected_item, "quantity": f"{quantity}"}
    cart_list.append(new_item)
    save_cart(cart_list)
    print(f"✅ Item '{selected_item} ({quantity})' added!\n") 

def update_cart_display():
    for item in cart_list:
        col1, col2 = st.columns([4, 1])
        col1.write(f"{item['item']} ({item.get('quantity')})")
        if col2.button("🗑️", key=str(item)):
            remove_item(item)
            st.success(f"{item['item']} ({item['quantity']}) was removed!") 
            st.button("Ok")

def remove_item(item):
    cart_list.remove(item)
    save_cart(cart_list)

# Load initial data
cart_list = load_cart()

st.set_page_config(page_title="Grocery Market", page_icon="🍳")
st.title("🍳 Grocery Market")
st.subheader("Shopping List")

# Generate list of product names
products_json = load_products()
product_items = [product['item'] for product in products_json if 'item' in product]

# Product selection
selected_item = st.selectbox("Product:", options=product_items)

# Quantity selection
quantity = st.slider("Quantity:", min_value=1, max_value=20, value=1)

# Button to add item
if st.button("Add"):
    add_item(selected_item, quantity)

st.subheader("🛒 Current Shopping List")
update_cart_display()
