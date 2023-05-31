import sys
from flask import Flask 
sys.path.append(r"D:\Modular coding End to end\ml_pipeline_project")
from src.logger import logging

app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def hello():
    logging.info("Testing....")
    return "Hello World"

if __name__ == "__main__":
    app.run(debug=True)
