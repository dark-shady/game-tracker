from flask import render_template
from project import app

dota_friends = {'darkshady':86904765, 'lopi-':50122249 }

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/dota')
def dota():

    return render_template('dota.html', title='DOTA stats')

@app.route('/fortnite')
def fortnite():
    return render_template('fortnite.html', title='Fortnite Stats')
