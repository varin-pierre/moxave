from flask import Flask, request, url_for, redirect, render_template, abort, g, flash, session
from werkzeug.contrib.fixers import ProxyFix

app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('WEBSITE_SETTINGS', silent=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sepia')
def sepia():
    return render_template('sepia.html')

@app.route('/monengagement')
def monengagement():
    return render_template('monengagement.html')

@app.route('/42')
def fortytow():
    return render_template('42.html')

@app.route('/photo')
def photo():
    return render_template('photo.html')

@app.route('/source')
def source():
    return render_template('source.html')

app.wsgi_app = ProxyFix(app.wsgi_app)
if __name__ == '__main__':
    app.run()
