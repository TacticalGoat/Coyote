from app import app
from .scraper import get_options
import json

@app.route('/options/<symbol>')
def options(symbol):
	return json.dumps(get_options(symbol),sort_keys=True,indent=4,separators=(',',': '))