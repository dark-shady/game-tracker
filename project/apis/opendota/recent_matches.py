from base import Opendota

class Matches(Opendota):
    def __init__(self, steam_id):
        Opendota.__init__(self)
        self.steam_id = steam_id

    def get_recent_matches(self):
        return self.make_request("players/{}/recentMatches".format(self.steam_id))

recent_matches = Matches(86904765)
print(recent_matches.get_recent_matches())

'''
https://api.opendota.com/api/players/{account_id}/recentMatches
    "match_id": 0,
    "player_slot": 0,
    "radiant_win": true,
    "duration": 0,
    "game_mode": 0,
    "lobby_type": 0,
    "hero_id": 0,
    "start_time": 0,
    "version": 0,
    "kills": 0,
    "deaths": 0,
    "assists": 0,
    "skill": 0,
    "lane": 0,
    "lane_role": 0,
    "is_roaming": true,
    "cluster": 0,
    "leaver_status": 0,
    "party_size": 0
'''
