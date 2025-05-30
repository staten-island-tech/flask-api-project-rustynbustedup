from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

def get_all_drivers():
    try:
        url = "http://ergast.com/api/f1/drivers.json?limit=2000"
        response = requests.get(url)
        data = response.json()
        return data['MRData']['DriverTable']['Drivers']
    except Exception as e:
        print(f"Error fetching drivers: {e}")
        return []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/drivers')
def drivers():
    try:
        drivers = get_all_drivers()
        nationality = request.args.get('nationality')
        sort_by = request.args.get('sort')

        if nationality:
            drivers = [d for d in drivers if d['nationality'].lower() == nationality.lower()]

        if sort_by == 'surname':
            drivers = sorted(drivers, key=lambda x: x['familyName'])
            
        elif sort_by == 'dob':
            drivers = sorted(drivers, key=lambda x: x['dateOfBirth'])

        return render_template('drivers.html', drivers=drivers)
    except Exception as e:
        return render_template('error.html', message=str(e)), 500

@app.route('/tracks')
def tracks():
    try:
        url = "http://ergast.com/api/f1/circuits.json?limit=100"
        response = requests.get(url)
        data = response.json()
        circuits = data['MRData']['CircuitTable']['Circuits']
        return render_template('tracks.html', circuits=circuits)
    except Exception as e:
        return render_template('error.html', message="Error fetching track data."), 500

@app.route('/driver/<driver_id>')
def driver_detail(driver_id):
    try:
        url = f"http://ergast.com/api/f1/drivers/{driver_id}.json"
        response = requests.get(url)
        data = response.json()
        driver = data['MRData']['DriverTable']['Drivers'][0]
        return render_template('driver_detail.html', driver=driver)
    except Exception as e:
        return render_template("error.html", message="Driver not found."), 404

@app.errorhandler(404)
def not_found(e):
    return render_template("error.html", message="Page Not Found"), 404

@app.errorhandler(500)
def server_error(e):
    return render_template("error.html", message="Internal Server Error"), 500

if __name__ == '__main__':
    app.run(debug=True)
