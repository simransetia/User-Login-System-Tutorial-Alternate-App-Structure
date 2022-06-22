from flask import render_template
from flaskapp import app, login_required,db
from flaskapp.user.routes import *

@app.route('/login')
def home():
  return render_template('home.html')

@app.route('/')
def index():
  return render_template('test.html')

@app.route('/dashboard/')
@login_required
def dashboard():

  return render_template('dashboard.html')


if __name__ == '__main__':
  app.run(debug=True)