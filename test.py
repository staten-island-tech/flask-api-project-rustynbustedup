import requests

def get_all_drivers():
    try:
        url = "http://ergast.com/api/f1/drivers.json?limit=2000"
        response = requests.get(url)
        data = response.json()
        return data["MRData"]["DriverTable"]["Drivers"]
    except Exception as e:
        print("Error:", e)
        return []

drivers = get_all_drivers()

for driver in drivers:
    if driver['nationality'].lower() == 'american':
        print(driver)