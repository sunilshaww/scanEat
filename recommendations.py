"""
AI-Powered Meal Recommendation Engine
Provides personalized food recommendations
"""

import random

# Meal recommendations database
MEAL_RECOMMENDATIONS = {
    "Breakfast": {
        "healthy": ["idli", "dosa", "poha", "upma", "oats"],
        "protein_rich": ["paneer paratha", "egg bhurji", "moong dal chilla"],
        "light": ["fruit smoothie", "idli", "poha"],
        "weight_loss": ["oats with fruits", "sprouts salad", "vegetable poha"],
        "weight_gain": ["aloo paratha", "paneer sandwich", "banana shake"]
    },
    "Lunch": {
        "healthy": ["dal-roti", "rajma-rice", "vegetable pulao"],
        "protein_rich": ["chicken curry with roti", "paneer tikka"],
        "light": ["dal-roti", "vegetable khichdi"],
        "weight_loss": ["dal with roti", "brown rice with dal"],
        "weight_gain": ["chicken biryani", "paneer butter masala with naan"]
    },
    "Dinner": {
        "healthy": ["dal-roti", "palak paneer", "vegetable curry"],
        "protein_rich": ["grilled chicken", "paneer tikka", "dal tadka"],
        "light": ["vegetable soup", "khichdi", "dal-roti"],
        "weight_loss": ["vegetable soup", "dal with roti"],
        "weight_gain": ["chicken curry with rice", "paneer butter masala"]
    },
    "Late Night Snack": {
        "healthy": ["fruit", "nuts", "green tea"],
        "protein_rich": ["boiled eggs", "paneer cubes"],
        "light": ["green tea", "fruit"],
        "weight_loss": ["green tea", "cucumber slices"],
        "weight_gain": ["banana shake", "nuts"]
    }
}

def get_meal_recommendation(meal_time, current_food, user_goal, nutrition_data):
    """
    Generate personalized meal recommendations
    """
    recommendations = {
        "message": "",
        "alternatives": [],
        "tips": []
    }

    # Get nutrition values
    calories = nutrition_data.get('calories', 0)
    protein = nutrition_data.get('protein', 0)
    carbs = nutrition_data.get('carbs', 0)
    fat = nutrition_data.get('fat', 0)

    # Goal mapping
    goal_mapping = {
        "Lose Weight": "weight_loss",
        "Gain Weight": "weight_gain",
        "Maintain Weight": "healthy"
    }

    goal_key = goal_mapping.get(user_goal, "healthy")

    # Generate message based on analysis
    if user_goal == "Lose Weight":
        if calories > 400:
            recommendations["message"] = f"⚠️ This meal is quite calorie-dense ({calories} kcal). For weight loss, consider lighter alternatives."
            if meal_time in MEAL_RECOMMENDATIONS:
                recommendations["alternatives"] = random.sample(
                    MEAL_RECOMMENDATIONS[meal_time].get("weight_loss", []), 
                    min(3, len(MEAL_RECOMMENDATIONS[meal_time].get("weight_loss", [])))
                )
            recommendations["tips"] = [
                "Aim for 300-400 calories per meal for weight loss",
                "Include more vegetables and lean proteins",
                "Avoid fried and heavy foods"
            ]
        else:
            recommendations["message"] = f"✅ Good choice! At {calories} kcal, this aligns well with your weight loss goal."
            recommendations["tips"] = [
                "Maintain portion control for best results",
                "Stay hydrated throughout the day"
            ]

    elif user_goal == "Gain Weight":
        if calories < 400:
            recommendations["message"] = f"💪 This meal has {calories} kcal. Consider adding calorie-dense foods to reach your weight gain goal."
            if meal_time in MEAL_RECOMMENDATIONS:
                recommendations["alternatives"] = random.sample(
                    MEAL_RECOMMENDATIONS[meal_time].get("weight_gain", []), 
                    min(3, len(MEAL_RECOMMENDATIONS[meal_time].get("weight_gain", [])))
                )
            recommendations["tips"] = [
                "Aim for 500-600 calories per meal for weight gain",
                "Include healthy fats and proteins"
            ]
        else:
            recommendations["message"] = f"✅ Excellent! At {calories} kcal with {protein}g protein, this supports your weight gain goal."
            recommendations["tips"] = [
                "Great choice for building muscle mass",
                "Stay consistent with your meal plan"
            ]

    else:  # Maintain Weight
        if 250 <= calories <= 450:
            recommendations["message"] = f"✅ Perfect balance! This {calories} kcal meal is ideal for maintaining your weight."
            recommendations["tips"] = [
                "Well-balanced meal for your goals",
                "Stay active and hydrated"
            ]
        else:
            recommendations["message"] = f"ℹ️ This meal has {calories} kcal. For weight maintenance, aim for balanced meals."
            if meal_time in MEAL_RECOMMENDATIONS:
                recommendations["alternatives"] = random.sample(
                    MEAL_RECOMMENDATIONS[meal_time].get("healthy", []), 
                    min(3, len(MEAL_RECOMMENDATIONS[meal_time].get("healthy", [])))
                )

    # Add nutrition-specific tips
    if protein > 25:
        recommendations["tips"].append("🥩 High protein content - great for muscle building!")

    if carbs > 50:
        recommendations["tips"].append("🍚 High in carbs - provides quick energy")

    # Ensure we have at least some tips
    if not recommendations["tips"]:
        recommendations["tips"] = [
            "Balance your meals throughout the day",
            "Stay hydrated with 8-10 glasses of water"
        ]

    return recommendations
