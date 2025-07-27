# 🛒 Grocery Store Management System

A simple, interactive web-based inventory and billing system for a grocery store, built using **Streamlit**. This application helps manage items, generate customer bills, and maintain transaction history with a user-friendly interface.

---

## 🚀 Features

- **View Items:** Display all available items in the store with details like category, quantity, and price.
- **Add Item:** Add new items to the inventory by specifying name, category, quantity, and price.
- **Purchase Items (Billing):** Select items to purchase, specify quantity, generate and display a detailed bill.
- **Search Item:** Search for an item by name and display its details.
- **Edit Item:** Modify item details including name, quantity, category, and price.
- **View Bills:** View all generated customer bills in reverse chronological order.

---

## 📂 Project Structure

📁 Grocery-Store-Management
│
├── grocery_store.py # Main Streamlit app file
├── items_data.json # JSON file for storing items
├── bills_data.json # JSON file for storing customer bills
└── README.md 


--

## 🧑‍💻 Installation

1. **Clone the repository**

```bash
git clone https://github.com/your-username/Grocery-Store-Management.git
cd Grocery-Store-Management
```

2. Install dependencies

   pip install streamlit

3. Run the application

   streamlit run grocery_store.py


4. screenshot

<img width="1882" height="917" alt="image" src="https://github.com/user-attachments/assets/df461c9a-d900-42f8-bf50-bb0963de64a5" />


5. 🧠 Tech Stack
   
Python 3
Streamlit - Web framework
JSON - For storing data persistently


6. Data Files

items_data.json: Contains the list of items available in the store.
bills_data.json: Stores billing records with customer names, dates, item details, and totals.

✅ These files are created automatically if they don’t exist.
