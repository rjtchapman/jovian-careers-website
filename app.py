from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Douala, Cameroon',
    'salary': '400,000 XAF'
  },
  {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Kribi, Cameroon',
    'salary': '670,000 XAF'
  },
  {
    'id': 3,
    'title': 'Frontend Engineer',
    'location': 'Yaounde, Cameroon',
    'salary': '250,000 XAF'
  },
  {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'Douala, Cameroon',
    'salary': '350,000 XAF'
  }
]

@app.route("/")
def hello_jovian():
  return render_template('home.html', jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)