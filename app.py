from flask import Flask, jsonify, render_template
import json

app = Flask(__name__)

@app.route('/')
def index():
    with open('Cars.Json', 'r') as file:
        cars = json.load(file)
    return render_template('index.html', cars=cars)

@app.route('/api/cars', methods=['GET'])
def get_cars():
    with open('Cars.Json', 'r') as file:
        cars = json.load(file)
    return jsonify(cars)

@app.route('/api/cars/<int:car_index>', methods=['GET'])
def get_car_by_index(car_index):
    with open('Cars.Json', 'r') as file:
        cars = json.load(file)
    if 0 <= car_index < len(cars):
        return jsonify(cars[car_index])
    else:
        return jsonify({"error": "Car not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)