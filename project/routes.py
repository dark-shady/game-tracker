from flask import render_template
from project import app
from project.apis.opendota.Opendota import Opendota


#################REMOVE######################
import pprint
pp = pprint.PrettyPrinter(indent=4)
YOUR_STEAM_ID = 86904765

dota_friends = {'darkshady':86904765, 'lopi-':50122249 }
#####################END REMOVE##################

# Initialize API wrappers
opendota_api = Opendota()


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/dota')
@app.route('/dota/self')
def dota_self():
    '''
        Displays your own most recent DOTA games
    '''

    self_recent_matches = opendota_api.get_recent_matches(YOUR_STEAM_ID)

    return render_template('dota_self.html', title='DOTA stats', matches=self_recent_matches)

@app.route('/dota/friends')
def dota():
    '''
        Displays the most recent games of your friends
    '''

    friends_matches = []
    for friend in dota_friends.keys():
        friends_matches.append(opendota_api.get_recent_matches(dota_friends[friend]))

    return render_template('dota_friends.html', title='DOTA stats', friends_matches=friends_matches)

@app.route('/fortnite')
def fortnite():
    return render_template('fortnite.html', title='Fortnite Stats')
