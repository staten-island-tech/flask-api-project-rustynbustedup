from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

# Getting All driers from the API 
def get_all_drivers():
    try:
        url = "http://ergast.com/api/f1/drivers.json?limit=2000"
        response = requests.get(url)
        data = response.json()
        return data['MRData']['DriverTable']['Drivers']
    except Exception as e:
        print(f"Error fetching drivers: {e}")
        return []

# Home Page
@app.route('/')
def home():
    return render_template('index.html') #goes to index.html 

# All drivers page
@app.route('/drivers') #links to all drivers page
def drivers():
    try:
        drivers = get_all_drivers() #gets all drivers from the API
        nationality = request.args.get('nationality') #sorts by nationality
        sort_by = request.args.get('sort') #actually sorts if said 

        if nationality:
            drivers = [d for d in drivers if d['nationality'].lower() == nationality.lower()] #show driver names in ordder of nationality

        if sort_by == 'surname':
            drivers = sorted(drivers, key=lambda x: x['familyName'])    #sorts by surname
        elif sort_by == 'dob':
            drivers = sorted(drivers, key=lambda x: x['dateOfBirth'])

        return render_template('drivers.html', drivers=drivers)
    except Exception as e:
        return render_template('error.html', message=str(e)), 500
    
@app.route('/tracks')   #links to all tracks page
def tracks(): #makes the tracks page
    try:
        url = "http://ergast.com/api/f1/circuits.json?limit=100" #takes the data from the API
        response = requests.get(url)
        data = response.json() #converts the data from JSON to python
        circuits = data['MRData']['CircuitTable']['Circuits'] #pulls data and puts into one circuts variable
        return render_template('tracks.html', circuits=circuits) #return the circuts variable
    except Exception as e:
        return render_template('error.html', message="Error fetching track data."), 500 

# Driver detail page
@app.route('/driver/<driver_id>') #links to driver detail page
def driver_detail(driver_id):
    try:
        url = f"http://ergast.com/api/f1/drivers/{driver_id}.json" #pulls data from the API 
        response = requests.get(url)
        data = response.json() #converts the data from JSON to python
        driver = data['MRData']['DriverTable']['Drivers'][0] #puts all data into one variable
        return render_template('driver_detail.html', driver=driver) #puts the variable data intot the driverdetail page
    except Exception as e:
        return render_template('error.html', message="Driver not found."), 404 #error handling 

@app.errorhandler(404)
def not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(500)
def server_error(e):
    return render_template("error.html", message="Internal Server Error"), 500

if __name__ == '__main__':
    app.run(debug=True) # Run the Flask app