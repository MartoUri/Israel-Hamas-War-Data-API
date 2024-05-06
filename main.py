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

if __name__ == "__main__":
    app.run(debug=True)