import streamlit as st
from PIL import Image
import requests
import json
from datetime import datetime
import io
import base64
import numpy as np

# Page config
st.set_page_config(
    page_title="FoodScan - AI Nutrition Scanner",
    page_icon="🍽️",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        color: #FF6B6B;
        margin-bottom: 2rem;
    }
    .sub-header {
        font-size: 1.5rem;
        text-align: center;
        color: #4ECDC4;
        margin-bottom: 3rem;
    }
    .nutrition-card {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
    }
    .recommendation-card {
        background-color: #e8f4f8;
        padding: 15px;
        border-radius: 8px;
        margin: 10px 0;
    }
    .stCamera {
        border-radius: 10px;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="main-header">🍽️ FoodScan AI</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Scan Any Food & Know Your Nutrition Instantly</div>', unsafe_allow_html=True)

# Sidebar for user preferences
with st.sidebar:
    st.header("⚙️ Your Profile")
    user_weight = st.number_input("Current Weight (kg)", min_value=30.0, max_value=200.0, value=70.0)
    user_goal = st.selectbox("Goal", ["Maintain Weight", "Lose Weight", "Gain Weight"])
    activity_level = st.selectbox("Activity Level", ["Sedentary", "Moderate", "Active"])

    st.divider()
    st.header("🕐 Current Time")
    current_hour = datetime.now().hour
    if 5 <= current_hour < 12:
        meal_time = "Breakfast"
        meal_emoji = "🌅"
    elif 12 <= current_hour < 17:
        meal_time = "Lunch"
        meal_emoji = "☀️"
    elif 17 <= current_hour < 21:
        meal_time = "Dinner"
        meal_emoji = "🌙"
    else:
        meal_time = "Late Night Snack"
        meal_emoji = "⭐"

    st.markdown(f"### {meal_emoji} {meal_time} Time")

    st.divider()
    st.header("ℹ️ About")
    st.info("This app uses advanced AI to identify food and provide accurate nutritional information.")

# Main content area
col1, col2 = st.columns([1, 1])

with col1:
    st.header("📸 Capture or Upload Food")

    # Camera or upload option
    upload_method = st.radio("Choose input method:", ["📁 Upload Image", "📷 Take Live Photo"], horizontal=True)

    uploaded_file = None

    if upload_method == "📷 Take Live Photo":
        st.info("👇 Click 'Take Photo' to capture your food using camera")
        camera_photo = st.camera_input("Take a picture of your food")
        if camera_photo is not None:
            uploaded_file = camera_photo
    else:
        st.info("👇 Upload an image of your food (JPG, PNG)")
        uploaded_file = st.file_uploader("Choose a food image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Load and validate image
        try:
            image = Image.open(uploaded_file)

            # Display image
            st.image(image, caption="Your Food", use_container_width=True)

            # Image validation
            img_array = np.array(image)

            # Check if image is too dark or too bright
            brightness = img_array.mean()

            if brightness < 20:
                st.warning("⚠️ Image is too dark. Try taking photo in better lighting.")
            elif brightness > 250:
                st.warning("⚠️ Image is too bright. Adjust lighting for better results.")

            # Analyze button
            if st.button("🔍 Analyze Food", type="primary", use_container_width=True):
                with st.spinner("🤖 AI is analyzing your food..."):
                    # Import modules
                    from food_recognition import recognize_food_advanced, validate_food_image
                    from nutrition_api import get_nutrition_data
                    from recommendations import get_meal_recommendation

                    # Validate if image contains food
                    is_food, confidence = validate_food_image(image)

                    if not is_food:
                        st.error("❌ This doesn't appear to be a food image. Please upload a photo of actual food.")
                        st.stop()

                    # Get food recognition result
                    food_result = recognize_food_advanced(image)
                    food_name = food_result['name']
                    detection_confidence = food_result['confidence']

                    # Show confidence
                    if detection_confidence < 0.6:
                        st.warning(f"⚠️ Low confidence detection ({detection_confidence*100:.1f}%). Results may not be accurate.")

                    # Get nutrition data
                    nutrition_data = get_nutrition_data(food_name)

                    # Store in session state
                    st.session_state['food_name'] = food_name
                    st.session_state['nutrition_data'] = nutrition_data
                    st.session_state['confidence'] = detection_confidence
                    st.session_state['analyzed'] = True
                    st.rerun()

        except Exception as e:
            st.error(f"❌ Error processing image: {str(e)}")
            st.info("Please upload a valid image file.")

with col2:
    st.header("📊 Nutrition Analysis")

    if 'analyzed' in st.session_state and st.session_state['analyzed']:
        food_name = st.session_state['food_name']
        nutrition_data = st.session_state['nutrition_data']
        confidence = st.session_state.get('confidence', 0.8)

        # Display detected food with confidence
        conf_emoji = "✅" if confidence > 0.7 else "⚠️"
        st.success(f"{conf_emoji} Detected: **{food_name.title()}** (Confidence: {confidence*100:.1f}%)")

        # Display nutrition information
        st.markdown("### Nutritional Information")
        st.caption(f"Serving size: {nutrition_data.get('serving_size', 'N/A')}")

        col_a, col_b, col_c = st.columns(3)
        with col_a:
            st.metric("Calories", f"{nutrition_data['calories']} kcal")
        with col_b:
            st.metric("Protein", f"{nutrition_data['protein']} g")
        with col_c:
            st.metric("Carbs", f"{nutrition_data['carbs']} g")

        col_d, col_e, col_f = st.columns(3)
        with col_d:
            st.metric("Fat", f"{nutrition_data['fat']} g")
        with col_e:
            st.metric("Fiber", f"{nutrition_data['fiber']} g")
        with col_f:
            st.metric("Sugar", f"{nutrition_data['sugar']} g")

        # Weight gain/loss estimate
        st.markdown("### ⚖️ Weight Impact")
        calories = nutrition_data['calories']
        # 7700 kcal = 1 kg weight change
        weight_change = calories / 7700

        if user_goal == "Lose Weight":
            calorie_target = 1800
            if calories > calorie_target * 0.3:
                st.warning(f"⚠️ This meal has {calories} kcal. Consider a lighter option for weight loss.")
            else:
                st.success(f"✅ Good choice! This aligns with your weight loss goal.")
        elif user_goal == "Gain Weight":
            st.info(f"📈 Eating this will provide {weight_change:.4f} kg worth of calories.")
        else:
            st.info(f"This meal contains {calories} kcal, contributing {weight_change:.4f} kg to weight if fully stored.")

        # Vitamins and minerals
        st.markdown("### 💊 Vitamins & Minerals")
        vitamins_col1, vitamins_col2 = st.columns(2)

        with vitamins_col1:
            st.write("**Vitamins:**")
            for vitamin in nutrition_data['vitamins']:
                st.write(f"✓ {vitamin}")

        with vitamins_col2:
            st.write("**Minerals:**")
            for mineral in nutrition_data['minerals']:
                st.write(f"✓ {mineral}")

        # AI Recommendations
        st.markdown("---")
        st.markdown("### 🤖 AI Recommendations")

        from recommendations import get_meal_recommendation
        recommendations = get_meal_recommendation(
            meal_time=meal_time,
            current_food=food_name,
            user_goal=user_goal,
            nutrition_data=nutrition_data
        )

        st.markdown(f"**For {meal_time}:**")
        st.info(recommendations['message'])

        if recommendations['alternatives']:
            st.markdown("**Healthier Alternatives:**")
            for alt in recommendations['alternatives']:
                st.markdown(f"• {alt}")

        if recommendations['tips']:
            st.markdown("**Tips:**")
            for tip in recommendations['tips']:
                st.markdown(f"💡 {tip}")

        # Reset button
        if st.button("🔄 Analyze Another Food", use_container_width=True):
            st.session_state['analyzed'] = False
            st.rerun()

    else:
        st.info("👆 Upload or capture a food image and click 'Analyze Food' to see nutrition details")

        # Show example
        with st.expander("💡 Tips for best results"):
            st.markdown("""
            - **Good lighting**: Take photos in well-lit conditions
            - **Clear focus**: Make sure the food is in focus
            - **Close-up**: Get closer to the food for better detection
            - **Single item**: Works best with one food item at a time
            - **Avoid filters**: Use natural photos without filters
            - **Common foods**: Works best with popular Indian dishes
            """)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666;'>
    <p>🚀 Powered by Advanced AI | Built for Health-Conscious Indians</p>
    <p>💪 Track your nutrition, achieve your goals</p>
    <p style='font-size: 0.8em;'>⚠️ Note: This is an AI-powered tool. For medical advice, consult a healthcare professional.</p>
</div>
""", unsafe_allow_html=True)
