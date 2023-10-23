#!/usr/bin/python3

""" 7-states_list module """

from flask import Flask, abort, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def rm_curr_SQLAlchemy(error):
    storage.close()


@app.route('/states', strict_slashes=False)
def disp_states():
    """ display a HTML page with all the states stored """
    return render_template('9-states.html',
                           states=storage.all(State).values())


@app.route('/states/<id>', strict_slashes=False)
def disp_A_state_cities(id):
    """
    Display a HTML page with a state with given id if there is one.
    Along with all the cities in that state
    """
    states = storage.all(State).values()
    a_state = None
    for state in states:
        if state.id == id:
            a_state = state

    return render_template('9-states.html',
                           states=states,
                           f_id=True,
                           a_state=a_state)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
