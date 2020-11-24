from flask import Flask

import sys
sys.path.append(sys.path[0] + '/Controllers')
from TurnController import turnController
from CamerasController import camerasController

class Routes:
    def Register(app):
        app.register_blueprint(turnController)
        app.register_blueprint(camerasController)
