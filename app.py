# Flask app for personal portfolio

from flask import Flask, redirect, render_template, session, flash, request

app = Flask(__name__)

@app.route('/')
def show_home():
    return render_template('index.html')

@app.route('/l')
def next():
    return 'over here'