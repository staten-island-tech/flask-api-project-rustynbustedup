from flask import Flask, render_template, request, redirect, url_for #imports Flask tools needed for the web app
import requests #used to send HTTP requests to APIs

app = Flask(__name__) #initialize the Flask app

# Getting all drivers from the API 
def get_all_drivers():
    try:
        url = "http://ergast.com/api/f1/drivers.json?limit=2000" #API endpoint to get all F1 drivers
        response = requests.get(url) #send GET request to the API
        data = response.json() #convert the response into a Python dictionary
        return data['MRData']['DriverTable']['Drivers'] #return the list of drivers from the data
    except Exception as e:
        print(f"Error fetching drivers: {e}") #print error if something goes wrong
        return [] #return empty list on error

# Home Page
@app.route('/') #route for homepage
def home():
    return render_template('index.html') #load index.html when user visits root URL

# All drivers page
@app.route('/drivers') #route for drivers page
def drivers():
    try:
        drivers = get_all_drivers() #fetch all drivers using the function
        nationality = request.args.get('nationality') #get nationality filter from query params
        sort_by = request.args.get('sort') #get sorting preference from query params

        if nationality:
            drivers = [d for d in drivers if d['nationality'].lower() == nationality.lower()] 
            #filter the list by nationality

        if sort_by == 'surname':
            drivers = sorted(drivers, key=lambda x: x['familyName']) #sort drivers by surname if selected
        elif sort_by == 'dob':
            drivers = sorted(drivers, key=lambda x: x['dateOfBirth']) #sort by date of birth if selected

        return render_template('drivers.html', drivers=drivers) #show the driver list 
    except Exception as e:
        return render_template('error.html', message=str(e)), 500 #shows error page if smtn goe wong

@app.route('/tracks') #route for tracks page
def tracks():
    try:
        url = "http://ergast.com/api/f1/circuits.json?limit=100" #API endpoint to get all F1 circuits
        response = requests.get(url) #send GET request to the API
        data = response.json() #convert JSON response to Python dict
        circuits = data['MRData']['CircuitTable']['Circuits'] #tae the list of circuits
        return render_template('tracks.html', circuits=circuits) #show the circuits in the template
    except Exception as e:
        return render_template('error.html', message="Error fetching track data."), 500 #error page if API fails

# Driver detail page
@app.route('/driver/<driver_id>') #dynamic route for individual driver pages
def driver_detail(driver_id): #gives id about driver on the page (named)
    try:
        url = f"http://ergast.com/api/f1/drivers/{driver_id}.json" #API endpoint to get driver details by ID
        response = requests.get(url) #send GET request
        data = response.json() #convert JSON to Python
        driver = data['MRData']['DriverTable']['Drivers'][0] #get the first driver 
        return render_template('driver_detail.html', driver=driver) #show the driver details in template
    except Exception as e:
        return render_template("error.html", message="Driver not found."), 404 #show error page if not found

@app.errorhandler(404) # 404 page not foud
def not_found(e):
    return render_template("404.html"), 404 #404 page

@app.errorhandler(500) #custom handler for server error
def server_error(e):
    return render_template("error.html", message="Internal Server Error"), 500 #error page for server error

if __name__ == '__main__': 
    app.run(debug=True) #run the app 
