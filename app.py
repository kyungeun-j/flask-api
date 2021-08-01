from flask import Flask, request
from flask_api import status
import json
import crawling

app = Flask(__name__)

@app.route("/")
def api():
    return "api"

@app.route('/TodayCount', methods=['GET'])
def get_TodayCount():
    today = json.dumps(crawling.TodayCount)
    return today