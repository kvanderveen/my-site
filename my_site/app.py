from flask import Flask, render_template, jsonify
import os


app = Flask(__name__, template_folder="templates", static_folder="static")

JOBS = [
    {"id": 1, "title": "Data Analyst", "location": "Denver, CO", "salary": "$60,000"},
    {
        "id": 2,
        "title": "Data Scientist",
        "location": "Chicago, IL",
        "salary": "$80,000",
    },
    {"id": 3, "title": "Web Designer", "location": "Boulder, CO", "salary": "$75,000"},
]


@app.route("/")
def index():
    return render_template("index.html", jobs=JOBS)


@app.route("/api/jobs")
def jobs():
    return jsonify(JOBS)


if __name__ == "__main__":
    app.run(debug=True)
