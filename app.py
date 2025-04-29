from flask import Flask, jsonify, render_template
import json

app = Flask(__name__)

# Load cars
with open('cars.json') as f:
    cars = json.load(f)

# Clean line breaks
for car in cars:
    car['Vehicle'] = car['Vehicle'].replace('\n', ' ')
    car['Value'] = car['Value'].replace('\n', ' ')

@app.route('/')
def index():
    return render_template('index.html', cars=cars)

@app.route('/api/cars', methods=['GET'])
def get_cars():
    return jsonify(cars)

@app.route('/api/cars/<int:car_index>', methods=['GET'])
def get_car_by_index(car_index):
    if 0 <= car_index < len(cars):
        return jsonify(cars[car_index])
    else:
        return jsonify({"error": "Car not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)