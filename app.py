from flask import Flask, render_template

# A class to represent a cities info (Anthony)
import City
app = Flask(__name__)


# Get Current location (Anthony)
# Get weather based on location (Anthony)
# Get list of other major city weather stats (Anthony)
@app.route('/')
def Home():
    # LocWeather: City should be a City class with the current location's weather. (Anthony)
    # Cities: City (array) should contain all the cities data. (Anthony)
    return render_template('main.html', LocWeather=City.City, Cities=[])


if __name__ == '__main__':
    app.run()
