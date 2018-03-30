import json
import requests
import time
import inflect
from urllib.parse import urljoin
p = inflect.engine()

class Opendota:
    def __init__(self):
        self.BASE_URL = "https://api.opendota.com/api/"


    def make_request(self, api_url):
        try:
            r = requests.get(urljoin(self.BASE_URL, api_url))
            r.raise_for_status()
        except requests.exceptions.HTTPError as err:
            return "HTTPError"

        return json.loads(r.text)


    def get_recent_matches(self, steam_id):
        return (steam_id, self.get_player_steam_details(steam_id),
                self.make_request("players/{}/recentMatches".format(steam_id)))

    def get_player_steam_details(self, steam_id):
        request = self.make_request("players/{}".format(steam_id))
        return {
                'personaname': request['profile']['personaname'],
                'avatarmedium': request['profile']['avatarmedium'],
                'profileurl': request['profile']['profileurl']
                }

    def get_hero_icon(self, hero):
        pass

    def last_game_played(self, game_start, duration):
        current_time = int(time.time())
        time_since_played = current_time - game_start + duration
        print("{} {} {} {}".format(time_since_played, current_time, game_start, duration))
        if time_since_played < 3600:
            return "less than an hour ago"
        elif time_since_played < 86400:
            hours_since_played = time_since_played // 3600
            return f"{hours_since_played} {p.plural('hour', hours_since_played)} ago"
        elif time_since_played < 2592000:
            days_since_played = time_since_played // 86400
            return f"{days_since_played} {p.plural('day', days_since_played)} ago"
        elif time_since_played < 31536000:
            months_since_played = time_since_played // 2592000
            return f"{months_since_played} {p.plural('month', months_since_played)} ago"
        else:
            return "more than a year ago"

'''
https://dota2api.readthedocs.io/en/latest/responses.html#player-slot
https://api.opendota.com/api/players/{account_id}/recentMatches
'assists': 11,
          'cluster': 121,
          'deaths': 2, ********************
          'duration': 2335, *******************
          'game_mode': 3,*******************
          'gold_per_min': 472, *******************
          'hero_damage': 21742,
          'hero_healing': 0,
          'hero_id': 47, *******************
          'is_roaming': False,
          'kills': 7, *******************
          'lane': 2,
          'lane_role': 2,
          'last_hits': 164,
          'leaver_status': 0,
          'lobby_type': 7, *******************
          'match_id': 3663098425, *******************
          'party_size': 3, *******************
          'player_slot': 1, *******************
          'radiant_win': True,*******************
          'skill': None,
          'start_time': 1515209299,
          'tower_damage': 5092,
          'version': 21,
          'xp_per_min': 571}
'''
