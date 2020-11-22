from flask import Flask

import sys
sys.path.append(sys.path[0] + '/Controllers')
from Turn import turn
from Cameras import cameras

class Routes:
    def Register(app):
        app.register_blueprint(turn)
        app.register_blueprint(cameras)
