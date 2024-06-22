from os import getenv

from dotenv import load_dotenv
from flask import Flask

load_dotenv()

app = Flask(__name__)

from src import prices_routes
from src import symbols_routes


@app.errorhandler(500)
def internal_error(error):
    return {'message': error.name}, 500


port = int(getenv('STORAGE_API_PORT', 3000))

app.run(host='127.0.0.1', port=port)
