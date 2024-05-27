import os
from flask import Flask, send_file

app = Flask(__name__, static_folder='./staticFolder')

@app.route("/")
def index():
    return send_file('HTML/index.html')
    return send_file('CSS/index.css')
    return send_file('IMG/bench-tree.png')
    return send_file('IMG/house-chimney.png')

def main():
    app.run(port=int(os.environ.get('PORT', 80)))

if __name__ == "__main__":
    main()
