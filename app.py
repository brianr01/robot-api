from flask import Flask
import serial
from Routes import Routes

app = Flask(__name__)

Routes.Register(app)

if __name__ == "__main__":
    app.run(debug=False)