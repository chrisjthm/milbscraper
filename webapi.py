import json
from flask import Flask
from flask import request
import playerpagecollector

app = Flask(__name__)

@app.route("/stats", methods=['GET'])
def get_stats():
	ppc = playerpagecollector.PlayerPageCollector()
	url = ''
	if 'playerid' in request.args:
		playerid = request.args.get('playerid')
		url = ppc.get_player_page_url_by_id(playerid)
	if 'lastname' in request.args and 'firstname' in request.args:
		lastname = request.args.get('lastname')
		firstname = request.args.get('firstname')
		url = ppc.get_player_page_url_by_name(lastname, firstname)
	return json.dumps(ppc.get_latest_game_data(url))


