from ...index import app

@app.route('/game')
def list_games():
    return 'this should be a list of all active games'