import streamlit as st
import json
import os
import datetime

ITEMS_FILE = 'items_data.json'
BILLS_FILE = 'bills_data.json'

# Load items from file
def load_items():
    if os.path.exists(ITEMS_FILE):
        with open(ITEMS_FILE, 'r') as file:
            return json.load(file)
    return []

# Save items to file
def save_items(items):
    with open(ITEMS_FILE, 'w') as file:
        json.dump(items, file, indent=4)

# Load saved bills
def load_bills():
    if os.path.exists(BILLS_FILE):
        with open(BILLS_FILE, 'r') as file:
            return json.load(file)
    return []

# Save bills
def save_bills(bills):
    with open(BILLS_FILE, 'w') as file:
        json.dump(bills, file, indent=4)

# Initialize
items = load_items()
bills = load_bills()

st.set_page_config(page_title="Grocery Store Management", page_icon="🏍️")
st.title("🛒 Grocery Store Management System")

menu = st.sidebar.selectbox("Menu", [
    "View Items",
    "Add Item",
    "Purchase Items (Billing)",
    "Search Item",
    "Edit Item",
    "View Bills"
])

# View Items
if menu == "View Items":
    st.header("📦 All Items in Store")
    if items:
        for i, item in enumerate(items):
            with st.expander(f"Item {i+1}: {item.get('name', 'Unnamed')}"):
                st.write(f"📁 Category: {item.get('category', 'N/A')}")
                st.write(f"📦 Quantity: {item.get('quantity', 'N/A')}")
                st.write(f"💰 Price: ₹{item.get('price', 'N/A')}")
    else:
        st.warning("No items available in inventory.")

# Add Items
elif menu == "Add Item":
    st.header("➕ Add New Item")
    name = st.text_input("Item Name")
    category = st.selectbox("Category", ["Fruits", "Vegetables", "Dairy", "Snacks", "Beverages", "Other"])
    quantity = st.selectbox("Quantity", [
        "1/2 kg", "1 kg", "2 kg", "5 kg", "10 kg",
        "500 ml", "1 L", "2 L", "5 L"
    ])
    price = st.number_input("Price (₹)", min_value=1, step=1)

    if st.button("Add Item"):
        if name:
            item = {'name': name, 'quantity': quantity, 'price': price, 'category': category}
            items.append(item)
            save_items(items)
            st.success(f"✅ Item '{name}' added successfully!")
        else:
            st.warning("⚠️ Please enter the item name.")

# Purchase Items with Billing
elif menu == "Purchase Items (Billing)":
    st.header("🛍️ Purchase Items and Generate Bill")
    customer_name = st.text_input("Enter Customer Name:")

    if items:
        selected_items = st.multiselect("Select Items to Purchase", [item['name'] for item in items])

        purchased = [item for item in items if item['name'] in selected_items]
        quantities = {}
        total = 0

        for item in purchased:
            qty = st.number_input(f"Enter quantity for {item['name']} (₹{item['price']} each):", min_value=1, step=1, key=item['name'])
            item_total = item['price'] * qty
            total += item_total
            quantities[item['name']] = qty

        if st.button("📟 Generate Bill"):
            if not customer_name:
                st.warning("🚨 Please enter a customer name.")
            elif not purchased:
                st.warning("⚠️ Please select at least one item.")
            else:
                bill = {
                    "name": customer_name,
                    "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "items": [{"name": i['name'], "qty": quantities[i['name']], "price": i['price']} for i in purchased],
                    "total": total
                }
                bills.append(bill)
                save_bills(bills)
                st.success(f"✅ Bill generated successfully for {customer_name}!")

                st.subheader("📟 Bill Receipt")
                st.write(f"**Customer Name:** {bill['name']}")
                st.write(f"**Date:** {bill['date']}")
                for item in bill['items']:
                    st.write(f"- {item['name']} x {item['qty']} = ₹{item['price'] * item['qty']}")
                st.write(f"**Total: ₹{bill['total']}**")

    else:
        st.warning("⚠️ No items available to purchase.")

# Search Item
elif menu == "Search Item":
    st.header("🔍 Search Item")
    search_name = st.text_input("Enter item name to search:")
    found = False
    for item in items:
        if item['name'].lower() == search_name.lower():
            st.success("✅ Item Found:")
            st.json(item)
            found = True
            break
    if not found and search_name:
        st.error("❌ Item not found.")

# Edit Item
elif menu == "Edit Item":
    st.header("✏️ Edit Item")
    item_names = [item['name'] for item in items]
    if item_names:
        selected_item = st.selectbox("Select Item to Edit", item_names)

        for item in items:
            if item['name'] == selected_item:
                new_name = st.text_input("New Name", value=item['name'])
                new_category = st.selectbox("New Category", ["Fruits", "Vegetables", "Dairy", "Snacks", "Beverages", "Other"], index=["Fruits", "Vegetables", "Dairy", "Snacks", "Beverages", "Other"].index(item.get('category', 'Other')))
                new_quantity = st.selectbox("New Quantity", [
                    "1/2 kg", "1 kg", "2 kg", "5 kg", "10 kg",
                    "500 ml", "1 L", "2 L", "5 L"
                ], index=["1/2 kg", "1 kg", "2 kg", "5 kg", "10 kg", "500 ml", "1 L", "2 L", "5 L"].index(item.get('quantity', '1 kg')))
                new_price = st.number_input("New Price", value=int(item['price']), min_value=1)

                if st.button("Update Item"):
                    item['name'] = new_name
                    item['category'] = new_category
                    item['quantity'] = new_quantity
                    item['price'] = new_price
                    save_items(items)
                    st.success("✅ Item updated successfully!")
    else:
        st.warning("⚠️ No items available to edit.")

# View Bills
elif menu == "View Bills":
    st.header("📄 View All Customer Bills")
    if bills:
        for bill in bills[::-1]:  # Latest first
            with st.expander(f"{bill['name']} - ₹{bill['total']} on {bill['date']}"):
                for item in bill['items']:
                    st.write(f"- {item['name']} x {item['qty']} = ₹{item['price'] * item['qty']}")
                st.write(f"**Total Bill: ₹{bill['total']}**")
    else:
        st.info("No bills found.")
