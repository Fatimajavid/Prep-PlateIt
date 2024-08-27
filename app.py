from flask import Flask, request, render_template, jsonify
import os
from dotenv import load_dotenv
import requests
load_dotenv()

app= Flask(__name__)
API_KEY = os.getenv('API_KEY')
BASE_URL = 'https://api.spoonacular.com'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/cuisines')
def cuisines():
    cuisines_list = [
        "Italian", "Mexican", "Chinese", "Indian",
        "Thai", "Japanese", "Greek",
        "Spanish", "French", "Mediterranean"
    ]
    return render_template('cuisines.html', cuisines={'cuisines': cuisines_list})

@app.route('/meal-types')
def meal_types():
    meal_types = ["breakfast", "lunch", "dinner", "dessert", "snack"]
    return render_template('meal_types.html', meal_types=meal_types)

@app.route('/recipes')
def recipes():
    query = request.args.get('query')  # Can be cuisine or meal type
    url = f"{BASE_URL}/recipes/complexSearch?query={query}&apiKey={API_KEY}"
    response = requests.get(url)
    recipes_data = response.json() if response.status_code == 200 else {}
    return render_template('recipes.html', recipes=recipes_data)

@app.route('/recipe/<int:recipe_id>')
def recipe_detail(recipe_id):
    url = f"{BASE_URL}/recipes/{recipe_id}/information?apiKey={API_KEY}"
    response = requests.get(url)
    recipe = response.json() if response.status_code == 200 else {}
    return render_template('recipe_detail.html', recipe=recipe)

if __name__ == '__main__':
    app.run(
        port=int(os.getenv('PORT', 8080)),
        host=os.getenv('IP', '0.0.0.0'),
        debug=True
)