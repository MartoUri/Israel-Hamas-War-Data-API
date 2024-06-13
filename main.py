import functions
from flask import Flask, jsonify
import threading
while True:
    try:
        Palestine = functions.Palestine()
        Israel = functions.Israel()
        both = functions.Both()
    except:
        print("Error. Continuing")
        continue
    break

threading.Thread(target=functions.ConstantUpdate).start()

app = Flask(__name__)

@app.route("/both")
def Both():
    return jsonify(both), 200

@app.route("/israel")
def israel():
    return jsonify(Israel), 200

@app.route("/palestine-gaza")
def Gaza():
    return jsonify(Palestine[0]), 200

@app.route("/palestine-westbank")
def WestBank():
    return jsonify(Palestine[1]), 200

@app.route("/palestine-all")
def palestine():
    return jsonify(Palestine[2]), 200

@app.route("/")
def index():
    return """
    <h1>Welcome to the Israel-Hamas War Data API</h1>
    <p>Available endpoints:</p>
    <ul>
        <li><a href="/both">/both</a> - Get data for both Palestine and Israel</li>
        <li><a href="/israel">/israel</a> - Get data for Israel</li>
        <li><a href="/palestine-gaza">/palestine-gaza</a> - Get data for Palestine in Gaza</li>
        <li><a href="/palestine-westbank">/palestine-westbank</a> - Get data for Palestine in West Bank</li>
        <li><a href="/palestine-all">/palestine-all</a> - Get data for all of Palestine</li>
    </ul>
    <p>The data is fetched from:</p>
    <ul>
        <li><a href="https://www.aljazeera.com/news/longform/2023/10/9/israel-hamas-war-in-maps-and-charts-live-tracker">https://www.aljazeera.com/news/longform/2023/10/9/israel-hamas-war-in-maps-and-charts-live-tracker</a></li>
        <li><a href="https://www.standwithus.com/situationroom">https://www.standwithus.com/situationroom</a></li>
        </ul>
    """

if __name__ == "__main__":
    app.run(debug=True)