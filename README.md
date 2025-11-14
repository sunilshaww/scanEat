ScanEat - AI-Powered Food Nutrition Scanner
Description
ScanEat is a mobile-friendly AI-powered app that allows users in India and beyond to instantly scan any food item by uploading a photo or taking a live picture. The app analyzes the food image to provide detailed nutritional information including calories, protein, carbohydrates, fats, fiber, vitamins, and minerals.

Additionally, the app offers personalized meal recommendations tailored to the user's health goals such as weight loss, weight gain, or maintenance. The suggestions adapt based on the time of day and nutritional content, helping users make informed and healthy eating decisions effortlessly.

Features Implemented
Food image recognition using advanced AI feature-based detection

Support for live camera photo capture and image upload

Validation of images to detect if actual food is present

Detailed nutrition information from a comprehensive database of 30+ common Indian foods

Weight impact estimation based on calories consumed

Personalized AI-powered meal recommendations based on user goals (lose/gain/maintain weight)

Time-aware suggestions for breakfast, lunch, dinner, and snacks

Beautiful and responsive user interface powered by Streamlit

Full backend integrated with modular code for easy updates and API extension

Easy deployment via GitHub and Streamlit Cloud for live public access

What You Have Done So Far
Designed and built the core AI-powered food scanner prototype

Created food recognition module analyzing food image features for accurate detection

Integrated Indian-specific nutrition database with detailed macro and micronutrients

Developed an AI recommendation engine for personalized meal planning

Added live camera support and image quality validation in the user interface

Fixed all known bugs and deployment errors (including version conflicts)

Deployed the app for local testing with smooth user experience

How to Run Locally
Download all 5 main files: app.py, food_recognition.py, nutrition_api.py, recommendations.py, requirements.txt

Put all files in the same folder, e.g. C:\Users\HP\scanEat\

Open terminal/command prompt and navigate there:

text
cd C:\Users\HP\scanEat
Install dependencies:

text
pip install -r requirements.txt
Run the app:

text
streamlit run app.py
Open browser at http://localhost:8501 and use ScanEat!

Deployment Instructions
For live deployment, push your code to GitHub (username: sunilshaww, repo name: scanEat) and deploy via Streamlit Cloud.

See full deployment instructions in the DEPLOYMENT_GUIDE.md.

Future Improvements
Integrate external AI APIs like Clarifai or Google Vision for improved food detection accuracy

Expand nutrition database with more Indian regional foods and international items

Add user authentication, meal history logging, and progress tracking

Include barcode scanning for packaged foods

Implement social sharing and community features

Contact
For support, feedback or collaboration, please contact sunilshaww via GitHub or LinkedIn- sunil shaw
