from flask import Flask

import sys
sys.path.append(sys.path[0] + '/Controllers')
from Turn_Controller import turn_controller
from Cameras_Controller import cameras_controller
from Cube_Controller import cube_controller
from Launch_Programs_Controller import launch_programs_controller

class Routes:
    def Register(app):
        app.register_blueprint(turn_controller)
        app.register_blueprint(cameras_controller)
        app.register_blueprint(cube_controller)
        app.register_blueprint(launch_programs_controller)
