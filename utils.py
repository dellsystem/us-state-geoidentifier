import json


class State:
    def __init__(self, state_code, vertices):
        self.state_code = state_code
        self.vertices = vertices

    def contains(self, point_x, point_y):
        """
        For every pair of adjacent vertices, draw an semi-infinite horizontal
        ray starting from the point and going in the positive x direction, and
        check if this ray intersects the edge between this pair of vertices. If
        the number of intersections is even, the point is outside; odd, it's
        inside. Adapted from
        http://www.ecse.rpi.edu/Homepages/wrf/Research/Short_Notes/pnpoly.html
        """
        flag = False
        x_2, y_2 = self.vertices[-1]

        for x, y in self.vertices:
            if ((y > point_y) is not (y_2 > point_y)) and (point_x < (x_2-x) *
                (point_y - y) / (y_2 - y) + x):
                flag = not flag

            x_2, y_2 = x, y

        return flag

    def __repr__(self):
        return '<State: %s>' % self.state_code


def _load_states():
    data = json.load(open('data/states.json'))
    states = []

    for state_code, vertices in data:
        state = State(state_code, vertices)
        states.append(state)

    return states


STATES = _load_states()

def find_state(latitude, longitude):
    """
    Returns the two-letter state code (e.g., "NY") of the state the point is
    found to be contained within. If no such state exists, returns None.
    """
    for state in STATES:
        if state.contains(longitude, latitude):
            return state.state_code
