import json
import requests
from urllib.parse import urljoin


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
        return (steam_id, self.get_personaname(steam_id),
                self.make_request("players/{}/recentMatches".format(steam_id)))

    def get_personaname(self, steam_id):
        return self.make_request("players/{}".format(steam_id))['profile']['personaname']

    def get_hero_icon(hero):
        pass

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
