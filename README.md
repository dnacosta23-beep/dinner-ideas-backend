# Dinner Ideas Backend

The Dinner Ideas backend is a small Flask API that provides random dinner recipes for the React frontend.

It uses TheMealDB API to retrieve random recipes, filters out breakfast, dessert, starter, and side dishes, removes duplicate meals, and returns 10 unique dinner ideas.

## API Routes

### Home

```text
GET /
```

Returns a message confirming that the API is running.

### Meals

```text
GET /meals
```

Returns an array of 10 unique dinner recipes.

Each recipe includes:

- ID
- Name
- Category
- Cuisine
- Image
- Instructions
- YouTube recipe link

## Technologies

- Python
- Flask
- Flask-CORS
- Requests
- TheMealDB API
- Gunicorn

## Hosted Backend

https://your-backend-url.onrender.com

## Run Locally

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the project dependencies:

```bash
pip install -r requirements.txt
```

Start the Flask server:

```bash
python3 app.py
```

The API will be available at:

```text
http://127.0.0.1:5000
```