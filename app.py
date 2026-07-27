import requests
from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS

load_dotenv()

app = Flask(__name__)
CORS(app)

MEAL_API = "https://www.themealdb.com/api/json/v1/1/random.php"

@app.route("/")
def home():
    return {
        "message": "Dinner Ideas API is running"
    }

@app.route("/meals")
def get_meals():
    meals = []
    seen_meals = set()

    excluded_categories = {
        "Breakfast",
        "Dessert",
        "Starter",
        "Side",
    }

    while len(meals) < 10:
        response = requests.get(MEAL_API, timeout=10)
        response.raise_for_status()

        meal = response.json()["meals"][0]

        if meal["strCategory"] in excluded_categories:
            continue

        if meal["idMeal"] in seen_meals:
            continue

        seen_meals.add(meal["idMeal"])

        meals.append(
            {
                "id": meal["idMeal"],
                "name": meal["strMeal"],
                "category": meal["strCategory"],
                "area": meal["strArea"],
                "image": meal["strMealThumb"],
                "instructions": meal["strInstructions"],
                "youtube": meal["strYoutube"],
            }
        )

    return meals


if __name__ == "__main__":
    app.run(debug=True)
