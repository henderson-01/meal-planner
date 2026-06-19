# 🛒 Budget Bytes 2026

**A smart Meal planner with estimated costs for the UK market.**

The Project. Budget Bytes 2026 is a desktop application built with Python and `CustomTkinter` and `Pillow`. While many apps calculate "cost per serving," this app focuses on **Total Basket Cost**. It tells you how much cash you need at the supermarket checkout to buy the full packs of ingredients required to start a meal.

---

## ✨ Key Features

- 🇬🇧 **Estimated UK Pricing:** Data updated for **April 2026** market trends (reflecting current costs for staples, oils, and proteins).
- 💰 **Budget Filtering:** Enter your available cash, and the app instantly suggests meals you can afford to buy "from scratch" right now.
- 🛒 **Ingredient Breakdown:** See a transparent list of every item in your shopping basket and its individual price.
- 🏬 **Multi-Shop Data:** Prices sourced dynamically from major UK retailers including **ALDI, Lidl, Tesco, ASDA, Morrisons, and Sainsbury's**.
- ⚙️ **Customizable Database:** Meal data is stored in a separate `meals.json` file, allowing you to easily add, edit, or remove recipes without touching the core Python code.
- 🖥️ **Modern UI:** Sleek, dark-mode interface built for a clean and scannable experience.
- 🖼️ **Logo Package** Includes `logo.png` with background removed to fit in nicely with the existing sleek dark mode interface.

---

## 📸 How It Works

- **Enter your budget** (e.g., £10.00) in the sidebar.
- **Click "Find Meals"** to see a curated list of recipes.
- **Browse the cards** to see the shopping list, full cost breakdown, and simple cooking instructions.

---

## 🌇 Screenshots Of The App

![Meal Planner Screenshot 1](Images/Screenshot%201.png)
![Meal Planner Screenshot 2](Images/Screenshot%202.png)

---

## 🛠️ Technical Setup (Linux / Desktop)

On Linux, it is best practice to use a **Virtual Environment** to avoid "externally managed environment" errors and keep your system Python clean.

**Open your terminal** in the project folder path or **Right click** the project folder and **open in terminal.** Ensure have `meal_planner.py` and `meals.json` and `logo.png` are in the same folder before starting.

- **Create the virtual environment**:

    ```bash
    python3 -m venv .venv
    ```

- **Activate the environment**:

    ```bash
    source .venv/bin/activate
    ```

- **Install Dependencies**:

    ```bash
    pip install customtkinter
    pip install Pillow
    ```

> [!NOTE]
> **Linux Dependency:** If you see a `ModuleNotFoundError: No module named 'tkinter'`, run the command below in your **main terminal** (not inside the venv):

```bash
sudo apt install python3-tk
```

- **Then Run the application in the `.venv`**:

    ```bash
    source .venv/bin/activate
    python3 meal_planner.py
    ```

---

## 📊 Data Philosophy: "The Basket Reality"

Most budget apps claim a meal costs **£0.50 per serving**, but they ignore the fact that you cannot buy a single teaspoon of turmeric or two individual chicken thighs.

**Budget Bytes 2026** solves this by showing the **Full Pack Cost**. If a recipe requires Olive Oil, the app accounts for the **£6.00** bottle price, ensuring your budget reflects what you actually spend at the till.

---

## 📝 Learning Journey

This project was developed to practice key software development concepts:

- **GUI Development:** Implementing modern layouts and scrollable frames with `CustomTkinter`.
- **Separation of Concerns:** Decoupling application logic from raw data by utilizing external `JSON` files for the database.
- **Data Management:** Handling and filtering nested Lists of Dictionaries.
- **UX/UI Design:** Using color theory (dull whites vs. vibrant accents) to improve scannability.

---

## ⚠️ Disclaimer

**Budget Bytes 2026** is an educational project designed to assist with meal planning and budgeting.

- **Price Accuracy:** All prices reflect estimated UK supermarket costs as of **April 2026**. Prices in the real world fluctuate daily based on location, store size (e.g., "Local" vs. "Superstore"), and ongoing inflation.
- **Affiliation:** This project is not affiliated with, sponsored by, or endorsed by ALDI, Lidl, Tesco, ASDA, Morrisons, or Sainsbury's. All trademarks belong to their respective owners.
- **Nutritional Advice:** Recipes are provided for convenience; please check individual product labels for allergens and nutritional information.

> [!CAUTION]
> This is provided "as is" without warranty of any kind. I am not responsible for any damage, data loss, or issues caused by the use of this Program. **Use it at your own risk.**
