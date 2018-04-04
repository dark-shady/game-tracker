from flask import render_template
from project import app
from project.apis.opendota.Opendota import Opendota


#################REMOVE######################
import pprint
pp = pprint.PrettyPrinter(indent=4)
YOUR_STEAM_ID = 86904765

dota_friends_dict = {'darkshady':86904765, 'lopi-':50122249, 'face!':879272,  'remix':42951414, 'rekyks':293127408}
#####################END REMOVE##################

# Initialize API wrappers
opendota_api = Opendota()


# Add functions to JINJA templates
app.add_template_global(opendota_api.last_game_played, name='last_game_played')

@app.template_filter('hour_sec')
def hour_sec(seconds):
    minutes, second = divmod(seconds, 60)
    return f"{minutes}:{second:02d}"


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
def dota_friends():
    '''
        Displays the most recent games of your friends
    '''

    friends_matches = []
    for friend in dota_friends_dict.keys():
        friends_matches.append(opendota_api.get_recent_matches(dota_friends_dict[friend]))

    return render_template('dota_friends.html', title='DOTA stats', friends_matches=friends_matches)

@app.route('/dota/friends/expanded')
def dota_friends_expanded():
    '''
        Displays the most recent games of your friends
    '''

    friends_matches = []
    for friend in dota_friends_dict.keys():
        friends_matches.append(opendota_api.get_recent_matches(dota_friends_dict[friend]))

    return render_template('dota_friends_expanded.html', title='DOTA stats', friends_matches=friends_matches)

@app.route('/fortnite')
def fortnite():
    return render_template('fortnite.html', title='Fortnite Stats')
