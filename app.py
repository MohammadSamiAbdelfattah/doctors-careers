from flask import Flask, render_template, jsonify

app = Flask(__name__)

jobs = [{
    "id": 1,
    "title": "Pediatrician",
    "salary": "£30,000",
    "location": "Cairo, Egypt",
}, {
    "id": 2,
    "title": "Pediatric Surgeon",
    "salary": "£10,000",
    "location": "Cairo, Egypt",
}, {
    "id": 3,
    "title": "General Surgeon",
    "salary": "£15,000",
    "location": "Cairo, Egypt",
}, {
    "id": 4,
    "title": "Plastic Surgeon",
    "salary": "£20,000",
    "location": "Cairo, Egypt",
}]


@app.route('/')
def doctors_careers():
  return render_template("index.html", jobs=jobs)


@app.route('/api/jobs')
def list_jobs():
  return jsonify(jobs)


if __name__ == "__main__":
  app.run("0.0.0.0", debug=True)
