#!/usr/bin/python3

""" 10-hbnb_filters module """

from flask import Flask, abort, render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.teardown_appcontext
def rm_curr_SQLAlchemy(error):
    """
    remove the current SQLAlchemy Session
    """
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def disp_state_cities():
    """
    Display a HTML page with all the states stored
    along with all the cities in those named states
    """
    return render_template('10-hbnb_filters.html',
                           states=storage.all(State).values(),
                           amenities=storage.all(Amenity).values())

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
