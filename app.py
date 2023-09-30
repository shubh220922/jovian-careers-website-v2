import os
from flask import Flask, render_template, send_from_directory, jsonify

app = Flask(__name__)

JOBS = [{
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bengaluru, India',
    'salary': 'Rs. 10,00,000'
}, {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Delhi, India',
    'salary': 'Rs. 15,00,000'
}, {
    'id': 3,
    'title': 'Frontend Engineer',
    'location': 'Remote',
}, {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'San Francisco, USA',
    'salary': '$120,000'
}, {
    'id': 5,
    'title': 'CEO of X',
    'location': 'Patna, USA',
    'salary': '$120,000,000,000,000'
}]


@app.route("/")
def hello_world():
    return render_template('/home.html',
                           jobs=JOBS,
                           company_name="Jovian")


@app.route("/favicon.ico")
def favicon():
    return send_from_directory(os. path.join(app.root_path, 'static'),
                               'favicon.ico')


@app.route("/jobs")
def list_jobs():
    return jsonify(JOBS)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
