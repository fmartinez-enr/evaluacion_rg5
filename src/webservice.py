from flask import Flask, jsonify

import csv


app = Flask(__name__, static_url_path="")


@app.route("/", methods=["GET"])
def get_json():
    file_path = "/data/employees.csv"
    data = []

    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)

    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
