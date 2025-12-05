from flask import Flask, request, render_template_string
from .generator import generate_password

app = Flask(__name__)

TEMPLATE = "<html><body><h2>Gerador</h2></body></html>"

@app.route("/", methods=["GET", "POST"])
def index():
    password = None
    return render_template_string(TEMPLATE, password=password)

if __name__ == "__main__":
    app.run(debug=True)
