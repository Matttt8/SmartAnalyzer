import os
import getData
from flask import Flask, send_file

app = Flask(__name__, static_folder='./staticFolder')

@app.route("localhost/")
def index():
    return send_file('HTML/index.html')

@app.route("localhost/home")
def home():
    return send_file('HTML/home.html')

@app.route("localhost/outdoors")
def outdoors():
    return send_file('HTML/outdoors.html')

def main():
    app.run(port=int(os.environ.get('PORT', 80)))

if __name__ == "__main__":
    main()
