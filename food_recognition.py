"""
Advanced Food Recognition Module
Uses multiple methods for accurate food detection
"""
from PIL import Image
import numpy as np
import io

# Comprehensive Indian food database
INDIAN_FOOD_DATABASE = {
    "rice": {
        "keywords": ["white", "plain", "basmati", "steamed"],
        "color_profile": [220, 220, 210],
        "common_names": ["rice", "chawal", "white rice", "steamed rice"]
    },
    "dal tadka": {
        "keywords": ["yellow", "lentil", "dal"],
        "color_profile": [200, 180, 100],
        "common_names": ["dal", "dal tadka", "dal fry", "yellow dal"]
    },
    "roti": {
        "keywords": ["round", "flatbread", "wheat"],
        "color_profile": [180, 160, 120],
        "common_names": ["roti", "chapati", "phulka"]
    },
    "paneer butter masala": {
        "keywords": ["red", "gravy", "creamy", "paneer"],
        "color_profile": [220, 120, 80],
        "common_names": ["paneer butter masala", "paneer makhani"]
    },
    "chicken curry": {
        "keywords": ["red", "brown", "gravy", "chicken"],
        "color_profile": [180, 100, 70],
        "common_names": ["chicken curry", "murgh curry", "chicken masala"]
    },
    "biryani": {
        "keywords": ["rice", "mixed", "yellow", "layered"],
        "color_profile": [200, 170, 100],
        "common_names": ["biryani", "chicken biryani", "veg biryani"]
    },
    "dosa": {
        "keywords": ["crispy", "golden", "flat", "round"],
        "color_profile": [200, 180, 140],
        "common_names": ["dosa", "masala dosa", "plain dosa"]
    },
    "idli": {
        "keywords": ["white", "round", "steamed"],
        "color_profile": [240, 240, 235],
        "common_names": ["idli", "steamed idli"]
    },
    "samosa": {
        "keywords": ["triangular", "fried", "golden"],
        "color_profile": [200, 150, 80],
        "common_names": ["samosa", "punjabi samosa"]
    },
    "chole": {
        "keywords": ["chickpeas", "brown", "gravy"],
        "color_profile": [150, 100, 60],
        "common_names": ["chole", "chana masala", "chole bhature"]
    },
    "rajma": {
        "keywords": ["kidney beans", "red", "gravy"],
        "color_profile": [140, 70, 60],
        "common_names": ["rajma", "rajma chawal"]
    },
    "palak paneer": {
        "keywords": ["green", "spinach", "paneer"],
        "color_profile": [80, 140, 80],
        "common_names": ["palak paneer", "saag paneer"]
    },
}

def validate_food_image(image):
    """
    Validate if the image actually contains food
    Returns: (is_food: bool, confidence: float)
    """
    try:
        img_array = np.array(image.resize((224, 224)))

        # Check if image is too uniform
        std_dev = img_array.std()
        if std_dev < 15:
            return False, 0.2

        # Check color distribution
        avg_color = img_array.mean(axis=(0, 1))
        color_variance = np.std(avg_color)

        if color_variance < 5:
            return False, 0.3

        # Check brightness
        brightness = avg_color.mean()
        if brightness < 20 or brightness > 250:
            return True, 0.5

        # Calculate edge density
        gray = np.mean(img_array, axis=2)
        edges = np.abs(gray[1:] - gray[:-1]).mean()

        if edges < 5:
            return False, 0.4

        confidence = min(0.95, 0.6 + (edges / 50) + (std_dev / 100))
        return True, confidence

    except Exception as e:
        print(f"Validation error: {e}")
        return True, 0.5

def analyze_image_features(image):
    """
    Detailed image analysis for better food recognition
    """
    img_array = np.array(image.resize((224, 224)))

    # Color analysis
    avg_color = img_array.mean(axis=(0, 1))
    red, green, blue = avg_color[0], avg_color[1], avg_color[2]

    # Brightness and saturation
    brightness = avg_color.mean()
    saturation = np.std(img_array)

    # Dominant color detection
    red_dominant = red > green + 20 and red > blue + 20
    green_dominant = green > red + 20 and green > blue + 20
    yellow_dominant = red > 150 and green > 150 and blue < 120
    brown_dominant = 80 < red < 150 and 60 < green < 120 and blue < 100
    white_dominant = brightness > 200 and saturation < 30

    # Texture analysis
    gray = np.mean(img_array, axis=2)
    edges_horizontal = np.abs(gray[:, 1:] - gray[:, :-1]).mean()
    edges_vertical = np.abs(gray[1:, :] - gray[:-1, :]).mean()
    texture_score = (edges_horizontal + edges_vertical) / 2

    return {
        'avg_color': avg_color,
        'brightness': brightness,
        'saturation': saturation,
        'red_dominant': red_dominant,
        'green_dominant': green_dominant,
        'yellow_dominant': yellow_dominant,
        'brown_dominant': brown_dominant,
        'white_dominant': white_dominant,
        'texture_score': texture_score
    }

def match_food_by_features(features):
    """
    Match food based on visual features with confidence scoring
    """
    candidates = []

    # Green foods
    if features['green_dominant']:
        candidates.append(('palak paneer', 0.85))
        candidates.append(('green salad', 0.75))

    # Red/orange foods
    if features['red_dominant']:
        if features['texture_score'] > 20:
            candidates.append(('paneer butter masala', 0.80))
            candidates.append(('chicken curry', 0.75))
        else:
            candidates.append(('tomato soup', 0.70))

    # Yellow foods
    if features['yellow_dominant']:
        if features['brightness'] > 180:
            candidates.append(('dal tadka', 0.85))
            candidates.append(('biryani', 0.75))
        else:
            candidates.append(('curry', 0.65))

    # Brown foods
    if features['brown_dominant']:
        if features['texture_score'] > 25:
            candidates.append(('samosa', 0.80))
            candidates.append(('pakora', 0.75))
        else:
            candidates.append(('chole', 0.75))
            candidates.append(('rajma', 0.70))

    # White foods
    if features['white_dominant']:
        if features['texture_score'] < 15:
            candidates.append(('idli', 0.85))
            candidates.append(('rice', 0.80))
        else:
            candidates.append(('dosa', 0.75))
            candidates.append(('roti', 0.70))

    # If no strong match
    if not candidates:
        if features['brightness'] > 150:
            candidates.append(('rice', 0.60))
        else:
            candidates.append(('mixed curry', 0.55))

    candidates.sort(key=lambda x: x[1], reverse=True)
    return candidates[0] if candidates else ('unknown food', 0.3)

def recognize_food_advanced(image):
    """
    Advanced food recognition with confidence scoring
    """
    features = analyze_image_features(image)
    food_name, confidence = match_food_by_features(features)

    all_matches = []
    for food_key, food_data in INDIAN_FOOD_DATABASE.items():
        color_diff = np.abs(np.array(food_data['color_profile']) - features['avg_color']).mean()
        similarity = max(0, 1 - (color_diff / 255))

        if similarity > 0.5:
            all_matches.append((food_key, similarity * 0.9))

    all_matches.sort(key=lambda x: x[1], reverse=True)
    alternatives = [m[0] for m in all_matches[1:4]]

    return {
        'name': food_name,
        'confidence': confidence,
        'alternatives': alternatives
    }
