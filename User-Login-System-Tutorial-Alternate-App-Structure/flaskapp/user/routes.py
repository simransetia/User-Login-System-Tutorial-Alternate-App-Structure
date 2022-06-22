from flask import render_template,request,redirect
from flaskapp import app
from flaskapp.user.models import User
import speech_recognition as sr

@app.route('/user/signup', methods=['POST'])
def signup():
  return User().signup()

@app.route('/user/signout')
def signout():
  return User().signout()

@app.route('/user/login', methods=['POST'])
def login():
  return User().login()

@app.route('/user/listening',methods=["GET", "POST"])
def listening():
  return User().listen()
