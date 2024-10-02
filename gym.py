import streamlit as st
from PIL import Image
from textwrap import fill
import pandas as pd
import pickle
import base64
import os

# Set page configuration at the very top

st.set_page_config(page_title="Personalized Diet and Exercise", layout="centered")

# Function to encode image
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

def add_bg_from_local(image_path):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/jpeg;base64,{image_path});
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Path to background image
image_path = r"C:\Users\mahes\OneDrive\Pictures\baf.avif"

# Add background to Streamlit app
bg_image = get_base64_image(image_path)
add_bg_from_local(bg_image)
# Example usage

# Path to background image


# Initialize session state for navigation
if 'page' not in st.session_state:
    st.session_state['page'] = 'home'

# Function to navigate to different pages
def go_to_page(page_name):
    st.session_state['page'] = page_name

# Home Page
if st.session_state['page'] == 'home':
    # Load the first image
    image1 = Image.open(r"C:\Users\mahes\OneDrive\Pictures\yoga.webp")  # Replace with the correct path

    # Center the title
    st.markdown("<h1 style='text-align: center;'>Hello And Welcome</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center;'>We help with your diet plan</h2>", unsafe_allow_html=True)

    # Display the first image
    st.image(image1, caption='Get Fit and Stay Healthy', use_column_width=True)

    # Section: About Us
    st.markdown("<h3 style='text-align: center;'>About Us</h3>", unsafe_allow_html=True)

    # Load and display another image (optional)
    image2 = Image.open(r"C:\Users\mahes\OneDrive\Pictures\a.jpg")  # Replace with the correct path
    st.image(image2, caption='Our Team', use_column_width=True)

    # Write some content
    st.write("""
    We are a team of dedicated professionals committed to helping individuals achieve their health and wellness goals. 
    With personalized nutrition and fitness plans tailored to each person's unique needs, 
    we aim to empower you to live your healthiest and happiest life.
    """)

    # Section: Why Personalized Diet and Exercise
    st.markdown("<h3 style='text-align: center;'>Why Personalized Diet and Exercise?</h3>", unsafe_allow_html=True)

    # Create a grid with 2 rows and 2 columns
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("✅ **Tailored for You**")
        st.write("Each plan is customized to fit your unique needs, goals, and preferences.")

    with col2:
        st.markdown("💪 **Better Results**")
        st.write("Personalized plans are proven to help you achieve faster and more sustainable results.")

    with col1:
        st.markdown("🥗 **Health First**")
        st.write("Ensures your body gets the right nutrients and exercise while considering any restrictions.")

    with col2:
        st.markdown("🚴‍♂️ **Sustainable Lifestyle**")
        st.write("Build long-term healthy habits that are easy to maintain, even after reaching your goals.")

    # Example of a 150-word personalized recommendation
    personalized_plan = """
    Based on your goals and preferences, we recommend a balanced diet rich in whole grains, lean proteins, and vegetables. 
    Start your day with a high-protein breakfast like eggs or Greek yogurt to keep your energy levels up. For lunch and dinner, 
    focus on lean meats such as chicken or tofu paired with steamed vegetables and whole grains like quinoa or brown rice.

    For exercise, a combination of strength training and cardio will help you achieve optimal results. 
    We suggest 3 days of strength training focusing on major muscle groups, along with 2 days of moderate-intensity cardio such as brisk walking or cycling. 
    Be sure to incorporate stretching or yoga on your rest days to improve flexibility and recovery.

    Remember, consistency is key, and we’re here to guide you every step of the way!
    """
    st.write(fill(personalized_plan, width=70))

    # Button to navigate to the next page
    if st.button("Get Started"):
        go_to_page('recommendation')

