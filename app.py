from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Joselito Bompat Jr. BSIT - 3B'