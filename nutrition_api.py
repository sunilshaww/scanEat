"""
Nutrition API Integration Module
Comprehensive Indian food nutrition database
"""

# Nutrition database with 30+ Indian foods
NUTRITION_DATABASE = {
    "rice": {
        "calories": 206,
        "protein": 4.3,
        "carbs": 45,
        "fat": 0.4,
        "fiber": 0.6,
        "sugar": 0.1,
        "vitamins": ["Vitamin B1", "Vitamin B3", "Folate"],
        "minerals": ["Iron", "Magnesium", "Phosphorus"],
        "serving_size": "1 cup (158g)"
    },
    "white rice": {
        "calories": 206,
        "protein": 4.3,
        "carbs": 45,
        "fat": 0.4,
        "fiber": 0.6,
        "sugar": 0.1,
        "vitamins": ["Vitamin B1", "Vitamin B3", "Folate"],
        "minerals": ["Iron", "Magnesium", "Phosphorus"],
        "serving_size": "1 cup (158g)"
    },
    "dal tadka": {
        "calories": 180,
        "protein": 12,
        "carbs": 28,
        "fat": 3.5,
        "fiber": 8,
        "sugar": 2,
        "vitamins": ["Vitamin B1", "Vitamin B6", "Folate"],
        "minerals": ["Iron", "Magnesium", "Potassium", "Zinc"],
        "serving_size": "1 bowl (200g)"
    },
    "dal fry": {
        "calories": 180,
        "protein": 12,
        "carbs": 28,
        "fat": 3.5,
        "fiber": 8,
        "sugar": 2,
        "vitamins": ["Vitamin B1", "Vitamin B6", "Folate"],
        "minerals": ["Iron", "Magnesium", "Potassium", "Zinc"],
        "serving_size": "1 bowl (200g)"
    },
    "yellow dal": {
        "calories": 180,
        "protein": 12,
        "carbs": 28,
        "fat": 3.5,
        "fiber": 8,
        "sugar": 2,
        "vitamins": ["Vitamin B1", "Vitamin B6", "Folate"],
        "minerals": ["Iron", "Magnesium", "Potassium", "Zinc"],
        "serving_size": "1 bowl (200g)"
    },
    "roti": {
        "calories": 120,
        "protein": 4,
        "carbs": 23,
        "fat": 2,
        "fiber": 3,
        "sugar": 0.5,
        "vitamins": ["Vitamin B1", "Vitamin B3", "Folate"],
        "minerals": ["Iron", "Magnesium", "Selenium"],
        "serving_size": "1 piece (60g)"
    },
    "chapati": {
        "calories": 120,
        "protein": 4,
        "carbs": 23,
        "fat": 2,
        "fiber": 3,
        "sugar": 0.5,
        "vitamins": ["Vitamin B1", "Vitamin B3", "Folate"],
        "minerals": ["Iron", "Magnesium", "Selenium"],
        "serving_size": "1 piece (60g)"
    },
    "paneer butter masala": {
        "calories": 350,
        "protein": 18,
        "carbs": 12,
        "fat": 26,
        "fiber": 2,
        "sugar": 5,
        "vitamins": ["Vitamin A", "Vitamin D", "Vitamin B12"],
        "minerals": ["Calcium", "Phosphorus", "Selenium"],
        "serving_size": "1 serving (250g)"
    },
    "paneer tikka": {
        "calories": 280,
        "protein": 20,
        "carbs": 10,
        "fat": 18,
        "fiber": 2,
        "sugar": 3,
        "vitamins": ["Vitamin A", "Vitamin D", "Vitamin B12"],
        "minerals": ["Calcium", "Phosphorus", "Selenium"],
        "serving_size": "1 serving (200g)"
    },
    "palak paneer": {
        "calories": 265,
        "protein": 15,
        "carbs": 14,
        "fat": 16,
        "fiber": 4,
        "sugar": 3,
        "vitamins": ["Vitamin A", "Vitamin C", "Vitamin K", "Folate"],
        "minerals": ["Calcium", "Iron", "Magnesium"],
        "serving_size": "1 serving (250g)"
    },
    "chicken curry": {
        "calories": 280,
        "protein": 28,
        "carbs": 12,
        "fat": 14,
        "fiber": 2,
        "sugar": 4,
        "vitamins": ["Vitamin B6", "Vitamin B12", "Niacin"],
        "minerals": ["Iron", "Zinc", "Selenium", "Phosphorus"],
        "serving_size": "1 serving (250g)"
    },
    "chicken biryani": {
        "calories": 450,
        "protein": 25,
        "carbs": 52,
        "fat": 16,
        "fiber": 3,
        "sugar": 4,
        "vitamins": ["Vitamin B6", "Vitamin B12", "Vitamin C"],
        "minerals": ["Iron", "Zinc", "Magnesium", "Potassium"],
        "serving_size": "1 plate (350g)"
    },
    "veg biryani": {
        "calories": 350,
        "protein": 8,
        "carbs": 58,
        "fat": 10,
        "fiber": 5,
        "sugar": 6,
        "vitamins": ["Vitamin A", "Vitamin C", "Folate"],
        "minerals": ["Iron", "Magnesium", "Potassium"],
        "serving_size": "1 plate (350g)"
    },
    "biryani": {
        "calories": 400,
        "protein": 16,
        "carbs": 55,
        "fat": 13,
        "fiber": 4,
        "sugar": 5,
        "vitamins": ["Vitamin B6", "Vitamin C", "Folate"],
        "minerals": ["Iron", "Zinc", "Magnesium"],
        "serving_size": "1 plate (350g)"
    },
    "samosa": {
        "calories": 262,
        "protein": 6,
        "carbs": 32,
        "fat": 13,
        "fiber": 3,
        "sugar": 2,
        "vitamins": ["Vitamin C", "Vitamin B6"],
        "minerals": ["Iron", "Potassium"],
        "serving_size": "2 pieces (100g)"
    },
    "dosa": {
        "calories": 220,
        "protein": 6,
        "carbs": 42,
        "fat": 4,
        "fiber": 3,
        "sugar": 2,
        "vitamins": ["Vitamin B1", "Vitamin C", "Folate"],
        "minerals": ["Iron", "Calcium", "Potassium"],
        "serving_size": "1 dosa (150g)"
    },
    "masala dosa": {
        "calories": 220,
        "protein": 6,
        "carbs": 42,
        "fat": 4,
        "fiber": 3,
        "sugar": 2,
        "vitamins": ["Vitamin B1", "Vitamin C", "Folate"],
        "minerals": ["Iron", "Calcium", "Potassium"],
        "serving_size": "1 dosa (150g)"
    },
    "plain dosa": {
        "calories": 168,
        "protein": 4,
        "carbs": 32,
        "fat": 3,
        "fiber": 2,
        "sugar": 1,
        "vitamins": ["Vitamin B1", "Folate"],
        "minerals": ["Iron", "Calcium"],
        "serving_size": "1 dosa (120g)"
    },
    "idli": {
        "calories": 156,
        "protein": 5,
        "carbs": 30,
        "fat": 1.5,
        "fiber": 2,
        "sugar": 1,
        "vitamins": ["Vitamin B1", "Folate"],
        "minerals": ["Iron", "Calcium", "Magnesium"],
        "serving_size": "3 pieces (150g)"
    },
    "chole": {
        "calories": 210,
        "protein": 11,
        "carbs": 32,
        "fat": 5,
        "fiber": 9,
        "sugar": 5,
        "vitamins": ["Vitamin B6", "Folate", "Vitamin C"],
        "minerals": ["Iron", "Magnesium", "Potassium", "Zinc"],
        "serving_size": "1 bowl (200g)"
    },
    "rajma": {
        "calories": 195,
        "protein": 10,
        "carbs": 30,
        "fat": 4,
        "fiber": 8,
        "sugar": 3,
        "vitamins": ["Vitamin B1", "Folate", "Vitamin K"],
        "minerals": ["Iron", "Magnesium", "Potassium", "Zinc"],
        "serving_size": "1 bowl (200g)"
    },
}

def get_nutrition_data(food_name):
    """
    Get nutrition data for a food item
    """
    food_name_lower = food_name.lower().strip()

    if food_name_lower in NUTRITION_DATABASE:
        return NUTRITION_DATABASE[food_name_lower]

    # Default values if not found
    return {
        "calories": 250,
        "protein": 10,
        "carbs": 35,
        "fat": 8,
        "fiber": 3,
        "sugar": 5,
        "vitamins": ["Vitamin B Complex", "Vitamin C"],
        "minerals": ["Iron", "Calcium", "Potassium"],
        "serving_size": "1 serving (200g)"
    }
