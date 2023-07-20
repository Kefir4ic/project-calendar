from app import app
from flask import render_template, json, request, Markup, redirect, flash, send_file, url_for


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/')
@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/logout')
def logout():
    return redirect(url_for('index'))


@app.route('/google')
def google():
    return redirect(url_for('index'))
