import os
from flask import Flask, render_template, send_from_directory, jsonify
from database import load_jobs_from_db, load_job_from_db

app = Flask(__name__)


@app.route("/")
def hello_world():
    jobs = load_jobs_from_db()
    return render_template('/home.html',
                           jobs=jobs)


@app.route("/favicon.ico")
def favicon():
    return send_from_directory(os. path.join(app.root_path, 'static'),
                               'favicon.ico')


@app.route("/jobs")
def list_jobs():
    jobs = load_jobs_from_db()
    return jsonify(jobs)


@app.route("/job/<id>")
def show_job(id):
    job = load_job_from_db(id)
    if not job:
        return "Not Found", 404
    return render_template('/jobpage.html',
                           job=job)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
