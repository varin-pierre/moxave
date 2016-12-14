from flask import Flask, request, url_for, redirect, render_template, abort, g, flash, session
from werkzeug.contrib.fixers import ProxyFix

app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('WEBSITE_SETTING', silent=True)

@app.route('/')
def index():
    return render_template('inidex.html')
#'Flask is running! modify'


app.wsgi_app = ProxyFix(app.wsgi_app)
if __name__ == '__main__':
    app.run()

