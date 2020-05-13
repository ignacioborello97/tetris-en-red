from ...index import app

@app.route('/player')
def list_players():
    return 'this should be a list of players?'