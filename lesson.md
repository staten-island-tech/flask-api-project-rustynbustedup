# Lesson: Using Bootstrap in Flask with a Container of Food Item Cards

In this lesson, we're going to create a simple Flask web app that shows 9 food items for sale. We'll use Bootstrap to make our web page look attractive with a grid of cards, each displaying a food item with an image, a name, a description, and a price. I'll explain everything as if you're in 6th grade!

---

## What is Bootstrap?

Bootstrap is like a big box of art supplies for your website. It gives you pre-made styles for buttons, cards, grids, and much more. With Bootstrap, you don’t have to design everything yourself—it makes your website look awesome with just a few extra words in your HTML called "classes."

---

## How Does Flask and Bootstrap Work Together?

- **Flask** is like the brain of your website. It tells the computer what pages to show when someone visits your site.
- **Routes** in Flask are like addresses on a map. For example, when you go to `http://127.0.0.1:5000/`, Flask knows to show you the home page.
- **Bootstrap** is added to the HTML templates that Flask uses. By including a link to Bootstrap’s CSS file, you get access to all its cool design features.

---

## Step-by-Step Guide

### Step 1: Set Up Your Project Environment

#### 1.1 Create a Virtual Environment  
A virtual environment is like your own special workspace where all your project tools are kept safe and separate. Open your terminal and run:

```bash
python -m venv venv
```

#### 1.2 Activate the Virtual Environment  
Turn on your workspace:
- **On Windows:**
  ```bash
  venv\Scripts\activate
  ```
- **On Mac/Linux:**
  ```bash
  source venv/bin/activate
  ```

#### 1.3 Create a `requirements.txt` File  
This file tells your project which tools it needs. Create a file called `requirements.txt` and add:

```
Flask
```

#### 1.4 Install Flask  
Now, install Flask by running:

```bash
pip install -r requirements.txt
```

*Your workspace is now ready with all the tools you need!*

---

### Step 2: Create Your Flask App File

Create a file called `app.py`. This file will set up the routes (addresses) for your website and supply the data for your food items.

Here’s what `app.py` looks like:

```python
from flask import Flask, render_template

app = Flask(__name__)

# Route for the home page
@app.route("/")
def index():
    # Create a list of 9 food items for sale
    food_items = [
        {"name": "Pizza", "description": "Delicious cheesy pizza", "price": "$10", "image": "https://via.placeholder.com/150?text=Pizza"},
        {"name": "Burger", "description": "Juicy beef burger", "price": "$8", "image": "https://via.placeholder.com/150?text=Burger"},
        {"name": "Ice Cream", "description": "Cool and tasty ice cream", "price": "$5", "image": "https://via.placeholder.com/150?text=Ice+Cream"},
        {"name": "Sandwich", "description": "Healthy and fresh sandwich", "price": "$7", "image": "https://via.placeholder.com/150?text=Sandwich"},
        {"name": "Salad", "description": "Fresh mixed salad", "price": "$6", "image": "https://via.placeholder.com/150?text=Salad"},
        {"name": "Sushi", "description": "Traditional Japanese sushi", "price": "$12", "image": "https://via.placeholder.com/150?text=Sushi"},
        {"name": "Pasta", "description": "Italian pasta with sauce", "price": "$9", "image": "https://via.placeholder.com/150?text=Pasta"},
        {"name": "Donut", "description": "Sweet and yummy donut", "price": "$3", "image": "https://via.placeholder.com/150?text=Donut"},
        {"name": "Taco", "description": "Spicy and flavorful taco", "price": "$4", "image": "https://via.placeholder.com/150?text=Taco"}
    ]
    # Render the 'index.html' template and pass the food items list to it.
    return render_template("index.html", food_items=food_items)

if __name__ == '__main__':
    app.run(debug=True)
```

### Understanding the Routing

- **`@app.route("/")`**  
  This decorator tells Flask that when someone visits the root address (`http://127.0.0.1:5000/`), it should run the `index()` function.
  
- **The `index()` Function**  
  This function creates a list of food items. Each food item has a name, description, price, and image URL. Then, it tells Flask to show the `index.html` page with that list.

---

### Step 3: Create the HTML Template with Bootstrap

#### 3.1 Create a Folder Called `templates`  
In your project folder, create a folder named `templates`.

#### 3.2 Create an HTML File Called `index.html`  
Inside the `templates` folder, create a file named `index.html` and add the following code:

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8" />
    <title>Food Items for Sale</title>
    <!-- Link to Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
  </head>
  <body>
    <!-- Bootstrap container for proper spacing -->
    <div class="container mt-5">
      <h1 class="text-center mb-4">Food Items for Sale</h1>
      <div class="row">
        <!-- Loop through each food item and create a card -->
        {% for food in food_items %}
        <div class="col-md-4 mb-4">
          <div class="card h-100">
            <img src="{{ food.image }}" class="card-img-top" alt="{{ food.name }}">
            <div class="card-body">
              <h5 class="card-title">{{ food.name }}</h5>
              <p class="card-text">{{ food.description }}</p>
            </div>
            <div class="card-footer">
              <p class="card-text"><strong>Price:</strong> {{ food.price }}</p>
              <a href="#" class="btn btn-primary">Buy Now</a>
            </div>
          </div>
        </div>
        {% endfor %}
      </div>
    </div>
  </body>
</html>
```

#### Explanation of the HTML:
- **Bootstrap Link:**  
  The `<link>` tag in the `<head>` loads Bootstrap's CSS, which gives you access to all its pre-made styles.
- **Container:**  
  The `<div class="container mt-5">` creates a box that centers your content and adds a margin at the top.
- **Row and Columns:**  
  The `<div class="row">` creates a row. Inside this row, each food item is in a `<div class="col-md-4 mb-4">`, which makes 3 cards per row (since 12 columns divided by 4 equals 3).
- **Card Component:**  
  Each card uses Bootstrap’s card component classes (like `card`, `card-body`, `card-footer`) to organize the image, title, description, and price. The “Buy Now” button is styled with `btn btn-primary`.

---

### Step 4: Run Your Flask App

1. **Make sure your virtual environment is activated.**
2. **Run the app by typing:**

   ```bash
   python app.py
   ```

3. **Open your Web Browser:**  
   Go to [http://127.0.0.1:5000](http://127.0.0.1:5000) to see your food items page!

---

## Recap

- **Bootstrap:**  
  Provides pre-made styles to make your website look great. In our example, we used Bootstrap’s grid system and card components.
  
- **Flask Routes:**  
  The route `"/"` tells Flask to run the `index()` function, which sends the list of food items to `index.html`.

- **HTML with Bootstrap:**  
  In `index.html`, we created a container with a row of 9 cards. Each card displays a food item with its image, name, description, price, and a “Buy Now” button.

This lesson shows how easy it is to combine Flask and Bootstrap to build a beautiful, responsive website. Enjoy creating your food items shop and have fun experimenting with more Bootstrap features!