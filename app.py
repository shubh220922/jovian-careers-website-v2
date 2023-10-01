import os
from flask import Flask, render_template, send_from_directory, jsonify
from database import load_jobs_from_db

app = Flask(__name__)


@app.route("/")
def hello_world():
    jobs = load_jobs_from_db()
    return render_template('/home.html',
                           jobs=jobs,
                           company_name="Jovian")


@app.route("/favicon.ico")
def favicon():
    return send_from_directory(os. path.join(app.root_path, 'static'),
                               'favicon.ico')


@app.route("/jobs")
def list_jobs():
    jobs = load_jobs_from_db()
    return jsonify(jobs)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
