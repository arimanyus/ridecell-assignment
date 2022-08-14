import os
from flask import Flask, render_template

APP_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_PATH = os.path.join(APP_PATH, "rdc_frontend_service/templates")

app = Flask(__name__, template_folder=TEMPLATE_PATH)

@app.route("/track")
def run_track():
    """
    This function instantiates and renders the tracking page.

    Returns:
        Rendered tracking template
    """
    return render_template("track.html")

if __name__ == "__main__":
    app.run()