# Recommendation Page
if st.session_state['page'] == 'recommendation':
    st.title("Fitness Recommendation System")

    # Load the KMeans model and scaler
    with open(r"C:\Users\mahes\kmeans_model.pkl", 'rb') as file:
        kmeans = pickle.load(file)

    with open(r"C:\Users\mahes\scaler.pkl", 'rb') as file:
        scaler = pickle.load(file)

    # Function to recommend diet and exercise
    def recommend(gender, fitness_goal, activity_level):
        recommendations = {
        'Male': {
            'Weight Loss': {
                'Sedentary': {
                    'diet': {
                        'breakfast': ['Greek yogurt with honey', 'Boiled eggs (Non-Veg)', 'Smoothie bowl'],
                        'lunch': ['Salad with grilled chicken (Non-Veg)', 'Vegetable soup (Veg)', 'Chickpea salad (Veg)'],
                        'dinner': ['Tofu and vegetable stir-fry (Veg)', 'Grilled paneer (Veg)', 'Mixed vegetable salad (Veg)']
                    },
                    'exercise': ['Walking', 'Bodyweight exercises', 'Yoga', 'Stretching', 'Light swimming', 
                                'Tai chi', 'Cycling (low intensity)', 'Light pilates', 'Basic resistance bands', 'Elliptical trainer']
                },
                'Light': {
                    'diet': {
                        'breakfast': ['Quinoa salad (Veg)', 'Smoothie with protein', 'Grilled tofu (Veg)'],
                        'lunch': ['Baked fish with veggies (Non-Veg)', 'Eggs and avocado (Non-Veg)', 'Vegetable wrap (Veg)'],
                        'dinner': ['Chicken and quinoa (Non-Veg)', 'Chickpea curry (Veg)', 'Grilled paneer (Veg)']
                    },
                    'exercise': ['Jogging', 'Swimming', 'Cycling', 'Brisk walking', 'Resistance training', 
                                'Hiking', 'Low-impact aerobics', 'Dancing', 'Rowing machine', 'Power yoga']
                },
                'Moderate': {
                    'diet': {
                        'breakfast': ['Chicken stir-fry (Non-Veg)', 'Oatmeal with fruits', 'Protein shakes'],
                        'lunch': ['Lean beef with broccoli (Non-Veg)', 'Paneer bhurji (Veg)', 'Quinoa bowl (Veg)'],
                        'dinner': ['Fish curry with brown rice (Non-Veg)', 'Mixed bean salad (Veg)', 'Egg whites with spinach (Non-Veg)']
                    },
                    'exercise': ['HIIT workouts', 'Weightlifting', 'Running', 'Rowing', 'Boxing', 
                                'Circuit training', 'Stair climbing', 'CrossFit', 'Battle ropes', 'Jump rope']
                },
                'Active': {
                    'diet': {
                        'breakfast': ['Protein shake', 'Egg omelette with vegetables (Non-Veg)', 'Sprouts salad (Veg)'],
                        'lunch': ['Grilled salmon with brown rice (Non-Veg)', 'Chicken breast with quinoa (Non-Veg)', 'Vegetable couscous (Veg)'],
                        'dinner': ['Lentil soup (Veg)', 'Tuna salad (Non-Veg)', 'Tofu wrap (Veg)']
                    },
                    'exercise': ['CrossFit', 'Team sports', 'Marathon training', 'Kickboxing', 'Rowing', 
                                'Advanced weightlifting', 'Interval sprinting', 'Tennis', 'Climbing', 'Cross-country running']
                }
            },
            'Muscle Gain': {
                'Sedentary': {
                    'diet': {
                        'breakfast': ['Protein pancakes', 'Oatmeal with peanut butter', 'Scrambled eggs (Non-Veg)'],
                        'lunch': ['Grilled chicken with brown rice (Non-Veg)', 'Quinoa salad with nuts (Veg)', 'Pasta with meatballs (Non-Veg)'],
                        'dinner': ['Steak with sweet potatoes (Non-Veg)', 'Chickpea stew (Veg)', 'Paneer curry (Veg)']
                    },
                    'exercise': ['Bodyweight exercises', 'Stretching', 'Light weight lifting', 'Yoga', 'Pilates']
                },
                'Light': {
                    'diet': {
                        'breakfast': ['Greek yogurt with granola', 'Smoothie with spinach', 'Protein bars'],
                        'lunch': ['Chicken Caesar salad (Non-Veg)', 'Turkey wrap (Non-Veg)', 'Quinoa and black bean salad (Veg)'],
                        'dinner': ['Fish tacos (Non-Veg)', 'Vegetable stir-fry with tofu (Veg)', 'Pasta primavera (Veg)']
                    },
                    'exercise': ['Resistance training', 'Swimming', 'Cycling', 'Hiking', 'Low-impact aerobics']
                },
                'Moderate': {
                    'diet': {
                        'breakfast': ['Egg and cheese sandwich (Non-Veg)', 'Overnight oats with nuts', 'Protein smoothie'],
                        'lunch': ['Lean beef stir-fry (Non-Veg)', 'Vegetable and chicken salad (Non-Veg)', 'Lentil soup (Veg)'],
                        'dinner': ['Baked salmon with quinoa (Non-Veg)', 'Mixed vegetable curry (Veg)', 'Stuffed peppers (Veg)']
                    },
                    'exercise': ['Weightlifting', 'Running', 'Boxing', 'Circuit training', 'CrossFit']
                },
                'Active': {
                    'diet': {
                        'breakfast': ['Protein shake with fruit', 'Egg omelette with cheese (Non-Veg)', 'Tofu scramble (Veg)'],
                        'lunch': ['Chicken breast with sweet potatoes (Non-Veg)', 'Bulgur wheat salad (Veg)', 'Salmon with brown rice (Non-Veg)'],
                        'dinner': ['Steak with steamed broccoli (Non-Veg)', 'Vegetable stir-fry with brown rice (Veg)', 'Pasta with lentils (Veg)']
                    },
                    'exercise': ['CrossFit', 'Team sports', 'Marathon training', 'Advanced weightlifting', 'Interval sprints']
                }
            },
            'Maintenance': {
                'Sedentary': {
                    'diet': {
                        'breakfast': ['Smoothie with protein powder', 'Yogurt with fruits', 'Scrambled eggs (Non-Veg)'],
                        'lunch': ['Grilled chicken salad (Non-Veg)', 'Vegetable soup (Veg)', 'Quinoa bowl (Veg)'],
                        'dinner': ['Tofu stir-fry (Veg)', 'Grilled fish with vegetables (Non-Veg)', 'Pasta with marinara sauce (Veg)']
                    },
                    'exercise': ['Walking', 'Yoga', 'Stretching']
                },
                'Light': {
                    'diet': {
                        'breakfast': ['Oatmeal with fruits', 'Greek yogurt with honey', 'Smoothie bowl'],
                        'lunch': ['Baked chicken with vegetables (Non-Veg)', 'Vegetable wrap (Veg)', 'Quinoa salad (Veg)'],
                        'dinner': ['Fish with brown rice (Non-Veg)', 'Chickpea salad (Veg)', 'Stuffed bell peppers (Veg)']
                    },
                    'exercise': ['Brisk walking', 'Cycling', 'Light jogging']
                },
                'Moderate': {
                    'diet': {
                        'breakfast': ['Eggs with spinach (Non-Veg)', 'Protein pancakes', 'Overnight oats'],
                        'lunch': ['Turkey and avocado sandwich (Non-Veg)', 'Vegetable stir-fry (Veg)', 'Chicken salad (Non-Veg)'],
                        'dinner': ['Baked salmon with quinoa (Non-Veg)', 'Mixed vegetable curry (Veg)', 'Pasta with lentils (Veg)']
                    },
                    'exercise': ['Running', 'Swimming', 'Resistance training']
                },
                'Active': {
                    'diet': {
                        'breakfast': ['Greek yogurt with nuts', 'Egg white omelette (Non-Veg)', 'Smoothie with protein'],
                        'lunch': ['Grilled chicken salad (Non-Veg)', 'Paneer salad (Veg)', 'Vegetable stir-fry (Veg)'],
                        'dinner': ['Lentil soup (Veg)', 'Grilled fish with veggies (Non-Veg)', 'Tofu stir-fry (Veg)']
                    },
                    'exercise': ['CrossFit', 'Marathon training', 'Kickboxing']
                }
            }
        },
        'Female': {
            'Weight Loss': {
                'Sedentary': {
                    'diet': {
                        'breakfast': ['Oatmeal with berries', 'Boiled eggs (Non-Veg)', 'Smoothie with almond milk'],
                        'lunch': ['Salad with grilled tofu (Veg)', 'Vegetable stir-fry (Veg)', 'Chickpea salad (Veg)'],
                        'dinner': ['Grilled paneer (Veg)', 'Vegetable soup (Veg)', 'Mixed vegetable salad (Veg)']
                    },
                    'exercise': ['Walking', 'Yoga', 'Stretching', 'Light swimming', 'Pilates', 
                                'Cycling (low intensity)', 'Resistance band exercises', 'Elliptical machine', 'Tai chi', 'Bodyweight exercises']
                },
                'Light': {
                    'diet': {
                        'breakfast': ['Quinoa salad (Veg)', 'Smoothie with protein', 'Grilled tofu (Veg)'],
                        'lunch': ['Grilled chicken with veggies (Non-Veg)', 'Eggs and avocado (Non-Veg)', 'Vegetable wrap (Veg)'],
                        'dinner': ['Baked fish with veggies (Non-Veg)', 'Chickpea curry (Veg)', 'Grilled paneer (Veg)']
                    },
                    'exercise': ['Jogging', 'Swimming', 'Cycling', 'Brisk walking', 'Resistance training', 
                                'Hiking', 'Low-impact aerobics', 'Dance classes', 'Rowing machine', 'Yoga']
                },
                'Moderate': {
                    'diet': {
                        'breakfast': ['Oatmeal with almond butter', 'Boiled eggs (Non-Veg)', 'Protein shake'],
                        'lunch': ['Chicken stir-fry (Non-Veg)', 'Mixed bean salad (Veg)', 'Paneer tikka (Veg)'],
                        'dinner': ['Fish curry with brown rice (Non-Veg)', 'Grilled tofu with quinoa (Veg)', 'Chickpea wrap (Veg)']
                    },
                    'exercise': ['HIIT', 'Weightlifting', 'Running', 'Rowing', 'Dance cardio', 
                                'Circuit training', 'CrossFit', 'Stair climbing', 'Kettlebell swings', 'Boxing']
                },
                'Active': {
                    'diet': {
                        'breakfast': ['Greek yogurt with nuts', 'Egg white omelette (Non-Veg)', 'Smoothie with protein'],
                        'lunch': ['Grilled chicken salad (Non-Veg)', 'Paneer salad (Veg)', 'Vegetable stir-fry (Veg)'],
                        'dinner': ['Lentil soup (Veg)', 'Grilled fish with veggies (Non-Veg)', 'Tofu stir-fry (Veg)']
                    },
                    'exercise': ['CrossFit', 'Marathon training', 'Kickboxing', 'Advanced weightlifting', 
                                'Interval sprints', 'Tennis', 'Rock climbing', 'Plyometrics', 'Swimming', 'Team sports']
                }
            },
            'Muscle Gain': {
                'Sedentary': {
                    'diet': {
                        'breakfast': ['Protein pancakes', 'Greek yogurt with honey', 'Scrambled eggs (Non-Veg)'],
                        'lunch': ['Grilled chicken with quinoa (Non-Veg)', 'Quinoa salad with nuts (Veg)', 'Pasta with meatballs (Non-Veg)'],
                        'dinner': ['Steak with sweet potatoes (Non-Veg)', 'Chickpea stew (Veg)', 'Paneer curry (Veg)']
                    },
                    'exercise': ['Bodyweight exercises', 'Light weight lifting', 'Yoga', 'Pilates']
                },
                'Light': {
                    'diet': {
                        'breakfast': ['Oatmeal with almond butter', 'Smoothie with spinach', 'Protein bars'],
                        'lunch': ['Grilled chicken with vegetables (Non-Veg)', 'Vegetable stir-fry (Veg)', 'Quinoa and black bean salad (Veg)'],
                        'dinner': ['Fish tacos (Non-Veg)', 'Stuffed bell peppers (Veg)', 'Pasta primavera (Veg)']
                    },
                    'exercise': ['Resistance training', 'Swimming', 'Cycling', 'Hiking', 'Low-impact aerobics']
                },
                'Moderate': {
                    'diet': {
                        'breakfast': ['Egg and cheese sandwich (Non-Veg)', 'Overnight oats with nuts', 'Protein smoothie'],
                        'lunch': ['Lean beef stir-fry (Non-Veg)', 'Vegetable and chicken salad (Non-Veg)', 'Lentil soup (Veg)'],
                        'dinner': ['Baked salmon with quinoa (Non-Veg)', 'Mixed vegetable curry (Veg)', 'Stuffed peppers (Veg)']
                    },
                    'exercise': ['Weightlifting', 'Running', 'Boxing', 'Circuit training', 'CrossFit']
                },
                'Active': {
                    'diet': {
                        'breakfast': ['Protein shake with fruit', 'Egg omelette with cheese (Non-Veg)', 'Tofu scramble (Veg)'],
                        'lunch': ['Grilled chicken with sweet potatoes (Non-Veg)', 'Bulgur wheat salad (Veg)', 'Salmon with brown rice (Non-Veg)'],
                        'dinner': ['Steak with steamed broccoli (Non-Veg)', 'Vegetable stir-fry with brown rice (Veg)', 'Pasta with lentils (Veg)']
                    },
                    'exercise': ['CrossFit', 'Team sports', 'Marathon training', 'Advanced weightlifting', 'Interval sprints']
                }
            },
            'Maintenance': {
                'Sedentary': {
                    'diet': {
                        'breakfast': ['Smoothie with protein powder', 'Yogurt with fruits', 'Scrambled eggs (Non-Veg)'],
                        'lunch': ['Grilled chicken salad (Non-Veg)', 'Vegetable soup (Veg)', 'Quinoa bowl (Veg)'],
                        'dinner': ['Tofu stir-fry (Veg)', 'Grilled fish with vegetables (Non-Veg)', 'Pasta with marinara sauce (Veg)']
                    },
                    'exercise': ['Walking', 'Yoga', 'Stretching']
                },
                'Light': {
                    'diet': {
                        'breakfast': ['Oatmeal with fruits', 'Greek yogurt with honey', 'Smoothie bowl'],
                        'lunch': ['Grilled chicken with vegetables (Non-Veg)', 'Vegetable wrap (Veg)', 'Quinoa salad (Veg)'],
                        'dinner': ['Fish with brown rice (Non-Veg)', 'Chickpea salad (Veg)', 'Stuffed bell peppers (Veg)']
                    },
                    'exercise': ['Brisk walking', 'Cycling', 'Light jogging']
                },
                'Moderate': {
                    'diet': {
                        'breakfast': ['Eggs with spinach (Non-Veg)', 'Protein pancakes', 'Overnight oats'],
                        'lunch': ['Turkey and avocado sandwich (Non-Veg)', 'Vegetable stir-fry (Veg)', 'Chicken salad (Non-Veg)'],
                        'dinner': ['Baked salmon with quinoa (Non-Veg)', 'Mixed vegetable curry (Veg)', 'Pasta with lentils (Veg)']
                    },
                    'exercise': ['Running', 'Swimming', 'Resistance training']
                },
                'Active': {
                    'diet': {
                        'breakfast': ['Greek yogurt with nuts', 'Egg white omelette (Non-Veg)', 'Smoothie with protein'],
                        'lunch': ['Grilled chicken salad (Non-Veg)', 'Paneer salad (Veg)', 'Vegetable stir-fry (Veg)'],
                        'dinner': ['Lentil soup (Veg)', 'Grilled fish with veggies (Non-Veg)', 'Tofu stir-fry (Veg)']
                    },
                    'exercise': ['CrossFit', 'Marathon training', 'Kickboxing']
                }
            }
        }
    }

    # Fetch recommendations based on user input
        return recommendations.get(gender, {}).get(fitness_goal, {}).get(activity_level, 'No recommendations available.')


# Function to gather user input
    # User Input
    age = st.number_input("Please enter your age:", min_value=1, max_value=120, value=25)
    height = st.number_input("Please enter your height in cm:", min_value=50, max_value=250, value=170)
    weight = st.number_input("Please enter your weight in kg:", min_value=30, max_value=300, value=70)
    gender = st.selectbox("Please select your gender:", ["Male", "Female"])
    fitness_goal = st.selectbox("Please select your fitness goal:", ["Weight Loss", "Muscle Gain", "Maintenance"])
    activity_level = st.selectbox("Please select your activity level:", ["Sedentary", "Light", "Moderate", "Active"])

    # Prepare user data for scaling
    user_data = pd.DataFrame({
        'age': [age],
        'height': [height],
        'weight': [weight]
    })
    user_data['BMI'] = user_data['weight'] / (user_data['height'] / 100) ** 2

    # Get recommendations
    if st.button("Get Recommendations"):
        # Get and display recommendations
        recommendations = recommend(gender, fitness_goal, activity_level)

        if recommendations != 'No recommendations available.':
            st.subheader("Diet Recommendations:")
            st.write(recommendations['diet'])
            st.subheader("Exercise Recommendations:")
            st.write(recommendations['exercise'])
        else:
            st.write(recommendations)
